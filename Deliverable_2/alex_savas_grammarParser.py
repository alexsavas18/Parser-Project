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
        4,1,34,143,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,55,8,4,10,4,
        12,4,58,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,4,6,70,8,6,11,
        6,12,6,71,1,6,1,6,1,6,1,6,4,6,78,8,6,11,6,12,6,79,5,6,82,8,6,10,
        6,12,6,85,9,6,1,6,1,6,1,6,4,6,90,8,6,11,6,12,6,91,3,6,94,8,6,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,109,8,8,1,8,
        1,8,1,8,1,8,1,8,1,8,5,8,117,8,8,10,8,12,8,120,9,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,3,9,131,8,9,1,9,1,9,1,9,5,9,136,8,9,10,9,12,
        9,139,9,9,1,10,1,10,1,10,0,2,16,18,11,0,2,4,6,8,10,12,14,16,18,20,
        0,3,1,0,2,5,1,0,18,22,1,0,23,28,152,0,23,1,0,0,0,2,34,1,0,0,0,4,
        36,1,0,0,0,6,46,1,0,0,0,8,48,1,0,0,0,10,61,1,0,0,0,12,65,1,0,0,0,
        14,95,1,0,0,0,16,108,1,0,0,0,18,130,1,0,0,0,20,140,1,0,0,0,22,24,
        3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,
        26,27,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,35,3,4,2,0,30,35,3,6,
        3,0,31,35,3,8,4,0,32,35,3,10,5,0,33,35,3,12,6,0,34,29,1,0,0,0,34,
        30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,3,1,0,0,
        0,36,37,5,29,0,0,37,38,5,1,0,0,38,39,3,18,9,0,39,5,1,0,0,0,40,41,
        5,29,0,0,41,42,5,1,0,0,42,47,3,18,9,0,43,44,5,29,0,0,44,45,7,0,0,
        0,45,47,3,18,9,0,46,40,1,0,0,0,46,43,1,0,0,0,47,7,1,0,0,0,48,49,
        5,29,0,0,49,50,5,1,0,0,50,51,5,6,0,0,51,56,3,18,9,0,52,53,5,7,0,
        0,53,55,3,18,9,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,
        1,0,0,0,57,59,1,0,0,0,58,56,1,0,0,0,59,60,5,8,0,0,60,9,1,0,0,0,61,
        62,5,29,0,0,62,63,5,1,0,0,63,64,5,33,0,0,64,11,1,0,0,0,65,66,5,9,
        0,0,66,67,3,14,7,0,67,69,5,10,0,0,68,70,3,2,1,0,69,68,1,0,0,0,70,
        71,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,83,1,0,0,0,73,74,5,11,
        0,0,74,75,3,14,7,0,75,77,5,10,0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,
        79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,73,1,0,0,
        0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,93,1,0,0,0,85,83,
        1,0,0,0,86,87,5,12,0,0,87,89,5,10,0,0,88,90,3,2,1,0,89,88,1,0,0,
        0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,86,
        1,0,0,0,93,94,1,0,0,0,94,13,1,0,0,0,95,96,3,16,8,0,96,15,1,0,0,0,
        97,98,6,8,-1,0,98,99,5,15,0,0,99,109,3,16,8,3,100,101,3,18,9,0,101,
        102,3,20,10,0,102,103,3,18,9,0,103,109,1,0,0,0,104,105,5,16,0,0,
        105,106,3,16,8,0,106,107,5,17,0,0,107,109,1,0,0,0,108,97,1,0,0,0,
        108,100,1,0,0,0,108,104,1,0,0,0,109,118,1,0,0,0,110,111,10,5,0,0,
        111,112,5,13,0,0,112,117,3,16,8,6,113,114,10,4,0,0,114,115,5,14,
        0,0,115,117,3,16,8,5,116,110,1,0,0,0,116,113,1,0,0,0,117,120,1,0,
        0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,17,1,0,0,0,120,118,1,0,0,
        0,121,122,6,9,-1,0,122,123,5,16,0,0,123,124,3,18,9,0,124,125,5,17,
        0,0,125,131,1,0,0,0,126,131,5,30,0,0,127,131,5,31,0,0,128,131,5,
        32,0,0,129,131,5,29,0,0,130,121,1,0,0,0,130,126,1,0,0,0,130,127,
        1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,131,137,1,0,0,0,132,133,
        10,6,0,0,133,134,7,1,0,0,134,136,3,18,9,7,135,132,1,0,0,0,136,139,
        1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,19,1,0,0,0,139,137,1,
        0,0,0,140,141,7,2,0,0,141,21,1,0,0,0,14,25,34,46,56,71,79,83,91,
        93,108,116,118,130,137
    ]

