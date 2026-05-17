from MOCPVisitor import MOCPVisitor
from antlr4 import ParserRuleContext


class ASTBuilder(MOCPVisitor):
    def visitProgram(self, ctx):
        # Versão segura para iterar sobre os itens do programa
        items = []
        # O ANTLR pode gerar ctx.item() ou ctx.getChildren()
        child_nodes = ctx.item() if hasattr(ctx, 'item') else [ctx.getChild(i) for i in range(ctx.getChildCount())]
        
        for node in child_nodes:
            # Ignorar o token <EOF> que não tem método visit
            if hasattr(node, 'getRuleIndex') or isinstance(node, ParserRuleContext):
                res = self.visit(node)
                if res: items.append(res)
        
        return {
            "type": "Program",
            "items": items
        }

    def visitItem(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitPrototype(self, ctx):
        # prototype : functionHeader SEMI
        #           | VAZIO PRINCIPAL LPAR VAZIO RPAR SEMI
        if ctx.functionHeader():
            return {
                "type": "Prototype",
                "header": self.visit(ctx.functionHeader())
            }

        return {
            "type": "Prototype",
            "header": {
                "type": "FunctionHeader",
                "name": "principal",
                "returnType": "vazio",
                "params": []
            }
        }

    def visitFunctionDef(self, ctx):
        header = self.visit(ctx.functionHeader())
        return {
            "type": "FunctionDef",
            "name": header["name"],
            "returnType": header["returnType"],
            "params": header["params"],
            "body": self.visit(ctx.block()),
            "isPrincipal": False
        }

    def visitPrincipalDef(self, ctx):
        return {
            "type": "FunctionDef",
            "name": "principal",
            "returnType": "vazio",
            "params": [],
            "body": self.visit(ctx.block()),
            "isPrincipal": True
        }

    def visitFunctionHeader(self, ctx):
        return {
            "type": "FunctionHeader",
            "name": ctx.ID().getText(),
            "returnType": self.visit(ctx.returnType()),
            "params": self.visit(ctx.paramList()) if ctx.paramList() else []
        }

    def visitReturnType(self, ctx):
        return ctx.getText()

    def visitBaseType(self, ctx):
        return ctx.getText()

    def visitParamList(self, ctx):
        return [self.visit(param) for param in ctx.param()]

    def visitParam(self, ctx):
        # Tenta ctx.baseType(), se falhar usa index 0
        base_type_node = ctx.baseType() if hasattr(ctx, 'baseType') else ctx.getChild(0)
        # Tenta ctx.paramDecl(), se falhar usa index 1
        param_decl_node = ctx.paramDecl() if hasattr(ctx, 'paramDecl') else ctx.getChild(1)
        
        return {
            "type": "Param",
            "baseType": self.visit(base_type_node),
            "decl": self.visit(param_decl_node)
        }

    def visitParamDecl(self, ctx):
        text = ctx.getText()

        if text == "[]":
            return {
                "type": "ParamDecl",
                "kind": "array",
                "name": None
            }

        if text.endswith("[]"):
            return {
                "type": "ParamDecl",
                "kind": "array",
                "name": ctx.ID().getText()
            }

        return {
            "type": "ParamDecl",
            "kind": "scalar",
            "name": ctx.ID().getText()
        }

    def visitBlock(self, ctx):
        return {
            "type": "Block",
            "statements": [self.visit(stmt) for stmt in ctx.statement()]
        }

    def visitStatement(self, ctx):
        if ctx.getChildCount() == 1 and ctx.getText() == ";":
            return {"type": "EmptyStatement"}

        return self.visit(ctx.getChild(0))

    def visitDeclaration(self, ctx):
        # Tenta ctx.baseType(), se falhar usa o primeiro filho (index 0)
        base_type_node = ctx.baseType() if hasattr(ctx, 'baseType') else ctx.getChild(0)
        # Tenta ctx.initDeclaratorList(), se falhar usa o segundo filho (index 1)
        decl_list_node = ctx.initDeclaratorList() if hasattr(ctx, 'initDeclaratorList') else ctx.getChild(1)
        
        return {
            "type": "Declaration",
            "baseType": self.visit(base_type_node),
            "declarators": self.visit(decl_list_node)
        }

    def visitInitDeclaratorList(self, ctx):
        return [self.visit(item) for item in ctx.initDeclarator()]

    def visitInitDeclaratorListNoSemi(self, ctx):
        return [self.visit(item) for item in ctx.initDeclarator()]

    def visitInitDeclarator(self, ctx):
        return {
            "type": "InitDeclarator",
            "target": self.visit(ctx.declarator()),
            "value": self.visit(ctx.expr()) if ctx.expr() else None
        }

    def visitDeclarator(self, ctx):
        if ctx.expr():
            return {
                "type": "ArrayDeclarator",
                "name": ctx.ID().getText(),
                "size": self.visit(ctx.expr())
            }

        if ctx.getChildCount() > 1:
            return {
                "type": "ArrayDeclarator",
                "name": ctx.ID().getText(),
                "size": None
            }

        return {
            "type": "Identifier",
            "name": ctx.ID().getText()
        }

    def visitAssignment(self, ctx):
        return {
            "type": "Assignment",
            "target": self.visit(ctx.lvalue()),
            "value": self.visit(ctx.expr())
        }

    def visitLvalue(self, ctx):
        if ctx.expr():
            return {
                "type": "ArrayAccess",
                "name": ctx.ID().getText(),
                "index": self.visit(ctx.expr())
            }

        return {
            "type": "Identifier",
            "name": ctx.ID().getText()
        }

    def visitReturnStmt(self, ctx):
        return {
            "type": "Return",
            "value": self.visit(ctx.expr()) if ctx.expr() else None
        }

    def visitIfStmt(self, ctx):
        blocks = ctx.block()
        return {
            "type": "If",
            "condition": self.visit(ctx.expr()),
            "then": self.visit(blocks[0]),
            "else": self.visit(blocks[1]) if len(blocks) > 1 else None
        }

    def visitWhileStmt(self, ctx):
        return {
            "type": "While",
            "condition": self.visit(ctx.expr()),
            "body": self.visit(ctx.block())
        }

    def visitForStmt(self, ctx):
        return {
            "type": "For",
            "init": self.visit(ctx.forInit()) if ctx.forInit() else None,
            "condition": self.visit(ctx.expr()) if ctx.expr() else None,
            "update": self.visit(ctx.forUpdate()) if ctx.forUpdate() else None,
            "body": self.visit(ctx.block())
        }

    def visitForInit(self, ctx):
        if ctx.assignment():
            return self.visit(ctx.assignment())

        return {
            "type": "Declaration",
            "baseType": self.visit(ctx.baseType()),
            "declarators": self.visit(ctx.initDeclaratorListNoSemi())
        }

    def visitForUpdate(self, ctx):
        return self.visit(ctx.assignment())

    def visitFunctionCall(self, ctx):
        if ctx.builtInCall():
            return self.visit(ctx.builtInCall())

        return {
            "type": "Call",
            "name": ctx.ID().getText(),
            "args": self.visit(ctx.argumentList()) if ctx.argumentList() else []
        }

    def visitBuiltInCall(self, ctx):
        name = ctx.getChild(0).getText()

        expr_ctx = ctx.expr()
        if expr_ctx is None:
            args = []
        else:
            args = [self.visit(expr_ctx)]

        return {
            "type": "BuiltInCall",
            "name": name,
            "args": args
        }

    def visitArgumentList(self, ctx):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitExpr(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitLogicalOrExpr(self, ctx):
        return self._build_left_assoc(ctx)

    def visitLogicalAndExpr(self, ctx):
        return self._build_left_assoc(ctx)

    def visitEqualityExpr(self, ctx):
        return self._build_left_assoc(ctx)

    def visitRelationalExpr(self, ctx):
        return self._build_left_assoc(ctx)

    def visitAdditiveExpr(self, ctx):
        return self._build_left_assoc(ctx)

    def visitMultiplicativeExpr(self, ctx):
        return self._build_left_assoc(ctx)

    def visitUnaryExpr(self, ctx):
        if ctx.getChildCount() == 2:
            return {
                "type": "UnaryOp",
                "op": ctx.getChild(0).getText(),
                "operand": self.visit(ctx.getChild(1))
            }
        return self.visit(ctx.getChild(0))

    def visitCastExpr(self, ctx):
        return {
            "type": "Cast",
            "to": self.visit(ctx.baseType()),
            "value": self.visit(ctx.unaryExpr())
        }

    def visitPrimary(self, ctx):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            value = float(text) if "." in text else int(text)
            return {
                "type": "Number",
                "value": value
            }

        if ctx.STRING():
            text = ctx.STRING().getText()
            return {
                "type": "String",
                "value": text[1:-1]
            }

        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        if ctx.lvalue():
            return self.visit(ctx.lvalue())

        if ctx.arrayLiteral():
            return self.visit(ctx.arrayLiteral())

        return self.visit(ctx.expr())

    def visitArrayLiteral(self, ctx):
        return {
            "type": "ArrayLiteral",
            "elements": [self.visit(expr) for expr in ctx.expr()]
        }

    def _build_left_assoc(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        node = self.visit(ctx.getChild(0))
        i = 1

        while i < ctx.getChildCount():
            op = ctx.getChild(i).getText()
            rhs = self.visit(ctx.getChild(i + 1))
            node = {
                "type": "BinaryOp",
                "op": op,
                "left": node,
                "right": rhs
            }
            i += 2

        return node