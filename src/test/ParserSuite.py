import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_program(self):
        input = "Function: main \
                    Body:       \
                    EndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 1000))

    def test_program_with_var_decl(self):
        input = """ 
                    Var: x = 9, y, z = {1, 2, 3}; 
                    Function: main
                        Body:
                            x = 0;
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 1001))

        input2 = """Var: x = a;
                    Function: main
                        Body:
                            x = 0;
                        EndBody."""
        expect2 = "Error on line 1 col 9: a"
        self.assertTrue(TestParser.checkParser(input2, expect2, 1002))

        input3 = """Var x = a;
                    Function: main
                        Body:
                            x = 0;
                        EndBody."""
        expect3 = "Error on line 1 col 9: a"
        self.assertTrue(TestParser.checkParser(input3, expect3, 1003))

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_array_dimension(self):
        self.assertTrue(TestParser.checkParser("[ 2 ]" , "successful" , 203))