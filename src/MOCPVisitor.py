# Generated from grammar/MOCP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MOCPParser import MOCPParser
else:
    from MOCPParser import MOCPParser

# This class defines a complete generic visitor for a parse tree produced by MOCPParser.

class MOCPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MOCPParser#program.
    def visitProgram(self, ctx:MOCPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#item.
    def visitItem(self, ctx:MOCPParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#prototype.
    def visitPrototype(self, ctx:MOCPParser.PrototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#functionDef.
    def visitFunctionDef(self, ctx:MOCPParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#principalDef.
    def visitPrincipalDef(self, ctx:MOCPParser.PrincipalDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#functionHeader.
    def visitFunctionHeader(self, ctx:MOCPParser.FunctionHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#returnType.
    def visitReturnType(self, ctx:MOCPParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#baseType.
    def visitBaseType(self, ctx:MOCPParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#paramList.
    def visitParamList(self, ctx:MOCPParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#param.
    def visitParam(self, ctx:MOCPParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#paramDecl.
    def visitParamDecl(self, ctx:MOCPParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#block.
    def visitBlock(self, ctx:MOCPParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#statement.
    def visitStatement(self, ctx:MOCPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#declaration.
    def visitDeclaration(self, ctx:MOCPParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:MOCPParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#initDeclarator.
    def visitInitDeclarator(self, ctx:MOCPParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#declarator.
    def visitDeclarator(self, ctx:MOCPParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#assignment.
    def visitAssignment(self, ctx:MOCPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#lvalue.
    def visitLvalue(self, ctx:MOCPParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#returnStmt.
    def visitReturnStmt(self, ctx:MOCPParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#ifStmt.
    def visitIfStmt(self, ctx:MOCPParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#whileStmt.
    def visitWhileStmt(self, ctx:MOCPParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#forStmt.
    def visitForStmt(self, ctx:MOCPParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#forInit.
    def visitForInit(self, ctx:MOCPParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#forUpdate.
    def visitForUpdate(self, ctx:MOCPParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#initDeclaratorListNoSemi.
    def visitInitDeclaratorListNoSemi(self, ctx:MOCPParser.InitDeclaratorListNoSemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#functionCall.
    def visitFunctionCall(self, ctx:MOCPParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#builtInCall.
    def visitBuiltInCall(self, ctx:MOCPParser.BuiltInCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#argumentList.
    def visitArgumentList(self, ctx:MOCPParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#expr.
    def visitExpr(self, ctx:MOCPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:MOCPParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:MOCPParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#equalityExpr.
    def visitEqualityExpr(self, ctx:MOCPParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MOCPParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MOCPParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MOCPParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MOCPParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#castExpr.
    def visitCastExpr(self, ctx:MOCPParser.CastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#primary.
    def visitPrimary(self, ctx:MOCPParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MOCPParser.ArrayLiteralContext):
        return self.visitChildren(ctx)



del MOCPParser