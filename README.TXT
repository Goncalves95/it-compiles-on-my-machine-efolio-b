================================================================================
               MOCP COMPILER - E-FÓLIO B
               Unidade Curricular: Compilação (21018)
================================================================================

Grupo: It Compiles on My Machine 🚀
Estudantes:
  - Fernando Gonçalves
  - Ricardo Costa
  - Luís Almeida
  - Paulo Almeida

--------------------------------------------------------------------------------
1. DESCRIÇÃO DO REPOSITÓRIO
--------------------------------------------------------------------------------
Este repositório contém a evolução do compilador para a linguagem MOCP 
(My Own C in Português). O foco desta fase (E-fólio B) centra-se no 
pipeline de Análise Semântica, Geração de Código Intermédio (Three 
Address Code - TAC) com avaliação em curto-circuito, e Otimização 
Local de código intermédio (Constant Folding e Simplificação Algébrica).

--------------------------------------------------------------------------------
2. REQUISITOS DO SISTEMA
--------------------------------------------------------------------------------
- Python 3.10 ou superior
- Java Runtime Environment (JRE) instalado (obrigatório para compilar a gramática)
- Biblioteca antlr4-python3-runtime (versão 4.13.1)

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

Exemplos Práticos Incluídos:

  A) Executar código válido com Curto-Circuito Lógico:
     python src/main.py examples/curto_circuito.mocp --ast

  B) Executar o teste base funcional:
     python src/main.py examples/teste.mocp --ast

  C) Testar a robustez com Erros Sintáticos/Semânticos:
     python src/main.py examples/erro_sintatico.mocp --ast
     python src/main.py examples/erro_if_sem_chavetas.mocp --ast
     python src/main.py examples/erro_keyword_c.mocp --ast

Nota: A flag `--ast` exporta a estrutura lógica em JSON, valida as regras 
semânticas e dispara o motor TAC intermédio de forma sequencial.

--------------------------------------------------------------------------------
6. SCRIPT DE AUTOMAÇÃO DE TESTES (POWERSHELL - WINDOWS)
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
7. 📚 FONTES E REFERÊNCIAS
--------------------------------------------------------------------------------
- Enunciados e Especificações dos E-fólios A e B (UAb).
- Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers: Principles, 
  Techniques, and Tools (Dragon Book).
- Assistência de IA: Esta implementação contou com o apoio de Inteligência Artificial 
  (Gemini) no desenho estratégico do pipeline.