class alex_savas_grammarParser ( Parser ):

    grammarFileName = "alex_savas_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'['", "','", "']'", "'if'", "':'", "'elif'", "'else'", 
                     "'or'", "'and'", "'not'", "'('", "')'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "STRING", "BOOL", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_arithmetic = 3
    RULE_arrayInit = 4
    RULE_boolAssign = 5
    RULE_ifBlock = 6
    RULE_conditionBlock = 7
    RULE_condition = 8
    RULE_expr = 9
    RULE_comparisonOp = 10

    ruleNames =  [ "prog", "statement", "assignment", "arithmetic", "arrayInit", 
                   "boolAssign", "ifBlock", "conditionBlock", "condition", 
                   "expr", "comparisonOp" ]

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
    ID=29
    INT=30
    FLOAT=31
    STRING=32
    BOOL=33
    WS=34

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==29):
                    break

            self.state = 27
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
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.arithmetic()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.arrayInit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.boolAssign()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.ifBlock()
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
            self.state = 36
            self.match(alex_savas_grammarParser.ID)
            self.state = 37
            self.match(alex_savas_grammarParser.T__0)
            self.state = 38
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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(alex_savas_grammarParser.ID)
                self.state = 41
                self.match(alex_savas_grammarParser.T__0)
                self.state = 42
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(alex_savas_grammarParser.ID)
                self.state = 44
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
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
            self.state = 48
            self.match(alex_savas_grammarParser.ID)
            self.state = 49
            self.match(alex_savas_grammarParser.T__0)
            self.state = 50
            self.match(alex_savas_grammarParser.T__5)
            self.state = 51
            self.expr(0)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 52
                self.match(alex_savas_grammarParser.T__6)
                self.state = 53
                self.expr(0)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
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
            self.state = 61
            self.match(alex_savas_grammarParser.ID)
            self.state = 62
            self.match(alex_savas_grammarParser.T__0)
            self.state = 63
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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.StatementContext,i)


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
            self.state = 65
            self.match(alex_savas_grammarParser.T__8)
            self.state = 66
            self.conditionBlock()
            self.state = 67
            self.match(alex_savas_grammarParser.T__9)
            self.state = 69 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 68
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 71 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 73
                    self.match(alex_savas_grammarParser.T__10)
                    self.state = 74
                    self.conditionBlock()
                    self.state = 75
                    self.match(alex_savas_grammarParser.T__9)
                    self.state = 77 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 76
                            self.statement()

                        else:
                            raise NoViableAltException(self)
                        self.state = 79 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 86
                self.match(alex_savas_grammarParser.T__11)
                self.state = 87
                self.match(alex_savas_grammarParser.T__9)
                self.state = 89 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 88
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 91 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)



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


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return alex_savas_grammarParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a alex_savas_grammarParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ConditionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotCondition" ):
                listener.enterNotCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotCondition" ):
                listener.exitNotCondition(self)


    class ComparisonContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a alex_savas_grammarParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.ExprContext,i)

        def comparisonOp(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ComparisonOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)


    class ParenConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a alex_savas_grammarParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self):
            return self.getTypedRuleContext(alex_savas_grammarParser.ConditionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenCondition" ):
                listener.enterParenCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenCondition" ):
                listener.exitParenCondition(self)


    class OrConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a alex_savas_grammarParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.ConditionContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.ConditionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrCondition" ):
                listener.enterOrCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrCondition" ):
                listener.exitOrCondition(self)


    class AndConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a alex_savas_grammarParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(alex_savas_grammarParser.ConditionContext)
            else:
                return self.getTypedRuleContext(alex_savas_grammarParser.ConditionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndCondition" ):
                listener.enterAndCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndCondition" ):
                listener.exitAndCondition(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = alex_savas_grammarParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = alex_savas_grammarParser.NotConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 98
                self.match(alex_savas_grammarParser.T__14)
                self.state = 99
                self.condition(3)
                pass

            elif la_ == 2:
                localctx = alex_savas_grammarParser.ComparisonContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                self.expr(0)
                self.state = 101
                self.comparisonOp()
                self.state = 102
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = alex_savas_grammarParser.ParenConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(alex_savas_grammarParser.T__15)
                self.state = 105
                self.condition(0)
                self.state = 106
                self.match(alex_savas_grammarParser.T__16)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 116
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = alex_savas_grammarParser.OrConditionContext(self, alex_savas_grammarParser.ConditionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 110
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 111
                        self.match(alex_savas_grammarParser.T__12)
                        self.state = 112
                        self.condition(6)
                        pass

                    elif la_ == 2:
                        localctx = alex_savas_grammarParser.AndConditionContext(self, alex_savas_grammarParser.ConditionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 113
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 114
                        self.match(alex_savas_grammarParser.T__13)
                        self.state = 115
                        self.condition(5)
                        pass

             
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 122
                self.match(alex_savas_grammarParser.T__15)
                self.state = 123
                self.expr(0)
                self.state = 124
                self.match(alex_savas_grammarParser.T__16)
                pass
            elif token in [30]:
                self.state = 126
                self.match(alex_savas_grammarParser.INT)
                pass
            elif token in [31]:
                self.state = 127
                self.match(alex_savas_grammarParser.FLOAT)
                pass
            elif token in [32]:
                self.state = 128
                self.match(alex_savas_grammarParser.STRING)
                pass
            elif token in [29]:
                self.state = 129
                self.match(alex_savas_grammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = alex_savas_grammarParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 132
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 133
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8126464) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 134
                    self.expr(7) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
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
        self._predicates[8] = self.condition_sempred
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




