grammar RmdRules;

options { language = Python3; }

//----------------------------------------------------------------
// Parser Rules
//----------------------------------------------------------------

start
    : expr EOF
    ;

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

AND        : 'and' ;
OR         : 'or' ;
NOT        : 'not' ;
IN         : 'in' ;
REFRULE    : 'refRule' ;

EQ         : '==' ;
NEQ        : '!=' ;
GTE        : '>=' ;
LTE        : '<=' ;
GT         : '>' ;
LT         : '<' ;

BOOLEAN    : 'true' | 'false' ;

DATE       : [0-9]{4} '-' [0-9]{2} '-' [0-9]{2} ;
NUMBER     : '-'? [0-9]+ ('.' [0-9]+)? ;

fragment ESC : '\\' [btnfr"'\\] ;
STRING
    : '"' (ESC | ~["\\])* '"'
    | '\'' (ESC | ~['\\])* '\''
    ;

LBRACK     : '[' ;
RBRACK     : ']' ;
COMMA      : ',' ;
LPAREN     : '(' ;
RPAREN     : ')' ;

IDENTIFIER : [a-zA-Z_] [a-zA-Z0-9_]* ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
WS           : [ \t\r\n]+ -> skip ;
