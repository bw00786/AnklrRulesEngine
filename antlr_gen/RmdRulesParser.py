# Generated from RmdRules.g4 by ANTLR 4.13.2
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
        4,1,33,218,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,1,1,1,
        4,1,56,8,1,11,1,12,1,57,1,2,1,2,1,2,4,2,63,8,2,11,2,12,2,64,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,82,8,
        3,11,3,12,3,83,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,
        10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,
        12,1,12,5,12,113,8,12,10,12,12,12,116,9,12,1,13,1,13,1,13,1,13,1,
        13,1,13,5,13,124,8,13,10,13,12,13,127,9,13,1,14,1,14,1,14,1,14,1,
        14,1,14,5,14,135,8,14,10,14,12,14,138,9,14,1,15,1,15,1,15,1,15,1,
        15,1,15,5,15,146,8,15,10,15,12,15,149,9,15,1,16,1,16,1,16,3,16,154,
        8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,
        167,8,17,1,18,1,18,1,18,3,18,172,8,18,1,18,1,18,1,19,1,19,1,19,5,
        19,179,8,19,10,19,12,19,182,9,19,1,20,1,20,1,20,1,20,1,21,1,21,1,
        21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,201,8,
        22,1,23,1,23,1,23,1,23,5,23,207,8,23,10,23,12,23,210,9,23,3,23,212,
        8,23,1,23,1,23,1,24,1,24,1,24,0,4,24,26,28,30,25,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,4,1,0,2,
        3,1,0,4,5,2,0,26,26,32,32,2,0,10,10,13,18,217,0,50,1,0,0,0,2,53,
        1,0,0,0,4,59,1,0,0,0,6,68,1,0,0,0,8,85,1,0,0,0,10,87,1,0,0,0,12,
        89,1,0,0,0,14,91,1,0,0,0,16,93,1,0,0,0,18,95,1,0,0,0,20,97,1,0,0,
        0,22,101,1,0,0,0,24,106,1,0,0,0,26,117,1,0,0,0,28,128,1,0,0,0,30,
        139,1,0,0,0,32,153,1,0,0,0,34,166,1,0,0,0,36,168,1,0,0,0,38,175,
        1,0,0,0,40,183,1,0,0,0,42,187,1,0,0,0,44,200,1,0,0,0,46,202,1,0,
        0,0,48,215,1,0,0,0,50,51,3,2,1,0,51,52,5,0,0,1,52,1,1,0,0,0,53,55,
        3,4,2,0,54,56,3,6,3,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,
        57,58,1,0,0,0,58,3,1,0,0,0,59,62,5,6,0,0,60,61,5,20,0,0,61,63,5,
        6,0,0,62,60,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,
        66,1,0,0,0,66,67,5,21,0,0,67,5,1,0,0,0,68,69,3,8,4,0,69,70,5,20,
        0,0,70,71,3,10,5,0,71,72,5,20,0,0,72,73,3,12,6,0,73,74,5,20,0,0,
        74,75,3,14,7,0,75,76,5,20,0,0,76,77,3,16,8,0,77,78,5,20,0,0,78,79,
        3,18,9,0,79,81,5,21,0,0,80,82,3,20,10,0,81,80,1,0,0,0,82,83,1,0,
        0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,7,1,0,0,0,85,86,5,32,0,0,86,9,
        1,0,0,0,87,88,5,32,0,0,88,11,1,0,0,0,89,90,5,25,0,0,90,13,1,0,0,
        0,91,92,5,26,0,0,92,15,1,0,0,0,93,94,3,24,12,0,94,17,1,0,0,0,95,
        96,5,6,0,0,96,19,1,0,0,0,97,98,5,20,0,0,98,99,3,22,11,0,99,100,5,
        21,0,0,100,21,1,0,0,0,101,102,5,12,0,0,102,103,5,32,0,0,103,104,
        5,1,0,0,104,105,3,44,22,0,105,23,1,0,0,0,106,107,6,12,-1,0,107,108,
        3,26,13,0,108,114,1,0,0,0,109,110,10,2,0,0,110,111,5,8,0,0,111,113,
        3,26,13,0,112,109,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,
        1,0,0,0,115,25,1,0,0,0,116,114,1,0,0,0,117,118,6,13,-1,0,118,119,
        3,28,14,0,119,125,1,0,0,0,120,121,10,2,0,0,121,122,5,7,0,0,122,124,
        3,28,14,0,123,120,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,27,1,0,0,0,127,125,1,0,0,0,128,129,6,14,-1,0,129,130,
        3,30,15,0,130,136,1,0,0,0,131,132,10,2,0,0,132,133,7,0,0,0,133,135,
        3,30,15,0,134,131,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,
        1,0,0,0,137,29,1,0,0,0,138,136,1,0,0,0,139,140,6,15,-1,0,140,141,
        3,32,16,0,141,147,1,0,0,0,142,143,10,2,0,0,143,144,7,1,0,0,144,146,
        3,32,16,0,145,142,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,
        1,0,0,0,148,31,1,0,0,0,149,147,1,0,0,0,150,151,5,3,0,0,151,154,3,
        32,16,0,152,154,3,34,17,0,153,150,1,0,0,0,153,152,1,0,0,0,154,33,
        1,0,0,0,155,156,5,9,0,0,156,167,3,34,17,0,157,158,5,30,0,0,158,159,
        3,24,12,0,159,160,5,31,0,0,160,167,1,0,0,0,161,167,3,36,18,0,162,
        167,3,40,20,0,163,167,3,42,21,0,164,167,3,44,22,0,165,167,5,32,0,
        0,166,155,1,0,0,0,166,157,1,0,0,0,166,161,1,0,0,0,166,162,1,0,0,
        0,166,163,1,0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,35,1,0,0,0,
        168,169,5,32,0,0,169,171,5,30,0,0,170,172,3,38,19,0,171,170,1,0,
        0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,31,0,0,174,37,1,0,
        0,0,175,180,3,24,12,0,176,177,5,29,0,0,177,179,3,24,12,0,178,176,
        1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,39,1,
        0,0,0,182,180,1,0,0,0,183,184,5,32,0,0,184,185,3,48,24,0,185,186,
        3,44,22,0,186,41,1,0,0,0,187,188,5,11,0,0,188,189,5,30,0,0,189,190,
        7,2,0,0,190,191,5,31,0,0,191,43,1,0,0,0,192,201,5,23,0,0,193,201,
        5,25,0,0,194,201,5,26,0,0,195,201,5,24,0,0,196,201,3,46,23,0,197,
        201,5,32,0,0,198,201,3,36,18,0,199,201,3,42,21,0,200,192,1,0,0,0,
        200,193,1,0,0,0,200,194,1,0,0,0,200,195,1,0,0,0,200,196,1,0,0,0,
        200,197,1,0,0,0,200,198,1,0,0,0,200,199,1,0,0,0,201,45,1,0,0,0,202,
        211,5,27,0,0,203,208,3,44,22,0,204,205,5,29,0,0,205,207,3,44,22,
        0,206,204,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,
        0,209,212,1,0,0,0,210,208,1,0,0,0,211,203,1,0,0,0,211,212,1,0,0,
        0,212,213,1,0,0,0,213,214,5,28,0,0,214,47,1,0,0,0,215,216,7,3,0,
        0,216,49,1,0,0,0,14,57,64,83,114,125,136,147,153,166,171,180,200,
        208,211
    ]

