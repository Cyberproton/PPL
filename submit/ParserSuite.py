import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_simple_program_structure(self):
        input = "Function: main Body: EndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

        input = "Function: main \nBody:\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

        input = "Var: x; Function: main Body: EndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 303))

        input = """Var: x; Function: not_a_main_function Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 304))

        input = """Var: x; 
        Function: f1
            Body:
            EndBody.

        Function: main 
            Body: 
            EndBody.

        Function: f2
            Body:
            EndBody.

        Function: f3
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 305))

        input = "**Function: main Body: EndBody.**"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 306))

        input = """
            Var: a, b, c;

            Function: f1
                Body:
                EndBody.

            Function: main
                Body:
                EndBody.

            Function: f2
                Body:
                EndBody.

            Var: a, b, c;
            Var: d, e, f;
        """
        expect = "Error on line 16 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 307))

        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 308))

        input = """
            Var: a, b, c;

            Var: f1
                Body:
                EndBody.

            Function: main
                Body:
                EndBody.

            Function: f2
                Body:
                EndBody.
        """
        expect = "Error on line 5 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 309))


    def test_global_variable_declaration(self):
        input = """
            Var: a, b = 3.5, c = {1, "abc", 0xFFFF};

            Function: main
                Body:
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 320))
        
        input = """Var a, b = 3.5, c = {1, "abc", 0xFFFF};

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 1 col 4: a"
        self.assertTrue(TestParser.checkParser(input, expect, 321))

        input = """Var: a, b = 3.5, c = {1, "abc", 0xFFFF}

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 3 col 12: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 322))

        input = """Var: a, b = 3.5; c = {1, "abc", 0xFFFF};

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 1 col 17: c"
        self.assertTrue(TestParser.checkParser(input, expect, 323))

        input = """
            Var: a, b = 3.5, c = {1, "abc", 0xFFFF};
            Var:a=2.e+3,b,c=0O1234567,d[10],e,f;
            Var:   a[2][3] = 2;

            Function: main
                Body:
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 324))

        input = """
            Var: a, 
            b = "3.5"
            , c = {{}, "abc", 0xFFFF};

            Function: main
                Body:
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 325))

        input = """
            Var: Var: a, b, c;

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 17: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 326))

        input = """
            Var: a, b, c, Var: d, e, f;

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 26: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 327))

        input = """
            Function: a = 2.0, b[2], c = {{}};

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 24: ="
        self.assertTrue(TestParser.checkParser(input, expect, 328))

        input = """
            Var: a[2][] = 2.0, b[2], c = {};

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 22: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 329))

        input = """
            Var: 2.0, b[2], 0xF;

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 17: 2.0"
        self.assertTrue(TestParser.checkParser(input, expect, 330))

        input = """
            Var: ;

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 331))

        input = """
            Var: **a = 9.0, b[2] = {}**;

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 39: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 332))

        input = """
            Var: a = 9.0 + 2.0, b[2] = {};

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 25: +"
        self.assertTrue(TestParser.checkParser(input, expect, 333))

        input = """
            Var: a = -9.0, b[2] = {};

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 21: -"
        self.assertTrue(TestParser.checkParser(input, expect, 334))

        input = """
            Function: main
                Body:
                EndBody.

            Var: a = -9.0, b[2] = {};
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 335))

        input = """
            Var: a = 9.0, b[2] = { 1, main() };

            Function: main
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 33: {"
        self.assertTrue(TestParser.checkParser(input, expect, 336))


    def test_function_declaration(self):
        input = """
            Function: f
                Parameter: a, b[2][3]
                Body:
                EndBody.
            Function: main
                Body:
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 340))

        input = """
            Function: main
                Parameter: 
                Body:
                EndBody.
        """
        expect = "Error on line 4 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 341))

        input = """
            Function: main
                Body:
                EndBody.
                Parameter: a
        """
        expect = "Error on line 5 col 16: Parameter"
        self.assertTrue(TestParser.checkParser(input, expect, 342))

        input = """
            Function: main
                Parameter: a, b = 2
                Body:
                EndBody.
        """
        expect = "Error on line 3 col 32: ="
        self.assertTrue(TestParser.checkParser(input, expect, 343))

        input = """
            Function: main
                Parameter: a, b, c;
                Body:
                EndBody.
        """
        expect = "Error on line 3 col 34: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 344))

        input = """
            Function: main
                Parameter: a, b[2], c
                Body:
                    f();
                EndBody.

            Function: f
                Body:
                    f();
                    x = 10;
                    y = a + 10;
                    g();
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 345))

        input = """
            Function: main
                Parameter: a, b[2], c
                Body:
                    f();
                EndBody.

            Function: f
                f();
                x = 10;
                y = a + 10;
                g();
        """
        expect = "Error on line 9 col 16: f"
        self.assertTrue(TestParser.checkParser(input, expect, 346))

        input = """
            Function: main
                Parameter: a, b[2], c
                Body:
                EndBody.
                Body:
                    f();
                EndBody.

            Function: f
                f();
                x = 10;
                y = a + 10;
                g();
        """
        expect = "Error on line 6 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 347))

        input = """
            Function: main
                Parameter: a, b[2], c
                Body:
                    f();
                    Function: f
                        Body:
                        EndBody.
                EndBody.
        """
        expect = "Error on line 6 col 20: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 348))

        input = """
            Function: main
                Parameter: a, b[2], c
                Body:
                EndBody.Function: f
                        Body:
                        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 349))

        input = """
            Var: x = 2;
            x = x + 3;

            Function: main
                Parameter: a, b[2], c
                Body:
                EndBody.Function: f
                        Body:
                        EndBody.
        """
        expect = "Error on line 3 col 12: x"
        self.assertTrue(TestParser.checkParser(input, expect, 350))

        input = """
            Var: x = "";

            Function: "f"
                Body:
                EndBody.

            Function: main
                Parameter: a, b[2], c
                Body:
                EndBody.
        """
        expect = "Error on line 4 col 22: f"
        self.assertTrue(TestParser.checkParser(input, expect, 351))

        input = """
            Var: x = "";

            Body:
                Var: x = 2.;
            EndBody.

            Function: main
                Parameter: a, b[2], c
                Body:
                EndBody.
        """
        expect = "Error on line 4 col 12: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 352))

        input = """
            Var: x = "";
            Function: main
                Parameter: a, b[2], c
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 353))

        input = """
            Var: x = "";

            Function: Function
                Parameter: a, b[2], c
                Body:
                EndBody.
        """
        expect = "Error on line 4 col 22: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 354))


    def test_expression(self):
        input = """
            Function: main
                Body:
                    exp = a + 2 - c * d \\ e;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 360))

        input = """
            Function: main
                Body:
                    exp = ((a + 2) - c) * (d \\ e);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 361))

        input = """
            Function: main
                Body:
                    exp = a || True * foo(2) *. e[2][3];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 362))

        input = """
            Function: main
                Body:
                    exp = arr[2][foo(foo(2), 2 + 3)][array[3][4]] + 2.;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 363))

        input = """
            Function: main
                Body:
                    exp = (2 + 3)[4][0];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 364))

        input = """
            Function: main
                Body:
                    exp = + 3 - 2;
                EndBody.
        """
        expect = "Error on line 4 col 26: +"
        self.assertTrue(TestParser.checkParser(input, expect, 365))

        input = """
            Function: main
                Body:
                    exp = - 3 - foo();
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 366))

        input = """
            Function: main
                Body:
                    exp = 2. \ - 3 - foo();
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 367))

        input = """
            Function: main
                Body:
                    exp = ! - 5 + -. 3 <=. 2.0;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 368))

        input = """
            Function: main
                Body:
                    exp = (3 <=. 2.0)[0];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 369))

        input = """
            Function: main
                Body:
                    exp = True && (a) !(2 - 3);
                EndBody.
        """
        expect = "Error on line 4 col 38: !"
        self.assertTrue(TestParser.checkParser(input, expect, 370))

        input = """
            Function: main
                Body:
                    exp = e() f + && (a) !(2 - 3);
                EndBody.
        """
        expect = "Error on line 4 col 30: f"
        self.assertTrue(TestParser.checkParser(input, expect, 371))

        input = """
            Function: main
                Body:
                    exp = exp()[2][3 - exp()] =/= True;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 372))

        input = """
            Function: main
                Body:
                    exp = exp()[][] =/= True;
                EndBody.
        """
        expect = "Error on line 4 col 32: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 373))

        input = """
            Function: main
                Body:
                    exp = exp()["integer"][2] =/= True;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 374))

        input = """
            Function: main
                Body:
                    exp = (exp >) 3 + "string";
                EndBody.
        """
        expect = "Error on line 4 col 32: )"
        self.assertTrue(TestParser.checkParser(input, expect, 375))

        input = """
            Function: main
                Body:
                    exp = exp()[3][2]() =/= True;
                EndBody.
        """
        expect = "Error on line 4 col 37: ("
        self.assertTrue(TestParser.checkParser(input, expect, 376))

        input = """
            Function: main
                Body:
                    exp = (exp()[3][2] =/= True);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 377))

        input = """
            Function: main
                Body:
                    exp = a ! b *. abc =/= xyz;
                EndBody.
        """
        expect = "Error on line 4 col 28: !"
        self.assertTrue(TestParser.checkParser(input, expect, 378))

        input = """
            Function: main
                Body:
                    exp = a || *. abc =/= xyz;
                EndBody.
        """
        expect = "Error on line 4 col 31: *."
        self.assertTrue(TestParser.checkParser(input, expect, 379))


    def test_statement(self):
        input = """
            Function: main
                Body:
                    Var: x = 0o765, y[2][3] = {1, 2, {0}};
                    Var: z = "A Simple String";
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 380))

        input = """
            Function: main
                Body:
                    x = "" + 2 - 3. * (a[1][0] == a[2]);
                    y = - (x) + x(1, x(1, 2)); 
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 381))

        input = """
            Function: main
                Body:
                    x = "" + 2 - 3. * (a[1][0] == a[2]);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 382))

        input = """
            Function: main
                Body:
                    If x - 3 == 0 Then x = x + x(); EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 383))

        input = """
            Function: main
                Body:
                    If x - 3 == 0 Then 
                        x = x + x(); 
                    ElseIf x() + a[2][3] Then
                        Var: x = "";
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 384))

        input = """
            Function: main
                Body:
                    If x - 3 == 0 Then 
                        x = x + x(); 
                    ElseIf x() + a[2][3] Then
                        Var: x = "";
                    ElseIf !(2) Then
                        x = x == x;
                    Else
                        Var: x, x = {};
                        Var: x = "asfdgsgdsg";
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 385))

        input = """
            Function: main
                Body:
                    For (x = 3 * x(), x < 3, -1) Do

                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 386))

        input = """
            Function: main
                Body:
                    For ( x = 3 * x(), x < 3, -1 ) Do
                        Var: x = 1, y = 5e+3;

                        writeln(x);
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 387))

        input = """
            Function: main
                Body:
                    While x(1, x[2]) Do 
                        calc();
                        x = x * x \. x;
                    EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 388))

        input = """
            Function: main
                Body:
                    Do 
                        Var: x;
                        Var: x;
                        Var: x;
                        x = x == x == x;
                    While x == x EndDo.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 389))

        input = """
            Function: main
                Body:
                    Break;
                    Continue;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 390))

        input = """
            Function: main
                Body:
                    foo(2 + x, 4. \. y);
                    bar();
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 391))

        input = """
            Function: main
                Body:
                    Return x + 3;
                    Return foo(2 + x, 4. \. y);
                    Return;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 392))

        input = """
            Function: main
                Body:
                    Var: x = 1.;
                    x = x + x;
                    Var: y = {};
                    y();
                EndBody.
        """
        expect = "Error on line 6 col 20: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 393))

        input = """
            Function: main
                Body:
                    If x = x - 3 Then 
                        x = x + x(); 
                    EndIf.
                EndBody.
        """
        expect = "Error on line 4 col 25: ="
        self.assertTrue(TestParser.checkParser(input, expect, 394))

        input = """
            Function: main
                Body:
                    If x - 3 Then 
                        x = x + x(); 
                    Else x + 3
                        x();
                    EndIf.
                EndBody.
        """
        expect = "Error on line 6 col 27: +"
        self.assertTrue(TestParser.checkParser(input, expect, 395))

        input = """
            Function: main
                Body:
                    If x - 3 Then 
                        x = x + x(); 
                    ElseIf x Then

                    Else
                        x();
                    ElseIf x + 3 Then
                        Var x = "";
                    EndIf.
                EndBody.
        """
        expect = "Error on line 10 col 20: ElseIf"
        self.assertTrue(TestParser.checkParser(input, expect, 396))

        input = """
            Function: main
                Body:
                    If x - 3 Then 
                        x = x + x();
                    Else
                        x();
                    Else
                        Var x = "";
                    EndIf.
                EndBody.
        """
        expect = "Error on line 8 col 20: Else"
        self.assertTrue(TestParser.checkParser(input, expect, 397))

        input = """
            Function: main
                Body:
                    If x - 3 Then 
                        x = x + x();
                    ElseIf x == 3 Then
                        If y * 9 Then
                        ElseIf y =/= 2. Then
                        Else
                        EndIf.
                        x();
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 398))

        input = """
            Function: main
                Body:
                    If x - 3 Then 
                        If x && x Then
                    ElseIf x == 3 Then
                        If y * 9 Then
                        ElseIf y =/= 2. Then
                        Else
                        EndIf.
                        x();
                    EndIf.
                EndBody.
        """
        expect = "Error on line 13 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 399))

        input = """
            Function: main
                Body:
                    If x - 3 Then 
                        If x && x Then
                    EndIf.
                    ElseIf x == 3 Then
                        If y * 9 Then
                        ElseIf y =/= 2. Then
                        Else
                        EndIf.
                        x();
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 400))

        input = """
            Function: main
                Body:
                    For ( x + 3, x == 9, a + 3) Do
                    EndFor.
                EndBody.
        """
        expect = "Error on line 4 col 28: +"
        self.assertTrue(TestParser.checkParser(input, expect, 401))

        input = """
            Function: main
                Body:
                    For (x = x + 3, x = 9, a + 3) Do
                    EndFor.
                EndBody.
        """
        expect = "Error on line 4 col 38: ="
        self.assertTrue(TestParser.checkParser(input, expect, 402))

        input = """
            Function: main
                Body:
                    For (x = x + 3, x + 9, a(x()[0])) Do
                        writeln(x);
                        writeln(i);
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 403))

        input = """
            Function: main
                Body:
                    For (x = x + 3, x + 9, a(x()[0])) 
                        Do
                            writeln(x);
                            writeln(i);
                        While x == True EndDo.
                    EndFor.
                EndBody.
        """
        expect = "Error on line 8 col 24: While"
        self.assertTrue(TestParser.checkParser(input, expect, 404))

        input = """
            Function: main
                Body:
                    Do
                        writeln(x);
                        writeln(i);
                    While x == True Do
                        Var: x = 3;
                    EndWhile.
                    EndDo.
                EndBody.
        """
        expect = "Error on line 10 col 20: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 405))

        input = """
            Function: main
                Body:
                    While False 
                    Do
                        Var: x = 3;
                        While True EndDo.
                    EndWhile.
                EndBody.
        """
        expect = "Error on line 7 col 24: While"
        self.assertTrue(TestParser.checkParser(input, expect, 406))

        input = """
            Function: main
                Body:
                    Var: x[2] = 9e1;
                    Var: x[0] = 0x1;
                    While False 
                    Do
                        Var: x = 3;
                        Return x(a[2], 0);
                    EndWhile.
                    Var: y = 2.;
                EndBody.
        """
        expect = "Error on line 11 col 20: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 407))

        input = """
            Function: main
                Body:
                    Var: x[2] = 9e1;
                    Var: x[0] = 0x1;
                    Break loop();
                EndBody.
        """
        expect = "Error on line 6 col 26: loop"
        self.assertTrue(TestParser.checkParser(input, expect, 408))

        input = """
            Function: main
                Body:
                    Var: x = 2.;
                    x = f(); ;
                EndBody.
        """
        expect = "Error on line 5 col 29: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 409))

        input = """
            Function: main
                Body:
                    For (x = 0, x, x) Do EndDo.
                EndBody.
        """
        expect = "Error on line 4 col 41: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 410))

        input = """
            Function: main
                Body:
                    For (x = 0, x, x) Do 
                        return a();
                    EndFor.
                EndBody.
        """
        expect = "Error on line 5 col 31: a"
        self.assertTrue(TestParser.checkParser(input, expect, 411))

        input = """
            Function: main
                Body:
                    For (x = 0, x, x) Do 
                        Return Continue;
                    EndFor.
                EndBody.
        """
        expect = "Error on line 5 col 31: Continue"
        self.assertTrue(TestParser.checkParser(input, expect, 412))

        input = """
            Function: main
                Body:
                    If True Then 
                        foo(1, foo(), foo);
                        foo(1, 3, 2)[2];
                    EndIf.
                EndBody.
        """
        expect = "Error on line 6 col 36: ["
        self.assertTrue(TestParser.checkParser(input, expect, 413))
        

    def test_compound(self):
        input = """
            Var: x[3][1] = {{}, {{}}}, y = "String", z = 99999999.e-1;

            ** 
             * A very complex program structure
            **
            Function: main
                Parameter: p1, p2
                Body:
                    Var: x[2] = 9e1, x = "";
                    Var: x[0] = 0x1;
                    If x != 3 Then
                        If x == 3 Then
                            While x Do x = x + 1; EndWhile.
                        Else
                        EndIf.
                    ElseIf x >=. 4 Then
                        Do x = x + 2; While x <. 4 EndDo.
                    Else
                        For (x = 3, x =/= 3., 12 + 3 * 5) Do
                            If x <.3 Then
                                Var: x = 3;
                                x = 6 * x(1, 2, a[2][0]);
                            EndIf.
                        EndFor. 
                    EndIf.
                EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 420))

        input = """
            Var: x[3][1] = {{}, {{}}}, y = "String", z = 99999999.e-1;

            Function: main
                Body:
                    Var: x[2] = 9e1;
                EndBody.

            y = "Another String";

            Function: foo
                Body:
                EndBody.
        """
        expect = "Error on line 9 col 12: y"
        self.assertTrue(TestParser.checkParser(input, expect, 421))

        input = """
            Var: x[3][1] = {{}, {{}}}, y = "String", z = 99999999.e-1;

            Function: main
                Body:
                    Var: x[2] = 9e1;
                EndBody.

            Function: foo
                Body:
                    Var: a, b, c;
                    For (x = 3, x =/= 3., main()) Do
                        Var: x = {};
                        foo();
                        Function: subfoo
                            Body: EndBody.
                    EndFor. 
                EndBody.
        """
        expect = "Error on line 15 col 24: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 422))

        input = """
            Var: x[3][1] = {{}, {{}}}, y = "String", z = 99999999.e-1;

            Function: main
                Body:
                    Var: x[2] = 9e1;
                EndBody.

            Function: foo
                Body:
                    Var: a, b, c;
                    If x == 3 Then
                        Var: a = 0;
                        If x == 2 Then 
                            Var: b = 0;
                            If x == 1 Then
                                Var: c = 0;
                                If x == 0 Then
                                    Var: x = 4;
                                EndIf.
                            EndIf.
                        EndIf.
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 423))

        input = """
            Var: x[3][1] = {{}, {{}}}, y = "String", z = 99999999.e-1;

            ** 
             * A very complex program structure
            **
            Function: main
                Parameter: p1, p2
                Body:
                    Return 0xAF;
                    Do 
                        Continue; 
                        foo();
                        Continue;
                        While True Do
                            Var: x = 0;
                            foo();
                            x = x && foo();
                            Break;
                        EndWhile.
                    While 0xAF EndDo.
                EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 424))