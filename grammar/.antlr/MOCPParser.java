// Generated from /Users/fernandogoncalves/repos/it-compiles-on-my-machine-efolio-b/grammar/MOCP.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MOCPParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INTEIRO=1, REAL=2, VAZIO=3, PRINCIPAL=4, RETORNAR=5, SE=6, SENAO=7, ENQUANTO=8, 
		PARA=9, LER=10, LERC=11, LERS=12, ESCREVER=13, ESCREVERC=14, ESCREVERV=15, 
		ESCREVERS=16, ASSIGN=17, SEMI=18, COMMA=19, LPAR=20, RPAR=21, LBRACE=22, 
		RBRACE=23, LBRACK=24, RBRACK=25, OR=26, AND=27, NOT=28, EQ=29, NEQ=30, 
		LE=31, GE=32, LT=33, GT=34, PLUS=35, MINUS=36, STAR=37, DIV=38, MOD=39, 
		NUMBER=40, STRING=41, ID=42, BLOCK_COMMENT=43, LINE_COMMENT=44, WS=45;
	public static final int
		RULE_program = 0, RULE_item = 1, RULE_prototype = 2, RULE_functionDef = 3, 
		RULE_principalDef = 4, RULE_functionHeader = 5, RULE_returnType = 6, RULE_baseType = 7, 
		RULE_paramList = 8, RULE_param = 9, RULE_paramDecl = 10, RULE_block = 11, 
		RULE_statement = 12, RULE_declaration = 13, RULE_initDeclaratorList = 14, 
		RULE_initDeclarator = 15, RULE_declarator = 16, RULE_assignment = 17, 
		RULE_lvalue = 18, RULE_returnStmt = 19, RULE_ifStmt = 20, RULE_whileStmt = 21, 
		RULE_forStmt = 22, RULE_forInit = 23, RULE_forUpdate = 24, RULE_initDeclaratorListNoSemi = 25, 
		RULE_functionCall = 26, RULE_builtInCall = 27, RULE_argumentList = 28, 
		RULE_expr = 29, RULE_logicalOrExpr = 30, RULE_logicalAndExpr = 31, RULE_equalityExpr = 32, 
		RULE_relationalExpr = 33, RULE_additiveExpr = 34, RULE_multiplicativeExpr = 35, 
		RULE_unaryExpr = 36, RULE_castExpr = 37, RULE_primary = 38, RULE_arrayLiteral = 39;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "item", "prototype", "functionDef", "principalDef", "functionHeader", 
			"returnType", "baseType", "paramList", "param", "paramDecl", "block", 
			"statement", "declaration", "initDeclaratorList", "initDeclarator", "declarator", 
			"assignment", "lvalue", "returnStmt", "ifStmt", "whileStmt", "forStmt", 
			"forInit", "forUpdate", "initDeclaratorListNoSemi", "functionCall", "builtInCall", 
			"argumentList", "expr", "logicalOrExpr", "logicalAndExpr", "equalityExpr", 
			"relationalExpr", "additiveExpr", "multiplicativeExpr", "unaryExpr", 
			"castExpr", "primary", "arrayLiteral"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'inteiro'", "'real'", "'vazio'", "'principal'", "'retornar'", 
			"'se'", "'senao'", "'enquanto'", "'para'", "'ler'", "'lerc'", "'lers'", 
			"'escrever'", "'escreverc'", "'escreverv'", "'escrevers'", "'='", "';'", 
			"','", "'('", "')'", "'{'", "'}'", "'['", "']'", "'||'", "'&&'", "'!'", 
			"'=='", "'!='", "'<='", "'>='", "'<'", "'>'", "'+'", "'-'", "'*'", "'/'", 
			"'%'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INTEIRO", "REAL", "VAZIO", "PRINCIPAL", "RETORNAR", "SE", "SENAO", 
			"ENQUANTO", "PARA", "LER", "LERC", "LERS", "ESCREVER", "ESCREVERC", "ESCREVERV", 
			"ESCREVERS", "ASSIGN", "SEMI", "COMMA", "LPAR", "RPAR", "LBRACE", "RBRACE", 
			"LBRACK", "RBRACK", "OR", "AND", "NOT", "EQ", "NEQ", "LE", "GE", "LT", 
			"GT", "PLUS", "MINUS", "STAR", "DIV", "MOD", "NUMBER", "STRING", "ID", 
			"BLOCK_COMMENT", "LINE_COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MOCP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MOCPParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MOCPParser.EOF, 0); }
		public List<ItemContext> item() {
			return getRuleContexts(ItemContext.class);
		}
		public ItemContext item(int i) {
			return getRuleContext(ItemContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEIRO) | (1L << REAL) | (1L << VAZIO))) != 0)) {
				{
				{
				setState(80);
				item();
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(86);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ItemContext extends ParserRuleContext {
		public PrototypeContext prototype() {
			return getRuleContext(PrototypeContext.class,0);
		}
		public FunctionDefContext functionDef() {
			return getRuleContext(FunctionDefContext.class,0);
		}
		public PrincipalDefContext principalDef() {
			return getRuleContext(PrincipalDefContext.class,0);
		}
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public ItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterItem(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitItem(this);
		}
	}

	public final ItemContext item() throws RecognitionException {
		ItemContext _localctx = new ItemContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_item);
		try {
			setState(92);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				prototype();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(89);
				functionDef();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(90);
				principalDef();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(91);
				declaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrototypeContext extends ParserRuleContext {
		public FunctionHeaderContext functionHeader() {
			return getRuleContext(FunctionHeaderContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MOCPParser.SEMI, 0); }
		public List<TerminalNode> VAZIO() { return getTokens(MOCPParser.VAZIO); }
		public TerminalNode VAZIO(int i) {
			return getToken(MOCPParser.VAZIO, i);
		}
		public TerminalNode PRINCIPAL() { return getToken(MOCPParser.PRINCIPAL, 0); }
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public PrototypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prototype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterPrototype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitPrototype(this);
		}
	}

	public final PrototypeContext prototype() throws RecognitionException {
		PrototypeContext _localctx = new PrototypeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_prototype);
		try {
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				functionHeader();
				setState(95);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(97);
				match(VAZIO);
				setState(98);
				match(PRINCIPAL);
				setState(99);
				match(LPAR);
				setState(100);
				match(VAZIO);
				setState(101);
				match(RPAR);
				setState(102);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDefContext extends ParserRuleContext {
		public FunctionHeaderContext functionHeader() {
			return getRuleContext(FunctionHeaderContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FunctionDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterFunctionDef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitFunctionDef(this);
		}
	}

	public final FunctionDefContext functionDef() throws RecognitionException {
		FunctionDefContext _localctx = new FunctionDefContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_functionDef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			functionHeader();
			setState(106);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrincipalDefContext extends ParserRuleContext {
		public List<TerminalNode> VAZIO() { return getTokens(MOCPParser.VAZIO); }
		public TerminalNode VAZIO(int i) {
			return getToken(MOCPParser.VAZIO, i);
		}
		public TerminalNode PRINCIPAL() { return getToken(MOCPParser.PRINCIPAL, 0); }
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public PrincipalDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_principalDef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterPrincipalDef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitPrincipalDef(this);
		}
	}

	public final PrincipalDefContext principalDef() throws RecognitionException {
		PrincipalDefContext _localctx = new PrincipalDefContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_principalDef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(VAZIO);
			setState(109);
			match(PRINCIPAL);
			setState(110);
			match(LPAR);
			setState(111);
			match(VAZIO);
			setState(112);
			match(RPAR);
			setState(113);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionHeaderContext extends ParserRuleContext {
		public ReturnTypeContext returnType() {
			return getRuleContext(ReturnTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(MOCPParser.ID, 0); }
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public FunctionHeaderContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionHeader; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterFunctionHeader(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitFunctionHeader(this);
		}
	}

	public final FunctionHeaderContext functionHeader() throws RecognitionException {
		FunctionHeaderContext _localctx = new FunctionHeaderContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_functionHeader);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			returnType();
			setState(116);
			match(ID);
			setState(117);
			match(LPAR);
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INTEIRO || _la==REAL) {
				{
				setState(118);
				paramList();
				}
			}

			setState(121);
			match(RPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnTypeContext extends ParserRuleContext {
		public BaseTypeContext baseType() {
			return getRuleContext(BaseTypeContext.class,0);
		}
		public TerminalNode VAZIO() { return getToken(MOCPParser.VAZIO, 0); }
		public ReturnTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterReturnType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitReturnType(this);
		}
	}

	public final ReturnTypeContext returnType() throws RecognitionException {
		ReturnTypeContext _localctx = new ReturnTypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_returnType);
		try {
			setState(125);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEIRO:
			case REAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(123);
				baseType();
				}
				break;
			case VAZIO:
				enterOuterAlt(_localctx, 2);
				{
				setState(124);
				match(VAZIO);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BaseTypeContext extends ParserRuleContext {
		public TerminalNode INTEIRO() { return getToken(MOCPParser.INTEIRO, 0); }
		public TerminalNode REAL() { return getToken(MOCPParser.REAL, 0); }
		public BaseTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_baseType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterBaseType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitBaseType(this);
		}
	}

	public final BaseTypeContext baseType() throws RecognitionException {
		BaseTypeContext _localctx = new BaseTypeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_baseType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			_la = _input.LA(1);
			if ( !(_la==INTEIRO || _la==REAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamListContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MOCPParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MOCPParser.COMMA, i);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterParamList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitParamList(this);
		}
	}

	public final ParamListContext paramList() throws RecognitionException {
		ParamListContext _localctx = new ParamListContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			param();
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(130);
				match(COMMA);
				setState(131);
				param();
				}
				}
				setState(136);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public BaseTypeContext baseType() {
			return getRuleContext(BaseTypeContext.class,0);
		}
		public ParamDeclContext paramDecl() {
			return getRuleContext(ParamDeclContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitParam(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			baseType();
			setState(138);
			paramDecl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MOCPParser.ID, 0); }
		public TerminalNode LBRACK() { return getToken(MOCPParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(MOCPParser.RBRACK, 0); }
		public ParamDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterParamDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitParamDecl(this);
		}
	}

	public final ParamDeclContext paramDecl() throws RecognitionException {
		ParamDeclContext _localctx = new ParamDeclContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_paramDecl);
		try {
			setState(146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(141);
				match(ID);
				setState(142);
				match(LBRACK);
				setState(143);
				match(RBRACK);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(144);
				match(LBRACK);
				setState(145);
				match(RBRACK);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(MOCPParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(MOCPParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(LBRACE);
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEIRO) | (1L << REAL) | (1L << RETORNAR) | (1L << SE) | (1L << ENQUANTO) | (1L << PARA) | (1L << LER) | (1L << LERC) | (1L << LERS) | (1L << ESCREVER) | (1L << ESCREVERC) | (1L << ESCREVERV) | (1L << ESCREVERS) | (1L << SEMI) | (1L << LBRACE) | (1L << ID))) != 0)) {
				{
				{
				setState(149);
				statement();
				}
				}
				setState(154);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(155);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MOCPParser.SEMI, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ReturnStmtContext returnStmt() {
			return getRuleContext(ReturnStmtContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public ForStmtContext forStmt() {
			return getRuleContext(ForStmtContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_statement);
		try {
			setState(172);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(157);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(158);
				assignment();
				setState(159);
				match(SEMI);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(161);
				functionCall();
				setState(162);
				match(SEMI);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(164);
				returnStmt();
				setState(165);
				match(SEMI);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(167);
				ifStmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(168);
				whileStmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(169);
				forStmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(170);
				block();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(171);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public BaseTypeContext baseType() {
			return getRuleContext(BaseTypeContext.class,0);
		}
		public InitDeclaratorListContext initDeclaratorList() {
			return getRuleContext(InitDeclaratorListContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MOCPParser.SEMI, 0); }
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitDeclaration(this);
		}
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			baseType();
			setState(175);
			initDeclaratorList();
			setState(176);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitDeclaratorListContext extends ParserRuleContext {
		public List<InitDeclaratorContext> initDeclarator() {
			return getRuleContexts(InitDeclaratorContext.class);
		}
		public InitDeclaratorContext initDeclarator(int i) {
			return getRuleContext(InitDeclaratorContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MOCPParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MOCPParser.COMMA, i);
		}
		public InitDeclaratorListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initDeclaratorList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterInitDeclaratorList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitInitDeclaratorList(this);
		}
	}

	public final InitDeclaratorListContext initDeclaratorList() throws RecognitionException {
		InitDeclaratorListContext _localctx = new InitDeclaratorListContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_initDeclaratorList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			initDeclarator();
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(179);
				match(COMMA);
				setState(180);
				initDeclarator();
				}
				}
				setState(185);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitDeclaratorContext extends ParserRuleContext {
		public DeclaratorContext declarator() {
			return getRuleContext(DeclaratorContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(MOCPParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public InitDeclaratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initDeclarator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterInitDeclarator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitInitDeclarator(this);
		}
	}

	public final InitDeclaratorContext initDeclarator() throws RecognitionException {
		InitDeclaratorContext _localctx = new InitDeclaratorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_initDeclarator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			declarator();
			setState(189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(187);
				match(ASSIGN);
				setState(188);
				expr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclaratorContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MOCPParser.ID, 0); }
		public TerminalNode LBRACK() { return getToken(MOCPParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(MOCPParser.RBRACK, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public DeclaratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterDeclarator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitDeclarator(this);
		}
	}

	public final DeclaratorContext declarator() throws RecognitionException {
		DeclaratorContext _localctx = new DeclaratorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_declarator);
		int _la;
		try {
			setState(198);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(191);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(192);
				match(ID);
				setState(193);
				match(LBRACK);
				setState(195);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LER) | (1L << LERC) | (1L << LERS) | (1L << ESCREVER) | (1L << ESCREVERC) | (1L << ESCREVERV) | (1L << ESCREVERS) | (1L << LPAR) | (1L << LBRACE) | (1L << NOT) | (1L << MINUS) | (1L << NUMBER) | (1L << STRING) | (1L << ID))) != 0)) {
					{
					setState(194);
					expr();
					}
				}

				setState(197);
				match(RBRACK);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public LvalueContext lvalue() {
			return getRuleContext(LvalueContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(MOCPParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			lvalue();
			setState(201);
			match(ASSIGN);
			setState(202);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LvalueContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MOCPParser.ID, 0); }
		public TerminalNode LBRACK() { return getToken(MOCPParser.LBRACK, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RBRACK() { return getToken(MOCPParser.RBRACK, 0); }
		public LvalueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lvalue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterLvalue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitLvalue(this);
		}
	}

	public final LvalueContext lvalue() throws RecognitionException {
		LvalueContext _localctx = new LvalueContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_lvalue);
		try {
			setState(210);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(204);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(205);
				match(ID);
				setState(206);
				match(LBRACK);
				setState(207);
				expr();
				setState(208);
				match(RBRACK);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnStmtContext extends ParserRuleContext {
		public TerminalNode RETORNAR() { return getToken(MOCPParser.RETORNAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterReturnStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitReturnStmt(this);
		}
	}

	public final ReturnStmtContext returnStmt() throws RecognitionException {
		ReturnStmtContext _localctx = new ReturnStmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_returnStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(RETORNAR);
			setState(214);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LER) | (1L << LERC) | (1L << LERS) | (1L << ESCREVER) | (1L << ESCREVERC) | (1L << ESCREVERV) | (1L << ESCREVERS) | (1L << LPAR) | (1L << LBRACE) | (1L << NOT) | (1L << MINUS) | (1L << NUMBER) | (1L << STRING) | (1L << ID))) != 0)) {
				{
				setState(213);
				expr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode SE() { return getToken(MOCPParser.SE, 0); }
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode SENAO() { return getToken(MOCPParser.SENAO, 0); }
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterIfStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitIfStmt(this);
		}
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_ifStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			match(SE);
			setState(217);
			match(LPAR);
			setState(218);
			expr();
			setState(219);
			match(RPAR);
			setState(220);
			block();
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SENAO) {
				{
				setState(221);
				match(SENAO);
				setState(222);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileStmtContext extends ParserRuleContext {
		public TerminalNode ENQUANTO() { return getToken(MOCPParser.ENQUANTO, 0); }
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterWhileStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitWhileStmt(this);
		}
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_whileStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(ENQUANTO);
			setState(226);
			match(LPAR);
			setState(227);
			expr();
			setState(228);
			match(RPAR);
			setState(229);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForStmtContext extends ParserRuleContext {
		public TerminalNode PARA() { return getToken(MOCPParser.PARA, 0); }
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public List<TerminalNode> SEMI() { return getTokens(MOCPParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(MOCPParser.SEMI, i);
		}
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForInitContext forInit() {
			return getRuleContext(ForInitContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ForUpdateContext forUpdate() {
			return getRuleContext(ForUpdateContext.class,0);
		}
		public ForStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterForStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitForStmt(this);
		}
	}

	public final ForStmtContext forStmt() throws RecognitionException {
		ForStmtContext _localctx = new ForStmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_forStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(PARA);
			setState(232);
			match(LPAR);
			setState(234);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEIRO) | (1L << REAL) | (1L << ID))) != 0)) {
				{
				setState(233);
				forInit();
				}
			}

			setState(236);
			match(SEMI);
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LER) | (1L << LERC) | (1L << LERS) | (1L << ESCREVER) | (1L << ESCREVERC) | (1L << ESCREVERV) | (1L << ESCREVERS) | (1L << LPAR) | (1L << LBRACE) | (1L << NOT) | (1L << MINUS) | (1L << NUMBER) | (1L << STRING) | (1L << ID))) != 0)) {
				{
				setState(237);
				expr();
				}
			}

			setState(240);
			match(SEMI);
			setState(242);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(241);
				forUpdate();
				}
			}

			setState(244);
			match(RPAR);
			setState(245);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForInitContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public BaseTypeContext baseType() {
			return getRuleContext(BaseTypeContext.class,0);
		}
		public InitDeclaratorListNoSemiContext initDeclaratorListNoSemi() {
			return getRuleContext(InitDeclaratorListNoSemiContext.class,0);
		}
		public ForInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forInit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterForInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitForInit(this);
		}
	}

	public final ForInitContext forInit() throws RecognitionException {
		ForInitContext _localctx = new ForInitContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_forInit);
		try {
			setState(251);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(247);
				assignment();
				}
				break;
			case INTEIRO:
			case REAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(248);
				baseType();
				setState(249);
				initDeclaratorListNoSemi();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForUpdateContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ForUpdateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forUpdate; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterForUpdate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitForUpdate(this);
		}
	}

	public final ForUpdateContext forUpdate() throws RecognitionException {
		ForUpdateContext _localctx = new ForUpdateContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_forUpdate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			assignment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitDeclaratorListNoSemiContext extends ParserRuleContext {
		public List<InitDeclaratorContext> initDeclarator() {
			return getRuleContexts(InitDeclaratorContext.class);
		}
		public InitDeclaratorContext initDeclarator(int i) {
			return getRuleContext(InitDeclaratorContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MOCPParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MOCPParser.COMMA, i);
		}
		public InitDeclaratorListNoSemiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initDeclaratorListNoSemi; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterInitDeclaratorListNoSemi(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitInitDeclaratorListNoSemi(this);
		}
	}

	public final InitDeclaratorListNoSemiContext initDeclaratorListNoSemi() throws RecognitionException {
		InitDeclaratorListNoSemiContext _localctx = new InitDeclaratorListNoSemiContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_initDeclaratorListNoSemi);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(255);
			initDeclarator();
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(256);
				match(COMMA);
				setState(257);
				initDeclarator();
				}
				}
				setState(262);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionCallContext extends ParserRuleContext {
		public BuiltInCallContext builtInCall() {
			return getRuleContext(BuiltInCallContext.class,0);
		}
		public TerminalNode ID() { return getToken(MOCPParser.ID, 0); }
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterFunctionCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitFunctionCall(this);
		}
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_functionCall);
		int _la;
		try {
			setState(270);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LER:
			case LERC:
			case LERS:
			case ESCREVER:
			case ESCREVERC:
			case ESCREVERV:
			case ESCREVERS:
				enterOuterAlt(_localctx, 1);
				{
				setState(263);
				builtInCall();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(264);
				match(ID);
				setState(265);
				match(LPAR);
				setState(267);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LER) | (1L << LERC) | (1L << LERS) | (1L << ESCREVER) | (1L << ESCREVERC) | (1L << ESCREVERV) | (1L << ESCREVERS) | (1L << LPAR) | (1L << LBRACE) | (1L << NOT) | (1L << MINUS) | (1L << NUMBER) | (1L << STRING) | (1L << ID))) != 0)) {
					{
					setState(266);
					argumentList();
					}
				}

				setState(269);
				match(RPAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BuiltInCallContext extends ParserRuleContext {
		public TerminalNode LER() { return getToken(MOCPParser.LER, 0); }
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public TerminalNode LERC() { return getToken(MOCPParser.LERC, 0); }
		public TerminalNode LERS() { return getToken(MOCPParser.LERS, 0); }
		public TerminalNode ESCREVER() { return getToken(MOCPParser.ESCREVER, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ESCREVERC() { return getToken(MOCPParser.ESCREVERC, 0); }
		public TerminalNode ESCREVERV() { return getToken(MOCPParser.ESCREVERV, 0); }
		public TerminalNode ESCREVERS() { return getToken(MOCPParser.ESCREVERS, 0); }
		public BuiltInCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_builtInCall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterBuiltInCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitBuiltInCall(this);
		}
	}

	public final BuiltInCallContext builtInCall() throws RecognitionException {
		BuiltInCallContext _localctx = new BuiltInCallContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_builtInCall);
		try {
			setState(301);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LER:
				enterOuterAlt(_localctx, 1);
				{
				setState(272);
				match(LER);
				setState(273);
				match(LPAR);
				setState(274);
				match(RPAR);
				}
				break;
			case LERC:
				enterOuterAlt(_localctx, 2);
				{
				setState(275);
				match(LERC);
				setState(276);
				match(LPAR);
				setState(277);
				match(RPAR);
				}
				break;
			case LERS:
				enterOuterAlt(_localctx, 3);
				{
				setState(278);
				match(LERS);
				setState(279);
				match(LPAR);
				setState(280);
				match(RPAR);
				}
				break;
			case ESCREVER:
				enterOuterAlt(_localctx, 4);
				{
				setState(281);
				match(ESCREVER);
				setState(282);
				match(LPAR);
				setState(283);
				expr();
				setState(284);
				match(RPAR);
				}
				break;
			case ESCREVERC:
				enterOuterAlt(_localctx, 5);
				{
				setState(286);
				match(ESCREVERC);
				setState(287);
				match(LPAR);
				setState(288);
				expr();
				setState(289);
				match(RPAR);
				}
				break;
			case ESCREVERV:
				enterOuterAlt(_localctx, 6);
				{
				setState(291);
				match(ESCREVERV);
				setState(292);
				match(LPAR);
				setState(293);
				expr();
				setState(294);
				match(RPAR);
				}
				break;
			case ESCREVERS:
				enterOuterAlt(_localctx, 7);
				{
				setState(296);
				match(ESCREVERS);
				setState(297);
				match(LPAR);
				setState(298);
				expr();
				setState(299);
				match(RPAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MOCPParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MOCPParser.COMMA, i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterArgumentList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitArgumentList(this);
		}
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			expr();
			setState(308);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(304);
				match(COMMA);
				setState(305);
				expr();
				}
				}
				setState(310);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public LogicalOrExprContext logicalOrExpr() {
			return getRuleContext(LogicalOrExprContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			logicalOrExpr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LogicalOrExprContext extends ParserRuleContext {
		public List<LogicalAndExprContext> logicalAndExpr() {
			return getRuleContexts(LogicalAndExprContext.class);
		}
		public LogicalAndExprContext logicalAndExpr(int i) {
			return getRuleContext(LogicalAndExprContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(MOCPParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(MOCPParser.OR, i);
		}
		public LogicalOrExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOrExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterLogicalOrExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitLogicalOrExpr(this);
		}
	}

	public final LogicalOrExprContext logicalOrExpr() throws RecognitionException {
		LogicalOrExprContext _localctx = new LogicalOrExprContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_logicalOrExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(313);
			logicalAndExpr();
			setState(318);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(314);
				match(OR);
				setState(315);
				logicalAndExpr();
				}
				}
				setState(320);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LogicalAndExprContext extends ParserRuleContext {
		public List<EqualityExprContext> equalityExpr() {
			return getRuleContexts(EqualityExprContext.class);
		}
		public EqualityExprContext equalityExpr(int i) {
			return getRuleContext(EqualityExprContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(MOCPParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(MOCPParser.AND, i);
		}
		public LogicalAndExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAndExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterLogicalAndExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitLogicalAndExpr(this);
		}
	}

	public final LogicalAndExprContext logicalAndExpr() throws RecognitionException {
		LogicalAndExprContext _localctx = new LogicalAndExprContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_logicalAndExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(321);
			equalityExpr();
			setState(326);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(322);
				match(AND);
				setState(323);
				equalityExpr();
				}
				}
				setState(328);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EqualityExprContext extends ParserRuleContext {
		public List<RelationalExprContext> relationalExpr() {
			return getRuleContexts(RelationalExprContext.class);
		}
		public RelationalExprContext relationalExpr(int i) {
			return getRuleContext(RelationalExprContext.class,i);
		}
		public List<TerminalNode> EQ() { return getTokens(MOCPParser.EQ); }
		public TerminalNode EQ(int i) {
			return getToken(MOCPParser.EQ, i);
		}
		public List<TerminalNode> NEQ() { return getTokens(MOCPParser.NEQ); }
		public TerminalNode NEQ(int i) {
			return getToken(MOCPParser.NEQ, i);
		}
		public EqualityExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalityExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterEqualityExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitEqualityExpr(this);
		}
	}

	public final EqualityExprContext equalityExpr() throws RecognitionException {
		EqualityExprContext _localctx = new EqualityExprContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_equalityExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			relationalExpr();
			setState(334);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==EQ || _la==NEQ) {
				{
				{
				setState(330);
				_la = _input.LA(1);
				if ( !(_la==EQ || _la==NEQ) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(331);
				relationalExpr();
				}
				}
				setState(336);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RelationalExprContext extends ParserRuleContext {
		public List<AdditiveExprContext> additiveExpr() {
			return getRuleContexts(AdditiveExprContext.class);
		}
		public AdditiveExprContext additiveExpr(int i) {
			return getRuleContext(AdditiveExprContext.class,i);
		}
		public List<TerminalNode> LT() { return getTokens(MOCPParser.LT); }
		public TerminalNode LT(int i) {
			return getToken(MOCPParser.LT, i);
		}
		public List<TerminalNode> LE() { return getTokens(MOCPParser.LE); }
		public TerminalNode LE(int i) {
			return getToken(MOCPParser.LE, i);
		}
		public List<TerminalNode> GT() { return getTokens(MOCPParser.GT); }
		public TerminalNode GT(int i) {
			return getToken(MOCPParser.GT, i);
		}
		public List<TerminalNode> GE() { return getTokens(MOCPParser.GE); }
		public TerminalNode GE(int i) {
			return getToken(MOCPParser.GE, i);
		}
		public RelationalExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationalExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterRelationalExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitRelationalExpr(this);
		}
	}

	public final RelationalExprContext relationalExpr() throws RecognitionException {
		RelationalExprContext _localctx = new RelationalExprContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_relationalExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(337);
			additiveExpr();
			setState(342);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LE) | (1L << GE) | (1L << LT) | (1L << GT))) != 0)) {
				{
				{
				setState(338);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LE) | (1L << GE) | (1L << LT) | (1L << GT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(339);
				additiveExpr();
				}
				}
				setState(344);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AdditiveExprContext extends ParserRuleContext {
		public List<MultiplicativeExprContext> multiplicativeExpr() {
			return getRuleContexts(MultiplicativeExprContext.class);
		}
		public MultiplicativeExprContext multiplicativeExpr(int i) {
			return getRuleContext(MultiplicativeExprContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(MOCPParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(MOCPParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(MOCPParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(MOCPParser.MINUS, i);
		}
		public AdditiveExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterAdditiveExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitAdditiveExpr(this);
		}
	}

	public final AdditiveExprContext additiveExpr() throws RecognitionException {
		AdditiveExprContext _localctx = new AdditiveExprContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_additiveExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(345);
			multiplicativeExpr();
			setState(350);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(346);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(347);
				multiplicativeExpr();
				}
				}
				setState(352);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MultiplicativeExprContext extends ParserRuleContext {
		public List<UnaryExprContext> unaryExpr() {
			return getRuleContexts(UnaryExprContext.class);
		}
		public UnaryExprContext unaryExpr(int i) {
			return getRuleContext(UnaryExprContext.class,i);
		}
		public List<TerminalNode> STAR() { return getTokens(MOCPParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(MOCPParser.STAR, i);
		}
		public List<TerminalNode> DIV() { return getTokens(MOCPParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(MOCPParser.DIV, i);
		}
		public List<TerminalNode> MOD() { return getTokens(MOCPParser.MOD); }
		public TerminalNode MOD(int i) {
			return getToken(MOCPParser.MOD, i);
		}
		public MultiplicativeExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterMultiplicativeExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitMultiplicativeExpr(this);
		}
	}

	public final MultiplicativeExprContext multiplicativeExpr() throws RecognitionException {
		MultiplicativeExprContext _localctx = new MultiplicativeExprContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_multiplicativeExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			unaryExpr();
			setState(358);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR) | (1L << DIV) | (1L << MOD))) != 0)) {
				{
				{
				setState(354);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR) | (1L << DIV) | (1L << MOD))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(355);
				unaryExpr();
				}
				}
				setState(360);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnaryExprContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(MOCPParser.NOT, 0); }
		public UnaryExprContext unaryExpr() {
			return getRuleContext(UnaryExprContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(MOCPParser.MINUS, 0); }
		public CastExprContext castExpr() {
			return getRuleContext(CastExprContext.class,0);
		}
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public UnaryExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterUnaryExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitUnaryExpr(this);
		}
	}

	public final UnaryExprContext unaryExpr() throws RecognitionException {
		UnaryExprContext _localctx = new UnaryExprContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_unaryExpr);
		try {
			setState(367);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(361);
				match(NOT);
				setState(362);
				unaryExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(363);
				match(MINUS);
				setState(364);
				unaryExpr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(365);
				castExpr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(366);
				primary();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CastExprContext extends ParserRuleContext {
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public BaseTypeContext baseType() {
			return getRuleContext(BaseTypeContext.class,0);
		}
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public UnaryExprContext unaryExpr() {
			return getRuleContext(UnaryExprContext.class,0);
		}
		public CastExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_castExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterCastExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitCastExpr(this);
		}
	}

	public final CastExprContext castExpr() throws RecognitionException {
		CastExprContext _localctx = new CastExprContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_castExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(369);
			match(LPAR);
			setState(370);
			baseType();
			setState(371);
			match(RPAR);
			setState(372);
			unaryExpr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrimaryContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(MOCPParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(MOCPParser.STRING, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public LvalueContext lvalue() {
			return getRuleContext(LvalueContext.class,0);
		}
		public ArrayLiteralContext arrayLiteral() {
			return getRuleContext(ArrayLiteralContext.class,0);
		}
		public TerminalNode LPAR() { return getToken(MOCPParser.LPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAR() { return getToken(MOCPParser.RPAR, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterPrimary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitPrimary(this);
		}
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_primary);
		try {
			setState(383);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(374);
				match(NUMBER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(375);
				match(STRING);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(376);
				functionCall();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(377);
				lvalue();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(378);
				arrayLiteral();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(379);
				match(LPAR);
				setState(380);
				expr();
				setState(381);
				match(RPAR);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayLiteralContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(MOCPParser.LBRACE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RBRACE() { return getToken(MOCPParser.RBRACE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(MOCPParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MOCPParser.COMMA, i);
		}
		public ArrayLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayLiteral; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).enterArrayLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MOCPListener ) ((MOCPListener)listener).exitArrayLiteral(this);
		}
	}

	public final ArrayLiteralContext arrayLiteral() throws RecognitionException {
		ArrayLiteralContext _localctx = new ArrayLiteralContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_arrayLiteral);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(385);
			match(LBRACE);
			setState(386);
			expr();
			setState(391);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(387);
				match(COMMA);
				setState(388);
				expr();
				}
				}
				setState(393);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(394);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/\u018f\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\7\2T\n\2\f"+
		"\2\16\2W\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3_\n\3\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\5\4j\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7"+
		"\3\7\3\7\5\7z\n\7\3\7\3\7\3\b\3\b\5\b\u0080\n\b\3\t\3\t\3\n\3\n\3\n\7"+
		"\n\u0087\n\n\f\n\16\n\u008a\13\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\5\f\u0095\n\f\3\r\3\r\7\r\u0099\n\r\f\r\16\r\u009c\13\r\3\r\3\r\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\5\16\u00af\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\7\20\u00b8\n\20\f"+
		"\20\16\20\u00bb\13\20\3\21\3\21\3\21\5\21\u00c0\n\21\3\22\3\22\3\22\3"+
		"\22\5\22\u00c6\n\22\3\22\5\22\u00c9\n\22\3\23\3\23\3\23\3\23\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\5\24\u00d5\n\24\3\25\3\25\5\25\u00d9\n\25\3\26\3"+
		"\26\3\26\3\26\3\26\3\26\3\26\5\26\u00e2\n\26\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\30\3\30\3\30\5\30\u00ed\n\30\3\30\3\30\5\30\u00f1\n\30\3\30\3"+
		"\30\5\30\u00f5\n\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u00fe\n\31"+
		"\3\32\3\32\3\33\3\33\3\33\7\33\u0105\n\33\f\33\16\33\u0108\13\33\3\34"+
		"\3\34\3\34\3\34\5\34\u010e\n\34\3\34\5\34\u0111\n\34\3\35\3\35\3\35\3"+
		"\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3"+
		"\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0130"+
		"\n\35\3\36\3\36\3\36\7\36\u0135\n\36\f\36\16\36\u0138\13\36\3\37\3\37"+
		"\3 \3 \3 \7 \u013f\n \f \16 \u0142\13 \3!\3!\3!\7!\u0147\n!\f!\16!\u014a"+
		"\13!\3\"\3\"\3\"\7\"\u014f\n\"\f\"\16\"\u0152\13\"\3#\3#\3#\7#\u0157\n"+
		"#\f#\16#\u015a\13#\3$\3$\3$\7$\u015f\n$\f$\16$\u0162\13$\3%\3%\3%\7%\u0167"+
		"\n%\f%\16%\u016a\13%\3&\3&\3&\3&\3&\3&\5&\u0172\n&\3\'\3\'\3\'\3\'\3\'"+
		"\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0182\n(\3)\3)\3)\3)\7)\u0188\n)\f)\16"+
		")\u018b\13)\3)\3)\3)\2\2*\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&"+
		"(*,.\60\62\64\668:<>@BDFHJLNP\2\7\3\2\3\4\3\2\37 \3\2!$\3\2%&\3\2\')\2"+
		"\u019d\2U\3\2\2\2\4^\3\2\2\2\6i\3\2\2\2\bk\3\2\2\2\nn\3\2\2\2\fu\3\2\2"+
		"\2\16\177\3\2\2\2\20\u0081\3\2\2\2\22\u0083\3\2\2\2\24\u008b\3\2\2\2\26"+
		"\u0094\3\2\2\2\30\u0096\3\2\2\2\32\u00ae\3\2\2\2\34\u00b0\3\2\2\2\36\u00b4"+
		"\3\2\2\2 \u00bc\3\2\2\2\"\u00c8\3\2\2\2$\u00ca\3\2\2\2&\u00d4\3\2\2\2"+
		"(\u00d6\3\2\2\2*\u00da\3\2\2\2,\u00e3\3\2\2\2.\u00e9\3\2\2\2\60\u00fd"+
		"\3\2\2\2\62\u00ff\3\2\2\2\64\u0101\3\2\2\2\66\u0110\3\2\2\28\u012f\3\2"+
		"\2\2:\u0131\3\2\2\2<\u0139\3\2\2\2>\u013b\3\2\2\2@\u0143\3\2\2\2B\u014b"+
		"\3\2\2\2D\u0153\3\2\2\2F\u015b\3\2\2\2H\u0163\3\2\2\2J\u0171\3\2\2\2L"+
		"\u0173\3\2\2\2N\u0181\3\2\2\2P\u0183\3\2\2\2RT\5\4\3\2SR\3\2\2\2TW\3\2"+
		"\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\7\2\2\3Y\3\3\2\2\2Z_\5"+
		"\6\4\2[_\5\b\5\2\\_\5\n\6\2]_\5\34\17\2^Z\3\2\2\2^[\3\2\2\2^\\\3\2\2\2"+
		"^]\3\2\2\2_\5\3\2\2\2`a\5\f\7\2ab\7\24\2\2bj\3\2\2\2cd\7\5\2\2de\7\6\2"+
		"\2ef\7\26\2\2fg\7\5\2\2gh\7\27\2\2hj\7\24\2\2i`\3\2\2\2ic\3\2\2\2j\7\3"+
		"\2\2\2kl\5\f\7\2lm\5\30\r\2m\t\3\2\2\2no\7\5\2\2op\7\6\2\2pq\7\26\2\2"+
		"qr\7\5\2\2rs\7\27\2\2st\5\30\r\2t\13\3\2\2\2uv\5\16\b\2vw\7,\2\2wy\7\26"+
		"\2\2xz\5\22\n\2yx\3\2\2\2yz\3\2\2\2z{\3\2\2\2{|\7\27\2\2|\r\3\2\2\2}\u0080"+
		"\5\20\t\2~\u0080\7\5\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080\17\3\2\2\2\u0081"+
		"\u0082\t\2\2\2\u0082\21\3\2\2\2\u0083\u0088\5\24\13\2\u0084\u0085\7\25"+
		"\2\2\u0085\u0087\5\24\13\2\u0086\u0084\3\2\2\2\u0087\u008a\3\2\2\2\u0088"+
		"\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\23\3\2\2\2\u008a\u0088\3\2\2"+
		"\2\u008b\u008c\5\20\t\2\u008c\u008d\5\26\f\2\u008d\25\3\2\2\2\u008e\u0095"+
		"\7,\2\2\u008f\u0090\7,\2\2\u0090\u0091\7\32\2\2\u0091\u0095\7\33\2\2\u0092"+
		"\u0093\7\32\2\2\u0093\u0095\7\33\2\2\u0094\u008e\3\2\2\2\u0094\u008f\3"+
		"\2\2\2\u0094\u0092\3\2\2\2\u0095\27\3\2\2\2\u0096\u009a\7\30\2\2\u0097"+
		"\u0099\5\32\16\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098\3"+
		"\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d"+
		"\u009e\7\31\2\2\u009e\31\3\2\2\2\u009f\u00af\5\34\17\2\u00a0\u00a1\5$"+
		"\23\2\u00a1\u00a2\7\24\2\2\u00a2\u00af\3\2\2\2\u00a3\u00a4\5\66\34\2\u00a4"+
		"\u00a5\7\24\2\2\u00a5\u00af\3\2\2\2\u00a6\u00a7\5(\25\2\u00a7\u00a8\7"+
		"\24\2\2\u00a8\u00af\3\2\2\2\u00a9\u00af\5*\26\2\u00aa\u00af\5,\27\2\u00ab"+
		"\u00af\5.\30\2\u00ac\u00af\5\30\r\2\u00ad\u00af\7\24\2\2\u00ae\u009f\3"+
		"\2\2\2\u00ae\u00a0\3\2\2\2\u00ae\u00a3\3\2\2\2\u00ae\u00a6\3\2\2\2\u00ae"+
		"\u00a9\3\2\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00ac\3\2"+
		"\2\2\u00ae\u00ad\3\2\2\2\u00af\33\3\2\2\2\u00b0\u00b1\5\20\t\2\u00b1\u00b2"+
		"\5\36\20\2\u00b2\u00b3\7\24\2\2\u00b3\35\3\2\2\2\u00b4\u00b9\5 \21\2\u00b5"+
		"\u00b6\7\25\2\2\u00b6\u00b8\5 \21\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\3"+
		"\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\37\3\2\2\2\u00bb"+
		"\u00b9\3\2\2\2\u00bc\u00bf\5\"\22\2\u00bd\u00be\7\23\2\2\u00be\u00c0\5"+
		"<\37\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0!\3\2\2\2\u00c1\u00c9"+
		"\7,\2\2\u00c2\u00c3\7,\2\2\u00c3\u00c5\7\32\2\2\u00c4\u00c6\5<\37\2\u00c5"+
		"\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\7\33"+
		"\2\2\u00c8\u00c1\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c9#\3\2\2\2\u00ca\u00cb"+
		"\5&\24\2\u00cb\u00cc\7\23\2\2\u00cc\u00cd\5<\37\2\u00cd%\3\2\2\2\u00ce"+
		"\u00d5\7,\2\2\u00cf\u00d0\7,\2\2\u00d0\u00d1\7\32\2\2\u00d1\u00d2\5<\37"+
		"\2\u00d2\u00d3\7\33\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00ce\3\2\2\2\u00d4"+
		"\u00cf\3\2\2\2\u00d5\'\3\2\2\2\u00d6\u00d8\7\7\2\2\u00d7\u00d9\5<\37\2"+
		"\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9)\3\2\2\2\u00da\u00db\7"+
		"\b\2\2\u00db\u00dc\7\26\2\2\u00dc\u00dd\5<\37\2\u00dd\u00de\7\27\2\2\u00de"+
		"\u00e1\5\30\r\2\u00df\u00e0\7\t\2\2\u00e0\u00e2\5\30\r\2\u00e1\u00df\3"+
		"\2\2\2\u00e1\u00e2\3\2\2\2\u00e2+\3\2\2\2\u00e3\u00e4\7\n\2\2\u00e4\u00e5"+
		"\7\26\2\2\u00e5\u00e6\5<\37\2\u00e6\u00e7\7\27\2\2\u00e7\u00e8\5\30\r"+
		"\2\u00e8-\3\2\2\2\u00e9\u00ea\7\13\2\2\u00ea\u00ec\7\26\2\2\u00eb\u00ed"+
		"\5\60\31\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\3\2\2\2"+
		"\u00ee\u00f0\7\24\2\2\u00ef\u00f1\5<\37\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1"+
		"\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\7\24\2\2\u00f3\u00f5\5\62\32"+
		"\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7"+
		"\7\27\2\2\u00f7\u00f8\5\30\r\2\u00f8/\3\2\2\2\u00f9\u00fe\5$\23\2\u00fa"+
		"\u00fb\5\20\t\2\u00fb\u00fc\5\64\33\2\u00fc\u00fe\3\2\2\2\u00fd\u00f9"+
		"\3\2\2\2\u00fd\u00fa\3\2\2\2\u00fe\61\3\2\2\2\u00ff\u0100\5$\23\2\u0100"+
		"\63\3\2\2\2\u0101\u0106\5 \21\2\u0102\u0103\7\25\2\2\u0103\u0105\5 \21"+
		"\2\u0104\u0102\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107"+
		"\3\2\2\2\u0107\65\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u0111\58\35\2\u010a"+
		"\u010b\7,\2\2\u010b\u010d\7\26\2\2\u010c\u010e\5:\36\2\u010d\u010c\3\2"+
		"\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\7\27\2\2\u0110"+
		"\u0109\3\2\2\2\u0110\u010a\3\2\2\2\u0111\67\3\2\2\2\u0112\u0113\7\f\2"+
		"\2\u0113\u0114\7\26\2\2\u0114\u0130\7\27\2\2\u0115\u0116\7\r\2\2\u0116"+
		"\u0117\7\26\2\2\u0117\u0130\7\27\2\2\u0118\u0119\7\16\2\2\u0119\u011a"+
		"\7\26\2\2\u011a\u0130\7\27\2\2\u011b\u011c\7\17\2\2\u011c\u011d\7\26\2"+
		"\2\u011d\u011e\5<\37\2\u011e\u011f\7\27\2\2\u011f\u0130\3\2\2\2\u0120"+
		"\u0121\7\20\2\2\u0121\u0122\7\26\2\2\u0122\u0123\5<\37\2\u0123\u0124\7"+
		"\27\2\2\u0124\u0130\3\2\2\2\u0125\u0126\7\21\2\2\u0126\u0127\7\26\2\2"+
		"\u0127\u0128\5<\37\2\u0128\u0129\7\27\2\2\u0129\u0130\3\2\2\2\u012a\u012b"+
		"\7\22\2\2\u012b\u012c\7\26\2\2\u012c\u012d\5<\37\2\u012d\u012e\7\27\2"+
		"\2\u012e\u0130\3\2\2\2\u012f\u0112\3\2\2\2\u012f\u0115\3\2\2\2\u012f\u0118"+
		"\3\2\2\2\u012f\u011b\3\2\2\2\u012f\u0120\3\2\2\2\u012f\u0125\3\2\2\2\u012f"+
		"\u012a\3\2\2\2\u01309\3\2\2\2\u0131\u0136\5<\37\2\u0132\u0133\7\25\2\2"+
		"\u0133\u0135\5<\37\2\u0134\u0132\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134"+
		"\3\2\2\2\u0136\u0137\3\2\2\2\u0137;\3\2\2\2\u0138\u0136\3\2\2\2\u0139"+
		"\u013a\5> \2\u013a=\3\2\2\2\u013b\u0140\5@!\2\u013c\u013d\7\34\2\2\u013d"+
		"\u013f\5@!\2\u013e\u013c\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2"+
		"\2\u0140\u0141\3\2\2\2\u0141?\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0148"+
		"\5B\"\2\u0144\u0145\7\35\2\2\u0145\u0147\5B\"\2\u0146\u0144\3\2\2\2\u0147"+
		"\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149A\3\2\2\2"+
		"\u014a\u0148\3\2\2\2\u014b\u0150\5D#\2\u014c\u014d\t\3\2\2\u014d\u014f"+
		"\5D#\2\u014e\u014c\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150"+
		"\u0151\3\2\2\2\u0151C\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0158\5F$\2\u0154"+
		"\u0155\t\4\2\2\u0155\u0157\5F$\2\u0156\u0154\3\2\2\2\u0157\u015a\3\2\2"+
		"\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159E\3\2\2\2\u015a\u0158"+
		"\3\2\2\2\u015b\u0160\5H%\2\u015c\u015d\t\5\2\2\u015d\u015f\5H%\2\u015e"+
		"\u015c\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2"+
		"\2\2\u0161G\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0168\5J&\2\u0164\u0165"+
		"\t\6\2\2\u0165\u0167\5J&\2\u0166\u0164\3\2\2\2\u0167\u016a\3\2\2\2\u0168"+
		"\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169I\3\2\2\2\u016a\u0168\3\2\2\2"+
		"\u016b\u016c\7\36\2\2\u016c\u0172\5J&\2\u016d\u016e\7&\2\2\u016e\u0172"+
		"\5J&\2\u016f\u0172\5L\'\2\u0170\u0172\5N(\2\u0171\u016b\3\2\2\2\u0171"+
		"\u016d\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172K\3\2\2\2"+
		"\u0173\u0174\7\26\2\2\u0174\u0175\5\20\t\2\u0175\u0176\7\27\2\2\u0176"+
		"\u0177\5J&\2\u0177M\3\2\2\2\u0178\u0182\7*\2\2\u0179\u0182\7+\2\2\u017a"+
		"\u0182\5\66\34\2\u017b\u0182\5&\24\2\u017c\u0182\5P)\2\u017d\u017e\7\26"+
		"\2\2\u017e\u017f\5<\37\2\u017f\u0180\7\27\2\2\u0180\u0182\3\2\2\2\u0181"+
		"\u0178\3\2\2\2\u0181\u0179\3\2\2\2\u0181\u017a\3\2\2\2\u0181\u017b\3\2"+
		"\2\2\u0181\u017c\3\2\2\2\u0181\u017d\3\2\2\2\u0182O\3\2\2\2\u0183\u0184"+
		"\7\30\2\2\u0184\u0189\5<\37\2\u0185\u0186\7\25\2\2\u0186\u0188\5<\37\2"+
		"\u0187\u0185\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a"+
		"\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d\7\31\2\2"+
		"\u018dQ\3\2\2\2$U^iy\177\u0088\u0094\u009a\u00ae\u00b9\u00bf\u00c5\u00c8"+
		"\u00d4\u00d8\u00e1\u00ec\u00f0\u00f4\u00fd\u0106\u010d\u0110\u012f\u0136"+
		"\u0140\u0148\u0150\u0158\u0160\u0168\u0171\u0181\u0189";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}