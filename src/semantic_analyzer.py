class SemanticAnalyzer:
    def __init__(self):
        self.errors = []
        self.functions = {}
        self.prototypes = {}
        self.scopes = []
        self.current_function = None

    def analyze(self, ast):
        # Primeiro recolhe assinaturas para permitir chamadas a funcoes ja prototipadas.
        self._collect_functions(ast)

        for item in ast.get("items", []):
            if item["type"] == "FunctionDef":
                self._check_function(item)

        if "principal" not in self.functions:
            self._error("Funcao principal nao definida.")

        return self.errors

    def _collect_functions(self, ast):
        seen_non_proto = False

        for item in ast.get("items", []):
            if item["type"] == "Prototype":
                if seen_non_proto:
                    self._error("Prototipo declarado depois de uma funcao ou variavel global.")
                header = item["header"]
                self._register_signature(self.prototypes, header, "Prototipo")
            elif item["type"] == "FunctionDef":
                seen_non_proto = True
                self._register_signature(self.functions, item, "Funcao")
                proto = self.prototypes.get(item["name"])
                if proto and not self._same_signature(proto, self._signature(item)):
                    self._error(f"Definicao da funcao '{item['name']}' nao corresponde ao prototipo.")
            elif item["type"] == "Declaration":
                seen_non_proto = True

    def _register_signature(self, table, node, label):
        name = node["name"]
        signature = self._signature(node)

        if name in table:
            self._error(f"{label} '{name}' duplicado.")
            return

        table[name] = signature

    def _signature(self, node):
        params = []
        for param in node.get("params", []):
            decl = param["decl"]
            params.append({
                "baseType": param["baseType"],
                "kind": decl["kind"],
            })

        return {
            "returnType": node["returnType"],
            "params": params,
        }

    def _same_signature(self, left, right):
        return left["returnType"] == right["returnType"] and left["params"] == right["params"]

    def _check_function(self, node):
        self.current_function = node
        self.scopes = [{}]

        for param in node.get("params", []):
            decl = param["decl"]
            if decl["name"] is not None:
                self._define_var(decl["name"], param["baseType"], decl["kind"])

        self._check_node(node["body"])
        self.scopes = []
        self.current_function = None

    def _check_node(self, node):
        node_type = node["type"]

        match node_type:
            case "Block":
                self._push_scope()
                for statement in node["statements"]:
                    self._check_node(statement)
                self._pop_scope()

            case "Declaration":
                for decl in node["declarators"]:
                    self._check_declarator(node["baseType"], decl)

            case "Assignment":
                self._check_lvalue(node["target"])
                value_type = self._check_expr(node["value"])
                target_type = self._lvalue_type(node["target"])
                self._check_assign_compat(target_type, value_type, "atribuicao")

            case "BuiltInCall" | "Call":
                self._check_expr(node)

            case "Return":
                self._check_return(node)

            case "If":
                self._check_expr(node["condition"])
                self._check_node(node["then"])
                if node["else"] is not None:
                    self._check_node(node["else"])

            case "While":
                self._check_expr(node["condition"])
                self._check_node(node["body"])

            case "For":
                if node["init"] is not None:
                    self._check_node(node["init"])
                if node["condition"] is not None:
                    self._check_expr(node["condition"])
                if node["update"] is not None:
                    self._check_node(node["update"])
                self._check_node(node["body"])

            case "EmptyStatement":
                return

    def _check_declarator(self, base_type, node):
        target = node["target"]

        if target["type"] == "Identifier":
            self._define_var(target["name"], base_type, "scalar")
        elif target["type"] == "ArrayDeclarator":
            self._define_var(target["name"], base_type, "array")
            if target["size"] is not None:
                self._check_expr(target["size"])

        if node["value"] is not None:
            value_type = self._check_expr(node["value"])
            self._check_assign_compat(base_type, value_type, "inicializacao")

    def _check_return(self, node):
        expected = self.current_function["returnType"]
        value = node["value"]

        if expected == "vazio" and value is not None:
            self._error(f"Funcao '{self.current_function['name']}' nao deve retornar valor.")
        elif expected != "vazio" and value is None:
            self._error(f"Funcao '{self.current_function['name']}' deve retornar valor.")
        elif value is not None:
            value_type = self._check_expr(value)
            self._check_assign_compat(expected, value_type, "retorno")

    def _check_expr(self, node):
        node_type = node["type"]

        match node_type:
            case "Number":
                return "real" if isinstance(node["value"], float) else "inteiro"

            case "String":
                return "string"

            case "Identifier":
                symbol = self._resolve_var(node["name"])
                if symbol is None:
                    self._error(f"Variavel '{node['name']}' usada antes de ser declarada.")
                    return "unknown"
                return symbol["baseType"]

            case "ArrayAccess":
                self._check_lvalue(node)
                return self._resolve_var(node["name"])["baseType"] if self._resolve_var(node["name"]) else "unknown"

            case "ArrayLiteral":
                for element in node["elements"]:
                    self._check_expr(element)
                return "array"

            case "UnaryOp":
                return self._check_expr(node["operand"])

            case "BinaryOp":
                left_type = self._check_expr(node["left"])
                right_type = self._check_expr(node["right"])
                op = node["op"]

                if op in ["==", "!=", "<", "<=", ">", ">=", "&&", "||"]:
                    return "inteiro"

                return self._infer_arith_type(left_type, right_type, op)

            case "Cast":
                self._check_expr(node["value"])
                return node["to"]

            case "Call":
                return self._check_call(node)

            case "BuiltInCall":
                return self._check_builtin(node)

        return "unknown"

    def _infer_arith_type(self, left_type, right_type, op):
        # Tipo numerico resultante de +,-,*,/,%: real se algum operando for real,
        # inteiro se ambos forem inteiro; tipos nao numericos (string/array) sao erro.
        if left_type == "unknown" or right_type == "unknown":
            return "unknown"

        if left_type in ("inteiro", "real") and right_type in ("inteiro", "real"):
            return "real" if "real" in (left_type, right_type) else "inteiro"

        self._error(f"Operacao aritmetica '{op}' invalida entre os tipos '{left_type}' e '{right_type}'.")
        return "unknown"

    def _lvalue_type(self, node):
        if node["type"] not in ("Identifier", "ArrayAccess"):
            return "unknown"

        symbol = self._resolve_var(node["name"])
        return symbol["baseType"] if symbol else "unknown"

    def _check_assign_compat(self, target_type, value_type, context):
        # So valida coercoes entre os tipos numericos inteiro/real; ignora
        # string/array/unknown para nao gerar falsos positivos noutros casos.
        if target_type not in ("inteiro", "real") or value_type not in ("inteiro", "real"):
            return

        if target_type == value_type:
            return

        if target_type == "real" and value_type == "inteiro":
            return

        self._error(
            f"Atribuicao incompativel em {context}: nao e possivel atribuir um valor "
            f"'{value_type}' a um destino '{target_type}' sem conversao explicita."
        )

    def _check_lvalue(self, node):
        if node["type"] == "Identifier":
            if self._resolve_var(node["name"]) is None:
                self._error(f"Variavel '{node['name']}' usada antes de ser declarada.")
            return

        if node["type"] == "ArrayAccess":
            symbol = self._resolve_var(node["name"])
            if symbol is None:
                self._error(f"Vetor '{node['name']}' usado antes de ser declarado.")
            elif symbol["kind"] != "array":
                self._error(f"Variavel '{node['name']}' nao e um vetor.")
            self._check_expr(node["index"])

    def _check_call(self, node):
        name = node["name"]
        signature = self.functions.get(name) or self.prototypes.get(name)

        if signature is None:
            self._error(f"Funcao '{name}' chamada antes de ser declarada.")
            for arg in node["args"]:
                self._check_expr(arg)
            return "unknown"

        if len(node["args"]) != len(signature["params"]):
            self._error(f"Funcao '{name}' chamada com numero errado de argumentos.")

        for arg in node["args"]:
            self._check_expr(arg)

        return signature["returnType"]

    def _check_builtin(self, node):
        for arg in node["args"]:
            self._check_expr(arg)

        if node["name"] in ["ler", "lerc"]:
            return "inteiro"
        if node["name"] == "lers":
            return "array"

        return "vazio"

    def _define_var(self, name, base_type, kind):
        if name in self.scopes[-1]:
            self._error(f"Variavel '{name}' ja declarada neste escopo.")
            return

        self.scopes[-1][name] = {
            "baseType": base_type,
            "kind": kind,
        }

    def _resolve_var(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def _push_scope(self):
        self.scopes.append({})

    def _pop_scope(self):
        self.scopes.pop()

    def _error(self, message):
        self.errors.append(f"[SEMANTICO] {message}")
