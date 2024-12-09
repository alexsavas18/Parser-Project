# Generated from alex_savas_grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,162,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,58,8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,66,8,4,10,4,12,4,69,9,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,86,
        8,6,10,6,12,6,89,9,6,1,6,1,6,1,6,3,6,94,8,6,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,4,11,113,8,11,
        11,11,12,11,114,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,3,12,129,8,12,1,12,1,12,1,12,5,12,134,8,12,10,12,12,12,
        137,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,150,8,13,1,13,1,13,1,13,5,13,155,8,13,10,13,12,13,158,9,13,
        1,14,1,14,1,14,0,2,24,26,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,0,4,1,0,2,5,1,0,16,17,2,0,16,17,21,25,1,0,26,31,169,0,31,1,0,
        0,0,2,45,1,0,0,0,4,47,1,0,0,0,6,57,1,0,0,0,8,59,1,0,0,0,10,72,1,
        0,0,0,12,76,1,0,0,0,14,95,1,0,0,0,16,97,1,0,0,0,18,102,1,0,0,0,20,
        109,1,0,0,0,22,112,1,0,0,0,24,128,1,0,0,0,26,149,1,0,0,0,28,159,
        1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,
        33,34,1,0,0,0,34,35,1,0,0,0,35,36,5,0,0,1,36,1,1,0,0,0,37,46,3,4,
        2,0,38,46,3,6,3,0,39,46,3,8,4,0,40,46,3,10,5,0,41,46,3,12,6,0,42,
        46,3,16,8,0,43,46,3,18,9,0,44,46,3,20,10,0,45,37,1,0,0,0,45,38,1,
        0,0,0,45,39,1,0,0,0,45,40,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,0,45,
        43,1,0,0,0,45,44,1,0,0,0,46,3,1,0,0,0,47,48,5,32,0,0,48,49,5,1,0,
        0,49,50,3,26,13,0,50,5,1,0,0,0,51,52,5,32,0,0,52,53,5,1,0,0,53,58,
        3,26,13,0,54,55,5,32,0,0,55,56,7,0,0,0,56,58,3,26,13,0,57,51,1,0,
        0,0,57,54,1,0,0,0,58,7,1,0,0,0,59,60,5,32,0,0,60,61,5,1,0,0,61,62,
        5,6,0,0,62,67,3,26,13,0,63,64,5,7,0,0,64,66,3,26,13,0,65,63,1,0,
        0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,
        1,0,0,0,70,71,5,8,0,0,71,9,1,0,0,0,72,73,5,32,0,0,73,74,5,1,0,0,
        74,75,5,36,0,0,75,11,1,0,0,0,76,77,5,9,0,0,77,78,3,14,7,0,78,79,
        5,10,0,0,79,87,3,22,11,0,80,81,5,11,0,0,81,82,3,14,7,0,82,83,5,10,
        0,0,83,84,3,22,11,0,84,86,1,0,0,0,85,80,1,0,0,0,86,89,1,0,0,0,87,
        85,1,0,0,0,87,88,1,0,0,0,88,93,1,0,0,0,89,87,1,0,0,0,90,91,5,12,
        0,0,91,92,5,10,0,0,92,94,3,22,11,0,93,90,1,0,0,0,93,94,1,0,0,0,94,
        13,1,0,0,0,95,96,3,24,12,0,96,15,1,0,0,0,97,98,5,13,0,0,98,99,3,
        24,12,0,99,100,5,10,0,0,100,101,3,22,11,0,101,17,1,0,0,0,102,103,
        5,14,0,0,103,104,5,32,0,0,104,105,5,15,0,0,105,106,3,26,13,0,106,
        107,5,10,0,0,107,108,3,22,11,0,108,19,1,0,0,0,109,110,5,37,0,0,110,
        21,1,0,0,0,111,113,3,2,1,0,112,111,1,0,0,0,113,114,1,0,0,0,114,112,
        1,0,0,0,114,115,1,0,0,0,115,23,1,0,0,0,116,117,6,12,-1,0,117,118,
        5,18,0,0,118,129,3,24,12,4,119,120,3,26,13,0,120,121,3,28,14,0,121,
        122,3,26,13,0,122,129,1,0,0,0,123,124,5,19,0,0,124,125,3,24,12,0,
        125,126,5,20,0,0,126,129,1,0,0,0,127,129,5,36,0,0,128,116,1,0,0,
        0,128,119,1,0,0,0,128,123,1,0,0,0,128,127,1,0,0,0,129,135,1,0,0,
        0,130,131,10,5,0,0,131,132,7,1,0,0,132,134,3,24,12,6,133,130,1,0,
        0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,25,1,0,0,
        0,137,135,1,0,0,0,138,139,6,13,-1,0,139,140,5,19,0,0,140,141,3,26,
        13,0,141,142,5,20,0,0,142,150,1,0,0,0,143,144,5,22,0,0,144,150,3,
        26,13,5,145,150,5,33,0,0,146,150,5,34,0,0,147,150,5,35,0,0,148,150,
        5,32,0,0,149,138,1,0,0,0,149,143,1,0,0,0,149,145,1,0,0,0,149,146,
        1,0,0,0,149,147,1,0,0,0,149,148,1,0,0,0,150,156,1,0,0,0,151,152,
        10,7,0,0,152,153,7,2,0,0,153,155,3,26,13,8,154,151,1,0,0,0,155,158,
        1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,27,1,0,0,0,158,156,1,
        0,0,0,159,160,7,3,0,0,160,29,1,0,0,0,11,33,45,57,67,87,93,114,128,
        135,149,156
    ]

