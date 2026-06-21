# Relatório — MOCP Compiler — E-fólio Global

Unidade Curricular: Compilação (21018)
Grupo: It Compiles on My Machine 🚀 — Fernando Gonçalves, Ricardo Costa, Luís Almeida, Paulo Almeida


## 1. Pipeline geral

```
.mocp
  -> Lexer/Parser (ANTLR, grammar/MOCP.g4)
  -> AST (src/ast_builder.py)
  -> Análise Semântica (src/semantic_analyzer.py)
  -> Geração de TAC (src/tac_gen.py)
  -> Otimização local do TAC (src/tac_optimizer.py)
  -> Geração de código final x86-64 (src/x86_gen.py)
  -> nasm + gcc (montagem/ligação) -> executável nativo
```

O front-end (e-fólios A/B) mantém-se inalterado na sua arquitetura: o TAC
continua a ser a representação intermédia oficial, sobre a qual atua o
otimizador. A novidade do e-fólio Global é o back-end, que consome o **TAC já
otimizado** e gera o código final — não recria nada a partir da AST,
reaproveitando assim o trabalho da fase de otimização.

## 2. Diferenças face ao e-fólio B

O feedback recebido identificou 5 pontos concretos. Os 4 primeiros eram bugs
de código; o 5º era uma discrepância entre o relatório anterior e o
otimizador. Todos foram corrigidos.

### 2.1 Ciclo `for` com cláusulas opcionais (`tac_gen.py`)

**Antes:** o gerador assumia sempre `init`, `condition` e `update` presentes,
chamando `self.generate(node["init"])` etc. incondicionalmente. Como a
gramática permite `forInit?`, `expr?` e `forUpdate?`, um ciclo como
`para(;;){...}` ou `para(;i<10;){...}` fazia `self.generate(None)` e
rebentava com uma excepção (`node["type"]` sobre `None`).

**Depois:** cada cláusula só é gerada se não for `None`; quando a condição
está ausente, não se emite o salto `ifFalse`, o que equivale a `while(true)`.

```python
# depois (src/tac_gen.py)
if node["init"] is not None:
    self.generate(node["init"])
...
if node["condition"] is not None:
    cond = self.generate(node["condition"])
    self.emit(f"ifFalse {cond} goto {label_end}")
...
if node["update"] is not None:
    self.generate(node["update"])
```

**Prova:** `examples/teste_for_opcional.mocp` cobre `para(;;)` (com saída via
`retornar` dentro de um `se`) e `para(; i < limite ;)` (sem init/update). TAC
gerado para o primeiro caso, sem qualquer `ifFalse` antes do corpo (condição
ausente == sempre verdadeira):

```
L1:
write i
t1 = i + 1
i = t1
t2 = i >= 3
ifFalse t2 goto L3
return
L3:
goto L1
```

### 2.2 Tamanho de array inferido a partir do literal (`tac_gen.py`)

**Antes:** em `inteiro v[] = {1,2,3};`, com `size is None`, o gerador fazia
sempre `alloc 0`, independentemente do literal de inicialização.

**Depois:** se o tamanho for omitido e existir um `ArrayLiteral`, o `alloc`
usa `len(elements)`.

```python
# depois (src/tac_gen.py)
if target_node["size"] is not None:
    size = self.generate(target_node["size"])
elif node["value"] is not None and node["value"]["type"] == "ArrayLiteral":
    size = len(node["value"]["elements"])
else:
    size = 0
```

**Prova:** `examples/teste_array_sem_tamanho.mocp` (`inteiro v[] = {1,2,3,4};`)
agora gera `v = alloc 4` em vez de `v = alloc 0`, e o `--run` imprime
corretamente `1 2 3 4`.

### 2.3 `goto` redundante no `if` sem `senao` (`tac_gen.py`)

**Antes:** mesmo sem ramo `else`, o gerador emitia sempre `goto label_end`
depois do bloco `then` — instrução sem efeito (o fluxo já cai naturalmente em
`label_end:`), que só acrescentava ruído ao IR antes da otimização.

**Depois:** o `goto` só é emitido quando existe de facto um ramo `else` (caso
em que é necessário para saltar por cima dele).

```python
# depois (src/tac_gen.py)
if has_else:
    self.emit(f"goto {label_end}")
    self.emit(f"{label_else}:")
    self.generate(node["else"])
self.emit(f"{label_end}:")
```

**Prova:** o `if` sem `else` em `examples/teste_for_opcional.mocp` gera
`return` seguido diretamente de `L3:` — sem `goto L3` entre os dois.

### 2.4 Inferência de tipos em operações aritméticas e coerções (`semantic_analyzer.py`)

