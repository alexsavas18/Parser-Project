import sys
from antlr4 import FileStream, CommonTokenStream
from alex_savas_grammarLexer import alex_savas_grammarLexer
from alex_savas_grammarParser import alex_savas_grammarParser

def main():
    # Open the input file and read it
    file_path = 'project_deliverable_3.py'
    input_stream = FileStream(file_path)
    
    # Initialize the lexer and parser with the input stream
    lexer = alex_savas_grammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = alex_savas_grammarParser(stream)
    
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
# Deliverable 1
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

assign1 = ""

# Deliverable 2

if var1 > var2:
	arith_op1 = 1 + 2
	assign1 = "text data"

if var1 <= var2 and var3 == var4:
	arith_op1 = 1 + 2
	assign1 = "text data"
else:
	arith_op4 = 4.2 * 10
	arith_op3 *= arith_op4
	
data = 0

if var1 != var2 or var3 >= var4:
	flag = True
elif (not flag) and var3 > 10:
	flag = False
else:
	data = -1

# Deliverable 3

## comment test 1

''' 
	comment test 2
	adding more comments
	and more...
'''

while data > 0 or data != 0:
	data = data - 1
	if True:
		a = "This is the weirdest code I have ever written"

for data in array1:
	if data < 0:
		while(data != 0):
			b = "This code doesn't make any sense"
			data = data + 1
	elif data > 0:
		while(data != 0):
			c = "I feel like I have no purpose..."
			data = data - 1

for i in range(0,5):
	data = data * 2
	data = data - 1

''' I need help, this code shouldn't even exist '''
while True:
	data = 30
	data = data - 1