class RmdRulesParser ( Parser ):

    grammarFileName = "RmdRules.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'to'", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "'and'", "'or'", "'not'", "'in'", "'refRule'", "'set'", 
                     "'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "';'", 
                     "'    '", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "','", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SECTION_HEADER", "AND", 
                      "OR", "NOT", "IN", "REFRULE", "SET", "EQ", "NEQ", 
                      "GTE", "LTE", "GT", "LT", "SEMI", "TAB", "NEWLINE", 
                      "WS", "BOOLEAN", "DATE", "NUMBER", "STRING", "LBRACK", 
                      "RBRACK", "COMMA", "LPAREN", "RPAREN", "IDENTIFIER", 
                      "LINE_COMMENT" ]

    RULE_start = 0
    RULE_dslDocument = 1
    RULE_headerRow = 2
    RULE_ruleRow = 3
    RULE_context = 4
    RULE_name = 5
    RULE_priority = 6
    RULE_description = 7
    RULE_conditions = 8
    RULE_actionsHeader = 9
    RULE_actionLine = 10
    RULE_action = 11
    RULE_expr = 12
    RULE_term = 13
    RULE_arithmeticExpr = 14
    RULE_arithmeticTerm = 15
    RULE_arithmeticFactor = 16
    RULE_factor = 17
    RULE_functionCall = 18
    RULE_exprList = 19
    RULE_comparison = 20
    RULE_refRule = 21
    RULE_value = 22
    RULE_listLiteral = 23
    RULE_compOp = 24

    ruleNames =  [ "start", "dslDocument", "headerRow", "ruleRow", "context", 
                   "name", "priority", "description", "conditions", "actionsHeader", 
                   "actionLine", "action", "expr", "term", "arithmeticExpr", 
                   "arithmeticTerm", "arithmeticFactor", "factor", "functionCall", 
                   "exprList", "comparison", "refRule", "value", "listLiteral", 
                   "compOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    SECTION_HEADER=6
    AND=7
    OR=8
    NOT=9
    IN=10
    REFRULE=11
    SET=12
    EQ=13
    NEQ=14
    GTE=15
    LTE=16
    GT=17
    LT=18
    SEMI=19
    TAB=20
    NEWLINE=21
    WS=22
    BOOLEAN=23
    DATE=24
    NUMBER=25
    STRING=26
    LBRACK=27
    RBRACK=28
    COMMA=29
    LPAREN=30
    RPAREN=31
    IDENTIFIER=32
    LINE_COMMENT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dslDocument(self):
            return self.getTypedRuleContext(RmdRulesParser.DslDocumentContext,0)


        def EOF(self):
            return self.getToken(RmdRulesParser.EOF, 0)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = RmdRulesParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.dslDocument()
            self.state = 51
            self.match(RmdRulesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DslDocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def headerRow(self):
            return self.getTypedRuleContext(RmdRulesParser.HeaderRowContext,0)


        def ruleRow(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RmdRulesParser.RuleRowContext)
            else:
                return self.getTypedRuleContext(RmdRulesParser.RuleRowContext,i)


        def getRuleIndex(self):
            return RmdRulesParser.RULE_dslDocument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDslDocument" ):
                listener.enterDslDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDslDocument" ):
                listener.exitDslDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDslDocument" ):
                return visitor.visitDslDocument(self)
            else:
                return visitor.visitChildren(self)




    def dslDocument(self):

        localctx = RmdRulesParser.DslDocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dslDocument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.headerRow()
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.ruleRow()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderRowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECTION_HEADER(self, i:int=None):
            if i is None:
                return self.getTokens(RmdRulesParser.SECTION_HEADER)
            else:
                return self.getToken(RmdRulesParser.SECTION_HEADER, i)

        def NEWLINE(self):
            return self.getToken(RmdRulesParser.NEWLINE, 0)

        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(RmdRulesParser.TAB)
            else:
                return self.getToken(RmdRulesParser.TAB, i)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_headerRow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderRow" ):
                listener.enterHeaderRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderRow" ):
                listener.exitHeaderRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeaderRow" ):
                return visitor.visitHeaderRow(self)
            else:
                return visitor.visitChildren(self)




    def headerRow(self):

        localctx = RmdRulesParser.HeaderRowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_headerRow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(RmdRulesParser.SECTION_HEADER)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.match(RmdRulesParser.TAB)
                self.state = 61
                self.match(RmdRulesParser.SECTION_HEADER)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

            self.state = 66
            self.match(RmdRulesParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleRowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def context(self):
            return self.getTypedRuleContext(RmdRulesParser.ContextContext,0)


        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(RmdRulesParser.TAB)
            else:
                return self.getToken(RmdRulesParser.TAB, i)

        def name(self):
            return self.getTypedRuleContext(RmdRulesParser.NameContext,0)


        def priority(self):
            return self.getTypedRuleContext(RmdRulesParser.PriorityContext,0)


        def description(self):
            return self.getTypedRuleContext(RmdRulesParser.DescriptionContext,0)


        def conditions(self):
            return self.getTypedRuleContext(RmdRulesParser.ConditionsContext,0)


        def actionsHeader(self):
            return self.getTypedRuleContext(RmdRulesParser.ActionsHeaderContext,0)


        def NEWLINE(self):
            return self.getToken(RmdRulesParser.NEWLINE, 0)

        def actionLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RmdRulesParser.ActionLineContext)
            else:
                return self.getTypedRuleContext(RmdRulesParser.ActionLineContext,i)


        def getRuleIndex(self):
            return RmdRulesParser.RULE_ruleRow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleRow" ):
                listener.enterRuleRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleRow" ):
                listener.exitRuleRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleRow" ):
                return visitor.visitRuleRow(self)
            else:
                return visitor.visitChildren(self)




    def ruleRow(self):

        localctx = RmdRulesParser.RuleRowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ruleRow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.context()
            self.state = 69
            self.match(RmdRulesParser.TAB)
            self.state = 70
            self.name()
            self.state = 71
            self.match(RmdRulesParser.TAB)
            self.state = 72
            self.priority()
            self.state = 73
            self.match(RmdRulesParser.TAB)
            self.state = 74
            self.description()
            self.state = 75
            self.match(RmdRulesParser.TAB)
            self.state = 76
            self.conditions()
            self.state = 77
            self.match(RmdRulesParser.TAB)
            self.state = 78
            self.actionsHeader()
            self.state = 79
            self.match(RmdRulesParser.NEWLINE)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.actionLine()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RmdRulesParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_context

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContext" ):
                listener.enterContext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContext" ):
                listener.exitContext(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContext" ):
                return visitor.visitContext(self)
            else:
                return visitor.visitChildren(self)




    def context(self):

        localctx = RmdRulesParser.ContextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(RmdRulesParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RmdRulesParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = RmdRulesParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(RmdRulesParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PriorityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RmdRulesParser.NUMBER, 0)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_priority

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPriority" ):
                listener.enterPriority(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPriority" ):
                listener.exitPriority(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPriority" ):
                return visitor.visitPriority(self)
            else:
                return visitor.visitChildren(self)




    def priority(self):

        localctx = RmdRulesParser.PriorityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_priority)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(RmdRulesParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RmdRulesParser.STRING, 0)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescription" ):
                listener.enterDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescription" ):
                listener.exitDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescription" ):
                return visitor.visitDescription(self)
            else:
                return visitor.visitChildren(self)




    def description(self):

        localctx = RmdRulesParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(RmdRulesParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(RmdRulesParser.ExprContext,0)


        def getRuleIndex(self):
            return RmdRulesParser.RULE_conditions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditions" ):
                listener.enterConditions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditions" ):
                listener.exitConditions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditions" ):
                return visitor.visitConditions(self)
            else:
                return visitor.visitChildren(self)




    def conditions(self):

        localctx = RmdRulesParser.ConditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_conditions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionsHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECTION_HEADER(self):
            return self.getToken(RmdRulesParser.SECTION_HEADER, 0)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_actionsHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionsHeader" ):
                listener.enterActionsHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionsHeader" ):
                listener.exitActionsHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionsHeader" ):
                return visitor.visitActionsHeader(self)
            else:
                return visitor.visitChildren(self)




    def actionsHeader(self):

        localctx = RmdRulesParser.ActionsHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_actionsHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(RmdRulesParser.SECTION_HEADER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAB(self):
            return self.getToken(RmdRulesParser.TAB, 0)

        def action(self):
            return self.getTypedRuleContext(RmdRulesParser.ActionContext,0)


        def NEWLINE(self):
            return self.getToken(RmdRulesParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_actionLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionLine" ):
                listener.enterActionLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionLine" ):
                listener.exitActionLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionLine" ):
                return visitor.visitActionLine(self)
            else:
                return visitor.visitChildren(self)




    def actionLine(self):

        localctx = RmdRulesParser.ActionLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_actionLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(RmdRulesParser.TAB)
            self.state = 98
            self.action()
            self.state = 99
            self.match(RmdRulesParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(RmdRulesParser.SET, 0)

        def IDENTIFIER(self):
            return self.getToken(RmdRulesParser.IDENTIFIER, 0)

        def value(self):
            return self.getTypedRuleContext(RmdRulesParser.ValueContext,0)


        def getRuleIndex(self):
            return RmdRulesParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = RmdRulesParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(RmdRulesParser.SET)
            self.state = 102
            self.match(RmdRulesParser.IDENTIFIER)
            self.state = 103
            self.match(RmdRulesParser.T__0)
            self.state = 104
            self.value()
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


        def getRuleIndex(self):
            return RmdRulesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RmdRulesParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTerm" ):
                listener.enterSingleTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTerm" ):
                listener.exitSingleTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleTerm" ):
                return visitor.visitSingleTerm(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RmdRulesParser.ExprContext,0)

        def OR(self):
            return self.getToken(RmdRulesParser.OR, 0)
        def term(self):
            return self.getTypedRuleContext(RmdRulesParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RmdRulesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RmdRulesParser.SingleTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 107
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RmdRulesParser.OrExprContext(self, RmdRulesParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 109
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 110
                    self.match(RmdRulesParser.OR)
                    self.state = 111
                    self.term(0) 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticExpr(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleFactor" ):
                listener.enterSingleFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleFactor" ):
                listener.exitSingleFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleFactor" ):
                return visitor.visitSingleFactor(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RmdRulesParser.TermContext,0)

        def AND(self):
            return self.getToken(RmdRulesParser.AND, 0)
        def arithmeticExpr(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RmdRulesParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RmdRulesParser.SingleFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 118
            self.arithmeticExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RmdRulesParser.AndExprContext(self, RmdRulesParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 120
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 121
                    self.match(RmdRulesParser.AND)
                    self.state = 122
                    self.arithmeticExpr(0) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithmeticExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_arithmeticExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ArithmeticAtomContext(ArithmeticExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ArithmeticExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticTerm(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticAtom" ):
                listener.enterArithmeticAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticAtom" ):
                listener.exitArithmeticAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticAtom" ):
                return visitor.visitArithmeticAtom(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ArithmeticExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ArithmeticExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def arithmeticExpr(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticExprContext,0)

        def arithmeticTerm(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RmdRulesParser.ArithmeticExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_arithmeticExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RmdRulesParser.ArithmeticAtomContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 129
            self.arithmeticTerm(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RmdRulesParser.AddSubContext(self, RmdRulesParser.ArithmeticExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticExpr)
                    self.state = 131
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 132
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 133
                    self.arithmeticTerm(0) 
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithmeticTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_arithmeticTerm

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ArithmeticFactorOnlyContext(ArithmeticTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ArithmeticTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticFactor(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticFactorOnly" ):
                listener.enterArithmeticFactorOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticFactorOnly" ):
                listener.exitArithmeticFactorOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticFactorOnly" ):
                return visitor.visitArithmeticFactorOnly(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ArithmeticTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ArithmeticTermContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def arithmeticTerm(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticTermContext,0)

        def arithmeticFactor(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticTerm(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RmdRulesParser.ArithmeticTermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_arithmeticTerm, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RmdRulesParser.ArithmeticFactorOnlyContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 140
            self.arithmeticFactor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RmdRulesParser.MulDivContext(self, RmdRulesParser.ArithmeticTermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticTerm)
                    self.state = 142
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 143
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==4 or _la==5):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 144
                    self.arithmeticFactor() 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithmeticFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_arithmeticFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NegateExprContext(ArithmeticFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ArithmeticFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticFactor(self):
            return self.getTypedRuleContext(RmdRulesParser.ArithmeticFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegateExpr" ):
                listener.enterNegateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegateExpr" ):
                listener.exitNegateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegateExpr" ):
                return visitor.visitNegateExpr(self)
            else:
                return visitor.visitChildren(self)


    class EmbeddedLogicContext(ArithmeticFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ArithmeticFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(RmdRulesParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmbeddedLogic" ):
                listener.enterEmbeddedLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmbeddedLogic" ):
                listener.exitEmbeddedLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmbeddedLogic" ):
                return visitor.visitEmbeddedLogic(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticFactor(self):

        localctx = RmdRulesParser.ArithmeticFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arithmeticFactor)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = RmdRulesParser.NegateExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(RmdRulesParser.T__2)
                self.state = 151
                self.arithmeticFactor()
                pass
            elif token in [9, 11, 23, 24, 25, 26, 27, 30, 32]:
                localctx = RmdRulesParser.EmbeddedLogicContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdentExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RmdRulesParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentExpr" ):
                listener.enterIdentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentExpr" ):
                listener.exitIdentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentExpr" ):
                return visitor.visitIdentExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(RmdRulesParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(RmdRulesParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(RmdRulesParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class CompareContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparison(self):
            return self.getTypedRuleContext(RmdRulesParser.ComparisonContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(RmdRulesParser.NOT, 0)
        def factor(self):
            return self.getTypedRuleContext(RmdRulesParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(RmdRulesParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncExpr" ):
                listener.enterFuncExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncExpr" ):
                listener.exitFuncExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncExpr" ):
                return visitor.visitFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class ValueExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(RmdRulesParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueExpr" ):
                listener.enterValueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueExpr" ):
                listener.exitValueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueExpr" ):
                return visitor.visitValueExpr(self)
            else:
                return visitor.visitChildren(self)


    class RefExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def refRule(self):
            return self.getTypedRuleContext(RmdRulesParser.RefRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefExpr" ):
                listener.enterRefExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefExpr" ):
                listener.exitRefExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefExpr" ):
                return visitor.visitRefExpr(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = RmdRulesParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = RmdRulesParser.NotExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(RmdRulesParser.NOT)
                self.state = 156
                self.factor()
                pass

            elif la_ == 2:
                localctx = RmdRulesParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(RmdRulesParser.LPAREN)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(RmdRulesParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = RmdRulesParser.FuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.functionCall()
                pass

            elif la_ == 4:
                localctx = RmdRulesParser.CompareContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.comparison()
                pass

            elif la_ == 5:
                localctx = RmdRulesParser.RefExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.refRule()
                pass

            elif la_ == 6:
                localctx = RmdRulesParser.ValueExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 164
                self.value()
                pass

            elif la_ == 7:
                localctx = RmdRulesParser.IdentExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 165
                self.match(RmdRulesParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_functionCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionExprContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RmdRulesParser.IDENTIFIER, 0)
        def LPAREN(self):
            return self.getToken(RmdRulesParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(RmdRulesParser.RPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(RmdRulesParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpr" ):
                listener.enterFunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpr" ):
                listener.exitFunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionExpr" ):
                return visitor.visitFunctionExpr(self)
            else:
                return visitor.visitChildren(self)



    def functionCall(self):

        localctx = RmdRulesParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            localctx = RmdRulesParser.FunctionExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(RmdRulesParser.IDENTIFIER)
            self.state = 169
            self.match(RmdRulesParser.LPAREN)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5628758536) != 0):
                self.state = 170
                self.exprList()


            self.state = 173
            self.match(RmdRulesParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RmdRulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(RmdRulesParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RmdRulesParser.COMMA)
            else:
                return self.getToken(RmdRulesParser.COMMA, i)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = RmdRulesParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.expr(0)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 176
                self.match(RmdRulesParser.COMMA)
                self.state = 177
                self.expr(0)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_comparison

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompareOpContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RmdRulesParser.IDENTIFIER, 0)
        def compOp(self):
            return self.getTypedRuleContext(RmdRulesParser.CompOpContext,0)

        def value(self):
            return self.getTypedRuleContext(RmdRulesParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareOp" ):
                listener.enterCompareOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareOp" ):
                listener.exitCompareOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOp" ):
                return visitor.visitCompareOp(self)
            else:
                return visitor.visitChildren(self)



    def comparison(self):

        localctx = RmdRulesParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comparison)
        try:
            localctx = RmdRulesParser.CompareOpContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(RmdRulesParser.IDENTIFIER)
            self.state = 184
            self.compOp()
            self.state = 185
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RefRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_refRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RefRuleExprContext(RefRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.RefRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REFRULE(self):
            return self.getToken(RmdRulesParser.REFRULE, 0)
        def LPAREN(self):
            return self.getToken(RmdRulesParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(RmdRulesParser.RPAREN, 0)
        def STRING(self):
            return self.getToken(RmdRulesParser.STRING, 0)
        def IDENTIFIER(self):
            return self.getToken(RmdRulesParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefRuleExpr" ):
                listener.enterRefRuleExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefRuleExpr" ):
                listener.exitRefRuleExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefRuleExpr" ):
                return visitor.visitRefRuleExpr(self)
            else:
                return visitor.visitChildren(self)



    def refRule(self):

        localctx = RmdRulesParser.RefRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_refRule)
        self._la = 0 # Token type
        try:
            localctx = RmdRulesParser.RefRuleExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(RmdRulesParser.REFRULE)
            self.state = 188
            self.match(RmdRulesParser.LPAREN)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==26 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 190
            self.match(RmdRulesParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(RmdRulesParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberVal" ):
                listener.enterNumberVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberVal" ):
                listener.exitNumberVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberVal" ):
                return visitor.visitNumberVal(self)
            else:
                return visitor.visitChildren(self)


    class ListValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def listLiteral(self):
            return self.getTypedRuleContext(RmdRulesParser.ListLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListVal" ):
                listener.enterListVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListVal" ):
                listener.exitListVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListVal" ):
                return visitor.visitListVal(self)
            else:
                return visitor.visitChildren(self)


    class RefRuleValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def refRule(self):
            return self.getTypedRuleContext(RmdRulesParser.RefRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefRuleVal" ):
                listener.enterRefRuleVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefRuleVal" ):
                listener.exitRefRuleVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefRuleVal" ):
                return visitor.visitRefRuleVal(self)
            else:
                return visitor.visitChildren(self)


    class StringValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(RmdRulesParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringVal" ):
                listener.enterStringVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringVal" ):
                listener.exitStringVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringVal" ):
                return visitor.visitStringVal(self)
            else:
                return visitor.visitChildren(self)


    class BooleanValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(RmdRulesParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanVal" ):
                listener.enterBooleanVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanVal" ):
                listener.exitBooleanVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanVal" ):
                return visitor.visitBooleanVal(self)
            else:
                return visitor.visitChildren(self)


    class DateValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(RmdRulesParser.DATE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateVal" ):
                listener.enterDateVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateVal" ):
                listener.exitDateVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateVal" ):
                return visitor.visitDateVal(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RmdRulesParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierVal" ):
                listener.enterIdentifierVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierVal" ):
                listener.exitIdentifierVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierVal" ):
                return visitor.visitIdentifierVal(self)
            else:
                return visitor.visitChildren(self)


    class FunctionValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(RmdRulesParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionVal" ):
                listener.enterFunctionVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionVal" ):
                listener.exitFunctionVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionVal" ):
                return visitor.visitFunctionVal(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = RmdRulesParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_value)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = RmdRulesParser.BooleanValContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(RmdRulesParser.BOOLEAN)
                pass

            elif la_ == 2:
                localctx = RmdRulesParser.NumberValContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(RmdRulesParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = RmdRulesParser.StringValContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.match(RmdRulesParser.STRING)
                pass

            elif la_ == 4:
                localctx = RmdRulesParser.DateValContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.match(RmdRulesParser.DATE)
                pass

            elif la_ == 5:
                localctx = RmdRulesParser.ListValContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.listLiteral()
                pass

            elif la_ == 6:
                localctx = RmdRulesParser.IdentifierValContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.match(RmdRulesParser.IDENTIFIER)
                pass

            elif la_ == 7:
                localctx = RmdRulesParser.FunctionValContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 198
                self.functionCall()
                pass

            elif la_ == 8:
                localctx = RmdRulesParser.RefRuleValContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 199
                self.refRule()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RmdRulesParser.RULE_listLiteral

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListLitContext(ListLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RmdRulesParser.ListLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(RmdRulesParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(RmdRulesParser.RBRACK, 0)
        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RmdRulesParser.ValueContext)
            else:
                return self.getTypedRuleContext(RmdRulesParser.ValueContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RmdRulesParser.COMMA)
            else:
                return self.getToken(RmdRulesParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLit" ):
                listener.enterListLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLit" ):
                listener.exitListLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLit" ):
                return visitor.visitListLit(self)
            else:
                return visitor.visitChildren(self)



    def listLiteral(self):

        localctx = RmdRulesParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            localctx = RmdRulesParser.ListLitContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(RmdRulesParser.LBRACK)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4555016192) != 0):
                self.state = 203
                self.value()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==29:
                    self.state = 204
                    self.match(RmdRulesParser.COMMA)
                    self.state = 205
                    self.value()
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 213
            self.match(RmdRulesParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(RmdRulesParser.EQ, 0)

        def NEQ(self):
            return self.getToken(RmdRulesParser.NEQ, 0)

        def GTE(self):
            return self.getToken(RmdRulesParser.GTE, 0)

        def LTE(self):
            return self.getToken(RmdRulesParser.LTE, 0)

        def GT(self):
            return self.getToken(RmdRulesParser.GT, 0)

        def LT(self):
            return self.getToken(RmdRulesParser.LT, 0)

        def IN(self):
            return self.getToken(RmdRulesParser.IN, 0)

        def getRuleIndex(self):
            return RmdRulesParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOp" ):
                return visitor.visitCompOp(self)
            else:
                return visitor.visitChildren(self)




    def compOp(self):

        localctx = RmdRulesParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 517120) != 0)):
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
        self._predicates[12] = self.expr_sempred
        self._predicates[13] = self.term_sempred
        self._predicates[14] = self.arithmeticExpr_sempred
        self._predicates[15] = self.arithmeticTerm_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def arithmeticExpr_sempred(self, localctx:ArithmeticExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def arithmeticTerm_sempred(self, localctx:ArithmeticTermContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




