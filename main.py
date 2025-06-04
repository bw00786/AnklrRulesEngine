# main.py
import json
import os
from datetime import date
from sqlalchemy import JSON  # Add this import
from sqlalchemy.dialects.postgresql import JSONB  # Optional for PostgreSQL
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Dict, Any
import pandas as pd
import ast
import re
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import logging
import uuid
import time
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Float, Integer, func
from sqlalchemy.types import DateTime
from sqlalchemy.ext.declarative import declarative_base
from fastapi.responses import JSONResponse
from sys import float_info
import logging
import math
import re
import ast
from antlr4 import InputStream, CommonTokenStream
from antlr_gen.RmdRulesParser import RmdRulesParser
from antlr_gen.RmdRulesLexer  import RmdRulesLexer
from antlr_gen.RmdRulesVisitor import RmdRulesVisitor
from antlr4.error.Errors import ParseCancellationException
from antlr4 import RecognitionException
from life_table import get_life_expectancy_factor
from fastapi import HTTPException
from fastapi import APIRouter, UploadFile, File, status
from io import BytesIO
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from llm.dsl_generator import DSLGenerator
from functools import lru_cache
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from sqlalchemy import select
# main.py

# alias the inner contexts
DateValContext = RmdRulesParser.DateValContext
NumberValContext = RmdRulesParser.NumberValContext
StringValContext = RmdRulesParser.StringValContext
BoolValContext = RmdRulesParser.BooleanValContext  # Changed from BoolValContext
ListValContext = RmdRulesParser.ListValContext
IdentifierValContext = RmdRulesParser.IdentifierValContext  # Add if needed

VALID_RULE_FIELDS = {"conditions", "actions", "context", "priority", "active","name","description"} 
DATABASE_URL = "postgresql://user:password@localhost:5433/rules_db"
eengine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=300
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
LLM_ENABLED = os.getenv("LLM_FEATURE_FLAG", "false").lower() == "true"
dsl_generator = DSLGenerator() if LLM_ENABLED else None


def sanitize(value):
    if isinstance(value, str):
        return value.strip()
    return value

def sanitize_dict(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: sanitize(v) for k, v in d.items()}



class RuleCreateDTO(BaseModel):
    name: str
    description: str
    context: str = "RMD_Distribution"
    conditions: str
    actions: List[Dict[str, Any]]
    priority: int = 5
    active: bool = True

class BulkRuleCreate(BaseModel):
    rules: List[RuleCreateDTO]


