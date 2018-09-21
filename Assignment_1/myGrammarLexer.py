# Generated from myGrammar.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\67\u012c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write(u"\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write(u"\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write(u"\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3")
        buf.write(u"\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write(u"\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3")
        buf.write(u"#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3")
        buf.write(u"\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*")
        buf.write(u"\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write(u"/\3/\3\60\3\60\3\60\3\60\3\61\3\61\7\61\u0116\n\61\f")
        buf.write(u"\61\16\61\u0119\13\61\3\62\6\62\u011c\n\62\r\62\16\62")
        buf.write(u"\u011d\3\63\3\63\3\64\6\64\u0123\n\64\r\64\16\64\u0124")
        buf.write(u"\3\64\3\64\3\65\3\65\3\66\3\66\2\2\67\3\3\5\4\7\5\t\6")
        buf.write(u"\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write(u"\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write(u"\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]")
        buf.write(u"\60_\61a\62c\63e\64g\65i\66k\67\3\2\6\5\2C\\aac|\6\2")
        buf.write(u"\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2\u012e\2\3\3")
        buf.write(u"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write(u"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write(u"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write(u"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write(u"\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write(u"/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write(u"\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2")
        buf.write(u"\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2")
        buf.write(u"\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2")
        buf.write(u"\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3")
        buf.write(u"\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write(u"g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\3m\3\2\2\2\5x\3\2\2\2")
        buf.write(u"\7{\3\2\2\2\t\u0082\3\2\2\2\13\u0085\3\2\2\2\r\u008a")
        buf.write(u"\3\2\2\2\17\u008f\3\2\2\2\21\u0092\3\2\2\2\23\u0095\3")
        buf.write(u"\2\2\2\25\u0099\3\2\2\2\27\u009f\3\2\2\2\31\u00a2\3\2")
        buf.write(u"\2\2\33\u00a4\3\2\2\2\35\u00a6\3\2\2\2\37\u00aa\3\2\2")
        buf.write(u"\2!\u00b1\3\2\2\2#\u00b3\3\2\2\2%\u00b5\3\2\2\2\'\u00b7")
        buf.write(u"\3\2\2\2)\u00b9\3\2\2\2+\u00bb\3\2\2\2-\u00bd\3\2\2\2")
        buf.write(u"/\u00c1\3\2\2\2\61\u00c3\3\2\2\2\63\u00c5\3\2\2\2\65")
        buf.write(u"\u00c7\3\2\2\2\67\u00c9\3\2\2\29\u00cb\3\2\2\2;\u00cd")
        buf.write(u"\3\2\2\2=\u00cf\3\2\2\2?\u00d2\3\2\2\2A\u00d4\3\2\2\2")
        buf.write(u"C\u00d7\3\2\2\2E\u00d9\3\2\2\2G\u00dc\3\2\2\2I\u00df")
        buf.write(u"\3\2\2\2K\u00e4\3\2\2\2M\u00ea\3\2\2\2O\u00ee\3\2\2\2")
        buf.write(u"Q\u00f4\3\2\2\2S\u00fb\3\2\2\2U\u0100\3\2\2\2W\u0103")
        buf.write(u"\3\2\2\2Y\u0106\3\2\2\2[\u0109\3\2\2\2]\u010c\3\2\2\2")
        buf.write(u"_\u010f\3\2\2\2a\u0113\3\2\2\2c\u011b\3\2\2\2e\u011f")
        buf.write(u"\3\2\2\2g\u0122\3\2\2\2i\u0128\3\2\2\2k\u012a\3\2\2\2")
        buf.write(u"mn\7t\2\2no\7c\2\2op\7p\2\2pq\7i\2\2qr\7g\2\2rs\7*\2")
        buf.write(u"\2st\7n\2\2tu\7g\2\2uv\7p\2\2vw\7*\2\2w\4\3\2\2\2xy\7")
        buf.write(u"+\2\2yz\7<\2\2z\6\3\2\2\2{|\7t\2\2|}\7c\2\2}~\7p\2\2")
        buf.write(u"~\177\7i\2\2\177\u0080\7g\2\2\u0080\u0081\7*\2\2\u0081")
        buf.write(u"\b\3\2\2\2\u0082\u0083\7k\2\2\u0083\u0084\7h\2\2\u0084")
        buf.write(u"\n\3\2\2\2\u0085\u0086\7g\2\2\u0086\u0087\7n\2\2\u0087")
        buf.write(u"\u0088\7u\2\2\u0088\u0089\7g\2\2\u0089\f\3\2\2\2\u008a")
        buf.write(u"\u008b\7g\2\2\u008b\u008c\7n\2\2\u008c\u008d\7k\2\2\u008d")
        buf.write(u"\u008e\7h\2\2\u008e\16\3\2\2\2\u008f\u0090\7k\2\2\u0090")
        buf.write(u"\u0091\7p\2\2\u0091\20\3\2\2\2\u0092\u0093\7c\2\2\u0093")
        buf.write(u"\u0094\7u\2\2\u0094\22\3\2\2\2\u0095\u0096\7h\2\2\u0096")
        buf.write(u"\u0097\7q\2\2\u0097\u0098\7t\2\2\u0098\24\3\2\2\2\u0099")
        buf.write(u"\u009a\7y\2\2\u009a\u009b\7j\2\2\u009b\u009c\7k\2\2\u009c")
        buf.write(u"\u009d\7n\2\2\u009d\u009e\7g\2\2\u009e\26\3\2\2\2\u009f")
        buf.write(u"\u00a0\7(\2\2\u00a0\u00a1\7(\2\2\u00a1\30\3\2\2\2\u00a2")
        buf.write(u"\u00a3\7.\2\2\u00a3\32\3\2\2\2\u00a4\u00a5\7<\2\2\u00a5")
        buf.write(u"\34\3\2\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8\7g\2\2\u00a8")
        buf.write(u"\u00a9\7h\2\2\u00a9\36\3\2\2\2\u00aa\u00ab\7t\2\2\u00ab")
        buf.write(u"\u00ac\7g\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7w\2\2\u00ae")
        buf.write(u"\u00af\7t\2\2\u00af\u00b0\7p\2\2\u00b0 \3\2\2\2\u00b1")
        buf.write(u"\u00b2\7*\2\2\u00b2\"\3\2\2\2\u00b3\u00b4\7+\2\2\u00b4")
        buf.write(u"$\3\2\2\2\u00b5\u00b6\7}\2\2\u00b6&\3\2\2\2\u00b7\u00b8")
        buf.write(u"\7\177\2\2\u00b8(\3\2\2\2\u00b9\u00ba\7]\2\2\u00ba*\3")
        buf.write(u"\2\2\2\u00bb\u00bc\7_\2\2\u00bc,\3\2\2\2\u00bd\u00be")
        buf.write(u"\7p\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7v\2\2\u00c0.")
        buf.write(u"\3\2\2\2\u00c1\u00c2\7-\2\2\u00c2\60\3\2\2\2\u00c3\u00c4")
        buf.write(u"\7/\2\2\u00c4\62\3\2\2\2\u00c5\u00c6\7,\2\2\u00c6\64")
        buf.write(u"\3\2\2\2\u00c7\u00c8\7\61\2\2\u00c8\66\3\2\2\2\u00c9")
        buf.write(u"\u00ca\7\'\2\2\u00ca8\3\2\2\2\u00cb\u00cc\7`\2\2\u00cc")
        buf.write(u":\3\2\2\2\u00cd\u00ce\7@\2\2\u00ce<\3\2\2\2\u00cf\u00d0")
        buf.write(u"\7@\2\2\u00d0\u00d1\7?\2\2\u00d1>\3\2\2\2\u00d2\u00d3")
        buf.write(u"\7>\2\2\u00d3@\3\2\2\2\u00d4\u00d5\7>\2\2\u00d5\u00d6")
        buf.write(u"\7?\2\2\u00d6B\3\2\2\2\u00d7\u00d8\7?\2\2\u00d8D\3\2")
        buf.write(u"\2\2\u00d9\u00da\7?\2\2\u00da\u00db\7?\2\2\u00dbF\3\2")
        buf.write(u"\2\2\u00dc\u00dd\7#\2\2\u00dd\u00de\7?\2\2\u00deH\3\2")
        buf.write(u"\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2")
        buf.write(u"\7w\2\2\u00e2\u00e3\7g\2\2\u00e3J\3\2\2\2\u00e4\u00e5")
        buf.write(u"\7h\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write(u"\7u\2\2\u00e8\u00e9\7g\2\2\u00e9L\3\2\2\2\u00ea\u00eb")
        buf.write(u"\7n\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed\7p\2\2\u00edN")
        buf.write(u"\3\2\2\2\u00ee\u00ef\7r\2\2\u00ef\u00f0\7t\2\2\u00f0")
        buf.write(u"\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7v\2\2\u00f3")
        buf.write(u"P\3\2\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7r\2\2\u00f6")
        buf.write(u"\u00f7\7r\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write(u"\u00fa\7f\2\2\u00faR\3\2\2\2\u00fb\u00fc\7q\2\2\u00fc")
        buf.write(u"\u00fd\7r\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7p\2\2\u00ff")
        buf.write(u"T\3\2\2\2\u0100\u0101\7-\2\2\u0101\u0102\7?\2\2\u0102")
        buf.write(u"V\3\2\2\2\u0103\u0104\7/\2\2\u0104\u0105\7?\2\2\u0105")
        buf.write(u"X\3\2\2\2\u0106\u0107\7,\2\2\u0107\u0108\7?\2\2\u0108")
        buf.write(u"Z\3\2\2\2\u0109\u010a\7\61\2\2\u010a\u010b\7?\2\2\u010b")
        buf.write(u"\\\3\2\2\2\u010c\u010d\7q\2\2\u010d\u010e\7t\2\2\u010e")
        buf.write(u"^\3\2\2\2\u010f\u0110\7c\2\2\u0110\u0111\7p\2\2\u0111")
        buf.write(u"\u0112\7f\2\2\u0112`\3\2\2\2\u0113\u0117\t\2\2\2\u0114")
        buf.write(u"\u0116\t\3\2\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2\2")
        buf.write(u"\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118b\3\2")
        buf.write(u"\2\2\u0119\u0117\3\2\2\2\u011a\u011c\t\4\2\2\u011b\u011a")
        buf.write(u"\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write(u"\u011e\3\2\2\2\u011ed\3\2\2\2\u011f\u0120\7\f\2\2\u0120")
        buf.write(u"f\3\2\2\2\u0121\u0123\t\5\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write(u"\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2")
        buf.write(u"\2\u0125\u0126\3\2\2\2\u0126\u0127\b\64\2\2\u0127h\3")
        buf.write(u"\2\2\2\u0128\u0129\7%\2\2\u0129j\3\2\2\2\u012a\u012b")
        buf.write(u"\7\13\2\2\u012bl\3\2\2\2\6\2\u0117\u011d\u0124\3\b\2")
        buf.write(u"\2")
        return buf.getvalue()


class myGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    IF = 4
    ELSE = 5
    ELIF = 6
    IN = 7
    AS = 8
    FOR = 9
    WHILE = 10
    ANDAND = 11
    COMMA = 12
    COLON = 13
    DEF = 14
    RET = 15
    LPAREN = 16
    RPAREN = 17
    LBRACE = 18
    RBRACE = 19
    LBRACK = 20
    RBRACK = 21
    NOT = 22
    PLUS = 23
    MINUS = 24
    MULTIPLY = 25
    DIVIDE = 26
    MOD = 27
    POWER = 28
    GT = 29
    GE = 30
    LT = 31
    LE = 32
    ASSIGNMENT = 33
    EQUAL = 34
    NOTEQUAL = 35
    TRUE = 36
    FALSE = 37
    LENGTH = 38
    PRINT = 39
    APPEND = 40
    OPEN = 41
    PLUSEQUAL = 42
    MINUSEQUAL = 43
    MULTEQUAL = 44
    DIVEQUAL = 45
    OR = 46
    AND = 47
    ID = 48
    NUMBER = 49
    NEWLINE = 50
    WS = 51
    COMMENT = 52
    INDENT = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'range(len('", u"'):'", u"'range('", u"'if'", u"'else'", u"'elif'", 
            u"'in'", u"'as'", u"'for'", u"'while'", u"'&&'", u"','", u"':'", 
            u"'def'", u"'return'", u"'('", u"')'", u"'{'", u"'}'", u"'['", 
            u"']'", u"'not'", u"'+'", u"'-'", u"'*'", u"'/'", u"'%'", u"'^'", 
            u"'>'", u"'>='", u"'<'", u"'<='", u"'='", u"'=='", u"'!='", 
            u"'true'", u"'false'", u"'len'", u"'print'", u"'append'", u"'open'", 
            u"'+='", u"'-='", u"'*='", u"'/='", u"'or'", u"'and'", u"'\n'", 
            u"'#'", u"'\t'" ]

    symbolicNames = [ u"<INVALID>",
            u"IF", u"ELSE", u"ELIF", u"IN", u"AS", u"FOR", u"WHILE", u"ANDAND", 
            u"COMMA", u"COLON", u"DEF", u"RET", u"LPAREN", u"RPAREN", u"LBRACE", 
            u"RBRACE", u"LBRACK", u"RBRACK", u"NOT", u"PLUS", u"MINUS", 
            u"MULTIPLY", u"DIVIDE", u"MOD", u"POWER", u"GT", u"GE", u"LT", 
            u"LE", u"ASSIGNMENT", u"EQUAL", u"NOTEQUAL", u"TRUE", u"FALSE", 
            u"LENGTH", u"PRINT", u"APPEND", u"OPEN", u"PLUSEQUAL", u"MINUSEQUAL", 
            u"MULTEQUAL", u"DIVEQUAL", u"OR", u"AND", u"ID", u"NUMBER", 
            u"NEWLINE", u"WS", u"COMMENT", u"INDENT" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"IF", u"ELSE", u"ELIF", u"IN", 
                  u"AS", u"FOR", u"WHILE", u"ANDAND", u"COMMA", u"COLON", 
                  u"DEF", u"RET", u"LPAREN", u"RPAREN", u"LBRACE", u"RBRACE", 
                  u"LBRACK", u"RBRACK", u"NOT", u"PLUS", u"MINUS", u"MULTIPLY", 
                  u"DIVIDE", u"MOD", u"POWER", u"GT", u"GE", u"LT", u"LE", 
                  u"ASSIGNMENT", u"EQUAL", u"NOTEQUAL", u"TRUE", u"FALSE", 
                  u"LENGTH", u"PRINT", u"APPEND", u"OPEN", u"PLUSEQUAL", 
                  u"MINUSEQUAL", u"MULTEQUAL", u"DIVEQUAL", u"OR", u"AND", 
                  u"ID", u"NUMBER", u"NEWLINE", u"WS", u"COMMENT", u"INDENT" ]

    grammarFileName = u"myGrammar.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(myGrammarLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


