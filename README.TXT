# MOPC Compiler - Grupo "It Compiles on My Machine" 🚀

[cite_start]Projeto desenvolvido para a UC de Compilação (21018) da Universidade Aberta.
[cite_start]Este compilador processa a linguagem **MOCP** (My Own C in Português).

## 🛠️ Pré-requisitos
* **Python 3.10+**
* [cite_start]**Java Runtime Environment (JRE)** (necessário para correr o gerador ANTLR).
* **ANTLR 4.13.x** (ficheiro `.jar` incluído ou via sistema).

## 📦 Configuração do Ambiente (Primeira vez)

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/Goncalves95/MOPC-Compiler-UAberta-A.git](https://github.com/Goncalves95/MOPC-Compiler-UAberta-A.git)
   cd MOPC-Compiler-UAberta-A
   ```

2. **Criar ambiente virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instalar dependências:**
   ```bash
   Windows:
   py -m pip install -r requirements.txt

   macOS / Linux:
   python3 -m pip install -r requirements.txt
   ```


## Como Gerar o Parser

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o src grammar/MOCP.g4
```


## Como Executar

```bash
Windows:
py src/main.py examples/teste.mocp

macOS / Linux:
python3 src/main.py examples/teste.mocp
```

## Como Executar a AST

```bash
Windows:
py src/main.py examples/teste.mocp --ast

macOS / Linux:
python3 src/main.py examples/teste.mocp --ast
```

Nota: O comando --ast exporta a estrutura lógica do programa em formato JSON para facilitar a visualização da hierarquia de comandos.


## Alterar a Gramática

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o src grammar/MOCP.g4
# Nota: garante que os ficheiros .py são gerados na raiz da pasta src.
```

## 👥 Autores (Grupo: It Compiles on My Machine - Efolio A)
* **Fernando Gonçalves** - [Goncalves95](https://github.com/Goncalves95)
* **Ricardo Costa** - [Rtheghost](https://github.com/Rtheghost)

## 📚 Fontes e Referências
* **Enunciado do E-fólio A**: Disciplina de Compilação (UAb).
* **ANTLR4 Documentation**: [antlr.org](https://www.antlr.org/)
* **Python Runtime for ANTLR4**: [PyPI antlr4-python3-runtime](https://pypi.org/project/antlr4-python3-runtime/)
* **Assistência de IA**: Esta implementação contou com o apoio da Inteligência Artificial (Gemini/ChatGPT) para resolução de conflitos.
