import re
import struct

# System V AMD64 rgisters em ordem
_ARG_REGS = ['rdi', 'rsi', 'rdx', 'rcx', 'r8', 'r9']
_XMM_ARG_REGS = ['xmm0', 'xmm1', 'xmm2', 'xmm3', 'xmm4', 'xmm5', 'xmm6', 'xmm7']

class X86Gen:
    """
    Converte a lista de strings de TAC em x86-64 assembly com recurso a syntax NASM e System V AMD64 ABI
     (Existem calls com recurso a C -> libc)

    Calling convention:
      - Os primeiros 6 argumentos integer/pointer vão em rdi, rsi, rdx, rcx, r8, r9.
      - Os primeiros 8 argumentos `real` vão em xmm0..xmm7 (contador separado dos inteiros).
      - OS restatnes são empilhados right-to-left; Quem chama limpa a stack.
      - O return vai no rax (inteiro/ponteiro) ou em xmm0 (real).
      - rbp é o pointer da frame; Todas as variaveis estão em offsets negativos a partir de rbp
      — params(argumentos) são guradado a partir do prologue, para que a tabela de simbolos seja uniforme
      - rsp tem de ser alinhada a 16-byte antes de qualquer instrução de call.
      - Calls variádicas (printf, scanf) requerem al = 0 (sem argumentos).

    Tipos `inteiro`/`real`: o TAC em si é texto sem tipos, por isso o tipo de
    cada nome (variável/temporário) vem de um mapa externo (`types`,
    calculado pelo TACGen a partir da análise semântica) mais as assinaturas
    das funções (`signatures`, para saber o tipo de retorno/parâmetros de uma
    chamada). Valores `real` são sempre doubles de 64 bits, movidos via
    registos XMM/instruções SSE2 (movsd/addsd/.../cvtsi2sd/cvttsd2si).
    """

    def __init__(self):
        self._text = []
        self._str_literals = {}
        self._fmt_used = set()
        self.types = {}
        self.signatures = {}
        self.array_names = set()

    #-------------------------#
    # BASE DE PRODUCAO DO ASM #
    #-------------------------#
    def generate(self, tac_code, types=None, signatures=None, array_names=None):
        self.types = types or {}
        self.signatures = signatures or {}
        self.array_names = array_names or set()

        for line in tac_code:
            m = re.fullmatch(r'(\w+) = "(.*)"', line.strip())
            if m:
                self._str_literals[m.group(1)] = m.group(2)

        for func_name, func_lines in self._split_functions(tac_code):
            self._gen_function(func_name, func_lines)

        return self._build_output()

    def print_code(self, code):
        print(code)

    # ---------------#
    # Inicializações #
    # ---------------#
    def _split_functions(self, code):
        functions = []
        name = None
        lines = []
        # Split do TAC em [(name, [body_lines])] por funcao
        for raw in code:
            s = raw.strip()
            m = re.fullmatch(r'func (\w+):', s)
            if m:
                name, lines = m.group(1), []
            elif s == 'endfunc':
                if name is not None:
                    functions.append((name, lines))
                    name = None
            elif name is not None:
                lines.append(s)
        return functions

    def _collect_locals(self, func_lines, func_name=None):
        """
        Two-pass scan do corpo de uma função.

        Nota: o TAC usa a palavra 'param' tanto para parâmetros formais de uma
        função como para argumentos antes de uma chamada. Como a função
        principal não recebe parâmetros formais, não devemos interpretar um
        'param' inicial em principal como parâmetro da função; pode ser apenas
        o primeiro argumento de uma chamada, por exemplo escrever(dobro(5)).
        """
        params = []
        local_set = set()
        in_header = (func_name != "principal")

        for line in func_lines:
            if not line:
                continue

            if in_header:
                m = re.fullmatch(r'param (\w+)', line)
                if m:
                    params.append(m.group(1))
                    continue
                in_header = False

            # Linhas que nao adidicona novas variaveis
            if re.fullmatch(r'\w+:', line):                             continue
            if re.fullmatch(r'goto \w+', line):                         continue
            if re.fullmatch(r'ifFalse \S+ goto \S+', line):             continue
            if re.fullmatch(r'if \S+ goto \S+', line):                  continue
            if re.fullmatch(r'return( \S+)?', line):                    continue
            if re.fullmatch(r'(write|writec|writes|writev) \S+', line): continue
            if re.fullmatch(r'param \S+', line):                        continue

            m = re.fullmatch(r'(\w+) = .+', line)
            if m:
                local_set.add(m.group(1))

        # Arrays
        for line in func_lines:
            m = re.fullmatch(r'(\w+)\[\w+\] = \S+', line)
            if m:
                local_set.add(m.group(1))

        local_set -= set(params)
        return params, sorted(local_set)

    # ------------------------------#
    # Helpers de tipo inteiro/real  #
    # ------------------------------#
    def _kind(self, token):
        """Devolve 'real' ou 'inteiro' para o PROPRIO valor de `token`
        (registo/memoria que vai ser lido/escrito). Um vetor e sempre um
        apontador (inteiro), seja qual for o tipo dos seus elementos -
        por isso e verificado antes de consultar `self.types`, que para um
        nome de vetor guarda o tipo dos ELEMENTOS, nao do apontador em si."""
        if token in self.array_names:
            return 'inteiro'
        if token in self.types:
            return self.types[token]
        if re.fullmatch(r'-?\d+\.\d+', token):
            return 'real'
        return 'inteiro'

    def _element_kind(self, array_token):
        """Tipo dos elementos de um vetor (usado em ALOAD/ASTORE)."""
        return self.types.get(array_token, 'inteiro')

    def _double_bits(self, token):
        return struct.unpack('<Q', struct.pack('<d', float(token)))[0]

    def _load_gpr(self, token, sym, e, reg='rax'):
        """Carrega o valor de `token` para o registo geral `reg`,
        convertendo de double para inteiro (truncado) se necessário."""
        if self._kind(token) == 'real':
            self._load_xmm(token, sym, e, 'xmm15')
            e(f"    cvttsd2si {reg}, xmm15")
        elif token in sym:
            e(f"    mov {reg}, {sym[token]}")
        else:
            e(f"    mov {reg}, {token}")

    def _load_xmm(self, token, sym, e, xmm='xmm0'):
        """Carrega o valor de `token` para o registo XMM `xmm` (double),
        convertendo de inteiro se necessário."""
        if token in sym:
            if self._kind(token) == 'real':
                e(f"    movsd {xmm}, {sym[token]}")
            else:
                e(f"    mov rax, {sym[token]}")
                e(f"    cvtsi2sd {xmm}, rax")
        elif re.fullmatch(r'-?\d+\.\d+', token):
            bits = self._double_bits(token)
            e(f"    mov rax, {bits}")
            e(f"    movq {xmm}, rax")
        else:
            e(f"    mov rax, {token}")
            e(f"    cvtsi2sd {xmm}, rax")

    def _store_from_gpr(self, target, sym, e, reg='rax'):
        """Guarda o inteiro em `reg` na slot de `target`, convertendo para
        double se o destino for `real`."""
        if self._kind(target) == 'real':
            e(f"    cvtsi2sd xmm0, {reg}")
            e(f"    movsd {sym[target]}, xmm0")
        else:
            e(f"    mov {sym[target]}, {reg}")

    def _store_from_xmm(self, target, sym, e, xmm='xmm0'):
        """Guarda o double em `xmm` na slot de `target`, convertendo para
        inteiro (truncado) se o destino for `inteiro`."""
        if self._kind(target) == 'real':
            e(f"    movsd {sym[target]}, {xmm}")
        else:
            e(f"    cvttsd2si rax, {xmm}")
            e(f"    mov {sym[target]}, rax")

    #---------------------------#
    # PROCESSAMENTO DAS FUNCOES #
    #---------------------------#
    def _gen_function(self, name, lines):
        params, local_names = self._collect_locals(lines, name)

        all_vars = list(params) + local_names
        sym = {v: f"[rbp - {(i + 1) * 8}]" for i, v in enumerate(all_vars)}

        # Tamano da frame tem de ser de 16 para menter a stack alinhada.
        frame_size = len(all_vars) * 8
        if frame_size % 16 != 0:
            frame_size = (frame_size // 16 + 1) * 16

        is_main = (name == "principal")
        entry = "main" if is_main else f"_{name}"
        own_sig = self.signatures.get(name, {})
        ret_type = own_sig.get('returnType', 'inteiro')
        own_param_types = own_sig.get('paramTypes', [])
        e = self._text.append

        # Prologue
        e(f"{entry}:")
        e(f"    push rbp")
        e(f"    mov rbp, rsp")
        if frame_size > 0:
            e(f"    sub rsp, {frame_size}")

        # Guarda os argumentos nas suas stack slots (contadores separados
        # para registos inteiros/ponteiro vs registos XMM/real). A classe de
        # registo vem de paramTypes (que ja trata arrays sempre como
        # apontador/inteiro, independentemente do tipo dos seus elementos),
        # nao do tipo de elemento em self.types.
        int_i = 0
        float_i = 0
        for idx, p in enumerate(params):
            p_class = own_param_types[idx] if idx < len(own_param_types) else self.types.get(p, 'inteiro')
            if p_class == 'real':
                if float_i < len(_XMM_ARG_REGS):
                    e(f"    movsd {sym[p]}, {_XMM_ARG_REGS[float_i]}")
                else:
                    e(f"    movsd xmm0, [rbp + {16 + (float_i - len(_XMM_ARG_REGS)) * 8}]")
                    e(f"    movsd {sym[p]}, xmm0")
                float_i += 1
            else:
                if int_i < len(_ARG_REGS):
                    e(f"    mov {sym[p]}, {_ARG_REGS[int_i]}")
                else:
                    # args >=7 ficam em [rbp + 16], [rbp + 24], na frame do caller
                    # Copiamos para o nosso layout de offsets negativos.
                    e(f"    mov rax, [rbp + {16 + (int_i - len(_ARG_REGS)) * 8}]")
                    e(f"    mov {sym[p]}, rax")
                int_i += 1

        in_header = (name != "principal")
        pending_args = []   # args acumulados entre 'param' e 'call'

        for line in lines:
            if not line:
                continue

            # Ultrapassa o header que já foi establecido
            if in_header:
                if re.fullmatch(r'param \w+', line):
                    continue
                in_header = False

            # ---- Labels ----
            m = re.fullmatch(r'(\w+):', line)
            if m:
                e(f".{m.group(1)}:")
                continue

            # ----  Jump ----
            m = re.fullmatch(r'goto (\w+)', line)
            if m:
                e(f"    jmp .{m.group(1)}")
                continue

            # ---- Jump Condicional (false) ----
            # A condicao de um if/while/for e sempre o resultado de uma
            # comparacao/logica, logo e sempre 'inteiro' (booleano 0/1).
            m = re.fullmatch(r'ifFalse (\S+) goto (\S+)', line)
            if m:
                cond, lbl = m.group(1), m.group(2)
                e(f"    mov rax, {self._op(cond, sym)}")
                e(f"    cmp rax, 0")
                e(f"    je .{lbl}")
                continue

            # ---- Jump Condicional (true) ----
            m = re.fullmatch(r'if (\S+) goto (\S+)', line)
            if m:
                cond, lbl = m.group(1), m.group(2)
                e(f"    mov rax, {self._op(cond, sym)}")
                e(f"    cmp rax, 0")
                e(f"    jne .{lbl}")
                continue

            # ---- Return ----
            m = re.fullmatch(r'return (\S+)', line)
            if m:
                if ret_type == 'real':
                    self._load_xmm(m.group(1), sym, e, 'xmm0')
                else:
                    self._load_gpr(m.group(1), sym, e, 'rax')
                e(f"    mov rsp, rbp")
                e(f"    pop rbp")
                if is_main:
                    e(f"    xor eax, eax")
                e(f"    ret")
                continue

            # ---- Void return ----
            if line == 'return':
                e(f"    mov rsp, rbp")
                e(f"    pop rbp")
                if is_main:
                    e(f"    xor eax, eax")
                e(f"    ret")
                continue

            # ---- write (Int/Real) ----
            m = re.fullmatch(r'write (\S+)', line)
            if m:
                val = m.group(1)
                if self._kind(val) == 'real':
                    self._fmt_used.add('fmt_real_out')
                    self._load_xmm(val, sym, e, 'xmm0')
                    e(f"    lea rdi, [rel fmt_real_out]")
                    # AL = numero de registos XMM usados nesta chamada variadica
                    # (exigido pela System V ABI para que o printf/va_arg saiba
                    # quantos argumentos de virgula flutuante foram passados).
                    e(f"    mov eax, 1")
                    e(f"    call printf")
                else:
                    self._fmt_used.add('fmt_int_out')
                    e(f"    lea rdi, [rel fmt_int_out]")
                    self._load_gpr(val, sym, e, 'rsi')
                    e(f"    xor eax, eax")
                    e(f"    call printf")
                continue

            # ---- writec (Char) ----
            m = re.fullmatch(r'writec (\S+)', line)
            if m:
                self._fmt_used.add('fmt_char_out')
                e(f"    lea rdi, [rel fmt_char_out]")
                self._load_gpr(m.group(1), sym, e, 'rsi')
                e(f"    xor eax, eax")
                e(f"    call printf")
                continue

            # ---- writes / writev (string pointer) ----
            m = re.fullmatch(r'(writes|writev) (\S+)', line)
            if m:
                self._fmt_used.add('fmt_str_out')
                e(f"    lea rdi, [rel fmt_str_out]")
                e(f"    mov rsi, {self._op(m.group(2), sym)}")
                e(f"    xor eax, eax")
                e(f"    call printf")
                continue

            # ---- t = read (int do stdin) ----
            m = re.fullmatch(r'(\w+) = read', line)
            if m:
                t = m.group(1)
                self._fmt_used.add('fmt_int_in')
                e(f"    lea rdi, [rel fmt_int_in]")
                e(f"    lea rsi, {sym[t]}")
                e(f"    xor eax, eax")
                e(f"    call scanf")
                continue

            # ---- t = readc (char do stdin) ----
            m = re.fullmatch(r'(\w+) = readc', line)
            if m:
                t = m.group(1)
                self._fmt_used.add('fmt_char_in')
                e(f"    lea rdi, [rel fmt_char_in]")
                e(f"    lea rsi, {sym[t]}")
                e(f"    xor eax, eax")
                e(f"    call scanf")
                continue

            # ---- t = reads (string do stdin) ----
            m = re.fullmatch(r'(\w+) = reads', line)
            if m:
                t = m.group(1)
                self._fmt_used.add('fmt_str_in')
                e(f"    lea rdi, [rel fmt_str_in]")
                e(f"    mov rsi, {sym[t]}")
                e(f"    xor eax, eax")
                e(f"    call scanf")
                continue

            # ---- param (agregador de argumentos antes da call) ----
            m = re.fullmatch(r'param (\S+)', line)
            if m:
                pending_args.append(m.group(1))
                continue

            # ---- t = call name, n ----
            m = re.fullmatch(r'(\w+) = call (\w+), (\d+)', line)
            if m:
                t, callee, n = m.group(1), m.group(2), int(m.group(3))

                sig = self.signatures.get(callee, {})
                param_types = sig.get('paramTypes', [])
                callee_ret = sig.get('returnType', 'inteiro')

                args = pending_args
                pending_args = []

                classified = []
                int_i2 = 0
                float_i2 = 0
                for i, arg in enumerate(args):
                    ptype = param_types[i] if i < len(param_types) else self._kind(arg)
                    if ptype == 'real':
                        slot = float_i2 if float_i2 < len(_XMM_ARG_REGS) else None
                        float_i2 += 1
                    else:
                        slot = int_i2 if int_i2 < len(_ARG_REGS) else None
                        int_i2 += 1
                    classified.append((ptype, arg, slot))

                # 1) Argumentos que nao cabem nos registos vao para a stack,
                #    da direita para a esquerda (na ordem original).
                for ptype, arg, slot in reversed(classified):
                    if slot is None:
                        if ptype == 'real':
                            self._load_xmm(arg, sym, e, 'xmm0')
                            e(f"    sub rsp, 8")
                            e(f"    movsd [rsp], xmm0")
                        else:
                            self._load_gpr(arg, sym, e, 'rax')
                            e(f"    push rax")

                # 2) Argumentos de registo, pela ordem original (fontes sao
                #    sempre memoria/literais, nunca outro registo de
                #    argumento, por isso nao ha risco de sobreescrita).
                for ptype, arg, slot in classified:
                    if slot is not None:
                        if ptype == 'real':
                            self._load_xmm(arg, sym, e, _XMM_ARG_REGS[slot])
                        else:
                            self._load_gpr(arg, sym, e, _ARG_REGS[slot])

                callee_label = "main" if callee == "principal" else f"_{callee}"
                e(f"    call {callee_label}")

                stack_bytes = sum(8 for _, _, slot in classified if slot is None)
                if stack_bytes:
                    e(f"    add rsp, {stack_bytes}")

                if callee_ret == 'real':
                    self._store_from_xmm(t, sym, e, 'xmm0')
                else:
                    self._store_from_gpr(t, sym, e, 'rax')
                continue

            # ---- strN = "..." (carrega o pointer para um string literal) ----
            m = re.fullmatch(r'(\w+) = "(.*)"', line)
            if m:
                sid = m.group(1)
                e(f"    lea rax, [rel {sid}_data]")
                e(f"    mov {sym[sid]}, rax")
                continue

            # ---- t = alloc N  /  t = array N (heap allocation) ----
            m = re.fullmatch(r'(\w+) = (alloc|array) (\S+)', line)
            if m:
                t, size = m.group(1), m.group(3)
                if size.lstrip('-').isdigit():
                    e(f"    mov rdi, {int(size) * 8}")
                else:
                    e(f"    mov rdi, {self._op(size, sym)}")
                    e(f"    imul rdi, 8")
                e(f"    call malloc")
                e(f"    mov {sym[t]}, rax")
                continue

            # ---- arr[idx] = val (array store) ----
            m = re.fullmatch(r'(\w+)\[(\w+)\] = (\S+)', line)
            if m:
                arr, idx, val = m.group(1), m.group(2), m.group(3)
                e(f"    mov rdx, {sym[arr]}")
                e(f"    mov rcx, {self._op(idx, sym)}")
                if self._element_kind(arr) == 'real':
                    self._load_xmm(val, sym, e, 'xmm0')
                    e(f"    movsd [rdx + rcx*8], xmm0")
                else:
                    self._load_gpr(val, sym, e, 'rax')
                    e(f"    mov [rdx + rcx*8], rax")
                continue

            # ---- t = arr[idx] (array load) ----
            m = re.fullmatch(r'(\w+) = (\w+)\[(\w+)\]', line)
            if m:
                t, arr, idx = m.group(1), m.group(2), m.group(3)
                e(f"    mov rdx, {sym[arr]}")
                e(f"    mov rcx, {self._op(idx, sym)}")
                if self._element_kind(arr) == 'real':
                    e(f"    movsd xmm0, [rdx + rcx*8]")
                    self._store_from_xmm(t, sym, e, 'xmm0')
                else:
                    e(f"    mov rax, [rdx + rcx*8]")
                    self._store_from_gpr(t, sym, e, 'rax')
                continue

            # ---- t = (type) val (type cast explicito inteiro<->real) ----
            m = re.fullmatch(r'(\w+) = \((\w+)\) (\S+)', line)
            if m:
                t, to_type, val = m.group(1), m.group(2), m.group(3)
                if to_type == 'real':
                    self._load_xmm(val, sym, e, 'xmm0')
                    self._store_from_xmm(t, sym, e, 'xmm0')
                else:
                    self._load_gpr(val, sym, e, 'rax')
                    self._store_from_gpr(t, sym, e, 'rax')
                continue

            # ---- t = -val  /  t = !val  (unary) ----
            m = re.fullmatch(r'(\w+) = ([!-])(\S+)', line)
            if m:
                t, op, val = m.group(1), m.group(2), m.group(3)
                if self._kind(val) == 'real':
                    self._load_xmm(val, sym, e, 'xmm0')
                    if op == '-':
                        e(f"    pxor xmm1, xmm1")
                        e(f"    subsd xmm1, xmm0")
                        self._store_from_xmm(t, sym, e, 'xmm1')
                    else:  # !
                        e(f"    pxor xmm1, xmm1")
                        e(f"    comisd xmm0, xmm1")
                        e(f"    sete al")
                        e(f"    movzx eax, al")
                        self._store_from_gpr(t, sym, e, 'rax')
                else:
                    e(f"    mov rax, {self._op(val, sym)}")
                    if op == '-':
                        e(f"    neg rax")
                    else:  # !
                        e(f"    cmp rax, 0")
                        e(f"    sete al")
                        e(f"    movzx eax, al")
                    self._store_from_gpr(t, sym, e, 'rax')
                continue

            # ---- t = a op b  (operações aritmeticas/relacionais) ----
            m = re.fullmatch(r'(\w+) = (\S+) ([+\-*/%]|<=?|>=?|==|!=) (\S+)', line)
            if m:
                t, left, op, right = m.group(1), m.group(2), m.group(3), m.group(4)
                self._gen_binop(t, left, op, right, sym, e)
                continue

            # ---- t = val  (copy / load, com widening implicito inteiro->real) ----
            m = re.fullmatch(r'(\w+) = (\S+)', line)
            if m:
                t, val = m.group(1), m.group(2)
                if self._kind(val) == 'real' or self._kind(t) == 'real':
                    self._load_xmm(val, sym, e, 'xmm0')
                    self._store_from_xmm(t, sym, e, 'xmm0')
                else:
                    e(f"    mov rax, {self._op(val, sym)}")
                    e(f"    mov {sym[t]}, rax")
                continue

        # Workarround para as funções Void
        e(f"    mov rsp, rbp")
        e(f"    pop rbp")
        if is_main:
            e(f"    xor eax, eax")
        e(f"    ret")
        e(f"")

    def _gen_binop(self, t, left, op, right, sym, e):
        kind = 'real' if self._kind(left) == 'real' or self._kind(right) == 'real' else 'inteiro'

        if kind == 'real':
            self._load_xmm(left, sym, e, 'xmm0')
            self._load_xmm(right, sym, e, 'xmm1')
            if op == '+':
                e(f"    addsd xmm0, xmm1")
            elif op == '-':
                e(f"    subsd xmm0, xmm1")
            elif op == '*':
                e(f"    mulsd xmm0, xmm1")
            elif op in ('/', '%'):
                # MOCP nao define '%' para reais; a analise semantica so
                # permite '%' quando ambos os operandos sao inteiro, por
                # isso este ramo so e mesmo exercitado para '/'.
                e(f"    divsd xmm0, xmm1")
            else:
                setcc = {'<': 'setb', '<=': 'setbe', '>': 'seta',
                         '>=': 'setae', '==': 'sete', '!=': 'setne'}[op]
                e(f"    comisd xmm0, xmm1")
                e(f"    {setcc} al")
                e(f"    movzx eax, al")
                self._store_from_gpr(t, sym, e, 'rax')
                return
            self._store_from_xmm(t, sym, e, 'xmm0')
            return

        e(f"    mov rax, {self._op(left, sym)}")
        if op == '+':
            e(f"    add rax, {self._op(right, sym)}")
        elif op == '-':
            e(f"    sub rax, {self._op(right, sym)}")
        elif op == '*':
            e(f"    mov rcx, {self._op(right, sym)}")
            e(f"    imul rax, rcx")
        elif op in ('/', '%'):
            e(f"    cqo")
            e(f"    mov rcx, {self._op(right, sym)}")
            e(f"    idiv rcx")
            if op == '%':
                e(f"    mov rax, rdx")
        else:
            setcc = {'<': 'setl', '<=': 'setle', '>': 'setg',
                     '>=': 'setge', '==': 'sete', '!=': 'setne'}[op]
            e(f"    cmp rax, {self._op(right, sym)}")
            e(f"    {setcc} al")
            e(f"    movzx eax, al")
        self._store_from_gpr(t, sym, e, 'rax')

    def _op(self, val, sym):
        if val in sym:
            return sym[val]
        if re.fullmatch(r'-?\d+(\.\d+)?', val):
            return val
        return val  # !! Operação Indefenida sai e devolve erro !!

    # --------------#
    # OUTPUT FINAL  #
    # --------------#
    def _build_output(self):
        out = []
        out.append("; Para compilar: nasm -f elf64 out.asm -o out.o && gcc out.o -no-pie -o out")
        out.append("")

        out.append("section .data")
        if 'fmt_int_out'  in self._fmt_used: out.append('    fmt_int_out  db "%ld", 10, 0')
        if 'fmt_int_in'   in self._fmt_used: out.append('    fmt_int_in   db "%ld", 0')
        if 'fmt_real_out' in self._fmt_used: out.append('    fmt_real_out db "%f", 10, 0')
        if 'fmt_char_out' in self._fmt_used: out.append('    fmt_char_out db "%c", 0')
        if 'fmt_char_in'  in self._fmt_used: out.append('    fmt_char_in  db " %c", 0')
        if 'fmt_str_out'  in self._fmt_used: out.append('    fmt_str_out  db "%s", 0')
        if 'fmt_str_in'   in self._fmt_used: out.append('    fmt_str_in   db "%s", 0')

        for sid, val in self._str_literals.items():
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            out.append(f'    {sid}_data db "{escaped}", 0')

        out.append("")
        out.append("section .text")
        out.append("    global main")
        out.append("    extern printf, scanf, malloc")
        out.append("")

        out.extend(self._text)
        out.append("section .note.GNU-stack noalloc noexec nowrite progbits")
        return "\n".join(out)