class alex_savas_grammarParser ( Parser ):

    grammarFileName = "alex_savas_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'['", "','", "']'", "'if'", "':'", "'elif'", "'else'", 
                     "'while'", "'for'", "'in'", "'or'", "'and'", "'not'", 
                     "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "STRING", "BOOL", "COMMENT", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_arithmetic = 3
    RULE_arrayInit = 4
    RULE_boolAssign = 5
    RULE_ifBlock = 6
    RULE_conditionBlock = 7
    RULE_whileLoop = 8
    RULE_forLoop = 9
    RULE_comment = 10
    RULE_block = 11
    RULE_condition = 12
    RULE_expr = 13
    RULE_comparisonOp = 14

    ruleNames =  [ "prog", "statement", "assignment", "arithmetic", "arrayInit", 
                   "boolAssign", "ifBlock", "conditionBlock", "whileLoop", 
                   "forLoop", "comment", "block", "condition", "expr", "comparisonOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    ID=32
    INT=33
    FLOAT=34
    STRING=35
    BOOL=36
    COMMENT=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(alex_savas_grammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.StatementContext,i)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = alex_savas_grammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141733945856) != 0)):
                    break

            self.state = 35
            self.match(alex_savas_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.AssignmentContext,0)


        def arithmetic(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ArithmeticContext,0)


        def arrayInit(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ArrayInitContext,0)


        def boolAssign(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.BoolAssignContext,0)


        def ifBlock(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.IfBlockContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.WhileLoopContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ForLoopContext,0)


        def comment(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.CommentContext,0)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = alex_savas_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.arithmetic()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.arrayInit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.boolAssign()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.ifBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.whileLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 43
                self.forLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 44
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(alex_savas_grammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ExprContext,0)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = alex_savas_grammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(alex_savas_grammarParser.ID)
            self.state = 48
            self.match(alex_savas_grammarParser.T__0)
            self.state = 49
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(alex_savas_grammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ExprContext,0)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)




    def arithmetic(self):

        localctx = alex_savas_grammarParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(alex_savas_grammarParser.ID)
                self.state = 52
                self.match(alex_savas_grammarParser.T__0)
                self.state = 53
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(alex_savas_grammarParser.ID)
                self.state = 55
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(alex_savas_grammarParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.ExprContext,i)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_arrayInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayInit" ):
                listener.enterArrayInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayInit" ):
                listener.exitArrayInit(self)




    def arrayInit(self):

        localctx = alex_savas_grammarParser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(alex_savas_grammarParser.ID)
            self.state = 60
            self.match(alex_savas_grammarParser.T__0)
            self.state = 61
            self.match(alex_savas_grammarParser.T__5)
            self.state = 62
            self.expr(0)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 63
                self.match(alex_savas_grammarParser.T__6)
                self.state = 64
                self.expr(0)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(alex_savas_grammarParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(alex_savas_grammarParser.ID, 0)

        def BOOL(self):
            return self.getToken(alex_savas_grammarParser.BOOL, 0)

        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_boolAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolAssign" ):
                listener.enterBoolAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolAssign" ):
                listener.exitBoolAssign(self)




    def boolAssign(self):

        localctx = alex_savas_grammarParser.BoolAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_boolAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(alex_savas_grammarParser.ID)
            self.state = 73
            self.match(alex_savas_grammarParser.T__0)
            self.state = 74
            self.match(alex_savas_grammarParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.ConditionBlockContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.ConditionBlockContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.BlockContext,i)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)




    def ifBlock(self):

        localctx = alex_savas_grammarParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(alex_savas_grammarParser.T__8)
            self.state = 77
            self.conditionBlock()
            self.state = 78
            self.match(alex_savas_grammarParser.T__9)
            self.state = 79
            self.block()
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80
                    self.match(alex_savas_grammarParser.T__10)
                    self.state = 81
                    self.conditionBlock()
                    self.state = 82
                    self.match(alex_savas_grammarParser.T__9)
                    self.state = 83
                    self.block() 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 90
                self.match(alex_savas_grammarParser.T__11)
                self.state = 91
                self.match(alex_savas_grammarParser.T__9)
                self.state = 92
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ConditionContext,0)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_conditionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionBlock" ):
                listener.enterConditionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionBlock" ):
                listener.exitConditionBlock(self)




    def conditionBlock(self):

        localctx = alex_savas_grammarParser.ConditionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditionBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.condition(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ConditionContext,0)


        def block(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)




    def whileLoop(self):

        localctx = alex_savas_grammarParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(alex_savas_grammarParser.T__12)
            self.state = 98
            self.condition(0)
            self.state = 99
            self.match(alex_savas_grammarParser.T__9)
            self.state = 100
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(alex_savas_grammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)




    def forLoop(self):

        localctx = alex_savas_grammarParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(alex_savas_grammarParser.T__13)
            self.state = 103
            self.match(alex_savas_grammarParser.ID)
            self.state = 104
            self.match(alex_savas_grammarParser.T__14)
            self.state = 105
            self.expr(0)
            self.state = 106
            self.match(alex_savas_grammarParser.T__9)
            self.state = 107
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(alex_savas_grammarParser.COMMENT, 0)

        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = alex_savas_grammarParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(alex_savas_grammarParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.StatementContext,i)


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = alex_savas_grammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 111
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 114 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.ConditionContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.ConditionContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.ExprContext,i)


        def comparisonOp(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ComparisonOpContext,0)


        def BOOL(self):
            return self.getToken(alex_savas_grammarParser.BOOL, 0)

        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = alex_savas_grammarParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 117
                self.match(alex_savas_grammarParser.T__17)
                self.state = 118
                self.condition(4)
                pass

            elif la_ == 2:
                self.state = 119
                self.expr(0)
                self.state = 120
                self.comparisonOp()
                self.state = 121
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 123
                self.match(alex_savas_grammarParser.T__18)
                self.state = 124
                self.condition(0)
                self.state = 125
                self.match(alex_savas_grammarParser.T__19)
                pass

            elif la_ == 4:
                self.state = 127
                self.match(alex_savas_grammarParser.BOOL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = alex_savas_grammarParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 130
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 131
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 132
                    self.condition(6) 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.ExprContext,i)


        def INT(self):
            return self.getToken(alex_savas_grammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(alex_savas_grammarParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(alex_savas_grammarParser.STRING, 0)

        def ID(self):
            return self.getToken(alex_savas_grammarParser.ID, 0)

        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = alex_savas_grammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 139
                self.match(alex_savas_grammarParser.T__18)
                self.state = 140
                self.expr(0)
                self.state = 141
                self.match(alex_savas_grammarParser.T__19)
                pass
            elif token in [22]:
                self.state = 143
                self.match(alex_savas_grammarParser.T__21)
                self.state = 144
                self.expr(5)
                pass
            elif token in [33]:
                self.state = 145
                self.match(alex_savas_grammarParser.INT)
                pass
            elif token in [34]:
                self.state = 146
                self.match(alex_savas_grammarParser.FLOAT)
                pass
            elif token in [35]:
                self.state = 147
                self.match(alex_savas_grammarParser.STRING)
                pass
            elif token in [32]:
                self.state = 148
                self.match(alex_savas_grammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = alex_savas_grammarParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 151
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 152
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65208320) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 153
                    self.expr(8) 
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)




    def comparisonOp(self):

        localctx = alex_savas_grammarParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.condition_sempred
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