**Antes:** `_check_expr` devolvia `"unknown"` para `+ - * / %`, sem validar
nada; atribuições e retornos não comparavam tipos, pelo que
`inteiro x; x = expressaoReal;` passava sem qualquer aviso.

**Depois:** operações aritméticas inferem `real` se algum operando for
`real`, `inteiro` se ambos forem `inteiro`, e geram erro semântico para tipos
incompatíveis (`string`/`array`). Atribuições, inicializações e `retornar`
passam por `_check_assign_compat`, que permite o *widening* `inteiro → real`
e rejeita o *narrowing* `real → inteiro` sem `Cast` explícito.

**Prova — antes/depois real:** `examples/erro_tipo_incompativel.mocp`
(`real y = 3.5; inteiro x; x = y;`) antes da correção era aceite sem erros;
agora produz:

```
[SEMANTICO] Atribuicao incompativel em atribuicao: nao e possivel atribuir um
valor 'real' a um destino 'inteiro' sem conversao explicita.
```

### 2.5 Simplificação `x * 0` no otimizador (`tac_optimizer.py`)

**Antes:** o relatório do e-fólio B mencionava a simplificação `x * 0`, mas
`_simplify_neutral_ops` só tratava `*1`, `+0`, `-0` e `/1` — a regra não
existia de facto no código.

**Depois:** adicionadas as regras `x * 0 → 0` e `0 * x → 0`. É seguro porque,
ao nível do TAC, qualquer subexpressão com efeitos secundários (chamadas a
funções) já foi avaliada para o seu próprio temporário antes de entrar nesta
multiplicação — eliminar a multiplicação não elimina a chamada que gerou o
operando.

**Prova:** `examples/teste_otimizacao_mult_zero.mocp` (`y = x * 0;`, com `x`
variável e não literal, para não ser apanhado só pelo *constant folding*).
TAC antes da otimização: `t1 = x * 0`. TAC otimizado: `t1 = 0`.

## 3. Evidência comparativa do e-fólio A (rejeição de keywords de C)

O feedback pediu evidência mais concreta das melhorias do e-fólio A. O commit
`fc6327b` ("Reject C keywords as MOCP identifiers") introduziu a regra
`C_KEYWORD` na gramática, que antes não existia:

```diff
+C_KEYWORD
+    : 'int'
+    | 'double'
+    | 'void'
+    | 'main'
+    | 'if'
+    | 'else'
+    | 'while'
+    | 'for'
+    | 'return'
+    | 'read'
+    | 'readc'
+    | 'reads'
+    | 'write'
+    | 'writec'
+    | 'writev'
+    | 'writes'
+    ;
```

**Antes desta regra**, tokens como `void`, `main`, `if`, `while`, etc. caíam
na regra `ID` (`[a-zA-Z_][a-zA-Z0-9_]*`) por não haver nenhuma regra lexical
mais específica a "capturá-los" primeiro — ou seja, `void principal(...)` ou
`inteiro if = 1;` seriam lexicamente aceites como identificadores válidos,
contrariando o objetivo de impedir que palavras-chave de C fossem usadas como
identificadores em MOCP.

**Depois**, com `C_KEYWORD` definida antes de `ID` (o ANTLR resolve
ambiguidades lexicais pela ordem das regras), esses tokens passam a ser
rejeitados na fase de parsing. Prova com o compilador atual:

```
$ python src/main.py examples/erro_keyword_c.mocp
[PARSER] linha 1:0 -> mismatched input 'void' expecting {<EOF>, 'inteiro', 'real', 'vazio'}
[FALHA] Foram detetados 1 erro(s).

$ python src/main.py examples/erro_keyword_c_como_identificador.mocp
[PARSER] linha 2:12 -> mismatched input 'if' expecting ID
[FALHA] Foram detetados 1 erro(s).
```

## 4. Geração de código final

### 4.1 Linguagem escolhida

**x86-64 real** (sintaxe NASM, System V AMD64 ABI), gerado em `src/x86_gen.py`
a partir do TAC já otimizado. Em vez de uma máquina virtual inventada, o
código gerado é montado e ligado com ferramentas standard (`nasm` + `gcc`,
contra a `libc`) e corre nativamente — `printf`/`scanf` tratam toda a E/S, e
`malloc` aloca os vetores. Convenção de chamada:

- Os primeiros 6 argumentos inteiros/apontador vão em `rdi, rsi, rdx, rcx,
  r8, r9`; os primeiros 8 argumentos `real` (sempre `double` de 64 bits) vão
  em `xmm0..xmm7` — contadores **separados** por classe de registo, exatamente
  como a ABI exige quando uma chamada mistura os dois tipos.
