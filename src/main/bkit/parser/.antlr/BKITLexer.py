# Generated from e:\BK\Principles of Programing Languages\assignment\assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u022b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\38\78\u0163\n8\f8\168\u0166\138")
        buf.write("\38\38\38\38\78\u016c\n8\f8\168\u016f\138\38\38\38\38")
        buf.write("\78\u0175\n8\f8\168\u0178\138\58\u017a\n8\39\39\39\79")
        buf.write("\u017f\n9\f9\169\u0182\139\59\u0184\n9\39\39\79\u0188")
        buf.write("\n9\f9\169\u018b\139\39\59\u018e\n9\39\39\39\79\u0193")
        buf.write("\n9\f9\169\u0196\139\59\u0198\n9\39\59\u019b\n9\39\79")
        buf.write("\u019e\n9\f9\169\u01a1\139\39\59\u01a4\n9\3:\3:\5:\u01a8")
        buf.write("\n:\3:\6:\u01ab\n:\r:\16:\u01ac\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\5;\u01b8\n;\3<\3<\3<\3<\3<\7<\u01bf\n<\f<\16<\u01c2")
        buf.write("\13<\3<\3<\3=\3=\3=\3>\3>\5>\u01cb\n>\3>\3>\5>\u01cf\n")
        buf.write(">\3>\3>\5>\u01d3\n>\3>\7>\u01d6\n>\f>\16>\u01d9\13>\7")
        buf.write(">\u01db\n>\f>\16>\u01de\13>\3>\5>\u01e1\n>\3>\3>\3?\3")
        buf.write("?\3?\3?\3?\5?\u01ea\n?\3@\3@\3@\3@\7@\u01f0\n@\f@\16@")
        buf.write("\u01f3\13@\3@\3@\3@\3@\3@\3A\6A\u01fb\nA\rA\16A\u01fc")
        buf.write("\3A\3A\3B\3B\3B\3B\7B\u0205\nB\fB\16B\u0208\13B\3B\3B")
        buf.write("\3B\3B\5B\u020e\nB\3C\3C\3C\3C\7C\u0214\nC\fC\16C\u0217")
        buf.write("\13C\3C\5C\u021a\nC\3D\3D\3D\3D\7D\u0220\nD\fD\16D\u0223")
        buf.write("\13D\3D\5D\u0226\nD\3D\3D\3E\3E\4\u01c0\u01f1\2F\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s\2u;w<y")
        buf.write("\2{=}>\177?\u0081@\u0083A\u0085B\u0087C\u0089D\3\2\24")
        buf.write("\3\2c|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2ZZzz\4\2\63;")
        buf.write("CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\4\2GGgg\4\2--//\5")
        buf.write("\2$$))^^\t\2))^^ddhhppttvv\5\2\13\f\16\17\"\"\3\2$$\3")
        buf.write("\3\f\f\3\2,,\2\u0251\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\3\u008b\3\2\2\2\5\u0092\3\2\2\2\7\u0097\3\2\2\2\t\u009d")
        buf.write("\3\2\2\2\13\u00a6\3\2\2\2\r\u00a9\3\2\2\2\17\u00ae\3\2")
        buf.write("\2\2\21\u00b5\3\2\2\2\23\u00bd\3\2\2\2\25\u00c3\3\2\2")
        buf.write("\2\27\u00ca\3\2\2\2\31\u00d3\3\2\2\2\33\u00d7\3\2\2\2")
        buf.write("\35\u00e0\3\2\2\2\37\u00e3\3\2\2\2!\u00ed\3\2\2\2#\u00f4")
        buf.write("\3\2\2\2%\u00f9\3\2\2\2\'\u00fd\3\2\2\2)\u0103\3\2\2\2")
        buf.write("+\u0109\3\2\2\2-\u010b\3\2\2\2/\u010d\3\2\2\2\61\u010f")
        buf.write("\3\2\2\2\63\u0111\3\2\2\2\65\u0113\3\2\2\2\67\u0115\3")
        buf.write("\2\2\29\u0118\3\2\2\2;\u011b\3\2\2\2=\u011e\3\2\2\2?\u0121")
        buf.write("\3\2\2\2A\u0123\3\2\2\2C\u0126\3\2\2\2E\u0129\3\2\2\2")
        buf.write("G\u012c\3\2\2\2I\u012f\3\2\2\2K\u0131\3\2\2\2M\u0133\3")
        buf.write("\2\2\2O\u0136\3\2\2\2Q\u0139\3\2\2\2S\u013d\3\2\2\2U\u0140")
        buf.write("\3\2\2\2W\u0143\3\2\2\2Y\u0147\3\2\2\2[\u014b\3\2\2\2")
        buf.write("]\u014d\3\2\2\2_\u014f\3\2\2\2a\u0151\3\2\2\2c\u0153\3")
        buf.write("\2\2\2e\u0155\3\2\2\2g\u0157\3\2\2\2i\u0159\3\2\2\2k\u015b")
        buf.write("\3\2\2\2m\u015d\3\2\2\2o\u0179\3\2\2\2q\u01a3\3\2\2\2")
        buf.write("s\u01a5\3\2\2\2u\u01b7\3\2\2\2w\u01b9\3\2\2\2y\u01c5\3")
        buf.write("\2\2\2{\u01c8\3\2\2\2}\u01e9\3\2\2\2\177\u01eb\3\2\2\2")
        buf.write("\u0081\u01fa\3\2\2\2\u0083\u0200\3\2\2\2\u0085\u020f\3")
        buf.write("\2\2\2\u0087\u021b\3\2\2\2\u0089\u0229\3\2\2\2\u008b\u008f")
        buf.write("\t\2\2\2\u008c\u008e\t\3\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\4\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7D\2")
        buf.write("\2\u0093\u0094\7q\2\2\u0094\u0095\7f\2\2\u0095\u0096\7")
        buf.write("{\2\2\u0096\6\3\2\2\2\u0097\u0098\7D\2\2\u0098\u0099\7")
        buf.write("t\2\2\u0099\u009a\7g\2\2\u009a\u009b\7c\2\2\u009b\u009c")
        buf.write("\7m\2\2\u009c\b\3\2\2\2\u009d\u009e\7E\2\2\u009e\u009f")
        buf.write("\7q\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2")
        buf.write("\7k\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\n\3\2\2\2\u00a6\u00a7\7F\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\f\3\2\2\2\u00a9\u00aa\7G\2\2\u00aa\u00ab")
        buf.write("\7n\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7g\2\2\u00ad\16")
        buf.write("\3\2\2\2\u00ae\u00af\7G\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1")
        buf.write("\7u\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7K\2\2\u00b3\u00b4")
        buf.write("\7h\2\2\u00b4\20\3\2\2\2\u00b5\u00b6\7G\2\2\u00b6\u00b7")
        buf.write("\7p\2\2\u00b7\u00b8\7f\2\2\u00b8\u00b9\7D\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\u00bb\7f\2\2\u00bb\u00bc\7{\2\2\u00bc\22")
        buf.write("\3\2\2\2\u00bd\u00be\7G\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write("\7f\2\2\u00c0\u00c1\7K\2\2\u00c1\u00c2\7h\2\2\u00c2\24")
        buf.write("\3\2\2\2\u00c3\u00c4\7G\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6")
        buf.write("\7f\2\2\u00c6\u00c7\7H\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\26\3\2\2\2\u00ca\u00cb\7G\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce\7Y\2\2\u00ce\u00cf")
        buf.write("\7j\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2")
        buf.write("\7g\2\2\u00d2\30\3\2\2\2\u00d3\u00d4\7H\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7t\2\2\u00d6\32\3\2\2\2\u00d7\u00d8")
        buf.write("\7H\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da\7p\2\2\u00da\u00db")
        buf.write("\7e\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7p\2\2\u00df\34\3\2\2\2\u00e0\u00e1")
        buf.write("\7K\2\2\u00e1\u00e2\7h\2\2\u00e2\36\3\2\2\2\u00e3\u00e4")
        buf.write("\7R\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7")
        buf.write("\7c\2\2\u00e7\u00e8\7o\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7t\2\2\u00ec \3")
        buf.write("\2\2\2\u00ed\u00ee\7T\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0")
        buf.write("\7v\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\"\3\2\2\2\u00f4\u00f5\7V\2\2\u00f5\u00f6")
        buf.write("\7j\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7p\2\2\u00f8$\3")
        buf.write("\2\2\2\u00f9\u00fa\7X\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc&\3\2\2\2\u00fd\u00fe\7Y\2\2\u00fe\u00ff")
        buf.write("\7j\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7n\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102(\3\2\2\2\u0103\u0104\7G\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7f\2\2\u0106\u0107\7F\2\2\u0107\u0108")
        buf.write("\7q\2\2\u0108*\3\2\2\2\u0109\u010a\7?\2\2\u010a,\3\2\2")
        buf.write("\2\u010b\u010c\7-\2\2\u010c.\3\2\2\2\u010d\u010e\7/\2")
        buf.write("\2\u010e\60\3\2\2\2\u010f\u0110\7,\2\2\u0110\62\3\2\2")
        buf.write("\2\u0111\u0112\7^\2\2\u0112\64\3\2\2\2\u0113\u0114\7\'")
        buf.write("\2\2\u0114\66\3\2\2\2\u0115\u0116\7-\2\2\u0116\u0117\7")
        buf.write("\60\2\2\u01178\3\2\2\2\u0118\u0119\7/\2\2\u0119\u011a")
        buf.write("\7\60\2\2\u011a:\3\2\2\2\u011b\u011c\7,\2\2\u011c\u011d")
        buf.write("\7\60\2\2\u011d<\3\2\2\2\u011e\u011f\7^\2\2\u011f\u0120")
        buf.write("\7\60\2\2\u0120>\3\2\2\2\u0121\u0122\7#\2\2\u0122@\3\2")
        buf.write("\2\2\u0123\u0124\7(\2\2\u0124\u0125\7(\2\2\u0125B\3\2")
        buf.write("\2\2\u0126\u0127\7~\2\2\u0127\u0128\7~\2\2\u0128D\3\2")
        buf.write("\2\2\u0129\u012a\7?\2\2\u012a\u012b\7?\2\2\u012bF\3\2")
        buf.write("\2\2\u012c\u012d\7#\2\2\u012d\u012e\7?\2\2\u012eH\3\2")
        buf.write("\2\2\u012f\u0130\7>\2\2\u0130J\3\2\2\2\u0131\u0132\7@")
        buf.write("\2\2\u0132L\3\2\2\2\u0133\u0134\7>\2\2\u0134\u0135\7?")
        buf.write("\2\2\u0135N\3\2\2\2\u0136\u0137\7@\2\2\u0137\u0138\7?")
        buf.write("\2\2\u0138P\3\2\2\2\u0139\u013a\7?\2\2\u013a\u013b\7\61")
        buf.write("\2\2\u013b\u013c\7?\2\2\u013cR\3\2\2\2\u013d\u013e\7>")
        buf.write("\2\2\u013e\u013f\7\60\2\2\u013fT\3\2\2\2\u0140\u0141\7")
        buf.write("@\2\2\u0141\u0142\7\60\2\2\u0142V\3\2\2\2\u0143\u0144")
        buf.write("\7>\2\2\u0144\u0145\7?\2\2\u0145\u0146\7\60\2\2\u0146")
        buf.write("X\3\2\2\2\u0147\u0148\7@\2\2\u0148\u0149\7?\2\2\u0149")
        buf.write("\u014a\7\60\2\2\u014aZ\3\2\2\2\u014b\u014c\7\60\2\2\u014c")
        buf.write("\\\3\2\2\2\u014d\u014e\7.\2\2\u014e^\3\2\2\2\u014f\u0150")
        buf.write("\7=\2\2\u0150`\3\2\2\2\u0151\u0152\7<\2\2\u0152b\3\2\2")
        buf.write("\2\u0153\u0154\7}\2\2\u0154d\3\2\2\2\u0155\u0156\7\177")
        buf.write("\2\2\u0156f\3\2\2\2\u0157\u0158\7*\2\2\u0158h\3\2\2\2")
        buf.write("\u0159\u015a\7+\2\2\u015aj\3\2\2\2\u015b\u015c\7]\2\2")
        buf.write("\u015cl\3\2\2\2\u015d\u015e\7_\2\2\u015en\3\2\2\2\u015f")
        buf.write("\u017a\7\62\2\2\u0160\u0164\t\4\2\2\u0161\u0163\t\5\2")
        buf.write("\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u017a\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0167\u0168\7\62\2\2\u0168\u0169\t\6\2")
        buf.write("\2\u0169\u016d\t\7\2\2\u016a\u016c\t\b\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u017a\3\2\2\2\u016f\u016d\3\2\2\2")
        buf.write("\u0170\u0171\7\62\2\2\u0171\u0172\t\t\2\2\u0172\u0176")
        buf.write("\t\n\2\2\u0173\u0175\t\13\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u015f\3")
        buf.write("\2\2\2\u0179\u0160\3\2\2\2\u0179\u0167\3\2\2\2\u0179\u0170")
        buf.write("\3\2\2\2\u017ap\3\2\2\2\u017b\u0184\7\62\2\2\u017c\u0180")
        buf.write("\t\4\2\2\u017d\u017f\t\5\2\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u017b\3")
        buf.write("\2\2\2\u0183\u017c\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0189")
        buf.write("\7\60\2\2\u0186\u0188\t\5\2\2\u0187\u0186\3\2\2\2\u0188")
        buf.write("\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2")
        buf.write("\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018e\5")
        buf.write("s:\2\u018d\u018c\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u01a4")
        buf.write("\3\2\2\2\u018f\u0198\7\62\2\2\u0190\u0194\t\4\2\2\u0191")
        buf.write("\u0193\t\5\2\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2")
        buf.write("\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0198\3")
        buf.write("\2\2\2\u0196\u0194\3\2\2\2\u0197\u018f\3\2\2\2\u0197\u0190")
        buf.write("\3\2\2\2\u0198\u019a\3\2\2\2\u0199\u019b\7\60\2\2\u019a")
        buf.write("\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019f\3\2\2\2")
        buf.write("\u019c\u019e\t\5\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3")
        buf.write("\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a4\5s:\2\u01a3\u0183")
        buf.write("\3\2\2\2\u01a3\u0197\3\2\2\2\u01a4r\3\2\2\2\u01a5\u01a7")
        buf.write("\t\f\2\2\u01a6\u01a8\t\r\2\2\u01a7\u01a6\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01ab\t\5\2\2")
        buf.write("\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3")
        buf.write("\2\2\2\u01ac\u01ad\3\2\2\2\u01adt\3\2\2\2\u01ae\u01af")
        buf.write("\7V\2\2\u01af\u01b0\7t\2\2\u01b0\u01b1\7w\2\2\u01b1\u01b8")
        buf.write("\7g\2\2\u01b2\u01b3\7H\2\2\u01b3\u01b4\7c\2\2\u01b4\u01b5")
        buf.write("\7n\2\2\u01b5\u01b6\7u\2\2\u01b6\u01b8\7g\2\2\u01b7\u01ae")
        buf.write("\3\2\2\2\u01b7\u01b2\3\2\2\2\u01b8v\3\2\2\2\u01b9\u01c0")
        buf.write("\7$\2\2\u01ba\u01bf\5y=\2\u01bb\u01bf\n\16\2\2\u01bc\u01bd")
        buf.write("\7)\2\2\u01bd\u01bf\7$\2\2\u01be\u01ba\3\2\2\2\u01be\u01bb")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c3\3\2\2\2")
        buf.write("\u01c2\u01c0\3\2\2\2\u01c3\u01c4\7$\2\2\u01c4x\3\2\2\2")
        buf.write("\u01c5\u01c6\7^\2\2\u01c6\u01c7\t\17\2\2\u01c7z\3\2\2")
        buf.write("\2\u01c8\u01ca\7}\2\2\u01c9\u01cb\5\u0081A\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01dc\3\2\2\2\u01cc")
        buf.write("\u01d7\5}?\2\u01cd\u01cf\5\u0081A\2\u01ce\u01cd\3\2\2")
        buf.write("\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2")
        buf.write("\7.\2\2\u01d1\u01d3\5\u0081A\2\u01d2\u01d1\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d6\5}?\2\u01d5")
        buf.write("\u01ce\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3")
        buf.write("\2\2\2\u01da\u01cc\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01df\u01e1\5\u0081A\2\u01e0\u01df\3\2")
        buf.write("\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3")
        buf.write("\7\177\2\2\u01e3|\3\2\2\2\u01e4\u01ea\5o8\2\u01e5\u01ea")
        buf.write("\5q9\2\u01e6\u01ea\5u;\2\u01e7\u01ea\5w<\2\u01e8\u01ea")
        buf.write("\5{>\2\u01e9\u01e4\3\2\2\2\u01e9\u01e5\3\2\2\2\u01e9\u01e6")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01ea")
        buf.write("~\3\2\2\2\u01eb\u01ec\7,\2\2\u01ec\u01ed\7,\2\2\u01ed")
        buf.write("\u01f1\3\2\2\2\u01ee\u01f0\13\2\2\2\u01ef\u01ee\3\2\2")
        buf.write("\2\u01f0\u01f3\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f1\u01ef")
        buf.write("\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4")
        buf.write("\u01f5\7,\2\2\u01f5\u01f6\7,\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f8\b@\2\2\u01f8\u0080\3\2\2\2\u01f9\u01fb\t\20\2\2")
        buf.write("\u01fa\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fa\3")
        buf.write("\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff")
        buf.write("\bA\2\2\u01ff\u0082\3\2\2\2\u0200\u0206\7$\2\2\u0201\u0205")
        buf.write("\n\16\2\2\u0202\u0203\7)\2\2\u0203\u0205\7$\2\2\u0204")
        buf.write("\u0201\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0208\3\2\2\2")
        buf.write("\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u020d\3")
        buf.write("\2\2\2\u0208\u0206\3\2\2\2\u0209\u020a\7^\2\2\u020a\u020e")
        buf.write("\n\17\2\2\u020b\u020c\7)\2\2\u020c\u020e\n\21\2\2\u020d")
        buf.write("\u0209\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u0084\3\2\2\2")
        buf.write("\u020f\u0215\7$\2\2\u0210\u0214\n\21\2\2\u0211\u0212\7")
        buf.write(")\2\2\u0212\u0214\7$\2\2\u0213\u0210\3\2\2\2\u0213\u0211")
        buf.write("\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0218\u021a\t\22\2\2\u0219\u0218\3\2\2\2\u021a\u0086")
        buf.write("\3\2\2\2\u021b\u021c\7,\2\2\u021c\u021d\7,\2\2\u021d\u0221")
        buf.write("\3\2\2\2\u021e\u0220\n\23\2\2\u021f\u021e\3\2\2\2\u0220")
        buf.write("\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2")
        buf.write("\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2\u0224\u0226\7")
        buf.write(",\2\2\u0225\u0224\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227")
        buf.write("\3\2\2\2\u0227\u0228\7\2\2\3\u0228\u0088\3\2\2\2\u0229")
        buf.write("\u022a\13\2\2\2\u022a\u008a\3\2\2\2\'\2\u008f\u0164\u016d")
        buf.write("\u0176\u0179\u0180\u0183\u0189\u018d\u0194\u0197\u019a")
        buf.write("\u019f\u01a3\u01a7\u01ac\u01b7\u01be\u01c0\u01ca\u01ce")
        buf.write("\u01d2\u01d7\u01dc\u01e0\u01e9\u01f1\u01fc\u0204\u0206")
        buf.write("\u020d\u0213\u0215\u0219\u0221\u0225\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    BODY = 2
    BREAK = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    ELSE_IF = 7
    END_BODY = 8
    END_IF = 9
    END_FOR = 10
    END_WHILE = 11
    FOR = 12
    FUNCTION = 13
    IF = 14
    PARAM = 15
    RETURN = 16
    THEN = 17
    VAR = 18
    WHILE = 19
    END_DO = 20
    ASSIGN = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    ADDF = 27
    SUBF = 28
    MULF = 29
    DIVF = 30
    NOT = 31
    AND = 32
    OR = 33
    EQ = 34
    NEQ = 35
    LT = 36
    GT = 37
    LTE = 38
    GTE = 39
    NEQF = 40
    LTF = 41
    GTF = 42
    LTEF = 43
    GTEF = 44
    DOT = 45
    COMMA = 46
    SEMI = 47
    COLON = 48
    LB = 49
    RB = 50
    LP = 51
    RP = 52
    LS = 53
    RS = 54
    INT_LIT = 55
    FLOAT_LIT = 56
    BOOL_LIT = 57
    STRING_LIT = 58
    ARRAY_LIT = 59
    ARRAY_ELEM = 60
    COMMENT = 61
    WS = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64
    UNTERMINATED_COMMENT = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'EndDo'", "'='", "'+'", "'-'", "'*'", "'\\'", "'%'", "'+.'", 
            "'-.'", "'*.'", "'\\.'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", 
            "'>=.'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'('", "')'", 
            "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSE_IF", 
            "END_BODY", "END_IF", "END_FOR", "END_WHILE", "FOR", "FUNCTION", 
            "IF", "PARAM", "RETURN", "THEN", "VAR", "WHILE", "END_DO", "ASSIGN", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "ADDF", "SUBF", "MULF", "DIVF", 
            "NOT", "AND", "OR", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "NEQF", 
            "LTF", "GTF", "LTEF", "GTEF", "DOT", "COMMA", "SEMI", "COLON", 
            "LB", "RB", "LP", "RP", "LS", "RS", "INT_LIT", "FLOAT_LIT", 
            "BOOL_LIT", "STRING_LIT", "ARRAY_LIT", "ARRAY_ELEM", "COMMENT", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSE_IF", 
                  "END_BODY", "END_IF", "END_FOR", "END_WHILE", "FOR", "FUNCTION", 
                  "IF", "PARAM", "RETURN", "THEN", "VAR", "WHILE", "END_DO", 
                  "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "ADDF", "SUBF", 
                  "MULF", "DIVF", "NOT", "AND", "OR", "EQ", "NEQ", "LT", 
                  "GT", "LTE", "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", 
                  "DOT", "COMMA", "SEMI", "COLON", "LB", "RB", "LP", "RP", 
                  "LS", "RS", "INT_LIT", "FLOAT_LIT", "EXPONENT", "BOOL_LIT", 
                  "STRING_LIT", "ESC", "ARRAY_LIT", "ARRAY_ELEM", "COMMENT", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()

        if tk == self.STRING_LIT:
            result.text = result.text[1:][:-1]

        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