class AntlrRuleEvaluator:
    def __init__(self, db: Session):
        self.db = db
        self.current_context = None
        self.actions = []
        # Add database reference for visitor access
        self.database = db  # New line
        self.debug_mode = True  # Add debug flag

    def get_active_rules_for_context(db: Session, context: str):
        stmt = (select(Rule)
            .where(Rule.context == context)
            .where(Rule.active == True)
            .order_by(Rule.priority.desc()))
        return db.execute(stmt).scalars().all()

    def evaluate_conditions(self, dsl_text: str, facts: Dict[str, Any]) -> bool:

        if LLM_ENABLED:
            # Add LLM-based validation layer
            validation_prompt = f"Validate this DSL for logical consistency: {dsl_text}"
            validation_result = dsl_generator.validate_llm_dsl_response(validation_prompt)
        
            if "invalid" in validation_result.lower():
                logger.error(f"LLM validation failed because: {validation_result.text}")
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail="LLM validation failed: " + validation_result.text
                )
        try:
            # Normalize facts for evaluation
            normalized_facts = self._normalize_facts(facts)
            
            # Log condition being evaluated with normalized facts when in debug mode
            if self.debug_mode:
                logger.info(f"Evaluating condition: {dsl_text}")
                logger.info(f"With normalized facts: {normalized_facts}")
            
            input_stream = InputStream(dsl_text)
            lexer = RmdRulesLexer(input_stream)
            tokens = CommonTokenStream(lexer)
            parser = RmdRulesParser(tokens)
            tree = parser.expr()
            visitor = AntlrEvaluationVisitor(self, normalized_facts)  # Pass self instead of db
            visitor.current_context = self.current_context
            
            result = visitor.visit(tree)
            
            # Log result when in debug mode
            if self.debug_mode:
                logger.info(f"Condition evaluation result: {result}")
                
            return result
            
        except RecognitionException as e:
            logger.error(f"Syntax error in condition: {dsl_text}")
            logger.error(f"Error details: {e}")
            raise HTTPException(status_code=400, detail=f"Syntax error: {e}")
        
    def _normalize_facts(self, facts: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize facts for consistent rule evaluation"""
        normalized = facts.copy()
        
        # Add additional fact normalization for special fields
        
        # 1. Normalize plan_type to standardized formats
        if "plan_type" in normalized:
           # Get the value before trying to process it
           plan_type = normalized["plan_type"]
           if isinstance(plan_type, str):
               normalized_plan = plan_type.strip().upper().replace(" ", "").replace("-", "")
               normalized["plan_type"] = normalized_plan
               # Create variations
               normalized["PLAN_TYPE"] = normalized_plan
               normalized["Plan_Type"] = normalized_plan
        
        # 2. Add pre-computed conditions for common rule references
        #if "plan_type" in normalized:
         #   plan_type = normalized["plan_type"]
         #   # Add flag for refRule("Plan_Type") which checks plan_type in ["401K","403B","457B"]
       #     normalized["_plan_type_valid"] = plan_type.upper() in ["401K", "403B", "457B"]
        
        # 3. Handle dates and age calculations
        current_year = datetime.now().year
        
        # If dob exists, ensure it's a date object
        if "dob" in normalized and isinstance(normalized["dob"], str):
            try:
                normalized["dob"] = datetime.strptime(normalized["dob"], "%Y-%m-%d").date()
            except ValueError:
                logger.warning(f"Invalid date format for dob: {normalized['dob']}")
        
        return normalized    
       

    def evaluate_rules(self, context: str, facts: Dict[str, Any]):
        self.current_context = context
        self.actions = []  # Reset actions for each evaluation
        
        # Log the context and facts for debugging
        logger.info(f"Evaluating rules for context: {context}")
        logger.info(f"Facts provided: {facts}")
        
        # Get all active rules for the context
        rules = self.db.query(Rule).filter(
            Rule.context == context, 
            Rule.active == True
        ).order_by(Rule.priority.desc()).all()
        
        logger.info(f"Found {len(rules)} active rules for context: {context}")
        
        matched_rules_count = 0
        matched_rule_names = []

        for rule in rules:
            logger.info(f"Evaluating rule: {rule.name}")
            try:
                if self.evaluate_conditions(rule.conditions, facts):
                    matched_rules_count += 1
                    matched_rule_names.append(rule.name)
                    logger.info(f"Rule matched: {rule.name}")
                    logger.info(f"Rule actions: {rule.actions}")

                    # Accumulate processed actions
                    processed_actions = self.process_actions(rule.actions, facts)
                    if processed_actions:
                        self.actions.extend(processed_actions)

                    # Do NOT break — keep evaluating all rules to collect all applicable actions
                else:
                    logger.info(f"Rule did not match: {rule.name} — Conditions: {rule.conditions}")
            except Exception as e:
                logger.error(f"Error evaluating rule {rule.name}: {e}")

        logger.info(f"Successfully evaluated rules for context: {context} | Matched rules: {matched_rule_names}")
        logger.info(f"Actions triggered: {self.actions}")

        return {
            "context": context,
            "matched_rules": matched_rules_count,
            "matched_rule_names": matched_rule_names,
            "actions_triggered": self.actions.copy()  # Return a copy of the list
        }

    def process_actions(self, actions: List[Dict], facts: Dict):
        processed_actions = []
        logger.info(f"Raw actions received: {actions}")

        # Add JSON deserialization if needed
        if isinstance(actions, str):
            try:
               actions = json.loads(actions)
            except json.JSONDecodeError:
                logger.error(f"Invalid JSON in actions: {actions}")
                return []
    
        for action in actions:
            try:
                if isinstance(action, str):  # Handle string-formatted actions
                   action = json.loads(action)
                action_type = action.get('type')
                logger.info(f"Processing action: {action_type}")
                params = action.get('parameters', {})
                if not any(action.get('type') == 'calculate_rmd_amount' for action in actions):
                       return processed_actions
                if action_type == 'calculate_rmd_amount':
                    formula = params.get('formula')
                    metadata = {}
                
                    if formula:
                        try:
                           # Evaluate custom formula
                           rmd_amount = safe_eval_formula(formula, facts)
                           metadata['formula_used'] = formula
                           metadata['calculation_method'] = 'custom_formula'
                        except Exception as e:
                           logger.error(f"Formula evaluation failed: {e}")
                           continue
                    else:
                        # Fallback to standard calculation
                        balance_key = params.get('balance_field', 'prior_year_end_balance')
                        divisor_source = params.get('divisor_source', 'uniform_life_table_factor')
                        balance = facts.get(balance_key, 0.0)
                        divisor = facts.get(divisor_source, 1.0)
                        
                    
                        if divisor <= 0:
                            logger.error("Division by zero in RMD calculation")
                            continue
                    
                        rmd_amount = balance / divisor
                        metadata.update({
                            'formula_used': f"{balance_key}/{divisor_source}",
                            'balance_used': balance,
                            'divisor_used': divisor,
                            'calculation_method': 'standard_division'
                            

                        })

                    processed_actions.append({
                        'type': 'calculate_rmd',
                        'eligible': True,
                        'rmd_status': 'RMD Required',
                        'parameters': {
                           'rmd_amount': round(rmd_amount, 2),
                            **metadata
                        }
                    })
            
                # Handle other action types...
                elif action_type == 'rmd_eligibility':
                   processed_actions.append({
                    'type': 'rmd_eligibility',
                    'eligible_status': params.get('eligible_status', False)
                })
            
            except Exception as e:
               logger.error(f"Action processing failed: {e}")

        return processed_actions
    

class AntlrEvaluationVisitor(RmdRulesVisitor):
    def __init__(self, evaluator: AntlrRuleEvaluator, facts: Dict[str, Any]):
        self.evaluator = evaluator
        self.facts = facts  # Initialize facts properly
        self.current_context = None

    def visitCompareOp(self, ctx):
        field = ctx.IDENTIFIER().getText()
        op = ctx.compOp().getText()
        value = self._parse_value(ctx.value())
    
        # Get fact value first
        fact_value = self.facts.get(field)  # Moved outside conditional
    
        # Only normalize for plan_type comparisons
        if field == 'plan_type':
            # Normalize fact value (already done in facts normalization)
            if isinstance(fact_value, str):
               fact_value = fact_value.upper().replace(" ", "")
        
            # Normalize comparison value
            if isinstance(value, str):
                value = value.upper().replace(" ", "")
            elif isinstance(value, list):
                value = [v.upper().replace(" ", "") for v in value]

        return self._compare(fact_value, op, value)
    
    def _compare(self, left, op, right):
        # Defensive: if either side is None, comparison fails
        if left is None or right is None:
            logger.warning(f"Comparison with None: {op}")
            return False

        # For plan type comparisons, make case-insensitive
        if isinstance(left, str) and isinstance(right, str) and op == '==':
            # For certain field types, use case-insensitive comparison
            if any(kw in str(left).lower() for kw in ["plan", "type", "account"]):
                return left.upper() == right.upper()
        
        # Special handling for 'in' with string lists
        if op == 'in' and isinstance(right, (list, tuple)) and all(isinstance(x, str) for x in right) and isinstance(left, str):
            # For case-insensitive list membership
            return left.upper() in [x.upper() for x in right]

        # --- handle year-only ints against dates ---
        if isinstance(left, date) and isinstance(right, int):
            right = date(right, 1, 1)
        if isinstance(right, date) and isinstance(left, int):
            left = date(left, 1, 1)

        if op == '==':  return left == right
        if op == '!=':  return left != right
        if op == '>':   return left >  right
        if op == '<':   return left <  right
        if op == '>=':  return left >= right
        if op == '<=':  return left <= right
        if op == 'in':  return left in right
        return False
    
    def visitFunctionExpr(self, ctx):
        # function name:
        fname = ctx.IDENTIFIER().getText()
        # evaluate all arguments:
        args = [ self.visit(expr) for expr in ctx.exprList().expr() ] if ctx.exprList() else []
        if fname == "lifeExpectancyFactor":
            # assume single‐arg age
            return get_life_expectancy_factor(args[0])
        # add more built‐ins here
        raise ValueError(f"Unknown function: {fname}")
    

    def visitAndExpr(self, ctx):
       left = self.visit(ctx.term())
       right = self.visit(ctx.arithmeticExpr())
       return left and right
    
    def visitListLit(self, ctx):
        """Parse list literals like ["401K", "403B"] into Python lists."""
        return [self.visit(v) for v in ctx.value()]



    def visitOrExpr(self, ctx):
       left = self.visit(ctx.expr())
       right = self.visit(ctx.term())
       return left or right


    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def _parse_value(self, value_ctx):
        # Handle boolean values
        if hasattr(value_ctx, 'BOOLEAN') and value_ctx.BOOLEAN():
           return value_ctx.BOOLEAN().getText().lower() == 'true'

        # Handle numeric values
        if hasattr(value_ctx, 'NUMBER') and value_ctx.NUMBER():
            num_str = value_ctx.NUMBER().getText()
            return float(num_str) if '.' in num_str else int(num_str)

        # Handle string values (including dates)
        if hasattr(value_ctx, 'STRING') and value_ctx.STRING():
            str_val = value_ctx.STRING().getText().strip('"').strip("'")
            # Date parsing for YYYY-MM-DD format
            if re.fullmatch(r'\d{4}-\d{2}-\d{2}', str_val):
                try:
                   return datetime.strptime(str_val, "%Y-%m-%d").date()
                except ValueError:
                    pass
            return str_val

        # Handle explicit date tokens (if your grammar has them)
        if hasattr(value_ctx, 'DATE') and value_ctx.DATE():
            date_str = value_ctx.DATE().getText().strip('"').strip("'")
            try:
                return datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                return date_str  # Fallback to string

        # Handle lists
        if hasattr(value_ctx, 'listLiteral') and value_ctx.listLiteral():
           return [
                self._parse_value(item) 
                for item in value_ctx.listLiteral().value()
            ]

        # Handle identifiers (fact references)
        if hasattr(value_ctx, 'IDENTIFIER') and value_ctx.IDENTIFIER():
           return self.facts.get(value_ctx.IDENTIFIER().getText())

        # Handle nested expressions
        return self.visit(value_ctx)


        

    def _compare(self, left, op, right):
       # Defensive: if either side is None, comparison fails
        if left is None or right is None:
          logger.warning(f"Comparison with None: {op}")
          return False

        # --- handle year-only ints against dates ---
        if isinstance(left, date) and isinstance(right, int):
           right = date(right, 1, 1)
        if isinstance(right, date) and isinstance(left, int):
            left = date(left, 1, 1)

        if op == '==':  return left == right
        if op == '!=':  return left != right
        if op == '>':   return left >  right
        if op == '<':   return left <  right
        if op == '>=':  return left >= right
        if op == '<=':  return left <= right
        if op == 'in':  return left in right
        if op == 'in' and isinstance(right, (list, tuple, set)):
           # Check if comparing plan_type against valid types
           if isinstance(left, str) and left.lower() == 'plan_type':
              right = [x.upper() for x in right]
              left_val = self.facts.get('plan_type', '').upper()
              return left_val in right
        return False

    
    def visitNotExpr(self, ctx):
        # ctx.factor() is the child expression after ‘not’
        return not self.visit(ctx.factor())
    
    def visitBoolVal(self, ctx: BoolValContext):
        return ctx.BOOLEAN().getText() == 'true'

    # If your factor alternative was labeled `#refExpr`:
    def visitRefExpr(self, ctx):
        # just delegate into the inner refRule node
        return self.visit(ctx.refRule())
    
     # 2) refRule → 'refRule' LPAREN (STRING|IDENTIFIER) RPAREN  (#refRuleExpr)
    # In AntlrEvaluationVisitor class
    def visitRefRuleExpr(self, ctx):
        """Enhanced rule reference handling with better logging"""
        if ctx.STRING():
            rule_name = ctx.STRING().getText()[1:-1]  # Remove quotes
        else:
            rule_name = ctx.IDENTIFIER().getText()
        
        logger.info(f"Attempting to reference rule: '{rule_name}'")
        
        # Access database through evaluator
        rule = self.evaluator.database.query(Rule).filter(
            Rule.name == rule_name,
            Rule.context == self.evaluator.current_context,
            Rule.active == True
        ).first()
        
        if not rule:
            logger.warning(f"Referenced rule '{rule_name}' not found in context '{self.evaluator.current_context}'")
            return False
        
        # Use evaluator's condition evaluation
        result = self.evaluator.evaluate_conditions(rule.conditions, self.facts)
        logger.info(f"Referenced rule '{rule_name}' evaluated to: {result}")
        return result

class MyRulesVisitor(RmdRulesVisitor):
    def visitProgram(self, ctx):
        # Assuming 'program' is your top rule
        print("Visiting program")
        return self.visitChildren(ctx)

    def visitRuleDefinition(self, ctx):
        # Example if you have a rule like: ruleDefinition: 'RULE' ID '{' ... '}'
        rule_name = ctx.ID().getText()
        print(f"Evaluating rule: {rule_name}")
        # Add evaluation logic here
        return True

def evaluate_rules(rule_text: str):
    input_stream = InputStream(rule_text)
    lexer = RmdRulesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RmdRulesParser(token_stream)

    tree = parser.program()  # Adjust to match your top-level rule
    visitor = MyRulesVisitor()
    return visitor.visit(tree)

class ConditionsToJsonVisitor(RmdRulesVisitor):
    def visitOrExpr(self, ctx):
        left  = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        # flatten if needed
        return {"or": left["or"] + right["or"]} if "or" in left else {"or":[left,right]}

    def visitAndExpr(self, ctx):
        left  = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        return left and right

    def visitCompareOp(self, ctx):
        field = ctx.IDENTIFIER().getText()
        op = ctx.compOp().getText()
        value = self._parse_value(ctx.value())

        # Normalize plan_type comparisons
        if field == 'plan_type':
           # Normalize fact value (already done in facts normalization)
           fact_value = self.facts.get(field)
        
           # Normalize comparison value
           if isinstance(value, str):
               value = value.upper().replace(" ", "").replace("-", "")
           elif isinstance(value, list):
               value = [v.upper().replace(" ", "").replace("-", "") 
                    if isinstance(v, str) else v 
                    for v in value]

        return self._compare(fact_value, op, value)


    

    # Example fix for list parsing in DSL
    def visitListVal(self, ctx):
        return [self.visit(v) for v in ctx.value()]

    def visitRefRuleExpr(self, ctx):
        name = ctx.STRING().getText()[1:-1]
        return self.evaluator.evaluate_conditions(rule.conditions, self.facts)

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitSingleTerm(self, ctx):
        return self.visit(ctx.term())

    def visitSingleFactor(self, ctx):
        return self.visit(ctx.factor())
    
    def visitIdExpr(self, ctx):
       # treat bare identifier as boolean lookup
       return bool(self.facts.get(ctx.IDENTIFIER().getText(), False))
 

def parse_conditions_antlr(dsl_text: str) -> dict:
    stream = InputStream(dsl_text)
    lexer  = RmdRulesLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = RmdRulesParser(tokens)
    tree   = parser.start()
    visitor = ConditionsToJsonVisitor()
    return visitor.visit(tree)

# In main.py's validate_dsl function
def validate_dsl(conditions: str):
    """Validate just the conditions portion"""
    try:
        stream = InputStream(conditions)
        lexer = RmdRulesLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = RmdRulesParser(tokens)
        parser.expr()  # Validate only the expression
    except Exception as e:
        logger.error(f"Invalid conditions syntax: {str(e)}")
        raise HTTPException(
            status_code=422,
            detail=f"Invalid conditions syntax: {str(e)}"
        )

def extract_conditions(dsl: str) -> str:
    """Extract just the conditions portion from DSL table"""
    lines = dsl.split('\n')
    for line in lines:
        if 'conditions' in line.lower():
            # Find the conditions column
            parts = [p.strip() for p in line.split('    ') if p.strip()]
            if len(parts) >= 5:  # Assuming conditions is 5th column
                return parts[4]
    raise ValueError("No conditions found in DSL")


# Database Models
class Rule(Base):
    __tablename__ = "rules2056"

    id = Column(Integer, primary_key=True, index=True)
    context = Column(String, index=True)
    name = Column(String)
    description = Column(String)
    conditions = Column(Text)  # <-- now stores DSL string
    actions = Column(JSON)
    priority = Column(Integer)
    active = Column(Boolean, default=True)
    full_dsl = Column(Text)  # Optional: for debugging purposes

class UploadReport(Base):
    __tablename__ = "upload_reports2056"
    id = Column(String(36), primary_key=True)
    filename = Column(String(255))
    status = Column(String(20))
    context = Column(String(50))
    processing_time = Column(Float, nullable=True)
    success_rate = Column(Float, nullable=True)
    total_rules = Column(Integer)
    successful_uploads = Column(Integer)
    failed_uploads = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
)

class EvaluateRequest(BaseModel):
    context: str
    facts: Dict[str, Any]

class EvaluateResponse(BaseModel):
    eligible: bool
    rmd_status: str
    annual_rmd_amount: float = None
    calculation_details: dict = None
    rules_matched: int
    raw_response: dict

# Pydantic Models
class EvaluationRequest(BaseModel):
    context: str
    facts: Dict[str, Any]

class RuleCreate(BaseModel):
    context: str
    name: str
    priority: int
    description: str
    conditions: str
    actions: str

class RuleResponse(BaseModel):
    id: int
    context: str
    name: str
    priority: int
    description: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DSL Parser

class RuleEvaluator:

    def __init__(self, db: Session):
        self.db = db
        self.actions = []
        self.current_context = None  # if you need it in refRule()
    def safe_eval(self, expr: str, facts: Dict[str, Any]) -> Any:
        """
        Safely evaluate boolean expressions with these features:
        - Converts date strings to date objects
        - Handles numeric types safely
        - Prevents code injection
        - Supports basic comparison operations
        """
        
        # Clean and preprocess the expression
        expr = self._preprocess_expression(expr)
        
        # Convert date strings in facts to date objects
        sanitized_facts = self._sanitize_facts(facts)
        
        try:
            # Validate expression syntax first
            self._validate_expression_syntax(expr)
            
            # Create safe evaluation environment
            safe_env = {
                'date': date,
                'datetime': datetime,
                'true': True,
                'false': False,
                'null': None,
                **{k: v for k, v in sanitized_facts.items() if not callable(v)}
            }
            
            # Parse and validate allowed nodes
            self._check_allowed_nodes(ast.parse(expr, mode='eval'))
            
            return eval(
                expr,
                {"__builtins__": {}},
                safe_env
            )
        except Exception as e:
            logging.error(f"Evaluation failed for '{expr}': {str(e)}")
            return False
        
    # Add caching decorator
    @lru_cache(maxsize=1000)
    def get_parse_tree(dsl_text: str):
       input_stream = InputStream(dsl_text)
       lexer = RmdRulesLexer(input_stream)
       tokens = CommonTokenStream(lexer)
       parser = RmdRulesParser(tokens)
       return parser.expr()
    

    def _preprocess_expression(self, expr: str) -> str:
        """Fix common syntax issues before evaluation"""
        # Remove leading zeros from numbers
        expr = re.sub(r'\b0+(\d+)\b', r'\1', expr)
        # Convert common boolean strings
        expr = expr.replace('&&', 'and').replace('||', 'or')
        # Add spaces around operators for better parsing
        expr = re.sub(r'(?<![=!<>])(==|!=|>=|<=|>|<)', r' \1 ', expr)
        return expr.strip()

    def _sanitize_facts(self, facts: Dict) -> Dict:
        """Convert fact values to proper types"""
        sanitized = {}
        date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        
        for key, value in facts.items():
            if isinstance(value, str):
                # Convert date strings
                if date_pattern.match(value):
                    try:
                        sanitized[key] = datetime.strptime(value, "%Y-%m-%d").date()
                    except ValueError:
                        sanitized[key] = value
                else:
                    sanitized[key] = value
            else:
                sanitized[key] = value
        return sanitized

    def _validate_expression_syntax(self, expr: str):
        """Check for potentially dangerous syntax"""
        forbidden_patterns = [
            r'import\s+',
            r'__.*__',
            r'lambda\s+',
            r';',
            r'\{|\}'
        ]
        
        for pattern in forbidden_patterns:
            if re.search(pattern, expr):
                raise ValueError(f"Potentially dangerous pattern detected: {pattern}")

    def _check_allowed_nodes(self, node):
        """Recursively check AST for allowed nodes only"""
        allowed_nodes = {
            ast.Expression, ast.Call, ast.Name, ast.Load,
            ast.BinOp, ast.UnaryOp, ast.Compare, ast.BoolOp,
            ast.Num, ast.Str, ast.List, ast.Tuple, ast.Dict,
            ast.Attribute, ast.Subscript, ast.Index, ast.Constant,
            ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE,
            ast.And, ast.Or, ast.Not, ast.Add, ast.Sub, ast.Mult,
            ast.Div, ast.Mod, ast.Pow, ast.USub, ast.UAdd
        }
        
        for child in ast.iter_child_nodes(node):
            if type(child) not in allowed_nodes:
                raise ValueError(f"Disallowed AST node: {type(child).__name__}")
            self._check_allowed_nodes(child)


    def evaluate_conditions(self, conditions: Any, facts: Dict[str, Any]) -> bool:
        """
        Top‑level entry to evaluate parsed conditions JSON.
        """
        if isinstance(conditions, dict):
            if 'and' in conditions:
                return all(self.evaluate_conditions(c, facts) for c in conditions['and'])
            if 'or' in conditions:
                return any(self.evaluate_conditions(c, facts) for c in conditions['or'])
            if 'refRule' in conditions:
                return self.evaluate_ref_rule(conditions['refRule'], facts)
            # single‐field comparison
            return self._evaluate_expression(
                field=list(conditions.keys())[0],
                expr=list(conditions.values())[0],
                facts=facts
            )
        raise ValueError(f"Unexpected conditions type: {type(conditions)}")

    

    def evaluate_rules(self, context: str, facts: Dict[str, Any]) -> List[Dict]:
        self.current_context = context
        rules = (
            self.db.query(Rule)
            .filter(Rule.context == context, Rule.active == True)
            .order_by(Rule.priority.desc())
            .all()
        )

        for rule in rules:
            if self.evaluate_conditions(rule.conditions, facts):
                self.process_actions(rule.actions, facts)
                break
        return self.actions
    
    def _evaluate_expression(self, field: str, expr: Dict, facts: Dict) -> bool:
        op = expr['operator']
        value = expr['value']
        fv    = facts.get(field)
     
        # --- NEW: normalize date‐string facts when comparing to a date value ---
        if isinstance(value, date) and isinstance(fv, str):
            try:
                fv = datetime.strptime(fv, "%Y-%m-%d").date()
            except ValueError:
                pass
        
        # Handle dynamic values from facts
        if isinstance(value, dict):
            if 'use_fact' in value:
                value = facts.get(value['use_fact'], None)
            elif 'use_function' in value:
                return self._handle_function(value, facts)
        
        fact_value = facts.get(field, None)
        
        # Type conversions for dates
        if isinstance(value, str) and re.match(r'\d{4}-\d{2}-\d{2}', value):
            value = datetime.strptime(value, "%Y-%m-%d").date()
            # now convert fv if also a string
            if isinstance(fv, str) and re.match(r'^\d{4}-\d{2}-\d{2}$', fv):
                fv = datetime.strptime(fv, "%Y-%m-%d").date()
                ##fact_value = datetime.strptime(fact_value, "%Y-%m-%d").date() if isinstance(fact_value, str) else fact_value

        # Operator comparisons
        if op == 'in':
            # only do membership if RHS is a list/tuple/set
            if isinstance(value, (list, tuple, set)):
                return fv in value
            # fallback: treat `in` as exact match
            return fv == value
        
    

        try:
            return {
            '==':  fv == value,
            '!=':  fv != value,
            '>=':  fv >= value,
            '<=':  fv <= value,
            '>':   fv >  value,
            '<':   fv <  value,
        }[op]
        except KeyError:
            raise ValueError(f"Unsupported operator: {op}")
        
    def evaluate_ref_rule(self, rule_name: str, facts: Dict[str, Any]) -> bool:
        """
        Lookup another rule by name, evaluate it recursively.
        """
        # make sure any recursive call knows this context
        rule = (
            self.db.query(Rule)
            .filter(Rule.context == self.current_context, Rule.name == rule_name)
            .first()
        )
        if not rule:
            return False
        return self.evaluate_conditions(rule.conditions, facts)


# Add these new parser methods

def parse_conditions(condition_str: str) -> dict:
    """
    Convert a DSL condition string into a nested JSON structure:
      - supports top‑level “and” / “or” (even inside parentheses)
      - comparison operators: ==, !=, >=, <=, >, <, and = (alias for ==)
      - “in” operator with Python list syntax
      - refRule(ruleName) with or without quotes
    """
    def strip_parens(s: str) -> str:
        s = s.strip()
        # peel off one pair of outer parentheses if they wrap the entire expr
        if s.startswith("(") and s.endswith(")"):
            # make sure they match top‑level
            depth = 0
            for i, ch in enumerate(s):
                if ch == "(": depth += 1
                elif ch == ")": depth -= 1
                if depth == 0 and i < len(s) - 1:
                    break
            else:
                return strip_parens(s[1:-1])
        return s

    def split_top_level(expr: str, sep: str) -> list[str]:
        parts, buf, depth = [], [], 0
        i = 0
        while i < len(expr):
            # detect exact sep at top‑level
            if depth == 0 and expr[i:].startswith(sep):
                parts.append("".join(buf).strip())
                buf, i = [], i + len(sep)
                continue
            c = expr[i]
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
            buf.append(c)
            i += 1
        parts.append("".join(buf).strip())
        return parts

    expr = strip_parens(condition_str)

    # OR first
    or_parts = split_top_level(expr, " or ")
    if len(or_parts) > 1:
        return {"or": [parse_conditions(p) for p in or_parts]}

    # THEN AND
    and_parts = split_top_level(expr, " and ")
    if len(and_parts) > 1:
        return {"and": [parse_conditions(p) for p in and_parts]}

    atom = expr

    # refRule(…)
    m = re.fullmatch(r"refRule\(\s*['\"]?([^'\"]+)['\"]?\s*\)", atom)
    if m:
        return {"refRule": m.group(1)}

    # “in” operator
    in_parts = split_top_level(atom, " in ")
    if len(in_parts) == 2:
        field, raw_list = in_parts
        raw_list = raw_list.strip()
        try:
            # use literal_eval to parse the Python list syntax
            val_list = ast.literal_eval(raw_list)
        except Exception:
            # fallback to comma‑split
            val_list = [v.strip().strip("'\"") for v in raw_list.strip("[] ").split(",")]
        return {
            field.strip(): {
                "operator": "in",
                "value": val_list
            }
        }

    # comparison operators (>=, <=, ==, !=, >, <, or single “=”)
    comp_re = r"(.+?)\s*(>=|<=|==|!=|=|>|<)\s*(.+)"
    m = re.fullmatch(comp_re, atom)
    if m:
        field, op, raw_val = m.groups()
        if op == "=":
            op = "=="   # alias
        val = raw_val.strip()
        # strip quotes for strings
        if val.startswith(("'", '"')) and val.endswith(("'", '"')):
            val = val[1:-1]
        else:
            # try numeric
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass
        return {
            field.strip(): {
                "operator": op,
                "value": val
            }
        }

    raise ValueError(f"Unsupported condition format: {condition_str}")

import re
import ast

def parse_actions(action_str: str) -> list:
    """
    Convert DSL like:
      "set type to calculate_rmd; set rmd_type to \"initial\"; set balance_field to prior_year_end_balance; set divisor_source to uniform_life_table_factor"
    into:
      [{
        "type": "calculate_rmd",
        "parameters": {
          "rmd_type": "initial",
          "balance_field": "prior_year_end_balance",
          "divisor_source": "uniform_life_table_factor"
        }
      }]
    """
    actions = []
    current = None

    # split on semicolon, ignore empty parts
    for part in [p.strip() for p in action_str.split(";") if p.strip()]:
        m = re.fullmatch(r"set\s+type\s+to\s+['\"]?([^'\"]+)['\"]?", part, re.IGNORECASE)
        if m:
            # start a brand‑new action
            if current:
                actions.append(current)
            current = { "type": m.group(1), "parameters": {} }
            continue

        # must have an open action
        if current is None:
            raise ValueError(f"Action missing type before: {part}")

        # other parameters: set <key> to <value>
        m = re.fullmatch(r"set\s+(\w+)\s+to\s+(.+)", part, re.IGNORECASE)
        if not m:
            raise ValueError(f"Unrecognized action syntax: {part}")

        key, raw_val = m.group(1), m.group(2).strip()
        # strip quotes
        if raw_val.startswith(("'", '"')) and raw_val.endswith(("'", '"')):
            val = raw_val[1:-1]
        else:
            # booleans
            if raw_val.lower() in ("true", "false"):
                val = raw_val.lower() == "true"
            else:
                # numeric?
                try:
                    if "." in raw_val:
                        val = float(raw_val)
                    else:
                        val = int(raw_val)
                except ValueError:
                    val = raw_val

        current["parameters"][key] = val

    # push the last action
    if current:
        actions.append(current)

    return actions



# Update your upload_rules endpoint




@app.post("/upload_rules/")
async def upload_rules(file: UploadFile = File(...), db: Session = Depends(get_db)):
    report_id = str(uuid.uuid4())
    start_time = time.time()
    
    try:
        content = await file.read()
        df = pd.read_excel(content)
        success_count = 0
        error_count = 0
        errors = []

        # Validate required columns
        required_columns = ['context', 'name', 'priority', 'description', 'conditions', 'actions']
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(400, detail=f"Missing required columns: {required_columns}")
        
        # Process rules
        for index, row in df.iterrows():
            try:
                # Convert DSL to structured JSON
                row_data = sanitize_dict(dict(row))  # Assuming `row` is a pandas Series or dict
                
                filtered_data = {k: v for k, v in row_data.items() if k in VALID_RULE_FIELDS}
                actions = parse_actions(str(row['actions']))
                rule = Rule(
                    context=filtered_data.get("context"),
                    name=filtered_data.get("name"),
                    priority=int(filtered_data.get("priority", 0)),
                    description=filtered_data.get("description"),
                    conditions=filtered_data["conditions"],
                    actions=actions
                )
               

                db.add(rule)
                success_count += 1
            except Exception as e:
                error_count += 1
                logger.exception(f"Error processing row {index+1}")
                errors.append({
                    "row": index+1,
                    "error": str(e),
                    "data": {
                        "conditions": row.get('conditions'),
                        "actions": row.get('actions')
                    }
                })
                logger.error(f"Error in upload {e}")
                logger.error("f {errors}")

        # Commit transaction
        db.commit()

        # Calculate metrics
        total = success_count + error_count
        processing_time = round(time.time() - start_time, 2)
        success_rate = round((success_count / total) * 100, 2) if total > 0 else 0.0
        if not math.isfinite(processing_time):
           processing_time = 0.0
        if not math.isfinite(success_rate):
           success_rate = 0.0

        # Ensure valid float values
        if not math.isfinite(success_rate):
            success_rate = 0.0

        # Create report
        report = UploadReport(
            id=report_id,
            filename=file.filename,
            status="success",
            context="RMD_Distribution",
            processing_time=processing_time,
            success_rate=success_rate,
            total_rules=total,
            successful_uploads=success_count,
            failed_uploads=error_count
        )
        logger.info(f"Returning upload report: processing_time={processing_time!r}, success_rate={success_rate!r}")

        db.add(report)
        db.commit()
        
        for err in errors:
            a = err["data"]["actions"]
            if isinstance(a, float) and not math.isfinite(a):
               err["data"]["actions"] = None  # or str(a)

        return JSONResponse({
            "status": "success",
            "report_id": report_id,
            "successful_uploads": success_count,
            "failed_uploads": error_count,
            "errors": errors
        })

    except Exception as e:
        db.rollback()
        error_report_id = str(uuid.uuid4())
        
        # Handle float values in error response
        try:
            processing_time = round(time.time() - start_time, 2)
        except:
            processing_time = 0.0

        error_report = UploadReport(
            id=error_report_id,
            filename=file.filename,
            status="error",
            context="RMD_Distribution",
            processing_time=processing_time,
            success_rate=0.0,
            total_rules=0,
            successful_uploads=0,
            failed_uploads=0
        )
        
        try:
            db.add(error_report)
            db.commit()
        except Exception as db_error:
            db.rollback()

        return JSONResponse(
            status_code=500,
            content={
                "detail": str(e).replace("'", ""),  # Sanitize response
                "report_id": error_report_id,
                "original_report_id": report_id
            }
        )
      
        

# Add this to the top of your evaluate_rules endpoint
@app.post("/evaluate_rules/", response_model=EvaluateResponse)
@cache(expire=300)  # Cache results for 5 minutes
async def evaluate_rules(
     request: EvaluationRequest,
     db: Session = Depends(get_db)
):
    # Preprocess facts
    processed_facts = preprocess_facts(request.facts)
     
    logger.info(f"Processing evaluation request for context: {request.context}")
    logger.info(f"Original facts: {request.facts}")
    logger.info(f"Processed facts: {processed_facts}")
     
    evaluator = AntlrRuleEvaluator(db)
 
    try: 
        result = evaluator.evaluate_rules(request.context, processed_facts)
        logger.info(f"Raw evaluation result: {result}")

        # Build the richer response
        matched = result["matched_rule_names"]
        resp = {
            "eligible": False,
            "rmd_status": "Not Required",
            "rules_matched": result["matched_rules"],
            "raw_response": result
        }

        # If our uniform‑lifetime calculation rule fired, compute the RMD
        if "Execute_Uniform_Life_Calculation" in matched:
            bal = processed_facts.get("prior_year_end_balance", 0)
            div = processed_facts.get("uniform_life_table_factor", 1)
            annual_amt = round(bal / div, 2) if div else 0.0
            resp.update({
                "eligible": True,
                "rmd_status": "RMD Required",
                "annual_rmd_amount": annual_amt,
                "calculation_details": {
                    "balance_used": bal,
                    "divisor_used": div,
                    "calculation_method": "Uniform Lifetime Table"
                }
            })

        return JSONResponse(jsonable_encoder(resp))
 
    except (ParseCancellationException, RecognitionException, SyntaxError) as e:
         logger.warning(f"Rule syntax error for context {request.context}: {e}")

# Add this preprocessing function to handle common fact issues
def preprocess_facts(facts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Preprocess facts to handle common issues:
    1. Case normalization for plan types
    2. Default values for commonly required fields
    3. Type coercion for common fields
    """
    processed = facts.copy()
    if 'current_year' not in facts:
        facts['current_year'] = datetime.now().year
        return facts
    # 1. Normalize plan_type case
    #if "plan_type" in processed:
     #   # Convert to uppercase and remove any spaces or dashes
     #   processed["plan_type"] = processed["plan_type"].upper().replace(" ", "").replace("-", "")
    
    # 2. Add alias for plan_type to match refRule("Plan_Type")
    if "plan_type" in processed and isinstance(processed["plan_type"], str):
        pt = processed["plan_type"].upper().replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
        processed["plan_type"] = pt
        # also add alias if any rules reference PLAN_TYPE
        processed["PLAN_TYPE"] = pt
        
    # 3. Default values for commonly required fields (if not present)
    defaults = {
        "dob": "1950-01-01",                    # Default DOB for testing
        "account_type": "Traditional",          # Default account type
        "marital_status": "Single",             # Default marital status
        "participant_status": "Active",         # Default participant status
        "beneficiary": "None",                  # Default beneficiary
        "beneficiary_allocation": 0,            # Default allocation
        "ownership_percentage": 0,              # Default ownership
        "missed_rmd": False,                    # Default missed RMD
        "prev_count_balance": 0,                # Default previous balance
        "tax_withholding_eligible": True,       # Default tax withholding
        "rmd_amount": 0                         # Default RMD amount
    }
    
    # Only add defaults if not already present
    for key, value in defaults.items():
        if key not in processed:
            processed[key] = value

           
    
    # 4. Calculate other derived values used in rules
    if "participant_age" in processed and "dob" not in processed:
        # Generate a DOB based on the participant age
        current_year = datetime.now().year
        birth_year = current_year - int(processed["participant_age"])
        processed["dob"] = f"{birth_year}-01-01"
    
    return processed

# Also update the AntlrEvaluationVisitor._compare method to handle case insensitive string comparisons
def _compare(self, left, op, right):
    # Defensive: if either side is None, comparison fails
    if left is None or right is None:
        logger.warning(f"Comparison with None: {op}")
        return False

    # Handle case insensitive string comparisons for common fields
    if isinstance(left, str) and isinstance(right, str):
        # For plan types and similar fields, do case-insensitive comparison
        if op == '==' and (
            "plan" in str(left).lower() or 
            "type" in str(left).lower() or
            "account" in str(left).lower()
        ):
            return left.upper() == right.upper()
        # For 'in' operations with strings
        if op == 'in' and isinstance(right, (list, tuple)) and all(isinstance(x, str) for x in right):
            return left.upper() in [x.upper() for x in right]

    # --- handle year-only ints against dates ---
    if isinstance(left, date) and isinstance(right, int):
        right = date(right, 1, 1)
    if isinstance(right, date) and isinstance(left, int):
        left = date(left, 1, 1)

    if op == '==':  return left == right
    if op == '!=':  return left != right
    if op == '>':   return left > right
    if op == '<':   return left < right
    if op == '>=':  return left >= right
    if op == '<=':  return left <= right
    if op == 'in':  
        # If right is a list of strings, do case insensitive comparison
        if isinstance(right, (list, tuple)) and all(isinstance(x, str) for x in right) and isinstance(left, str):
            return left.upper() in [x.upper() for x in right]
        return left in right
    return False


@app.get("/upload_report/{report_id}")
def get_upload_report(report_id: str, db: Session = Depends(get_db)):
    report = db.query(UploadReport).filter(UploadReport.id == report_id).first()
    if not report:
        raise HTTPException(404, detail="Report not found")
    return report

@app.post("/rules/")
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    new_rule = Rule(
        context=rule.context,
        conditions=rule.conditions,  # <-- this is now DSL
        actions=json.loads(rule.actions),
        priority=rule.priority,
        active=True,
    )
    db.add(new_rule)
    db.commit()
    return {"status": "success", "id": new_rule.id}



# Add new endpoint
@app.post("/submit_rule/")
async def submit_rule(
    
    description: str = Form(...),
    context: str = Form(...),
    priority: int = Form(...),
    natural_language: str = Form(None),
    file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    logger.info("Processing LLM rules")
    if LLM_ENABLED:
        if not natural_language:
            logger.error("Natural language input required when LLM feature is enabled")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                
                detail="Natural language input required when LLM feature is enabled"
            )
            
        # Generate DSL from LLM
        try:
            generated = dsl_generator.generate_dsl(natural_language)
            logger.info(f"DSL after execution is {generated}")
            logger.info(f"Extracted conditions: {generated['conditions']}")  # Add this line
            # Validate generated DSL
            logger.info("validating dsl")
            validate_dsl(generated["conditions"])  # Now validates the actual expression
        except Exception as e:
            logger.error(f"LLM generated invalid DSL: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"LLM generated invalid DSL: {str(e)}"
            )
            
        # Create rule from generated DSL
        rule = Rule(
            context=context,
            name=f"Generated Rule - {description}",
            description=description,
            conditions=generated["conditions"],  # Store just conditions
            actions=json.dumps(generated["actions"]),  # Store actions as JSON
            priority=priority,
            active=True,
            full_dsl=generated["full_dsl"]  # Optional: store full DSL
        )
    else:
        # Existing Excel processing
        if not file:
            logger.error("Excel file required when LLM feature is disabled")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Excel file required when LLM feature is disabled"
            )
            
        # Existing Excel processing logic...
    
    db.add(rule)
    db.commit()
    
    return {"status": "success", "rule_id": rule.id}

@app.get("/feature-flags")
def get_feature_flags():
    return {
        "llmEnabled": LLM_ENABLED,
        "excelFallback": not LLM_ENABLED
    }

@app.post("/rules/bulk")
async def create_rules_bulk(rules: BulkRuleCreate, db: Session = Depends(get_db)):
    try:
        db_rules = []
        for rule in rules.rules:
            db_rule = Rule(
                name=rule.name,
                description=rule.description,
                context=rule.context,
                conditions=rule.conditions,
                actions=json.dumps(rule.actions),
                priority=rule.priority,
                active=rule.active
            )
            db.add(db_rule)
            db_rules.append(db_rule)
        
        db.commit()
        return {"created": len(db_rules), "errors": []}
    except Exception as e:
        db.rollback()
        raise HTTPException(400, detail=str(e))



