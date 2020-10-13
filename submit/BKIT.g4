grammar BKIT;

// ID: 1813715

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options {
	language=Python3;
}

program: var_declarations function_declarations EOF;

var_declarations: var_declaration*;

function_declarations: function_declaration*;

var_declaration: VAR COLON var_indentifier (ASSIGN literal)? (COMMA var_indentifier (ASSIGN literal)?)* SEMI;

var_indentifier: ID (array_dimension)*;

array_dimension: LS INT_LIT RS;

literal: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | ARRAY_LIT;

function_declaration: FUNCTION COLON ID (param_declaration)* function_body;

param_declaration: PARAM COLON var_indentifier (COMMA var_indentifier)*;

function_body: BODY COLON statements END_BODY DOT;

statements: var_declaration* (stmt_assignment | stmt_if | stmt_for | stmt_while | stmt_do_while | stmt_break | stmt_continue | stmt_call | stmt_return)*;

stmt_assignment: ID ASSIGN exp SEMI;

stmt_if: IF exp THEN statements (ELSE_IF exp THEN statements)* (ELSE statements)? END_IF DOT;

stmt_for: FOR LP for_iterator RP DO statements END_FOR DOT;

for_iterator: ID ASSIGN exp COMMA exp COMMA exp;

stmt_while: WHILE exp DO statements END_WHILE DOT;

stmt_do_while: DO statements WHILE exp END_DO DOT;

stmt_break: BREAK SEMI;

stmt_continue: CONTINUE SEMI;

stmt_call: call_expression SEMI;

call_expression: ID LP (call_param_list (COMMA call_param_list)*)? RP;

call_param_list: exp | ID;

stmt_return: RETURN exp? SEMI;

exp: exp op_rel exp | exp2;

exp2: exp2 op_log_binary exp3 | exp3;

exp3: exp3 op_add exp4 | exp4;

exp4: exp4 op_mul exp5 | exp5;

exp5: op_log_unary exp5 | exp6;

exp6: op_sign exp6 | exp7;

exp7: exp7 LS exp RS | exp8;

exp8: LP exp RP | call_expression | literal | ID;

op_rel: EQ | NEQ | LT | GT | GTE | LTE | NEQF | LTF | GTF | LTEF | GTEF;

op_log_binary: AND | OR;

op_add: ADD | SUB | ADDF | SUBF;

op_mul: MUL | DIV | MULF | DIVF;

op_log_unary: NOT;

op_sign: SUB | SUBF;

///////// Tokens

// Identifier

ID: [a-z][A-Za-z0-9_]* ;

// Keywords

BODY: 'Body' ;

BREAK: 'Break' ;

CONTINUE: 'Continue' ;

DO: 'Do' ;

ELSE: 'Else';

ELSE_IF: 'ElseIf' ;

END_BODY: 'EndBody' ;

END_IF: 'EndIf' ;

END_FOR: 'EndFor' ;

END_WHILE: 'EndWhile' ;

FOR: 'For' ;

FUNCTION: 'Function' ;

IF: 'If' ;

PARAM: 'Parameter' ;

RETURN: 'Return'; 

THEN: 'Then';

VAR: 'Var';

WHILE: 'While';

END_DO: 'EndDo';

// Operators

ASSIGN: '=' ;

ADD: '+' ;

SUB: '-' ;

MUL: '*' ;

DIV: '\\' ;

MOD: '%' ;

ADDF: '+.'; 

SUBF: '-.';

MULF: '*.';

DIVF: '\\.';

NOT: '!';

AND: '&&';

OR: '||';

EQ: '==';

NEQ: '!=';

LT: '<';

GT: '>';

LTE: '<=';

GTE: '>=';

NEQF: '=/=';

LTF: '<.';

GTF: '>.';

LTEF: '<=.';

GTEF: '>=.';

// Separators

DOT: '.' ;

COMMA: ',' ;

SEMI: ';' ;

COLON: ':' ;

LB: '{' ;

RB: '}' ;

LP: '(' ;

RP: ')' ;

LS: '[' ;

RS: ']' ;

// Literals

INT_LIT: '0' | [1-9][0-9]* | '0'[Xx][A-F1-9][A-F0-9]* | '0'[Oo][1-7][0-7]*;

FLOAT_LIT: ('0' | [1-9][0-9]*) '.' [0-9]* EXPONENT? | ('0' | [1-9][0-9]*) '.'? [0-9]* EXPONENT;

fragment EXPONENT: [Ee] ('+' | '-')? [0-9]+;

BOOL_LIT: 'True' | 'False';

STRING_LIT: '"' (ESC | ~['"\\] | '\'' '"')*? '"';

fragment ESC: '\\' [bfrnt'\\];

ARRAY_LIT: '{' WS? (ARRAY_ELEM (WS? ',' WS? ARRAY_ELEM)*)* WS? '}';

ARRAY_ELEM: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | ARRAY_LIT;

COMMENT: '**' .*? '**' -> skip;

WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

// Lexical Errors

ILLEGAL_ESCAPE: '"' (~[\\'"] | '\'' '"')* ('\\' ~[bfrnt'\\] | '\'' ~'"');

UNCLOSE_STRING: '"' (~'"' | '\'' '"')* ('\n' | EOF);

UNTERMINATED_COMMENT: '**' (~'*')* '*'? EOF;

ERROR_CHAR: .;