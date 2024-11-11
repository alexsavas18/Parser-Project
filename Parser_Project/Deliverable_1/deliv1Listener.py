# Generated from deliv1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .deliv1Parser import deliv1Parser
else:
    from deliv1Parser import deliv1Parser

# This class defines a complete listener for a parse tree produced by deliv1Parser.
class deliv1Listener(ParseTreeListener):

    # Enter a parse tree produced by deliv1Parser#prog.
    def enterProg(self, ctx:deliv1Parser.ProgContext):
        pass

    # Exit a parse tree produced by deliv1Parser#prog.
    def exitProg(self, ctx:deliv1Parser.ProgContext):
        pass


    # Enter a parse tree produced by deliv1Parser#statement.
    def enterStatement(self, ctx:deliv1Parser.StatementContext):
        pass

    # Exit a parse tree produced by deliv1Parser#statement.
    def exitStatement(self, ctx:deliv1Parser.StatementContext):
        pass


    # Enter a parse tree produced by deliv1Parser#assignment.
    def enterAssignment(self, ctx:deliv1Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by deliv1Parser#assignment.
    def exitAssignment(self, ctx:deliv1Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by deliv1Parser#arithmetic.
    def enterArithmetic(self, ctx:deliv1Parser.ArithmeticContext):
        pass

    # Exit a parse tree produced by deliv1Parser#arithmetic.
    def exitArithmetic(self, ctx:deliv1Parser.ArithmeticContext):
        pass


    # Enter a parse tree produced by deliv1Parser#arrayInit.
    def enterArrayInit(self, ctx:deliv1Parser.ArrayInitContext):
        pass

    # Exit a parse tree produced by deliv1Parser#arrayInit.
    def exitArrayInit(self, ctx:deliv1Parser.ArrayInitContext):
        pass


    # Enter a parse tree produced by deliv1Parser#boolAssign.
    def enterBoolAssign(self, ctx:deliv1Parser.BoolAssignContext):
        pass

    # Exit a parse tree produced by deliv1Parser#boolAssign.
    def exitBoolAssign(self, ctx:deliv1Parser.BoolAssignContext):
        pass


    # Enter a parse tree produced by deliv1Parser#expr.
    def enterExpr(self, ctx:deliv1Parser.ExprContext):
        pass

    # Exit a parse tree produced by deliv1Parser#expr.
    def exitExpr(self, ctx:deliv1Parser.ExprContext):
        pass



del deliv1Parser