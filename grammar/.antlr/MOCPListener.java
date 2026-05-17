// Generated from /Users/fernandogoncalves/repos/it-compiles-on-my-machine-efolio-b/grammar/MOCP.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MOCPParser}.
 */
public interface MOCPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MOCPParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MOCPParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MOCPParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#item}.
	 * @param ctx the parse tree
	 */
	void enterItem(MOCPParser.ItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#item}.
	 * @param ctx the parse tree
	 */
	void exitItem(MOCPParser.ItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#prototype}.
	 * @param ctx the parse tree
	 */
	void enterPrototype(MOCPParser.PrototypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#prototype}.
	 * @param ctx the parse tree
	 */
	void exitPrototype(MOCPParser.PrototypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#functionDef}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDef(MOCPParser.FunctionDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#functionDef}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDef(MOCPParser.FunctionDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#principalDef}.
	 * @param ctx the parse tree
	 */
	void enterPrincipalDef(MOCPParser.PrincipalDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#principalDef}.
	 * @param ctx the parse tree
	 */
	void exitPrincipalDef(MOCPParser.PrincipalDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#functionHeader}.
	 * @param ctx the parse tree
	 */
	void enterFunctionHeader(MOCPParser.FunctionHeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#functionHeader}.
	 * @param ctx the parse tree
	 */
	void exitFunctionHeader(MOCPParser.FunctionHeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#returnType}.
	 * @param ctx the parse tree
	 */
	void enterReturnType(MOCPParser.ReturnTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#returnType}.
	 * @param ctx the parse tree
	 */
	void exitReturnType(MOCPParser.ReturnTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#baseType}.
	 * @param ctx the parse tree
	 */
	void enterBaseType(MOCPParser.BaseTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#baseType}.
	 * @param ctx the parse tree
	 */
	void exitBaseType(MOCPParser.BaseTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(MOCPParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(MOCPParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(MOCPParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(MOCPParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#paramDecl}.
	 * @param ctx the parse tree
	 */
	void enterParamDecl(MOCPParser.ParamDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#paramDecl}.
	 * @param ctx the parse tree
	 */
	void exitParamDecl(MOCPParser.ParamDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(MOCPParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(MOCPParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(MOCPParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(MOCPParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(MOCPParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(MOCPParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#initDeclaratorList}.
	 * @param ctx the parse tree
	 */
	void enterInitDeclaratorList(MOCPParser.InitDeclaratorListContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#initDeclaratorList}.
	 * @param ctx the parse tree
	 */
	void exitInitDeclaratorList(MOCPParser.InitDeclaratorListContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#initDeclarator}.
	 * @param ctx the parse tree
	 */
	void enterInitDeclarator(MOCPParser.InitDeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#initDeclarator}.
	 * @param ctx the parse tree
	 */
	void exitInitDeclarator(MOCPParser.InitDeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#declarator}.
	 * @param ctx the parse tree
	 */
	void enterDeclarator(MOCPParser.DeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#declarator}.
	 * @param ctx the parse tree
	 */
	void exitDeclarator(MOCPParser.DeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(MOCPParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(MOCPParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#lvalue}.
	 * @param ctx the parse tree
	 */
	void enterLvalue(MOCPParser.LvalueContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#lvalue}.
	 * @param ctx the parse tree
	 */
	void exitLvalue(MOCPParser.LvalueContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(MOCPParser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(MOCPParser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(MOCPParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(MOCPParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(MOCPParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(MOCPParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(MOCPParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(MOCPParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(MOCPParser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(MOCPParser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void enterForUpdate(MOCPParser.ForUpdateContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void exitForUpdate(MOCPParser.ForUpdateContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#initDeclaratorListNoSemi}.
	 * @param ctx the parse tree
	 */
	void enterInitDeclaratorListNoSemi(MOCPParser.InitDeclaratorListNoSemiContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#initDeclaratorListNoSemi}.
	 * @param ctx the parse tree
	 */
	void exitInitDeclaratorListNoSemi(MOCPParser.InitDeclaratorListNoSemiContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(MOCPParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(MOCPParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#builtInCall}.
	 * @param ctx the parse tree
	 */
	void enterBuiltInCall(MOCPParser.BuiltInCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#builtInCall}.
	 * @param ctx the parse tree
	 */
	void exitBuiltInCall(MOCPParser.BuiltInCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(MOCPParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(MOCPParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MOCPParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MOCPParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#logicalOrExpr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpr(MOCPParser.LogicalOrExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#logicalOrExpr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpr(MOCPParser.LogicalOrExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#logicalAndExpr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpr(MOCPParser.LogicalAndExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#logicalAndExpr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpr(MOCPParser.LogicalAndExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#equalityExpr}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpr(MOCPParser.EqualityExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#equalityExpr}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpr(MOCPParser.EqualityExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#relationalExpr}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpr(MOCPParser.RelationalExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#relationalExpr}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpr(MOCPParser.RelationalExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#additiveExpr}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpr(MOCPParser.AdditiveExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#additiveExpr}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpr(MOCPParser.AdditiveExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#multiplicativeExpr}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpr(MOCPParser.MultiplicativeExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#multiplicativeExpr}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpr(MOCPParser.MultiplicativeExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpr(MOCPParser.UnaryExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpr(MOCPParser.UnaryExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#castExpr}.
	 * @param ctx the parse tree
	 */
	void enterCastExpr(MOCPParser.CastExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#castExpr}.
	 * @param ctx the parse tree
	 */
	void exitCastExpr(MOCPParser.CastExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(MOCPParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(MOCPParser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link MOCPParser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void enterArrayLiteral(MOCPParser.ArrayLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link MOCPParser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void exitArrayLiteral(MOCPParser.ArrayLiteralContext ctx);
}