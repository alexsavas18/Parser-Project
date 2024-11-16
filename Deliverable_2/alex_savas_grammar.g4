grammar alex_savas_grammar;

// Define the start rule
prog: statement+ EOF;

// Statements
statement
    : assignment
    | arithmetic
    | arrayInit
    | boolAssign
    | ifBlock
    ;

// Assignment rules
assignment : ID '=' expr ;

// Arithmetic operations and assignments
arithmetic : ID '=' expr | ID ('+=' | '-=' | '*=' | '/=') expr ;

// Array initialization
arrayInit : ID '=' '[' expr (',' expr)* ']' ;

// Boolean assignment
boolAssign : ID '=' BOOL ;

// Conditional blocks (if/elif/else only)
ifBlock : 'if' conditionBlock ':' statement+
           ('elif' conditionBlock ':' statement+)* 
           ('else' ':' statement+)? ;

// Condition block for 'if' and 'elif'
conditionBlock : condition ;

// Conditional expressions with precedence
condition
    : condition ('or'|'and') condition          # LogicalOperations
    | 'not' condition                            # NotCondition
    | expr comparisonOp expr                     # Comparison
    | '(' condition ')'                          # ParenCondition
    ;

// Expressions (supports arithmetic and variables)
expr
    : expr ('+' | '-' | '*' | '/' | '%') expr
    | '(' expr ')'
    | INT
    | FLOAT
    | STRING
    | ID
    ;

// Comparison operators
comparisonOp : '>' | '<' | '>=' | '<=' | '==' | '!=' ;

// Tokens
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
INT     : [0-9]+ ;
FLOAT   : [0-9]+ '.' [0-9]+ ;
STRING  : '"' ( ~["\\] | '\\' . )* '"' ;
BOOL    : 'True' | 'False' ;
WS      : [ \t\r\n]+ -> skip ;
