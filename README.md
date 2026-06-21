# MOCP COMPILER - E-FÓLIO GLOBAL
Unidade Curricular: Compilação (21018)

Grupo: It Compiles on My Machine 🚀

Estudantes:
  - Fernando Gonçalves
  - Ricardo Costa
  - Luís Almeida
  - Paulo Almeida

--------------------------------------------------------------------------------
1. DESCRIÇÃO DO REPOSITÓRIO
--------------------------------------------------------------------------------
Este repositório contém o compilador completo para a linguagem MOCP
(My Own C in Português): análise léxica/sintática (ANTLR), análise semântica,
geração de Código Intermédio (Three Address Code - TAC) com avaliação em
curto-circuito, Otimização Local do TAC (Constant Folding e Simplificação
Algébrica), e Geração de Código Final para x86-64 real (NASM + System V
AMD64 ABI), com suporte a `inteiro` e `real` (via SSE2).

Esta versão inclui correções de robustez ao pipeline de TAC e inferência de
tipos na análise semântica, feitas em resposta ao feedback do e-fólio B, e a
fase de Geração de Código Final do e-fólio Global (detalhes e exemplos em
RELATORIO.md).

--------------------------------------------------------------------------------
2. REQUISITOS DO SISTEMA
--------------------------------------------------------------------------------
- Python 3.10 ou superior
- Java Runtime Environment (JRE) instalado (obrigatório para compilar a gramática)
- Biblioteca antlr4-python3-runtime (versão 4.13.1)
- `nasm` + `gcc` (obrigatório apenas para montar/executar o código final
  x86-64 gerado pela flag `--asm`; ver PASSO 4). No Windows, o caminho mais
  simples é via WSL ou Docker Desktop — ver instruções no PASSO 4.

--------------------------------------------------------------------------------
3. PASSO 1: CONFIGURAÇÃO DO AMBIENTE (WINDOWS & MACOS)
--------------------------------------------------------------------------------

No Windows (PowerShell):
  1. Permitir a execução de scripts no sistema:
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  2. Criar o ambiente virtual (.venv):
     python -m venv .venv
  3. Ativar o ambiente virtual:
     .venv\Scripts\Activate.ps1
  4. Instalar as dependências do projeto:
     pip install -r requirements.txt

No macOS / Linux (Terminal):
  1. Criar o ambiente virtual (.venv):
     python3 -m venv .venv
  2. Ativar o ambiente virtual:
     source .venv/bin/activate
  3. Instalar as dependências do projeto:
     pip install -r requirements.txt

--------------------------------------------------------------------------------
4. PASSO 2: REGENERAR O PARSER ANTLR (OBRIGATÓRIO NA PRIMEIRA EXECUÇÃO)
--------------------------------------------------------------------------------
Para gerar as classes do Lexer e do Parser em Python na pasta "src" a partir 
da especificação gramatical em "grammar/MOCP.g4", execute o comando Java na 
raiz do projeto:

java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -Xexact-output-dir -o src grammar/MOCP.g4

--------------------------------------------------------------------------------
5. PASSO 3: COMO EXECUTAR O COMPILADOR
--------------------------------------------------------------------------------
O compilador aceita ficheiros com a extensão `.mocp`. Por omissão, o pipeline
realiza a análise sintática, a validação semântica, a geração de TAC e exibe
o TAC Otimizado no ecrã.

Comando Geral (A partir da raiz do projeto, com o ambiente virtual ativo):
  python src/main.py <caminho_do_ficheiro.mocp> --ast

Flags disponíveis:
  --tree   Mostra a parse tree do ANTLR.
  --ast    Mostra a AST em JSON.
  --asm    Gera o código x86-64 (NASM), mostra-o no ecrã e grava-o em out.asm.

