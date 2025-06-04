grammar RmdRules;

options { language = Python3; }

//----------------------------------------------------------------
// Parser Rules
//----------------------------------------------------------------

start
    : dslDocument EOF
    ;

dslDocument
    : headerRow ruleRow+
    ;

headerRow
    : SECTION_HEADER (TAB SECTION_HEADER)+ NEWLINE
    ;

ruleRow
    : context TAB name TAB priority TAB description TAB conditions TAB actionsHeader NEWLINE
      actionLine+
    ;

context: IDENTIFIER;
name: IDENTIFIER;
priority: NUMBER;
description: STRING;
conditions: expr;
actionsHeader: SECTION_HEADER; // "actions" header
actionLine: TAB action NEWLINE;

action
    : 'set' IDENTIFIER 'to' value
    ;

// Expression parsing rules
expr
    : expr OR term             # orExpr
    | term                     # singleTerm
    ;

term
    : term AND arithmeticExpr  # andExpr
    | arithmeticExpr           # singleFactor
    ;

arithmeticExpr
    : arithmeticExpr op=('+'|'-') arithmeticTerm  # addSub
    | arithmeticTerm                              # arithmeticAtom
    ;

arithmeticTerm
    : arithmeticTerm op=('*'|'/') arithmeticFactor # mulDiv
    | arithmeticFactor                             # arithmeticFactorOnly
    ;

arithmeticFactor
    : '-' arithmeticFactor        # negateExpr
    | factor                      # embeddedLogic
    ;

factor
    : NOT factor                 # notExpr
    | LPAREN expr RPAREN         # parens
    | functionCall               # funcExpr
    | comparison                 # compare
    | refRule                    # refExpr
    | value                      # valueExpr
    | IDENTIFIER                 # identExpr
    ;

functionCall
    : IDENTIFIER LPAREN exprList? RPAREN  # functionExpr
    ;

exprList
    : expr (COMMA expr)*
    ;

comparison
    : IDENTIFIER compOp value   # compareOp
    ;

refRule
    : REFRULE LPAREN (STRING | IDENTIFIER) RPAREN   # refRuleExpr
    ;

value
    : BOOLEAN       # BooleanVal
    | NUMBER        # NumberVal
    | STRING        # StringVal
    | DATE          # DateVal
    | listLiteral   # ListVal
    | IDENTIFIER    # IdentifierVal
    | functionCall  # FunctionVal
    | refRule       # RefRuleVal
    ;

listLiteral
    : LBRACK (value (COMMA value)*)? RBRACK  # listLit
    ;

compOp
    : EQ
    | NEQ
    | GTE
    | LTE
    | GT
    | LT
    | IN
    ;

//----------------------------------------------------------------
// Lexer Rules
//----------------------------------------------------------------

SECTION_HEADER: ('context' | 'name' | 'priority' | 'description' | 'conditions' | 'actions');

AND: 'and';
OR: 'or';
NOT: 'not';
IN: 'in';
REFRULE: 'refRule';
SET: 'set';

EQ: '==';
NEQ: '!=';
GTE: '>=';
LTE: '<=';
GT: '>';
LT: '<';
SEMI: ';';
TAB: '    ' -> channel(HIDDEN);
NEWLINE: '\r'?'\n';
WS: [ \t]+ -> channel(HIDDEN);

BOOLEAN: 'true' | 'false';

DATE: [0-9][0-9][0-9][0-9]'-'[0-9][0-9]'-'[0-9][0-9];
NUMBER: '-'?[0-9]+('.'[0-9]+)?;

STRING
    : '"' ('\\"'|.)*? '"'
    | '\'' ('\\\''|.)*? '\''
    ;

LBRACK: '[';
RBRACK: ']';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

LINE_COMMENT: '//' ~[\r\n]* -> skip;