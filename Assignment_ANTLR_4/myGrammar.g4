grammar myGrammar;

// TOKENS 
// strings not handled, while skipped
// couldn't handle Python indent and dedent
// Assignment submitted by: Ali Ahsan(18100071) and Muhammad Zain Qasmi(18100276)

IF : 'if';
ELSE : 'else';
ELIF : 'elif';
IN : 'in';
AS : 'as';
FOR : 'for';
WHILE : 'while';
ANDAND : '&&';
COMMA : ',';
COLON : ':';
DEF : 'def';
RET : 'return';
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
NOT : 'not';
PLUS : '+';
MINUS :  '-';
MULTIPLY : '*';
DIVIDE : '/';
MOD : '%';
POWER : '^';
GT : '>';
GE : '>=';
LT : '<';
LE : '<=';
ASSIGNMENT : '=';
EQUAL : '==';
NOTEQUAL : '!=';
TRUE : 'true';
FALSE : 'false'; 

LENGTH : 'len';
PRINT : 'print';
APPEND : 'append';
OPEN : 'open';

PLUSEQUAL : '+=';
MINUSEQUAL : '-=';
MULTEQUAL : '*=';
DIVEQUAL : '/=';

OR : 'or';
AND : 'and';

ID : [a-zA-Z_][a-zA-Z_0-9]* ; 
NUMBER : [0-9]+;
NEWLINE : '\n';
WS : [ \t\r\n]+ -> skip ;
COMMENT : '#' ;


INDENT : '\t';


// define lists, tuples and dictionaries?

lists : '[' expression? (',' expression)* ']' ;

// define string





// Parser



boolean : TRUE | FALSE ;


// for loop
forRule : FOR ID IN forconstruct ':';
forconstruct : ID | 'range(len(' ID '):' | 'range(' NUMBER ')';


// if construct
ifRule : IF ID comp_oper expression ':' |  ELSE ':' | ELIF ID comp_oper expression;


// Function grammar
functionDef : DEF ID '(' parameters* '):';   // block yet to be defined
parameters : ID (',' ID)* ;


// comparison operators 
comparison : expression comp_oper expression | '(' comparison ')' ;
comp_oper : GT | GE | LT | LE | EQUAL | NOTEQUAL ;


// main rule and basic operations
rules : statement+ EOF;   // initial rule

expression : '(' expression ')' | expression POWER expression | expression (MULTIPLY|DIVIDE) expression | expression (PLUS|MINUS) expression | lists | NUMBER | ID | functionDef | forRule | ifRule ;   // the last one is epsilon

statement :  ID '=' expression NEWLINE | expression NEWLINE | expression| functionDef| NEWLINE;