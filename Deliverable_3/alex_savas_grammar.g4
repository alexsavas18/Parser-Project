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
    | whileLoop
    | forLoop
    | comment
    ;

// Assignment rules
assignment: ID '=' expr ;

// Arithmetic operations and assignments
arithmetic: ID '=' expr
          | ID ('+=' | '-=' | '*=' | '/=') expr ;

// Array initialization
arrayInit: ID '=' '[' expr (',' expr)* ']' ;

// Boolean assignment
boolAssign: ID '=' BOOL ;

// Conditional blocks
ifBlock: 'if' conditionBlock ':' block
         ('elif' conditionBlock ':' block)* 
         ('else' ':' block)? ;

// Condition block
conditionBlock: condition ;

// Loops
whileLoop: 'while' condition ':' block ;
forLoop  : 'for' ID 'in' expr ':' block ;

// Comments
comment: COMMENT ;

// Block of statements (used in conditionals and loops)
block: statement+ ;

// Conditional expressions
condition
    : condition ('or' | 'and') condition
    | 'not' condition
    | expr comparisonOp expr
    | '(' condition ')'
    | BOOL
    ;

// Expressions
expr
    : expr ('+' | '-' | '*' | '/' | '%' | 'and' | 'or') expr    // Logical operators inside expressions
    | '(' expr ')'
    | '-' expr                      // Handling for negative numbers
    | INT
    | FLOAT
    | STRING
    | ID
    ;

// Comparison operators
comparisonOp: '>' | '<' | '>=' | '<=' | '==' | '!=' ;

// Tokens
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
INT     : [0-9]+ ;
FLOAT   : [0-9]+ '.' [0-9]+ ;
STRING  : '"' ( ~["\\] | '\\' . )* '"' // Double-quoted strings
        | '\'' ( ~['\\] | '\\' . )* '\'' ; // Single-quoted strings
BOOL    : 'True' | 'False' ;
COMMENT : '#' ~[\r\n]* -> skip; // Comments are ignored
WS      : [ \t\r\n]+ -> skip; // Ignore whitespace