# Generated from grammar/MOCP.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,397,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,5,0,82,8,0,10,0,12,0,85,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,93,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,104,8,2,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,120,8,5,1,5,1,5,1,
        6,1,6,3,6,126,8,6,1,7,1,7,1,8,1,8,1,8,5,8,133,8,8,10,8,12,8,136,
        9,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,147,8,10,1,11,
        1,11,5,11,151,8,11,10,11,12,11,154,9,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        173,8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,182,8,14,10,14,
        12,14,185,9,14,1,15,1,15,1,15,3,15,190,8,15,1,16,1,16,1,16,1,16,
        3,16,196,8,16,1,16,3,16,199,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,
        18,1,18,1,18,1,18,3,18,211,8,18,1,19,1,19,3,19,215,8,19,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,3,20,224,8,20,1,21,1,21,1,21,1,21,1,21,
        1,21,1,22,1,22,1,22,3,22,235,8,22,1,22,1,22,3,22,239,8,22,1,22,1,
        22,3,22,243,8,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,3,23,252,8,23,
        1,24,1,24,1,25,1,25,1,25,5,25,259,8,25,10,25,12,25,262,9,25,1,26,
        1,26,1,26,1,26,3,26,268,8,26,1,26,3,26,271,8,26,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,
        27,302,8,27,1,28,1,28,1,28,5,28,307,8,28,10,28,12,28,310,9,28,1,
        29,1,29,1,30,1,30,1,30,5,30,317,8,30,10,30,12,30,320,9,30,1,31,1,
        31,1,31,5,31,325,8,31,10,31,12,31,328,9,31,1,32,1,32,1,32,5,32,333,
        8,32,10,32,12,32,336,9,32,1,33,1,33,1,33,5,33,341,8,33,10,33,12,
        33,344,9,33,1,34,1,34,1,34,5,34,349,8,34,10,34,12,34,352,9,34,1,
        35,1,35,1,35,5,35,357,8,35,10,35,12,35,360,9,35,1,36,1,36,1,36,1,
        36,1,36,1,36,3,36,368,8,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,384,8,38,1,39,1,39,1,39,1,
        39,5,39,390,8,39,10,39,12,39,393,9,39,1,39,1,39,1,39,0,0,40,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,0,5,1,0,1,2,1,0,29,
        30,1,0,31,34,1,0,35,36,1,0,37,39,411,0,83,1,0,0,0,2,92,1,0,0,0,4,
        103,1,0,0,0,6,105,1,0,0,0,8,108,1,0,0,0,10,115,1,0,0,0,12,125,1,
        0,0,0,14,127,1,0,0,0,16,129,1,0,0,0,18,137,1,0,0,0,20,146,1,0,0,
        0,22,148,1,0,0,0,24,172,1,0,0,0,26,174,1,0,0,0,28,178,1,0,0,0,30,
        186,1,0,0,0,32,198,1,0,0,0,34,200,1,0,0,0,36,210,1,0,0,0,38,212,
        1,0,0,0,40,216,1,0,0,0,42,225,1,0,0,0,44,231,1,0,0,0,46,251,1,0,
        0,0,48,253,1,0,0,0,50,255,1,0,0,0,52,270,1,0,0,0,54,301,1,0,0,0,
        56,303,1,0,0,0,58,311,1,0,0,0,60,313,1,0,0,0,62,321,1,0,0,0,64,329,
        1,0,0,0,66,337,1,0,0,0,68,345,1,0,0,0,70,353,1,0,0,0,72,367,1,0,
        0,0,74,369,1,0,0,0,76,383,1,0,0,0,78,385,1,0,0,0,80,82,3,2,1,0,81,
        80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,
        0,85,83,1,0,0,0,86,87,5,0,0,1,87,1,1,0,0,0,88,93,3,4,2,0,89,93,3,
        6,3,0,90,93,3,8,4,0,91,93,3,26,13,0,92,88,1,0,0,0,92,89,1,0,0,0,
        92,90,1,0,0,0,92,91,1,0,0,0,93,3,1,0,0,0,94,95,3,10,5,0,95,96,5,
        18,0,0,96,104,1,0,0,0,97,98,5,3,0,0,98,99,5,4,0,0,99,100,5,20,0,
        0,100,101,5,3,0,0,101,102,5,21,0,0,102,104,5,18,0,0,103,94,1,0,0,
        0,103,97,1,0,0,0,104,5,1,0,0,0,105,106,3,10,5,0,106,107,3,22,11,
        0,107,7,1,0,0,0,108,109,5,3,0,0,109,110,5,4,0,0,110,111,5,20,0,0,
        111,112,5,3,0,0,112,113,5,21,0,0,113,114,3,22,11,0,114,9,1,0,0,0,
        115,116,3,12,6,0,116,117,5,42,0,0,117,119,5,20,0,0,118,120,3,16,
        8,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,122,5,21,
        0,0,122,11,1,0,0,0,123,126,3,14,7,0,124,126,5,3,0,0,125,123,1,0,
        0,0,125,124,1,0,0,0,126,13,1,0,0,0,127,128,7,0,0,0,128,15,1,0,0,
        0,129,134,3,18,9,0,130,131,5,19,0,0,131,133,3,18,9,0,132,130,1,0,
        0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,17,1,0,0,
        0,136,134,1,0,0,0,137,138,3,14,7,0,138,139,3,20,10,0,139,19,1,0,
        0,0,140,147,5,42,0,0,141,142,5,42,0,0,142,143,5,24,0,0,143,147,5,
        25,0,0,144,145,5,24,0,0,145,147,5,25,0,0,146,140,1,0,0,0,146,141,
        1,0,0,0,146,144,1,0,0,0,147,21,1,0,0,0,148,152,5,22,0,0,149,151,
        3,24,12,0,150,149,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,
        1,0,0,0,153,155,1,0,0,0,154,152,1,0,0,0,155,156,5,23,0,0,156,23,
        1,0,0,0,157,173,3,26,13,0,158,159,3,34,17,0,159,160,5,18,0,0,160,
        173,1,0,0,0,161,162,3,52,26,0,162,163,5,18,0,0,163,173,1,0,0,0,164,
        165,3,38,19,0,165,166,5,18,0,0,166,173,1,0,0,0,167,173,3,40,20,0,
        168,173,3,42,21,0,169,173,3,44,22,0,170,173,3,22,11,0,171,173,5,
        18,0,0,172,157,1,0,0,0,172,158,1,0,0,0,172,161,1,0,0,0,172,164,1,
        0,0,0,172,167,1,0,0,0,172,168,1,0,0,0,172,169,1,0,0,0,172,170,1,
        0,0,0,172,171,1,0,0,0,173,25,1,0,0,0,174,175,3,14,7,0,175,176,3,
        28,14,0,176,177,5,18,0,0,177,27,1,0,0,0,178,183,3,30,15,0,179,180,
        5,19,0,0,180,182,3,30,15,0,181,179,1,0,0,0,182,185,1,0,0,0,183,181,
        1,0,0,0,183,184,1,0,0,0,184,29,1,0,0,0,185,183,1,0,0,0,186,189,3,
        32,16,0,187,188,5,17,0,0,188,190,3,58,29,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,31,1,0,0,0,191,199,5,42,0,0,192,193,5,42,0,0,193,195,
        5,24,0,0,194,196,3,58,29,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,
        1,0,0,0,197,199,5,25,0,0,198,191,1,0,0,0,198,192,1,0,0,0,199,33,
        1,0,0,0,200,201,3,36,18,0,201,202,5,17,0,0,202,203,3,58,29,0,203,
        35,1,0,0,0,204,211,5,42,0,0,205,206,5,42,0,0,206,207,5,24,0,0,207,
        208,3,58,29,0,208,209,5,25,0,0,209,211,1,0,0,0,210,204,1,0,0,0,210,
        205,1,0,0,0,211,37,1,0,0,0,212,214,5,5,0,0,213,215,3,58,29,0,214,
        213,1,0,0,0,214,215,1,0,0,0,215,39,1,0,0,0,216,217,5,6,0,0,217,218,
        5,20,0,0,218,219,3,58,29,0,219,220,5,21,0,0,220,223,3,22,11,0,221,
        222,5,7,0,0,222,224,3,22,11,0,223,221,1,0,0,0,223,224,1,0,0,0,224,
        41,1,0,0,0,225,226,5,8,0,0,226,227,5,20,0,0,227,228,3,58,29,0,228,
        229,5,21,0,0,229,230,3,22,11,0,230,43,1,0,0,0,231,232,5,9,0,0,232,
        234,5,20,0,0,233,235,3,46,23,0,234,233,1,0,0,0,234,235,1,0,0,0,235,
        236,1,0,0,0,236,238,5,18,0,0,237,239,3,58,29,0,238,237,1,0,0,0,238,
        239,1,0,0,0,239,240,1,0,0,0,240,242,5,18,0,0,241,243,3,48,24,0,242,
        241,1,0,0,0,242,243,1,0,0,0,243,244,1,0,0,0,244,245,5,21,0,0,245,
        246,3,22,11,0,246,45,1,0,0,0,247,252,3,34,17,0,248,249,3,14,7,0,
        249,250,3,50,25,0,250,252,1,0,0,0,251,247,1,0,0,0,251,248,1,0,0,
        0,252,47,1,0,0,0,253,254,3,34,17,0,254,49,1,0,0,0,255,260,3,30,15,
        0,256,257,5,19,0,0,257,259,3,30,15,0,258,256,1,0,0,0,259,262,1,0,
        0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,51,1,0,0,0,262,260,1,0,0,
        0,263,271,3,54,27,0,264,265,5,42,0,0,265,267,5,20,0,0,266,268,3,
        56,28,0,267,266,1,0,0,0,267,268,1,0,0,0,268,269,1,0,0,0,269,271,
        5,21,0,0,270,263,1,0,0,0,270,264,1,0,0,0,271,53,1,0,0,0,272,273,
        5,10,0,0,273,274,5,20,0,0,274,302,5,21,0,0,275,276,5,11,0,0,276,
        277,5,20,0,0,277,302,5,21,0,0,278,279,5,12,0,0,279,280,5,20,0,0,
        280,302,5,21,0,0,281,282,5,13,0,0,282,283,5,20,0,0,283,284,3,58,
        29,0,284,285,5,21,0,0,285,302,1,0,0,0,286,287,5,14,0,0,287,288,5,
        20,0,0,288,289,3,58,29,0,289,290,5,21,0,0,290,302,1,0,0,0,291,292,
        5,15,0,0,292,293,5,20,0,0,293,294,3,58,29,0,294,295,5,21,0,0,295,
        302,1,0,0,0,296,297,5,16,0,0,297,298,5,20,0,0,298,299,3,58,29,0,
        299,300,5,21,0,0,300,302,1,0,0,0,301,272,1,0,0,0,301,275,1,0,0,0,
        301,278,1,0,0,0,301,281,1,0,0,0,301,286,1,0,0,0,301,291,1,0,0,0,
        301,296,1,0,0,0,302,55,1,0,0,0,303,308,3,58,29,0,304,305,5,19,0,
        0,305,307,3,58,29,0,306,304,1,0,0,0,307,310,1,0,0,0,308,306,1,0,
        0,0,308,309,1,0,0,0,309,57,1,0,0,0,310,308,1,0,0,0,311,312,3,60,
        30,0,312,59,1,0,0,0,313,318,3,62,31,0,314,315,5,26,0,0,315,317,3,
        62,31,0,316,314,1,0,0,0,317,320,1,0,0,0,318,316,1,0,0,0,318,319,
        1,0,0,0,319,61,1,0,0,0,320,318,1,0,0,0,321,326,3,64,32,0,322,323,
        5,27,0,0,323,325,3,64,32,0,324,322,1,0,0,0,325,328,1,0,0,0,326,324,
        1,0,0,0,326,327,1,0,0,0,327,63,1,0,0,0,328,326,1,0,0,0,329,334,3,
        66,33,0,330,331,7,1,0,0,331,333,3,66,33,0,332,330,1,0,0,0,333,336,
        1,0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,65,1,0,0,0,336,334,1,
        0,0,0,337,342,3,68,34,0,338,339,7,2,0,0,339,341,3,68,34,0,340,338,
        1,0,0,0,341,344,1,0,0,0,342,340,1,0,0,0,342,343,1,0,0,0,343,67,1,
        0,0,0,344,342,1,0,0,0,345,350,3,70,35,0,346,347,7,3,0,0,347,349,
        3,70,35,0,348,346,1,0,0,0,349,352,1,0,0,0,350,348,1,0,0,0,350,351,
        1,0,0,0,351,69,1,0,0,0,352,350,1,0,0,0,353,358,3,72,36,0,354,355,
        7,4,0,0,355,357,3,72,36,0,356,354,1,0,0,0,357,360,1,0,0,0,358,356,
        1,0,0,0,358,359,1,0,0,0,359,71,1,0,0,0,360,358,1,0,0,0,361,362,5,
        28,0,0,362,368,3,72,36,0,363,364,5,36,0,0,364,368,3,72,36,0,365,
        368,3,74,37,0,366,368,3,76,38,0,367,361,1,0,0,0,367,363,1,0,0,0,
        367,365,1,0,0,0,367,366,1,0,0,0,368,73,1,0,0,0,369,370,5,20,0,0,
        370,371,3,14,7,0,371,372,5,21,0,0,372,373,3,72,36,0,373,75,1,0,0,
        0,374,384,5,40,0,0,375,384,5,41,0,0,376,384,3,52,26,0,377,384,3,
        36,18,0,378,384,3,78,39,0,379,380,5,20,0,0,380,381,3,58,29,0,381,
        382,5,21,0,0,382,384,1,0,0,0,383,374,1,0,0,0,383,375,1,0,0,0,383,
        376,1,0,0,0,383,377,1,0,0,0,383,378,1,0,0,0,383,379,1,0,0,0,384,
        77,1,0,0,0,385,386,5,22,0,0,386,391,3,58,29,0,387,388,5,19,0,0,388,
        390,3,58,29,0,389,387,1,0,0,0,390,393,1,0,0,0,391,389,1,0,0,0,391,
        392,1,0,0,0,392,394,1,0,0,0,393,391,1,0,0,0,394,395,5,23,0,0,395,
        79,1,0,0,0,34,83,92,103,119,125,134,146,152,172,183,189,195,198,
        210,214,223,234,238,242,251,260,267,270,301,308,318,326,334,342,
        350,358,367,383,391
    ]

