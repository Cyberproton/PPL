import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_comment(self):
        input = "**This is an inline comment**"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 108))

        input = """**This is an 
                    * multiline 
                    * comment**"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 109))

        input = """** Unterminated Comment!"""
        expect = "Unterminated Comment"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 110))

        input = """****** Unterminated Comment!*"""
        expect = "Unterminated Comment"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 111))

        input = """****Var*"""
        expect = "Var,*,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 112))

        input = """*******"""
        expect = "Unterminated Comment"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 113))

        input = """1abc2 23**This is an 
                    multiline comment with tokens: Body 123 0x123** Function"""
        expect = "1,abc2,23,Function,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 114))
        

    def test_identifier(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

        input = "aBCd AbcD"
        expect = "aBCd,Error Token A"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

        input = "00aB123c    1a2dC_A _87mn"
        expect = "0,0,aB123c,1,a2dC_A,Error Token _"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

        input = "a_b__c______D___1ABC1_00@12345"
        expect = "a_b__c______D___1ABC1_00,Error Token @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

        input = "aB1c** _*_1a_**abc"
        expect = "aB1c,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test_keyword(self):
        input = "For Then"
        expect = "For,Then,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

        input = "IfThenabcElse"
        expect = "If,Then,abcElse,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

        input = "IfThenabc 123Else_If"
        expect = "If,Then,abc,123,Else,Error Token _"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

        input = "If Var a then"
        expect = "If,Var,a,then,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

        input = "THEN no then"
        expect = "Error Token T"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

        input = """ "This is a Function inside a String" Function ** This is a Function inside a comment** """
        expect = "This is a Function inside a String,Function,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

        input = """ "A stuck Bo"dy and another Bo"dy """
        expect = "A stuck Bo,dy,and,another,Error Token B"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

        input = """ **EndFor the** End If """
        expect = "Error Token E"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

        input = """ EndBodyEndIf**End**For """
        expect = "EndBody,EndIf,For,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))

        input = """ EndWhiLEFOR """
        expect = "Error Token E"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test_operator(self):
        input = """ + - * \ """
        expect = "+,-,*,\,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

        input = """ <==>====== """
        expect = "<=,=,>=,==,==,=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))

        input = """ Vara==2\.0 """
        expect = "Var,a,==,2,\.,0,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))

        input = """ * * = ** """
        expect = "*,*,=,Unterminated Comment"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

        input = """ a += b """
        expect = "a,+,=,b,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))

        input = """ "If+ Then" && ElseIf | | Else """
        expect = "If+ Then,&&,ElseIf,Error Token |"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))

        input = """ a4b5+-5 abcd \%._ """
        expect = "a4b5,+,-,5,abcd,\%,.,Error Token _"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

        input = """ !.!!2a&&b>=. """
        expect = "!,.,!,!,2,a,&&,b,>=.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

        input = """ \\\%/\ """
        expect = "\\\,Error Token %" 
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

        input = """ &**&&**& """
        expect = "Error Token &"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_separator(self):
        pass

    def test_literal(self):
        input = "{1, 2, 3}"
        expect = "{1, 2, 3},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

        input = "{{3, 4}, 1, 2, {}}"
        expect = "{{3, 4}, 1, 2, {}},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

