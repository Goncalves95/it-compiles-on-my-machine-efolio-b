grammar MOCP;

/* =========================
   PARSER RULES
   ========================= */

program
    : item* EOF
    ;

item
    : prototype
    | functionDef
    | principalDef
    | declaration
    ;

prototype
    : functionHeader SEMI
    | VAZIO PRINCIPAL LPAR VAZIO RPAR SEMI
    ;

functionDef
    : functionHeader block
    ;

principalDef
    : VAZIO PRINCIPAL LPAR VAZIO RPAR block
    ;

functionHeader
    : returnType ID LPAR paramList? RPAR
    ;

returnType
    : baseType
    | VAZIO
    ;

baseType
    : INTEIRO
    | REAL
    ;

paramList
    : param (COMMA param)*
    ;

param
    : baseType paramDecl
    ;

paramDecl
    : ID
    | ID LBRACK RBRACK
    | LBRACK RBRACK
    ;

block
    : LBRACE statement* RBRACE
    ;

statement
    : declaration
    | assignment SEMI
    | functionCall SEMI
    | returnStmt SEMI
    | ifStmt
    | whileStmt
    | forStmt
    | block
    | SEMI
    ;

declaration
    : baseType initDeclaratorList SEMI
    ;

initDeclaratorList
    : initDeclarator (COMMA initDeclarator)*
    ;

initDeclarator
    : declarator (ASSIGN expr)?
    ;

declarator
    : ID
    | ID LBRACK expr? RBRACK
    ;

assignment
    : lvalue ASSIGN expr
    ;

lvalue
    : ID
    | ID LBRACK expr RBRACK
    ;

returnStmt
    : RETORNAR expr?
    ;

ifStmt
    : SE LPAR expr RPAR block (SENAO block)?
    ;

whileStmt
    : ENQUANTO LPAR expr RPAR block
    ;

forStmt
    : PARA LPAR forInit? SEMI expr? SEMI forUpdate? RPAR block
    ;

forInit
    : assignment
    | baseType initDeclaratorListNoSemi
    ;

forUpdate
    : assignment
    ;

initDeclaratorListNoSemi
    : initDeclarator (COMMA initDeclarator)*
    ;

functionCall
    : builtInCall
    | ID LPAR argumentList? RPAR
    ;

builtInCall
    : LER LPAR RPAR
    | LERC LPAR RPAR
    | LERS LPAR RPAR
    | ESCREVER LPAR expr RPAR
    | ESCREVERC LPAR expr RPAR
    | ESCREVERV LPAR expr RPAR
    | ESCREVERS LPAR expr RPAR
    ;

argumentList
    : expr (COMMA expr)*
    ;

/* ---------- Expressões com precedência ---------- */

expr
    : logicalOrExpr
    ;

logicalOrExpr
    : logicalAndExpr (OR logicalAndExpr)*
    ;

logicalAndExpr
    : equalityExpr (AND equalityExpr)*
    ;

equalityExpr
    : relationalExpr ((EQ | NEQ) relationalExpr)*
    ;

relationalExpr
    : additiveExpr ((LT | LE | GT | GE) additiveExpr)*
    ;

additiveExpr
    : multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*
    ;

multiplicativeExpr
    : unaryExpr ((STAR | DIV | MOD) unaryExpr)*
    ;

unaryExpr
    : NOT unaryExpr
    | MINUS unaryExpr
    | castExpr
    | primary
    ;

castExpr
    : LPAR baseType RPAR unaryExpr
    ;

primary
    : NUMBER
    | STRING
    | functionCall
    | lvalue
    | arrayLiteral
    | LPAR expr RPAR
    ;

arrayLiteral
    : LBRACE expr (COMMA expr)* RBRACE
    ;

/* =========================
   LEXER RULES
   ========================= */

INTEIRO    : 'inteiro';
REAL       : 'real';
VAZIO      : 'vazio';
PRINCIPAL  : 'principal';
RETORNAR   : 'retornar';

SE         : 'se';
SENAO      : 'senao';
ENQUANTO   : 'enquanto';
PARA       : 'para';

LER        : 'ler';
LERC       : 'lerc';
LERS       : 'lers';
ESCREVER   : 'escrever';
ESCREVERC  : 'escreverc';
ESCREVERV  : 'escreverv';
ESCREVERS  : 'escrevers';

ASSIGN     : '=';
SEMI       : ';';
COMMA      : ',';

LPAR       : '(';
RPAR       : ')';
LBRACE     : '{';
RBRACE     : '}';
LBRACK     : '[';
RBRACK     : ']';

OR         : '||';
AND        : '&&';
NOT        : '!';

EQ         : '==';
NEQ        : '!=';
LE         : '<=';
GE         : '>=';
LT         : '<';
GT         : '>';

PLUS       : '+';
MINUS      : '-';
STAR       : '*';
DIV        : '/';
MOD        : '%';

NUMBER
    : DIGIT+ ('.' DIGIT+)?
    ;

STRING
    : '"' (~["\\\r\n] | '\\' .)* '"'
    ;

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

fragment DIGIT
    : [0-9]
    ;