from antlr4 import InputStream, CommonTokenStream
from antlr_gen.RmdRulesLexer  import RmdRulesLexer
from antlr_gen.RmdRulesParser import RmdRulesParser
from main import AntlrEvaluationVisitor

# alias the inner context classes
DateValContext   = RmdRulesParser.DateValContext
NumberValContext = RmdRulesParser.NumberValContext
StringValContext = RmdRulesParser.StringValContext
BoolValContext   = RmdRulesParser.BoolValContext
ListValContext   = RmdRulesParser.ListValContext
NotExprContext   = RmdRulesParser.NotExprContext

expr = 'not (age > 73 and refRule("RMD_Required"))'
input_stream = InputStream(expr)
lexer = RmdRulesLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = RmdRulesParser(tokens)
tree = parser.expr()
visitor = AntlrEvaluationVisitor({'age': 75, 'RMD_Required': True})
print(visitor.visit(tree))  # should print False

