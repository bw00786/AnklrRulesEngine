# Generated from RmdRules.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RmdRulesParser import RmdRulesParser
else:
    from RmdRulesParser import RmdRulesParser

# This class defines a complete listener for a parse tree produced by RmdRulesParser.
class RmdRulesListener(ParseTreeListener):

    # Enter a parse tree produced by RmdRulesParser#start.
    def enterStart(self, ctx:RmdRulesParser.StartContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#start.
    def exitStart(self, ctx:RmdRulesParser.StartContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#dslDocument.
    def enterDslDocument(self, ctx:RmdRulesParser.DslDocumentContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#dslDocument.
    def exitDslDocument(self, ctx:RmdRulesParser.DslDocumentContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#headerRow.
    def enterHeaderRow(self, ctx:RmdRulesParser.HeaderRowContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#headerRow.
    def exitHeaderRow(self, ctx:RmdRulesParser.HeaderRowContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#ruleRow.
    def enterRuleRow(self, ctx:RmdRulesParser.RuleRowContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#ruleRow.
    def exitRuleRow(self, ctx:RmdRulesParser.RuleRowContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#context.
    def enterContext(self, ctx:RmdRulesParser.ContextContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#context.
    def exitContext(self, ctx:RmdRulesParser.ContextContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#name.
    def enterName(self, ctx:RmdRulesParser.NameContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#name.
    def exitName(self, ctx:RmdRulesParser.NameContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#priority.
    def enterPriority(self, ctx:RmdRulesParser.PriorityContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#priority.
    def exitPriority(self, ctx:RmdRulesParser.PriorityContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#description.
    def enterDescription(self, ctx:RmdRulesParser.DescriptionContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#description.
    def exitDescription(self, ctx:RmdRulesParser.DescriptionContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#conditions.
    def enterConditions(self, ctx:RmdRulesParser.ConditionsContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#conditions.
    def exitConditions(self, ctx:RmdRulesParser.ConditionsContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#actionsHeader.
    def enterActionsHeader(self, ctx:RmdRulesParser.ActionsHeaderContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#actionsHeader.
    def exitActionsHeader(self, ctx:RmdRulesParser.ActionsHeaderContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#actionLine.
    def enterActionLine(self, ctx:RmdRulesParser.ActionLineContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#actionLine.
    def exitActionLine(self, ctx:RmdRulesParser.ActionLineContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#action.
    def enterAction(self, ctx:RmdRulesParser.ActionContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#action.
    def exitAction(self, ctx:RmdRulesParser.ActionContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#singleTerm.
    def enterSingleTerm(self, ctx:RmdRulesParser.SingleTermContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#singleTerm.
    def exitSingleTerm(self, ctx:RmdRulesParser.SingleTermContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#orExpr.
    def enterOrExpr(self, ctx:RmdRulesParser.OrExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#orExpr.
    def exitOrExpr(self, ctx:RmdRulesParser.OrExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#singleFactor.
    def enterSingleFactor(self, ctx:RmdRulesParser.SingleFactorContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#singleFactor.
    def exitSingleFactor(self, ctx:RmdRulesParser.SingleFactorContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#andExpr.
    def enterAndExpr(self, ctx:RmdRulesParser.AndExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#andExpr.
    def exitAndExpr(self, ctx:RmdRulesParser.AndExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#arithmeticAtom.
    def enterArithmeticAtom(self, ctx:RmdRulesParser.ArithmeticAtomContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#arithmeticAtom.
    def exitArithmeticAtom(self, ctx:RmdRulesParser.ArithmeticAtomContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#addSub.
    def enterAddSub(self, ctx:RmdRulesParser.AddSubContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#addSub.
    def exitAddSub(self, ctx:RmdRulesParser.AddSubContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#arithmeticFactorOnly.
    def enterArithmeticFactorOnly(self, ctx:RmdRulesParser.ArithmeticFactorOnlyContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#arithmeticFactorOnly.
    def exitArithmeticFactorOnly(self, ctx:RmdRulesParser.ArithmeticFactorOnlyContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#mulDiv.
    def enterMulDiv(self, ctx:RmdRulesParser.MulDivContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#mulDiv.
    def exitMulDiv(self, ctx:RmdRulesParser.MulDivContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#negateExpr.
    def enterNegateExpr(self, ctx:RmdRulesParser.NegateExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#negateExpr.
    def exitNegateExpr(self, ctx:RmdRulesParser.NegateExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#embeddedLogic.
    def enterEmbeddedLogic(self, ctx:RmdRulesParser.EmbeddedLogicContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#embeddedLogic.
    def exitEmbeddedLogic(self, ctx:RmdRulesParser.EmbeddedLogicContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#notExpr.
    def enterNotExpr(self, ctx:RmdRulesParser.NotExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#notExpr.
    def exitNotExpr(self, ctx:RmdRulesParser.NotExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#parens.
    def enterParens(self, ctx:RmdRulesParser.ParensContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#parens.
    def exitParens(self, ctx:RmdRulesParser.ParensContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#funcExpr.
    def enterFuncExpr(self, ctx:RmdRulesParser.FuncExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#funcExpr.
    def exitFuncExpr(self, ctx:RmdRulesParser.FuncExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#compare.
    def enterCompare(self, ctx:RmdRulesParser.CompareContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#compare.
    def exitCompare(self, ctx:RmdRulesParser.CompareContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#refExpr.
    def enterRefExpr(self, ctx:RmdRulesParser.RefExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#refExpr.
    def exitRefExpr(self, ctx:RmdRulesParser.RefExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#valueExpr.
    def enterValueExpr(self, ctx:RmdRulesParser.ValueExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#valueExpr.
    def exitValueExpr(self, ctx:RmdRulesParser.ValueExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#identExpr.
    def enterIdentExpr(self, ctx:RmdRulesParser.IdentExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#identExpr.
    def exitIdentExpr(self, ctx:RmdRulesParser.IdentExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#functionExpr.
    def enterFunctionExpr(self, ctx:RmdRulesParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#functionExpr.
    def exitFunctionExpr(self, ctx:RmdRulesParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#exprList.
    def enterExprList(self, ctx:RmdRulesParser.ExprListContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#exprList.
    def exitExprList(self, ctx:RmdRulesParser.ExprListContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#compareOp.
    def enterCompareOp(self, ctx:RmdRulesParser.CompareOpContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#compareOp.
    def exitCompareOp(self, ctx:RmdRulesParser.CompareOpContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#refRuleExpr.
    def enterRefRuleExpr(self, ctx:RmdRulesParser.RefRuleExprContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#refRuleExpr.
    def exitRefRuleExpr(self, ctx:RmdRulesParser.RefRuleExprContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#BooleanVal.
    def enterBooleanVal(self, ctx:RmdRulesParser.BooleanValContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#BooleanVal.
    def exitBooleanVal(self, ctx:RmdRulesParser.BooleanValContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#NumberVal.
    def enterNumberVal(self, ctx:RmdRulesParser.NumberValContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#NumberVal.
    def exitNumberVal(self, ctx:RmdRulesParser.NumberValContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#StringVal.
    def enterStringVal(self, ctx:RmdRulesParser.StringValContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#StringVal.
    def exitStringVal(self, ctx:RmdRulesParser.StringValContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#DateVal.
    def enterDateVal(self, ctx:RmdRulesParser.DateValContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#DateVal.
    def exitDateVal(self, ctx:RmdRulesParser.DateValContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#ListVal.
    def enterListVal(self, ctx:RmdRulesParser.ListValContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#ListVal.
    def exitListVal(self, ctx:RmdRulesParser.ListValContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#IdentifierVal.
    def enterIdentifierVal(self, ctx:RmdRulesParser.IdentifierValContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#IdentifierVal.
    def exitIdentifierVal(self, ctx:RmdRulesParser.IdentifierValContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#FunctionVal.
    def enterFunctionVal(self, ctx:RmdRulesParser.FunctionValContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#FunctionVal.
    def exitFunctionVal(self, ctx:RmdRulesParser.FunctionValContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#RefRuleVal.
    def enterRefRuleVal(self, ctx:RmdRulesParser.RefRuleValContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#RefRuleVal.
    def exitRefRuleVal(self, ctx:RmdRulesParser.RefRuleValContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#listLit.
    def enterListLit(self, ctx:RmdRulesParser.ListLitContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#listLit.
    def exitListLit(self, ctx:RmdRulesParser.ListLitContext):
        pass


    # Enter a parse tree produced by RmdRulesParser#compOp.
    def enterCompOp(self, ctx:RmdRulesParser.CompOpContext):
        pass

    # Exit a parse tree produced by RmdRulesParser#compOp.
    def exitCompOp(self, ctx:RmdRulesParser.CompOpContext):
        pass



del RmdRulesParser