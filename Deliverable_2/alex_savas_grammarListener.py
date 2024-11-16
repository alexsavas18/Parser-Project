# Generated from alex_savas_grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .alex_savas_grammarParser import alex_savas_grammarParser
else:
    from alex_savas_grammarParser import alex_savas_grammarParser

# This class defines a complete listener for a parse tree produced by alex_savas_grammarParser.
class alex_savas_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by alex_savas_grammarParser#prog.
    def enterProg(self, ctx:alex_savas_grammarParser.ProgContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#prog.
    def exitProg(self, ctx:alex_savas_grammarParser.ProgContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#statement.
    def enterStatement(self, ctx:alex_savas_grammarParser.StatementContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#statement.
    def exitStatement(self, ctx:alex_savas_grammarParser.StatementContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#assignment.
    def enterAssignment(self, ctx:alex_savas_grammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#assignment.
    def exitAssignment(self, ctx:alex_savas_grammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#arithmetic.
    def enterArithmetic(self, ctx:alex_savas_grammarParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#arithmetic.
    def exitArithmetic(self, ctx:alex_savas_grammarParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#arrayInit.
    def enterArrayInit(self, ctx:alex_savas_grammarParser.ArrayInitContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#arrayInit.
    def exitArrayInit(self, ctx:alex_savas_grammarParser.ArrayInitContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#boolAssign.
    def enterBoolAssign(self, ctx:alex_savas_grammarParser.BoolAssignContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#boolAssign.
    def exitBoolAssign(self, ctx:alex_savas_grammarParser.BoolAssignContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#ifBlock.
    def enterIfBlock(self, ctx:alex_savas_grammarParser.IfBlockContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#ifBlock.
    def exitIfBlock(self, ctx:alex_savas_grammarParser.IfBlockContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#conditionBlock.
    def enterConditionBlock(self, ctx:alex_savas_grammarParser.ConditionBlockContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#conditionBlock.
    def exitConditionBlock(self, ctx:alex_savas_grammarParser.ConditionBlockContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#NotCondition.
    def enterNotCondition(self, ctx:alex_savas_grammarParser.NotConditionContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#NotCondition.
    def exitNotCondition(self, ctx:alex_savas_grammarParser.NotConditionContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#Comparison.
    def enterComparison(self, ctx:alex_savas_grammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#Comparison.
    def exitComparison(self, ctx:alex_savas_grammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#ParenCondition.
    def enterParenCondition(self, ctx:alex_savas_grammarParser.ParenConditionContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#ParenCondition.
    def exitParenCondition(self, ctx:alex_savas_grammarParser.ParenConditionContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#OrCondition.
    def enterOrCondition(self, ctx:alex_savas_grammarParser.OrConditionContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#OrCondition.
    def exitOrCondition(self, ctx:alex_savas_grammarParser.OrConditionContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#AndCondition.
    def enterAndCondition(self, ctx:alex_savas_grammarParser.AndConditionContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#AndCondition.
    def exitAndCondition(self, ctx:alex_savas_grammarParser.AndConditionContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#expr.
    def enterExpr(self, ctx:alex_savas_grammarParser.ExprContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#expr.
    def exitExpr(self, ctx:alex_savas_grammarParser.ExprContext):
        pass


    # Enter a parse tree produced by alex_savas_grammarParser#comparisonOp.
    def enterComparisonOp(self, ctx:alex_savas_grammarParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by alex_savas_grammarParser#comparisonOp.
    def exitComparisonOp(self, ctx:alex_savas_grammarParser.ComparisonOpContext):
        pass



del alex_savas_grammarParser