import re

# System V AMD64 rgisters em ordem
_ARG_REGS = ['rdi', 'rsi', 'rdx', 'rcx', 'r8', 'r9']

class X86Gen:
    """
    Converte a lista de strings de TAC em x86-64 assembly com recurso a syntax NASM e System V AMD64 ABI
     (Existem calls com recurso a C -> libc)

    Calling convention:
      - Os primeiros 6 argumentos integer/pointer vão em rdi, rsi, rdx, rcx, r8, r9.
      - OS restatnes são empilhados right-to-left; Quem chama limpa a stack.
      - O return vai no rax.
      - rbp é o pointer da frame; Todas as variaveis estão em offsets negativos a partir de rbp
      — params(argumentos) são guradado a partir do prologue, para que a tabela de simbolos seja uniforme
      - rsp tem de ser alinhada a 16-byte antes de qualquer instrução de call.
      - Calls variádicas (printf, scanf) requerem al = 0 (sem argumentos).
    """

    def __init__(self):
        self._text = []           
        self._str_literals = {}   
        self._fmt_used = set()    

    #-------------------------#
    # BASE DE PRODUCAO DO ASM #
    #-------------------------#
    def generate(self, tac_code):
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
        e = self._text.append

        # Prologue
        e(f"{entry}:")
        e(f"    push rbp")
        e(f"    mov rbp, rsp")
        if frame_size > 0:
            e(f"    sub rsp, {frame_size}")

        # Guarda os argumentos nas suas stack slots
        for i, p in enumerate(params):
            if i < len(_ARG_REGS):
                e(f"    mov {sym[p]}, {_ARG_REGS[i]}")
            else:
                # args >=7 ficam em [rbp + 16], [rbp + 24], na frame do caller
                # Copiamos para o nosso layout de offsets negativos.
                e(f"    mov rax, [rbp + {16 + (i - len(_ARG_REGS)) * 8}]")
                e(f"    mov {sym[p]}, rax")

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
                e(f"    mov rax, {self._op(m.group(1), sym)}")
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

            # ---- write (Int) ----
            m = re.fullmatch(r'write (\S+)', line)
            if m:
                self._fmt_used.add('fmt_int_out')
                e(f"    lea rdi, [rel fmt_int_out]")
                e(f"    mov rsi, {self._op(m.group(1), sym)}")
                e(f"    xor eax, eax")
                e(f"    call printf")
                continue

            # ---- writec (Char) ----
            m = re.fullmatch(r'writec (\S+)', line)
            if m:
                self._fmt_used.add('fmt_char_out')
                e(f"    lea rdi, [rel fmt_char_out]")
                e(f"    mov rsi, {self._op(m.group(1), sym)}")
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

                reg_args   = pending_args[:len(_ARG_REGS)]
                stack_args = pending_args[len(_ARG_REGS):]
                pending_args = []

                # Push stack-overflow args da direita para a esquerda
                for arg in reversed(stack_args):
                    e(f"    mov rax, {self._op(arg, sym)}")
                    e(f"    push rax")

                # Load register args (must happen after stack pushes to avoid
                # clobbering rdi/rsi/... that might alias a source value)
                for i, arg in enumerate(reg_args):
                    e(f"    mov {_ARG_REGS[i]}, {self._op(arg, sym)}")

                callee_label = "main" if callee == "principal" else f"_{callee}"
                e(f"    call {callee_label}")

                if stack_args:
                    e(f"    add rsp, {len(stack_args) * 8}")

                e(f"    mov {sym[t]}, rax")
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
                e(f"    mov rax, {self._op(val, sym)}")
                e(f"    mov [rdx + rcx*8], rax")
                continue

            # ---- t = arr[idx] (array load) ----
            m = re.fullmatch(r'(\w+) = (\w+)\[(\w+)\]', line)
            if m:
                t, arr, idx = m.group(1), m.group(2), m.group(3)
                e(f"    mov rdx, {sym[arr]}")
                e(f"    mov rcx, {self._op(idx, sym)}")
                e(f"    mov rax, [rdx + rcx*8]")
                e(f"    mov {sym[t]}, rax")
                continue

            # ---- t = (type) val (type cast) ----
            m = re.fullmatch(r'(\w+) = \((\w+)\) (\S+)', line)
            if m:
                t, val = m.group(1), m.group(3)
                e(f"    mov rax, {self._op(val, sym)}")
                e(f"    mov {sym[t]}, rax")
                continue

            # ---- t = -val  /  t = !val  (unary) ----
            m = re.fullmatch(r'(\w+) = ([!-])(\S+)', line)
            if m:
                t, op, val = m.group(1), m.group(2), m.group(3)
                e(f"    mov rax, {self._op(val, sym)}")
                if op == '-':
                    e(f"    neg rax")
                else:  # !
                    e(f"    cmp rax, 0")
                    e(f"    sete al")
                    e(f"    movzx eax, al")
                e(f"    mov {sym[t]}, rax")
                continue

            # ---- t = a op b  (operações aritmeticas/relacionais) ----
            m = re.fullmatch(r'(\w+) = (\S+) ([+\-*/%]|<=?|>=?|==|!=) (\S+)', line)
            if m:
                t, left, op, right = m.group(1), m.group(2), m.group(3), m.group(4)
                self._gen_binop(t, left, op, right, sym, e)
                continue

            # ---- t = val  (copy / load) ----
            m = re.fullmatch(r'(\w+) = (\S+)', line)
            if m:
                t, val = m.group(1), m.group(2)
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
        e(f"    mov {sym[t]}, rax")

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