class MOCPParser ( Parser ):

    grammarFileName = "MOCP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'inteiro'", "'real'", "'vazio'", "'principal'", 
                     "'retornar'", "'se'", "'senao'", "'enquanto'", "'para'", 
                     "'ler'", "'lerc'", "'lers'", "'escrever'", "'escreverc'", 
                     "'escreverv'", "'escrevers'", "'='", "';'", "','", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "'||'", "'&&'", 
                     "'!'", "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "INTEIRO", "REAL", "VAZIO", "PRINCIPAL", 
                      "RETORNAR", "SE", "SENAO", "ENQUANTO", "PARA", "LER", 
                      "LERC", "LERS", "ESCREVER", "ESCREVERC", "ESCREVERV", 
                      "ESCREVERS", "ASSIGN", "SEMI", "COMMA", "LPAR", "RPAR", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "OR", "AND", 
                      "NOT", "EQ", "NEQ", "LE", "GE", "LT", "GT", "PLUS", 
                      "MINUS", "STAR", "DIV", "MOD", "NUMBER", "STRING", 
                      "ID", "BLOCK_COMMENT", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_item = 1
    RULE_prototype = 2
    RULE_functionDef = 3
    RULE_principalDef = 4
    RULE_functionHeader = 5
    RULE_returnType = 6
    RULE_baseType = 7
    RULE_paramList = 8
    RULE_param = 9
    RULE_paramDecl = 10
    RULE_block = 11
    RULE_statement = 12
    RULE_declaration = 13
    RULE_initDeclaratorList = 14
    RULE_initDeclarator = 15
    RULE_declarator = 16
    RULE_assignment = 17
    RULE_lvalue = 18
    RULE_returnStmt = 19
    RULE_ifStmt = 20
    RULE_whileStmt = 21
    RULE_forStmt = 22
    RULE_forInit = 23
    RULE_forUpdate = 24
    RULE_initDeclaratorListNoSemi = 25
    RULE_functionCall = 26
    RULE_builtInCall = 27
    RULE_argumentList = 28
    RULE_expr = 29
    RULE_logicalOrExpr = 30
    RULE_logicalAndExpr = 31
    RULE_equalityExpr = 32
    RULE_relationalExpr = 33
    RULE_additiveExpr = 34
    RULE_multiplicativeExpr = 35
    RULE_unaryExpr = 36
    RULE_castExpr = 37
    RULE_primary = 38
    RULE_arrayLiteral = 39

    ruleNames =  [ "program", "item", "prototype", "functionDef", "principalDef", 
                   "functionHeader", "returnType", "baseType", "paramList", 
                   "param", "paramDecl", "block", "statement", "declaration", 
                   "initDeclaratorList", "initDeclarator", "declarator", 
                   "assignment", "lvalue", "returnStmt", "ifStmt", "whileStmt", 
                   "forStmt", "forInit", "forUpdate", "initDeclaratorListNoSemi", 
                   "functionCall", "builtInCall", "argumentList", "expr", 
                   "logicalOrExpr", "logicalAndExpr", "equalityExpr", "relationalExpr", 
                   "additiveExpr", "multiplicativeExpr", "unaryExpr", "castExpr", 
                   "primary", "arrayLiteral" ]

    EOF = Token.EOF
    INTEIRO=1
    REAL=2
    VAZIO=3
    PRINCIPAL=4
    RETORNAR=5
    SE=6
    SENAO=7
    ENQUANTO=8
    PARA=9
    LER=10
    LERC=11
    LERS=12
    ESCREVER=13
    ESCREVERC=14
    ESCREVERV=15
    ESCREVERS=16
    ASSIGN=17
    SEMI=18
    COMMA=19
    LPAR=20
    RPAR=21
    LBRACE=22
    RBRACE=23
    LBRACK=24
    RBRACK=25
    OR=26
    AND=27
    NOT=28
    EQ=29
    NEQ=30
    LE=31
    GE=32
    LT=33
    GT=34
    PLUS=35
    MINUS=36
    STAR=37
    DIV=38
    MOD=39
    NUMBER=40
    STRING=41
    ID=42
    BLOCK_COMMENT=43
    LINE_COMMENT=44
    WS=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MOCPParser.EOF, 0)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.ItemContext)
            else:
                return self.getTypedRuleContext(MOCPParser.ItemContext,i)


        def getRuleIndex(self):
            return MOCPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MOCPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 80
                self.item()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(MOCPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prototype(self):
            return self.getTypedRuleContext(MOCPParser.PrototypeContext,0)


        def functionDef(self):
            return self.getTypedRuleContext(MOCPParser.FunctionDefContext,0)


        def principalDef(self):
            return self.getTypedRuleContext(MOCPParser.PrincipalDefContext,0)


        def declaration(self):
            return self.getTypedRuleContext(MOCPParser.DeclarationContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = MOCPParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_item)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.prototype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.functionDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.principalDef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionHeader(self):
            return self.getTypedRuleContext(MOCPParser.FunctionHeaderContext,0)


        def SEMI(self):
            return self.getToken(MOCPParser.SEMI, 0)

        def VAZIO(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.VAZIO)
            else:
                return self.getToken(MOCPParser.VAZIO, i)

        def PRINCIPAL(self):
            return self.getToken(MOCPParser.PRINCIPAL, 0)

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_prototype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototype" ):
                return visitor.visitPrototype(self)
            else:
                return visitor.visitChildren(self)




    def prototype(self):

        localctx = MOCPParser.PrototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_prototype)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.functionHeader()
                self.state = 95
                self.match(MOCPParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(MOCPParser.VAZIO)
                self.state = 98
                self.match(MOCPParser.PRINCIPAL)
                self.state = 99
                self.match(MOCPParser.LPAR)
                self.state = 100
                self.match(MOCPParser.VAZIO)
                self.state = 101
                self.match(MOCPParser.RPAR)
                self.state = 102
                self.match(MOCPParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionHeader(self):
            return self.getTypedRuleContext(MOCPParser.FunctionHeaderContext,0)


        def block(self):
            return self.getTypedRuleContext(MOCPParser.BlockContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_functionDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)




    def functionDef(self):

        localctx = MOCPParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.functionHeader()
            self.state = 106
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrincipalDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAZIO(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.VAZIO)
            else:
                return self.getToken(MOCPParser.VAZIO, i)

        def PRINCIPAL(self):
            return self.getToken(MOCPParser.PRINCIPAL, 0)

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def block(self):
            return self.getTypedRuleContext(MOCPParser.BlockContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_principalDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrincipalDef" ):
                return visitor.visitPrincipalDef(self)
            else:
                return visitor.visitChildren(self)




    def principalDef(self):

        localctx = MOCPParser.PrincipalDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_principalDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MOCPParser.VAZIO)
            self.state = 109
            self.match(MOCPParser.PRINCIPAL)
            self.state = 110
            self.match(MOCPParser.LPAR)
            self.state = 111
            self.match(MOCPParser.VAZIO)
            self.state = 112
            self.match(MOCPParser.RPAR)
            self.state = 113
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(MOCPParser.ReturnTypeContext,0)


        def ID(self):
            return self.getToken(MOCPParser.ID, 0)

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def paramList(self):
            return self.getTypedRuleContext(MOCPParser.ParamListContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_functionHeader

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionHeader" ):
                return visitor.visitFunctionHeader(self)
            else:
                return visitor.visitChildren(self)




    def functionHeader(self):

        localctx = MOCPParser.FunctionHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionHeader)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.returnType()
            self.state = 116
            self.match(MOCPParser.ID)
            self.state = 117
            self.match(MOCPParser.LPAR)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 118
                self.paramList()


            self.state = 121
            self.match(MOCPParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(MOCPParser.BaseTypeContext,0)


        def VAZIO(self):
            return self.getToken(MOCPParser.VAZIO, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = MOCPParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnType)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.baseType()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(MOCPParser.VAZIO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEIRO(self):
            return self.getToken(MOCPParser.INTEIRO, 0)

        def REAL(self):
            return self.getToken(MOCPParser.REAL, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_baseType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = MOCPParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.ParamContext)
            else:
                return self.getTypedRuleContext(MOCPParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.COMMA)
            else:
                return self.getToken(MOCPParser.COMMA, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MOCPParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.param()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 130
                self.match(MOCPParser.COMMA)
                self.state = 131
                self.param()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(MOCPParser.BaseTypeContext,0)


        def paramDecl(self):
            return self.getTypedRuleContext(MOCPParser.ParamDeclContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MOCPParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.baseType()
            self.state = 138
            self.paramDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MOCPParser.ID, 0)

        def LBRACK(self):
            return self.getToken(MOCPParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MOCPParser.RBRACK, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_paramDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDecl" ):
                return visitor.visitParamDecl(self)
            else:
                return visitor.visitChildren(self)




    def paramDecl(self):

        localctx = MOCPParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramDecl)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(MOCPParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(MOCPParser.ID)
                self.state = 142
                self.match(MOCPParser.LBRACK)
                self.state = 143
                self.match(MOCPParser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.match(MOCPParser.LBRACK)
                self.state = 145
                self.match(MOCPParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MOCPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MOCPParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.StatementContext)
            else:
                return self.getTypedRuleContext(MOCPParser.StatementContext,i)


        def getRuleIndex(self):
            return MOCPParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MOCPParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MOCPParser.LBRACE)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398051098470) != 0):
                self.state = 149
                self.statement()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(MOCPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MOCPParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MOCPParser.AssignmentContext,0)


        def SEMI(self):
            return self.getToken(MOCPParser.SEMI, 0)

        def functionCall(self):
            return self.getTypedRuleContext(MOCPParser.FunctionCallContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MOCPParser.ReturnStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MOCPParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MOCPParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MOCPParser.ForStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(MOCPParser.BlockContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MOCPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.assignment()
                self.state = 159
                self.match(MOCPParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.functionCall()
                self.state = 162
                self.match(MOCPParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.returnStmt()
                self.state = 165
                self.match(MOCPParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.ifStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 168
                self.whileStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 169
                self.forStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 170
                self.block()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 171
                self.match(MOCPParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(MOCPParser.BaseTypeContext,0)


        def initDeclaratorList(self):
            return self.getTypedRuleContext(MOCPParser.InitDeclaratorListContext,0)


        def SEMI(self):
            return self.getToken(MOCPParser.SEMI, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MOCPParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.baseType()
            self.state = 175
            self.initDeclaratorList()
            self.state = 176
            self.match(MOCPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitDeclaratorListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.InitDeclaratorContext)
            else:
                return self.getTypedRuleContext(MOCPParser.InitDeclaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.COMMA)
            else:
                return self.getToken(MOCPParser.COMMA, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_initDeclaratorList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitDeclaratorList" ):
                return visitor.visitInitDeclaratorList(self)
            else:
                return visitor.visitChildren(self)




    def initDeclaratorList(self):

        localctx = MOCPParser.InitDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_initDeclaratorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.initDeclarator()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 179
                self.match(MOCPParser.COMMA)
                self.state = 180
                self.initDeclarator()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(MOCPParser.DeclaratorContext,0)


        def ASSIGN(self):
            return self.getToken(MOCPParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_initDeclarator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitDeclarator" ):
                return visitor.visitInitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def initDeclarator(self):

        localctx = MOCPParser.InitDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_initDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.declarator()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 187
                self.match(MOCPParser.ASSIGN)
                self.state = 188
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MOCPParser.ID, 0)

        def LBRACK(self):
            return self.getToken(MOCPParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MOCPParser.RBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_declarator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarator" ):
                return visitor.visitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def declarator(self):

        localctx = MOCPParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(MOCPParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(MOCPParser.ID)
                self.state = 193
                self.match(MOCPParser.LBRACK)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7765574679552) != 0):
                    self.state = 194
                    self.expr()


                self.state = 197
                self.match(MOCPParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(MOCPParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(MOCPParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MOCPParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.lvalue()
            self.state = 201
            self.match(MOCPParser.ASSIGN)
            self.state = 202
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MOCPParser.ID, 0)

        def LBRACK(self):
            return self.getToken(MOCPParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MOCPParser.RBRACK, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_lvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvalue" ):
                return visitor.visitLvalue(self)
            else:
                return visitor.visitChildren(self)




    def lvalue(self):

        localctx = MOCPParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lvalue)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(MOCPParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(MOCPParser.ID)
                self.state = 206
                self.match(MOCPParser.LBRACK)
                self.state = 207
                self.expr()
                self.state = 208
                self.match(MOCPParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(MOCPParser.RETORNAR, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MOCPParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MOCPParser.RETORNAR)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7765574679552) != 0):
                self.state = 213
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SE(self):
            return self.getToken(MOCPParser.SE, 0)

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.BlockContext)
            else:
                return self.getTypedRuleContext(MOCPParser.BlockContext,i)


        def SENAO(self):
            return self.getToken(MOCPParser.SENAO, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MOCPParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MOCPParser.SE)
            self.state = 217
            self.match(MOCPParser.LPAR)
            self.state = 218
            self.expr()
            self.state = 219
            self.match(MOCPParser.RPAR)
            self.state = 220
            self.block()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 221
                self.match(MOCPParser.SENAO)
                self.state = 222
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENQUANTO(self):
            return self.getToken(MOCPParser.ENQUANTO, 0)

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def block(self):
            return self.getTypedRuleContext(MOCPParser.BlockContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MOCPParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MOCPParser.ENQUANTO)
            self.state = 226
            self.match(MOCPParser.LPAR)
            self.state = 227
            self.expr()
            self.state = 228
            self.match(MOCPParser.RPAR)
            self.state = 229
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(MOCPParser.PARA, 0)

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.SEMI)
            else:
                return self.getToken(MOCPParser.SEMI, i)

        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def block(self):
            return self.getTypedRuleContext(MOCPParser.BlockContext,0)


        def forInit(self):
            return self.getTypedRuleContext(MOCPParser.ForInitContext,0)


        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(MOCPParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MOCPParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MOCPParser.PARA)
            self.state = 232
            self.match(MOCPParser.LPAR)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046511110) != 0):
                self.state = 233
                self.forInit()


            self.state = 236
            self.match(MOCPParser.SEMI)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7765574679552) != 0):
                self.state = 237
                self.expr()


            self.state = 240
            self.match(MOCPParser.SEMI)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 241
                self.forUpdate()


            self.state = 244
            self.match(MOCPParser.RPAR)
            self.state = 245
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MOCPParser.AssignmentContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MOCPParser.BaseTypeContext,0)


        def initDeclaratorListNoSemi(self):
            return self.getTypedRuleContext(MOCPParser.InitDeclaratorListNoSemiContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_forInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = MOCPParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forInit)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.assignment()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.baseType()
                self.state = 249
                self.initDeclaratorListNoSemi()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MOCPParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_forUpdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = MOCPParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitDeclaratorListNoSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.InitDeclaratorContext)
            else:
                return self.getTypedRuleContext(MOCPParser.InitDeclaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.COMMA)
            else:
                return self.getToken(MOCPParser.COMMA, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_initDeclaratorListNoSemi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitDeclaratorListNoSemi" ):
                return visitor.visitInitDeclaratorListNoSemi(self)
            else:
                return visitor.visitChildren(self)




    def initDeclaratorListNoSemi(self):

        localctx = MOCPParser.InitDeclaratorListNoSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_initDeclaratorListNoSemi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.initDeclarator()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 256
                self.match(MOCPParser.COMMA)
                self.state = 257
                self.initDeclarator()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def builtInCall(self):
            return self.getTypedRuleContext(MOCPParser.BuiltInCallContext,0)


        def ID(self):
            return self.getToken(MOCPParser.ID, 0)

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MOCPParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MOCPParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.builtInCall()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(MOCPParser.ID)
                self.state = 265
                self.match(MOCPParser.LPAR)
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7765574679552) != 0):
                    self.state = 266
                    self.argumentList()


                self.state = 269
                self.match(MOCPParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuiltInCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LER(self):
            return self.getToken(MOCPParser.LER, 0)

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def LERC(self):
            return self.getToken(MOCPParser.LERC, 0)

        def LERS(self):
            return self.getToken(MOCPParser.LERS, 0)

        def ESCREVER(self):
            return self.getToken(MOCPParser.ESCREVER, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def ESCREVERC(self):
            return self.getToken(MOCPParser.ESCREVERC, 0)

        def ESCREVERV(self):
            return self.getToken(MOCPParser.ESCREVERV, 0)

        def ESCREVERS(self):
            return self.getToken(MOCPParser.ESCREVERS, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_builtInCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuiltInCall" ):
                return visitor.visitBuiltInCall(self)
            else:
                return visitor.visitChildren(self)




    def builtInCall(self):

        localctx = MOCPParser.BuiltInCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_builtInCall)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(MOCPParser.LER)
                self.state = 273
                self.match(MOCPParser.LPAR)
                self.state = 274
                self.match(MOCPParser.RPAR)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(MOCPParser.LERC)
                self.state = 276
                self.match(MOCPParser.LPAR)
                self.state = 277
                self.match(MOCPParser.RPAR)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.match(MOCPParser.LERS)
                self.state = 279
                self.match(MOCPParser.LPAR)
                self.state = 280
                self.match(MOCPParser.RPAR)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.match(MOCPParser.ESCREVER)
                self.state = 282
                self.match(MOCPParser.LPAR)
                self.state = 283
                self.expr()
                self.state = 284
                self.match(MOCPParser.RPAR)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 286
                self.match(MOCPParser.ESCREVERC)
                self.state = 287
                self.match(MOCPParser.LPAR)
                self.state = 288
                self.expr()
                self.state = 289
                self.match(MOCPParser.RPAR)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 291
                self.match(MOCPParser.ESCREVERV)
                self.state = 292
                self.match(MOCPParser.LPAR)
                self.state = 293
                self.expr()
                self.state = 294
                self.match(MOCPParser.RPAR)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 296
                self.match(MOCPParser.ESCREVERS)
                self.state = 297
                self.match(MOCPParser.LPAR)
                self.state = 298
                self.expr()
                self.state = 299
                self.match(MOCPParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MOCPParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.COMMA)
            else:
                return self.getToken(MOCPParser.COMMA, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = MOCPParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.expr()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 304
                self.match(MOCPParser.COMMA)
                self.state = 305
                self.expr()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpr(self):
            return self.getTypedRuleContext(MOCPParser.LogicalOrExprContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MOCPParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.logicalOrExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.LogicalAndExprContext)
            else:
                return self.getTypedRuleContext(MOCPParser.LogicalAndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.OR)
            else:
                return self.getToken(MOCPParser.OR, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_logicalOrExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpr" ):
                return visitor.visitLogicalOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpr(self):

        localctx = MOCPParser.LogicalOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_logicalOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.logicalAndExpr()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 314
                self.match(MOCPParser.OR)
                self.state = 315
                self.logicalAndExpr()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.EqualityExprContext)
            else:
                return self.getTypedRuleContext(MOCPParser.EqualityExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.AND)
            else:
                return self.getToken(MOCPParser.AND, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_logicalAndExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpr" ):
                return visitor.visitLogicalAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpr(self):

        localctx = MOCPParser.LogicalAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_logicalAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.equalityExpr()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 322
                self.match(MOCPParser.AND)
                self.state = 323
                self.equalityExpr()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(MOCPParser.RelationalExprContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.EQ)
            else:
                return self.getToken(MOCPParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.NEQ)
            else:
                return self.getToken(MOCPParser.NEQ, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_equalityExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpr(self):

        localctx = MOCPParser.EqualityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_equalityExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.relationalExpr()
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==30:
                self.state = 330
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 331
                self.relationalExpr()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(MOCPParser.AdditiveExprContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.LT)
            else:
                return self.getToken(MOCPParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.LE)
            else:
                return self.getToken(MOCPParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.GT)
            else:
                return self.getToken(MOCPParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.GE)
            else:
                return self.getToken(MOCPParser.GE, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_relationalExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = MOCPParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.additiveExpr()
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0):
                self.state = 338
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 339
                self.additiveExpr()
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(MOCPParser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.PLUS)
            else:
                return self.getToken(MOCPParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.MINUS)
            else:
                return self.getToken(MOCPParser.MINUS, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_additiveExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = MOCPParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.multiplicativeExpr()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35 or _la==36:
                self.state = 346
                _la = self._input.LA(1)
                if not(_la==35 or _la==36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 347
                self.multiplicativeExpr()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(MOCPParser.UnaryExprContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.STAR)
            else:
                return self.getToken(MOCPParser.STAR, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.DIV)
            else:
                return self.getToken(MOCPParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.MOD)
            else:
                return self.getToken(MOCPParser.MOD, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_multiplicativeExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = MOCPParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.unaryExpr()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 962072674304) != 0):
                self.state = 354
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 962072674304) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 355
                self.unaryExpr()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MOCPParser.NOT, 0)

        def unaryExpr(self):
            return self.getTypedRuleContext(MOCPParser.UnaryExprContext,0)


        def MINUS(self):
            return self.getToken(MOCPParser.MINUS, 0)

        def castExpr(self):
            return self.getTypedRuleContext(MOCPParser.CastExprContext,0)


        def primary(self):
            return self.getTypedRuleContext(MOCPParser.PrimaryContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = MOCPParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unaryExpr)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(MOCPParser.NOT)
                self.state = 362
                self.unaryExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(MOCPParser.MINUS)
                self.state = 364
                self.unaryExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                self.castExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 366
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def baseType(self):
            return self.getTypedRuleContext(MOCPParser.BaseTypeContext,0)


        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def unaryExpr(self):
            return self.getTypedRuleContext(MOCPParser.UnaryExprContext,0)


        def getRuleIndex(self):
            return MOCPParser.RULE_castExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpr" ):
                return visitor.visitCastExpr(self)
            else:
                return visitor.visitChildren(self)




    def castExpr(self):

        localctx = MOCPParser.CastExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_castExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(MOCPParser.LPAR)
            self.state = 370
            self.baseType()
            self.state = 371
            self.match(MOCPParser.RPAR)
            self.state = 372
            self.unaryExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MOCPParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(MOCPParser.STRING, 0)

        def functionCall(self):
            return self.getTypedRuleContext(MOCPParser.FunctionCallContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(MOCPParser.LvalueContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(MOCPParser.ArrayLiteralContext,0)


        def LPAR(self):
            return self.getToken(MOCPParser.LPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(MOCPParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(MOCPParser.RPAR, 0)

        def getRuleIndex(self):
            return MOCPParser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MOCPParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_primary)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(MOCPParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(MOCPParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self.lvalue()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 378
                self.arrayLiteral()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 379
                self.match(MOCPParser.LPAR)
                self.state = 380
                self.expr()
                self.state = 381
                self.match(MOCPParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MOCPParser.LBRACE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MOCPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MOCPParser.ExprContext,i)


        def RBRACE(self):
            return self.getToken(MOCPParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MOCPParser.COMMA)
            else:
                return self.getToken(MOCPParser.COMMA, i)

        def getRuleIndex(self):
            return MOCPParser.RULE_arrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = MOCPParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MOCPParser.LBRACE)
            self.state = 386
            self.expr()
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 387
                self.match(MOCPParser.COMMA)
                self.state = 388
                self.expr()
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 394
            self.match(MOCPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





