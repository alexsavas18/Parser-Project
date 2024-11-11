# Generated from deliv1.g4 by ANTLR 4.13.2
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
        4,1,21,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,36,8,3,1,4,1,4,1,4,1,4,1,4,1,
        4,5,4,44,8,4,10,4,12,4,47,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,64,8,6,1,6,1,6,1,6,5,6,69,8,6,10,6,
        12,6,72,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,2,1,0,2,5,1,0,9,13,77,
        0,15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,35,1,0,0,0,8,37,1,0,0,0,
        10,50,1,0,0,0,12,63,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,
        0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,24,3,4,2,0,20,
        24,3,6,3,0,21,24,3,8,4,0,22,24,3,10,5,0,23,19,1,0,0,0,23,20,1,0,
        0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,16,0,0,26,27,
        5,1,0,0,27,28,3,12,6,0,28,5,1,0,0,0,29,30,5,16,0,0,30,31,5,1,0,0,
        31,36,3,12,6,0,32,33,5,16,0,0,33,34,7,0,0,0,34,36,3,12,6,0,35,29,
        1,0,0,0,35,32,1,0,0,0,36,7,1,0,0,0,37,38,5,16,0,0,38,39,5,1,0,0,
        39,40,5,6,0,0,40,45,3,12,6,0,41,42,5,7,0,0,42,44,3,12,6,0,43,41,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,
        47,45,1,0,0,0,48,49,5,8,0,0,49,9,1,0,0,0,50,51,5,16,0,0,51,52,5,
        1,0,0,52,53,5,20,0,0,53,11,1,0,0,0,54,55,6,6,-1,0,55,56,5,14,0,0,
        56,57,3,12,6,0,57,58,5,15,0,0,58,64,1,0,0,0,59,64,5,17,0,0,60,64,
        5,18,0,0,61,64,5,19,0,0,62,64,5,16,0,0,63,54,1,0,0,0,63,59,1,0,0,
        0,63,60,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,70,1,0,0,0,65,66,
        10,6,0,0,66,67,7,1,0,0,67,69,3,12,6,7,68,65,1,0,0,0,69,72,1,0,0,
        0,70,68,1,0,0,0,70,71,1,0,0,0,71,13,1,0,0,0,72,70,1,0,0,0,6,17,23,
        35,45,63,70
    ]

class deliv1Parser ( Parser ):

    grammarFileName = "deliv1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'['", "','", "']'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "STRING", "BOOL", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_arithmetic = 3
    RULE_arrayInit = 4
    RULE_boolAssign = 5
    RULE_expr = 6

    ruleNames =  [ "prog", "statement", "assignment", "arithmetic", "arrayInit", 
                   "boolAssign", "expr" ]

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
    ID=16
    INT=17
    FLOAT=18
    STRING=19
    BOOL=20
    WS=21

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliv1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(deliv1Parser.StatementContext,i)


        def getRuleIndex(self):
            return deliv1Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = deliv1Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

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
            return self.getTypedRuleContext(deliv1Parser.AssignmentContext,0)


        def arithmetic(self):
            return self.getTypedRuleContext(deliv1Parser.ArithmeticContext,0)


        def arrayInit(self):
            return self.getTypedRuleContext(deliv1Parser.ArrayInitContext,0)


        def boolAssign(self):
            return self.getTypedRuleContext(deliv1Parser.BoolAssignContext,0)


        def getRuleIndex(self):
            return deliv1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = deliv1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.arithmetic()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.arrayInit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.boolAssign()
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
            return self.getToken(deliv1Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(deliv1Parser.ExprContext,0)


        def getRuleIndex(self):
            return deliv1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = deliv1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(deliv1Parser.ID)
            self.state = 26
            self.match(deliv1Parser.T__0)
            self.state = 27
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
            return self.getToken(deliv1Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(deliv1Parser.ExprContext,0)


        def getRuleIndex(self):
            return deliv1Parser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)




    def arithmetic(self):

        localctx = deliv1Parser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(deliv1Parser.ID)
                self.state = 30
                self.match(deliv1Parser.T__0)
                self.state = 31
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(deliv1Parser.ID)
                self.state = 33
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 34
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
            return self.getToken(deliv1Parser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliv1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(deliv1Parser.ExprContext,i)


        def getRuleIndex(self):
            return deliv1Parser.RULE_arrayInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayInit" ):
                listener.enterArrayInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayInit" ):
                listener.exitArrayInit(self)




    def arrayInit(self):

        localctx = deliv1Parser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(deliv1Parser.ID)
            self.state = 38
            self.match(deliv1Parser.T__0)
            self.state = 39
            self.match(deliv1Parser.T__5)
            self.state = 40
            self.expr(0)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 41
                self.match(deliv1Parser.T__6)
                self.state = 42
                self.expr(0)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(deliv1Parser.T__7)
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
            return self.getToken(deliv1Parser.ID, 0)

        def BOOL(self):
            return self.getToken(deliv1Parser.BOOL, 0)

        def getRuleIndex(self):
            return deliv1Parser.RULE_boolAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolAssign" ):
                listener.enterBoolAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolAssign" ):
                listener.exitBoolAssign(self)




    def boolAssign(self):

        localctx = deliv1Parser.BoolAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_boolAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(deliv1Parser.ID)
            self.state = 51
            self.match(deliv1Parser.T__0)
            self.state = 52
            self.match(deliv1Parser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliv1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(deliv1Parser.ExprContext,i)


        def INT(self):
            return self.getToken(deliv1Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(deliv1Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(deliv1Parser.STRING, 0)

        def ID(self):
            return self.getToken(deliv1Parser.ID, 0)

        def getRuleIndex(self):
            return deliv1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = deliv1Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 55
                self.match(deliv1Parser.T__13)
                self.state = 56
                self.expr(0)
                self.state = 57
                self.match(deliv1Parser.T__14)
                pass
            elif token in [17]:
                self.state = 59
                self.match(deliv1Parser.INT)
                pass
            elif token in [18]:
                self.state = 60
                self.match(deliv1Parser.FLOAT)
                pass
            elif token in [19]:
                self.state = 61
                self.match(deliv1Parser.STRING)
                pass
            elif token in [16]:
                self.state = 62
                self.match(deliv1Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = deliv1Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 65
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 66
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 67
                    self.expr(7) 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         




