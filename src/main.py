import sys
import os
import json
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNode

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

try:
    from MOCPLexer import MOCPLexer
    from MOCPParser import MOCPParser
    from ast_builder import ASTBuilder
except ImportError as e:
    print(f"[ERRO CRÍTICO] Não foi possível importar os ficheiros gerados: {e}")
    sys.exit(1)


class CollectingErrorListener(ErrorListener):
    def __init__(self, source_name="ANALISADOR"):
        super().__init__()
        self.source_name = source_name
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"[{self.source_name}] linha {line}:{column} -> {msg}"
        self.errors.append(error_msg)
        print(error_msg)


def print_parse_tree(node, parser, indent=0):
    prefix = "  " * indent

    if isinstance(node, TerminalNode):
        text = node.getText().replace("\n", "\\n")
        token_type = node.symbol.type
        if 0 <= token_type < len(parser.symbolicNames):
            token_name = parser.symbolicNames[token_type]
        else:
            token_name = str(token_type)

        print(f"{prefix}- TOKEN({token_name}): {text}")
        return

    rule_index = node.getRuleIndex()
    rule_name = parser.ruleNames[rule_index]
    print(f"{prefix}{rule_name}")

    for i in range(node.getChildCount()):
        print_parse_tree(node.getChild(i), parser, indent + 1)


def parse_arguments():
    args = sys.argv[1:]

    show_tree = False
    show_ast = False
    input_file = None

    for arg in args:
        if arg == "--tree":
            show_tree = True
        elif arg == "--ast":
            show_ast = True
        elif input_file is None:
            input_file = arg
        else:
            print("[ERRO] Argumentos a mais.")
            print("Uso: py src/main.py <ficheiro.mocp> [--tree] [--ast]")
            sys.exit(1)

    if input_file is None:
        print("Uso: py src/main.py <ficheiro.mocp> [--tree] [--ast]")
        sys.exit(1)

    return input_file, show_tree, show_ast

def main():
    input_file, show_tree, show_ast = parse_arguments()

    if not os.path.exists(input_file):
        print(f"[ERRO] Ficheiro não encontrado: {input_file}")
        sys.exit(1)

    input_stream = FileStream(input_file, encoding="utf-8")

    lexer = MOCPLexer(input_stream)
    lexer_listener = CollectingErrorListener("LEXER")
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_listener)

    token_stream = CommonTokenStream(lexer)

    parser = MOCPParser(token_stream)
    parser_listener = CollectingErrorListener("PARSER")
    parser.removeErrorListeners()
    parser.addErrorListener(parser_listener)

    try:
        tree = parser.program()

        total_errors = len(lexer_listener.errors) + len(parser_listener.errors)

        if total_errors > 0:
            print(f"\n[FALHA] Foram detetados {total_errors} erro(s).")
        else:
            print("\n[SUCESSO] Código MOCP validado com sucesso!")

            if show_tree:
                print("\n=== PARSE TREE ===")
                print_parse_tree(tree, parser)
                
            if show_ast:
                print("\n=== AST ===")
                ast = ASTBuilder().visit(tree)
                print(json.dumps(ast, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"[ERRO] Exceção durante a análise: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()