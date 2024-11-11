import sys
from antlr4 import *
from deliv1Lexer import deliv1Lexer
from deliv1Parser import deliv1Parser

def main():
    # Open the input file and read it
    file_path = 'project_deliverable_1.py'
    input_stream = FileStream(file_path)
    
    # Initialize the lexer and parser with the input stream
    lexer = deliv1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = deliv1Parser(stream)
    
    # Parse using the starting rule (e.g., `prog`)
    tree = parser.prog()

    # Print the parse tree (for debugging)
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()

assign1 = "20"
assign2 = 123
assign3 = 1.23
assign4 = assign1

arith_op1 = 1 + 2
arith_op2 = 13 - 3
arith_op3 = 10 / arith_op1
arith_op4 = 4.2 * 10
arith_op5 = arith_op1 % arith_op2

arith_op1 += arith_op2
arith_op2 -= arith_op3
arith_op3 *= arith_op4
arith_op4 /= arith_op5

array1 = [1, 2, 3, 4, 5]
array2 = ['a', 'b', 'c']
array3 = [1.6, 2.7, 3.8, 4.9, 5.0]

var1 = 10
var2 = var1/2 + 5
var3 = var2 % 2
var4 = 1

flag = True