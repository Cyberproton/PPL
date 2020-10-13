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

        input = """**"""
        expect = "Unterminated Comment"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 115))

        input = """* * * *"""
        expect = "*,*,*,*,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 116))
        

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

        input = """ EndThen is not a keyword """
        expect = "Error Token E"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))


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

        input = """ a4b5+-5 abcd %._ """
        expect = "a4b5,+,-,5,abcd,%,.,Error Token _"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

        input = """ !.!!2a&&b>=. """
        expect = "!,.,!,!,2,a,&&,b,>=.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

        input = """ %/\ """
        expect = "%,Error Token /" 
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

        input = """ &**&&**& """
        expect = "Error Token &"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))


    def test_separator(self):
        input = """ { . } """
        expect = "{,.,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

        input = """abcA12[a4;7g"""
        expect = "abcA12,[,a4,;,7,g,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

        input = """ a1__)___ """
        expect = "a1__,),Error Token _"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

        input = """ a[2][3][a-1] """
        expect = "a,[,2,],[,3,],[,a,-,1,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

        input = """ fun(a*8,  12 + 3);   (  Function)* """
        expect = "fun,(,a,*,8,,,12,+,3,),;,(,Function,),*,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

        input = """ {**{{{}}}**} """
        expect = "{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

        input = """ Then,abc+If-Else*endIf """
        expect = "Then,,,abc,+,If,-,Else,*,endIf,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

        input = """ [[1-2] \% 3] + 4 """
        expect = "[,[,1,-,2,],\,%,3,],+,4,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))


    def test_integer_literal(self):
        input = "23 345 0"
        expect = "23,345,0,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

        input = "000001203"
        expect = "0,0,0,0,0,1203,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

        input = "0X0 123"
        expect = "0,Error Token X"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

        input = "00x0123"
        expect = "0,0,x0123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

        input = "0xFFFF 0O4567 0O9999"
        expect = "0xFFFF,0O4567,0,Error Token O"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

        input = "2+0o1238=2XG "
        expect = "2,+,0o123,8,=,2,Error Token X"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

        input = "arr[0x1][01230][2o77] = 0O777"
        expect = "arr,[,0x1,],[,0,1230,],[,2,o77,],=,0O777,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

        input = "0x(1234) 0o7[77777]; 0X[FABC]"
        expect = "0,x,(,1234,),0o7,[,77777,],;,0,Error Token X"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

        input = "456789(0x1230O123)"
        expect = "456789,(,0x1230,Error Token O"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

        input = "Function0xABCDo"
        expect = "Function,0xABCD,o,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))


    def test_float_literal(self):
        input = "0.0"
        expect = "0.0,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

        input = "0. 0E0"
        expect = "0.,0E0,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

        input = "00120.0e-1"
        expect = "0,0,120.0e-1,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

        input = "53.234e-240.55"
        expect = "53.234e-240,.,55,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

        input = "0x123.0e123FFF"
        expect = "0x123,.,0e123,Error Token F"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

        input = "123e+5 e+ 5 123.E+999xFF"
        expect = "123e+5,e,+,5,123.E+999,xFF,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

        input = "0xF*0.e23E+123"
        expect = "0xF,*,0.e23,Error Token E"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

        input = "abc0.456e-123"
        expect = "abc0,.,456e-123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

        input = "Var 45... = 0x0.3"
        expect = "Var,45.,.,.,=,0,x0,.,3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

        input = "0(.e-2).E-2"
        expect = "0,(,.,e,-,2,),.,Error Token E"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))


    def test_boolean_literal(self):
        input = "TrueFalse"
        expect = "True,False,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

        input = "Truefalse FalseTRUE"
        expect = "True,false,False,Error Token T"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

        input = "While (False) Do For 1+xTruex-False+falseFalse;"
        expect = "While,(,False,),Do,For,1,+,xTruex,-,False,+,falseFalse,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

        input = """ **No True Here** "Only" True "HERE" """
        expect = """Only,True,HERE,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

        input = """a FalsetrueFalseTrue"""
        expect = "a,False,trueFalseTrue,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

        input = """ "This is not a real True" """
        expect = """This is not a real True,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))


    def test_string_literal(self):
        input = """ "Simple string of 123" """
        expect = "Simple string of 123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

        input = """ "" "Abc123""1.0e3""a+3,4" """
        expect = ",Abc123,1.0e3,a+3,4,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

        input = """ F"x1a2 True"unction """
        expect = "Error Token F"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

        input = """ "afdfdsbbv\\b\\n" """
        expect = "afdfdsbbv\\b\\n,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

        input = """ "afdfdsbbv\\v\\n" """
        expect = "Illegal Escape In String: afdfdsbbv\\v"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

        input = """ "asfdfdfsfdf 123+4"""
        expect = "Unclosed String: asfdfdfsfdf 123+4"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

        input = """ " "String inside a string" " """
        expect = " ,Error Token S"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

        input = """ "String and **a comment**" """
        expect = "String and **a comment**,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

        input = """"String and **a comment**"""
        expect = "Unclosed String: String and **a comment**"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

        input = """ "He asked me: '"Where is John?'"" """
        expect = "He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))

        input = """ "He asked me: \\'"Where is John?'"" """
        expect = "He asked me: \\',Error Token W"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))

        input = """ "He asked me: '\"Where' is'''\" John?'\"" """
        expect = """Illegal Escape In String: He asked me: '"Where' """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 201))

        input = """ "This is a string with a '" """
        expect = """Unclosed String: This is a string with a '" """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 202))

        input = """ "This is a string with a '" "And this is another string" """
        expect = """This is a string with a '" ,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 203))

        input = """ **"A commented string, this string is ignored"** """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 204))

        input = """ "**Comment inside a string**" """
        expect = "**Comment inside a string**,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect , 205))

    def test_array_literal(self):
        input = """ {1, 2,3 } """
        expect = "{1, 2,3 },<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 210))

        input = """ {1, "3a*",{} } """
        expect = """{1, "3a*",{} },<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 211))

        input = """ {{1, "abc", {}}, {1 , 2},{ 2.0e-1, "abcd\\n" }} """
        expect = """{{1, "abc", {}}, {1 , 2},{ 2.0e-1, "abcd\\n" }},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 212))

        input = """ {{1, "abc", {}} {1 , 2}} """
        expect = """{,{1, "abc", {}},{1 , 2},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 213))

        input = """ {{1, "abc", {}} {1 , 2, Function}} """
        expect = """{,{1, "abc", {}},{,1,,,2,,,Function,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 214))

        input = """ {{1, "abc", {}}, { 0x123 , 2e0, True}}, { "123", "abc" , 123 } """
        expect = """{{1, "abc", {}}, { 0x123 , 2e0, True}},,,{ "123", "abc" , 123 },<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 215))

        input = """ "{ 1, 2, 3} {sdffs, dsfd, asdd}" """
        expect = "{ 1, 2, 3} {sdffs, dsfd, asdd},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 216))

        input = """ {{{}, {}}, {}, {{}, {}, {{}}}} """
        expect = "{{{}, {}}, {}, {{}, {}, {{}}}},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 217))

        input = """ { { ** THIS IS A COMMENT **, 2 } } """
        expect = "{,{,,,2,},},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 218))

        input = """ { { , "",  } } {}"""
        expect = "{,{,,,,,,},},{},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 219))









