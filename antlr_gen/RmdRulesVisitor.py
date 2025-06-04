# Generated from RmdRules.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RmdRulesParser import RmdRulesParser
else:
    from RmdRulesParser import RmdRulesParser

# This class defines a complete generic visitor for a parse tree produced by RmdRulesParser.

class RmdRulesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RmdRulesParser#start.
    def visitStart(self, ctx:RmdRulesParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#dslDocument.
    def visitDslDocument(self, ctx:RmdRulesParser.DslDocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#headerRow.
    def visitHeaderRow(self, ctx:RmdRulesParser.HeaderRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#ruleRow.
    def visitRuleRow(self, ctx:RmdRulesParser.RuleRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#context.
    def visitContext(self, ctx:RmdRulesParser.ContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#name.
    def visitName(self, ctx:RmdRulesParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#priority.
    def visitPriority(self, ctx:RmdRulesParser.PriorityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#description.
    def visitDescription(self, ctx:RmdRulesParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#conditions.
    def visitConditions(self, ctx:RmdRulesParser.ConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#actionsHeader.
    def visitActionsHeader(self, ctx:RmdRulesParser.ActionsHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#actionLine.
    def visitActionLine(self, ctx:RmdRulesParser.ActionLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#action.
    def visitAction(self, ctx:RmdRulesParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#singleTerm.
    def visitSingleTerm(self, ctx:RmdRulesParser.SingleTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#orExpr.
    def visitOrExpr(self, ctx:RmdRulesParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#singleFactor.
    def visitSingleFactor(self, ctx:RmdRulesParser.SingleFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#andExpr.
    def visitAndExpr(self, ctx:RmdRulesParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#arithmeticAtom.
    def visitArithmeticAtom(self, ctx:RmdRulesParser.ArithmeticAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#addSub.
    def visitAddSub(self, ctx:RmdRulesParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#arithmeticFactorOnly.
    def visitArithmeticFactorOnly(self, ctx:RmdRulesParser.ArithmeticFactorOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#mulDiv.
    def visitMulDiv(self, ctx:RmdRulesParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#negateExpr.
    def visitNegateExpr(self, ctx:RmdRulesParser.NegateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#embeddedLogic.
    def visitEmbeddedLogic(self, ctx:RmdRulesParser.EmbeddedLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#notExpr.
    def visitNotExpr(self, ctx:RmdRulesParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#parens.
    def visitParens(self, ctx:RmdRulesParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#funcExpr.
    def visitFuncExpr(self, ctx:RmdRulesParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#compare.
    def visitCompare(self, ctx:RmdRulesParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#refExpr.
    def visitRefExpr(self, ctx:RmdRulesParser.RefExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#valueExpr.
    def visitValueExpr(self, ctx:RmdRulesParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#identExpr.
    def visitIdentExpr(self, ctx:RmdRulesParser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#functionExpr.
    def visitFunctionExpr(self, ctx:RmdRulesParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#exprList.
    def visitExprList(self, ctx:RmdRulesParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#compareOp.
    def visitCompareOp(self, ctx:RmdRulesParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#refRuleExpr.
    def visitRefRuleExpr(self, ctx:RmdRulesParser.RefRuleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#BooleanVal.
    def visitBooleanVal(self, ctx:RmdRulesParser.BooleanValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#NumberVal.
    def visitNumberVal(self, ctx:RmdRulesParser.NumberValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#StringVal.
    def visitStringVal(self, ctx:RmdRulesParser.StringValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#DateVal.
    def visitDateVal(self, ctx:RmdRulesParser.DateValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#ListVal.
    def visitListVal(self, ctx:RmdRulesParser.ListValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#IdentifierVal.
    def visitIdentifierVal(self, ctx:RmdRulesParser.IdentifierValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#FunctionVal.
    def visitFunctionVal(self, ctx:RmdRulesParser.FunctionValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#RefRuleVal.
    def visitRefRuleVal(self, ctx:RmdRulesParser.RefRuleValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#listLit.
    def visitListLit(self, ctx:RmdRulesParser.ListLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RmdRulesParser#compOp.
    def visitCompOp(self, ctx:RmdRulesParser.CompOpContext):
        return self.visitChildren(ctx)



del RmdRulesParser