Exemplos Práticos Incluídos:

  A) Executar código válido com Curto-Circuito Lógico:
     python src/main.py examples/curto_circuito.mocp --ast

  B) Executar o teste base funcional:
     python src/main.py examples/teste.mocp --ast

  C) Testar a robustez com Erros Sintáticos/Semânticos:
     python src/main.py examples/erro_sintatico.mocp --ast
     python src/main.py examples/erro_if_sem_chavetas.mocp --ast
     python src/main.py examples/erro_keyword_c.mocp --ast
     python src/main.py examples/erro_tipo_incompativel.mocp --ast

  D) Gerar o código final x86-64 e correr o executável (requer nasm + gcc,
     por exemplo num ambiente Linux/WSL/Docker):
     python src/main.py examples/teste_fatorial.mocp --asm
     nasm -f elf64 out.asm -o out.o && gcc out.o -no-pie -o out && ./out

Nota: A flag `--ast` exporta a estrutura lógica em JSON, valida as regras 
semânticas e dispara o motor TAC intermédio de forma sequencial. Detalhes da
fase de código final (ABI, suporte a `real`, exemplos) em RELATORIO.md.

--------------------------------------------------------------------------------
6. PASSO 4: TESTAR O CÓDIGO FINAL x86-64 (MONTAR E CORRER COM NASM + GCC)
--------------------------------------------------------------------------------
A flag `--asm` gera o ficheiro `out.asm` na raiz do projeto. Para o montar,
ligar e executar como um programa nativo é preciso `nasm` + `gcc`. No
Windows, a forma mais simples é usar WSL ou Docker (escolher uma das duas):

Opção A — WSL (Windows Subsystem for Linux):
  1. Instalar o WSL, se ainda não tiver (PowerShell como Administrador,
     reiniciar se for pedido):
       wsl --install
  2. Abrir a distro instalada (ex. Ubuntu) e instalar as ferramentas:
       sudo apt update && sudo apt install -y nasm gcc
  3. No Windows, gerar o assembly (com o ambiente virtual ativo):
       python src/main.py examples/teste_fatorial.mocp --asm
  4. Dentro do WSL, ir até à pasta do projeto (em /mnt/c/...) e montar+correr:
       nasm -f elf64 out.asm -o out.o && gcc out.o -no-pie -o out && ./out

Opção B — Docker Desktop:
  1. Instalar e arrancar o Docker Desktop (docker.com/products/docker-desktop).
  2. Gerar o assembly (com o ambiente virtual ativo):
       python src/main.py examples/teste_fatorial.mocp --asm
  3. Montar e correr num container temporário (PowerShell, a partir da raiz
     do projeto):
       docker run --rm -i -v ${PWD}:/work -w /work gcc:13 bash -c "apt-get update -qq && apt-get install -y -qq nasm && nasm -f elf64 out.asm -o out.o && gcc out.o -no-pie -o out && ./out"

No macOS / Linux, `nasm` e `gcc` podem ser instalados diretamente (ex.
`brew install nasm` / `sudo apt install nasm gcc`), sem precisar de WSL nem
Docker.

Nota: exemplos que leem input (ex. `teste_fatorial.mocp`, `teste_media_vetor.mocp`)
pedem dados ao executar `./out` — basta escrever o valor pedido e pressionar
Enter, ou usar `echo 5 | ./out` para automatizar.

--------------------------------------------------------------------------------
7. SCRIPT DE AUTOMAÇÃO DE TESTES (POWERSHELL - WINDOWS)
--------------------------------------------------------------------------------
Para varrer toda a pasta de exemplos e validar o comportamento do compilador
de forma automática sequencial, execute o seguinte bloco no PowerShell:

Get-ChildItem examples/*.mocp | ForEach-Object {
    Write-Host "`n==================================================" -ForegroundColor Cyan
    Write-Host "A TESTAR: $($_.Name)" -ForegroundColor Yellow
    Write-Host "==================================================" -ForegroundColor Cyan
    python src/main.py $_.FullName --ast
}

--------------------------------------------------------------------------------
8. 📚 FONTES E REFERÊNCIAS
--------------------------------------------------------------------------------
- Enunciados e Especificações dos E-fólios A e B (UAb).
- Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers: Principles, 
  Techniques, and Tools (Dragon Book).
- Assistência de IA: Esta implementação contou com o apoio de Inteligência Artificial 
  (Gemini) no desenho estratégico do pipeline.