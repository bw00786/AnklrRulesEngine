import pytest
from datetime import date
from antlr4 import InputStream, CommonTokenStream
from antlr_gen.RmdRulesLexer import RmdRulesLexer
from antlr_gen.RmdRulesParser import RmdRulesParser
from main import AntlrEvaluationVisitor


def evaluate(expr: str, facts: dict) -> bool:
    """
    Helper to parse and evaluate a DSL expression.
    """
    input_stream = InputStream(expr)
    lexer = RmdRulesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RmdRulesParser(token_stream)
    tree = parser.expr()
    visitor = AntlrEvaluationVisitor(facts)
    return visitor.visit(tree)


# --- Test cases for comparison operators ---

def test_greater_than_true():
    assert evaluate("age > 65", {"age": 70}) is True


def test_greater_than_false():
    assert evaluate("age > 65", {"age": 60}) is False


def test_less_equal_true():
    assert evaluate("balance <= 1000", {"balance": 1000}) is True


def test_equal_string_true():
    assert evaluate("status == \"active\"", {"status": "active"}) is True


def test_not_equal_string_false():
    assert evaluate("type != \"initial\"", {"type": "initial"}) is False


# --- Test cases for 'in' operator and list literal ---

def test_in_operator_true():
    assert evaluate("status in [\"active\", \"pending\"]", {"status": "pending"}) is True


def test_in_operator_false():
    assert evaluate("status in ['active','pending']", {"status": "closed"}) is False


# --- Test boolean literals ---

def test_boolean_true():
    assert evaluate("flag == true", {"flag": True}) is True


def test_boolean_false():
    assert evaluate("flag == false", {"flag": False}) is True


# --- Test logical operators: and, or, not ---

def test_and_or_not_combination():
    expr = 'not (age > 73 and refRule("eligible")) or status == \'active\''
    facts = {"age": 75, "eligible": True, "status": "active"}
    # age > 73 and eligible => True; not True => False; status == 'active' => True; False or True => True
    assert evaluate(expr, facts) is True


# --- Test date comparisons using date objects ---

def test_date_greater():
    # Provide fact as date object, not string
    expr = "startDate > 2025-01-01"
    facts = {"startDate": date(2025, 2, 15)}
    assert evaluate(expr, facts) is True


def test_date_less_false():
    expr = "endDate < 2024-12-31"
    facts = {"endDate": date(2025, 1, 1)}
    assert evaluate(expr, facts) is False


# --- Test nested parentheses with explicit comparison ---

def test_nested_parens():
    expr = '(a == 1 or b == 2) and not (c == true)'
    facts = {"a": 1, "b": 3, "c": False}
    # (True or False) and not (False) => True and True => True
    assert evaluate(expr, facts) is True
