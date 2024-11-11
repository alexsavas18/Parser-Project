grammar deliv1;

// Define the start rule
prog: statement+;

// Statements
statement
    : assignment
    | arithmetic
    | arrayInit
    | boolAssign
    ;

// Assignment rules
assignment
    : ID '=' expr
    ;

// Arithmetic operations and assignments
arithmetic
    : ID '=' expr
    | ID ('+=' | '-=' | '*=' | '/=') expr
    ;

// Array initialization
arrayInit
    : ID '=' '[' expr (',' expr)* ']'
    ;

// Boolean assignment
boolAssign
    : ID '=' BOOL
    ;

// Expressions (supports arithmetic and variables)
expr
    : expr ('*' | '/' | '%') expr
    | expr ('+' | '-') expr
    | '(' expr ')'
    | INT
    | FLOAT
    | STRING
    | ID
    | BOOL
    ;

// Tokens
ID      : [a-zA-Z_][a-zA-Z_0-9]*;
INT     : [0-9]+;
FLOAT   : [0-9]+ '.' [0-9]+;
STRING  : '"' .*? '"';
BOOL    : 'True' | 'False';
WS      : [ \t\r\n]+ -> skip;