- O valor de retorno vai em `rax` (inteiro/apontador) ou `xmm0` (`real`).
- Cada função tem a sua própria stack frame (`push rbp` / `mov rbp,rsp` /
  `sub rsp,N`), com todas as variáveis/temporários em offsets negativos a
  partir de `rbp`. Isto dá **recursão correta de fábrica** (testado com
  `fact(8) = 40320`): cada chamada recursiva tem a sua própria frame, sem
  qualquer estado partilhado entre chamadas.
- Vetores são sempre alocados no heap (`malloc(N*8)`) e passados por
  referência (o apontador de 8 bytes); o `param nome_do_vetor` do TAC
  corresponde a passar esse apontador como argumento normal.

### 4.2 Suporte a `inteiro` e `real`

O TAC é texto sem tipos — por isso o `tac_gen.py` foi reforçado para também
calcular, durante a geração, o tipo (`inteiro`/`real`) de cada variável e
temporário (`tac.types`), mais que nomes correspondem a vetores
(`tac.array_names`, necessário porque um vetor é **sempre um apontador**,
independentemente do tipo dos seus elementos). Esta informação, em conjunto
com as assinaturas das funções vindas da análise semântica, é passada ao
`X86Gen` para decidir, em cada instrução, entre o caminho inteiro (`rax`,
`add`/`idiv`/...) e o caminho real via SSE2 (`xmm`, `movsd`/`addsd`/`divsd`/
`cvtsi2sd`/`cvttsd2si`).

**Bug encontrado e corrigido durante a integração:** a primeira versão do
gerador x86-64 (commits `d4ff5a7`/`f5efcc5`) tratava todos os valores como
inteiros de 64 bits — incluindo `real`. Isto tinha dois efeitos: literais
reais geravam assembly inválido (`mov rax, 3.5`, que o `nasm` rejeita), e
divisões `real` (ex. `soma / tamanho` em `media()`) usavam `idiv` (divisão
inteira), dando resultados errados para médias não-exatas (`1` e `2` dava
`1`, em vez de `1.5`). Confirmado a gerar o código e a executá-lo num
ambiente Linux (container Docker com `nasm`+`gcc`) antes e depois da
correção. Depois de adicionar o caminho SSE2 completo (literais reais
codificados como bits IEEE-754, conversões `inteiro↔real` em cada
atribuição/chamada/retorno, e o registo `AL` corrigido para `1` nas chamadas
variádicas a `printf` que passam um `real` — exigido pela ABI para que o
`va_arg` interno saiba que um registo XMM foi usado), `1` e `2` passam a dar
`1.500000` corretamente.

### 4.3 Exemplo completo

`examples/teste_media_vetor.mocp`, entrada `tamanho=2`, valores `1` e `2`:

```
TAC otimizado (excerto, funcao media):
func media:
param v
param tamanho
...
t10 = soma / tamanho
return t10
endfunc

x86-64 gerado (mesmo excerto):
_media:
    ...
.L4:
    movsd xmm0, [rbp - 32]      ; soma
    mov rax, [rbp - 16]         ; tamanho (inteiro)
    cvtsi2sd xmm1, rax          ; widening inteiro -> real
    divsd xmm0, xmm1
    movsd [rbp - 40], xmm0
    movsd xmm0, [rbp - 40]
    mov rsp, rbp
    pop rbp
    ret

Montagem e execução real (Docker, gcc:13 + nasm):
$ nasm -f elf64 out.asm -o out.o && gcc out.o -no-pie -o out
$ printf '2\n1\n2\n' | ./out
Introduza tamanho e valores: 1.500000
```

### 4.4 Limitações conhecidas

- Funções com mais de 6 argumentos inteiros ou 8 argumentos `real` (overflow
  para a stack) não foram testadas com combinações mistas — nenhum exemplo
  do grupo usa mais de 2 parâmetros, pelo que esse caminho é best-effort.
- Não há verificação de "todos os caminhos retornam valor"; uma função não
  `vazio` que termine sem `retornar` deixa o valor de retorno indefinido.

## 5. Como testar

```
# pipeline completo, mostra TAC + TAC otimizado
python src/main.py examples/teste_fatorial.mocp --ast

# gera o código x86-64 (grava out.asm)
python src/main.py examples/teste_media_vetor.mocp --asm

# montar e ligar com nasm + gcc (ambiente Linux/WSL/Docker; ex. imagem gcc:13 + apt install nasm)
nasm -f elf64 out.asm -o out.o && gcc out.o -no-pie -o out && ./out
```
