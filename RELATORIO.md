# Relatório — MOCP Compiler — E-fólio Global

Unidade Curricular: Compilação (21018)
Grupo: It Compiles on My Machine 🚀 — Fernando Gonçalves, Ricardo Costa, Luís Almeida, Paulo Almeida

> Este documento é a base de trabalho para o relatório a entregar. Cobre as
> correções feitas em resposta ao feedback do e-fólio B e a nova fase de
> geração de código final exigida no e-fólio Global. Deve ser adaptado/revisto
> pelo grupo antes da entrega oficial.

## 1. Pipeline geral

```
.mocp
  -> Lexer/Parser (ANTLR, grammar/MOCP.g4)
  -> AST (src/ast_builder.py)
  -> Análise Semântica (src/semantic_analyzer.py)
  -> Geração de TAC (src/tac_gen.py)
  -> Otimização local do TAC (src/tac_optimizer.py)
  -> Geração de código final x86-64 (src/x86_gen.py) [EM FINALIZAÇÃO]
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

*(Secção em finalização — o grupo optou por gerar x86-64 real, NASM +
System V AMD64 ABI, com chamadas a `printf`/`scanf`/`malloc` da libc, em vez
de uma máquina simulada própria. Esta secção será completada com a descrição
da ABI, o modelo de memória/stack frames, suporte a `inteiro`/`real`, e um
exemplo `.mocp -> TAC -> x86-64 -> execução real`, depois de validado com
`nasm`+`gcc`.)*

## 5. Como testar

```
# pipeline completo, mostra TAC + TAC otimizado
python src/main.py examples/teste_fatorial.mocp --ast

# gera o código x86-64 (grava out.asm)
python src/main.py examples/teste_fatorial.mocp --asm

# montar e ligar com nasm + gcc (ambiente Linux/WSL/Docker)
nasm -f elf64 out.asm -o out.o && gcc out.o -no-pie -o out && ./out
```
