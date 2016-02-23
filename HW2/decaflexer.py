import string
import ply.lex as lex


# null

# List of token names.   This is always required
reserved = {
    'boolean' : 'BOOLEAN', 
    'break' : 'BREAK', 
    'continue' : 'CONTINUE', 
    'class' : 'CLASS', 
    'do' : 'DO',
    'else' : 'ELSE',
    'extends' : 'EXTENDS', 
    False : 'FALSE', 
    'float' : 'FLOAT', 
    'for' : 'FOR', 
    'if' : 'IF', 
    'int' : 'INT',
    'new' : 'NEW', 
    None : 'NULL', 
    'private' : 'PRIVATE', 
    'public' : 'PUBLIC', 
    'return' : 'RETURN', 
    'static' : 'STATIC',
    'super' : 'SUPER', 
    'this' : 'THIS', 
    True : 'TRUE', 
    'void' : 'VOID', 
    'while' : 'WHILE',
}

tokens = [
   'INT_CONST', 'FLOAT_CONST', 'STRING_CONST',
   'ASSIGN',
   'PLUS', 'MINUS', 'MULTI', 'DIVIDE', 'INCREMENT', 'DECREMENT',
   'AND', 'OR', 'EQUAL', 'NOTEQUAL', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL',
   'NOT', 
   'LPAREN', 'RPAREN', 'LSQ', 'RSQ', 'LBIG', 'RBIG', 'POINT', 'COMMA',
   'SEMICOLON',
   'ID',
] + list(reserved.values())

# Reserved words
t_BOOLEAN = r'boolean'
t_BREAK = r'break'
t_CONTINUE = r'continue'
t_CLASS = r'class'
t_DO = r'do'
t_ELSE = r'else'
t_EXTENDS = r'extends'
t_FLOAT = r'float'
t_FOR = r'for'
t_IF = r'if'
t_INT = r'(int)'
t_NEW = r'(new)'
t_PRIVATE = r'private'
t_PUBLIC = r'public'
t_RETURN = r'return'
t_STATIC = r'static'
t_SUPER = r'super'
t_THIS = r'this'
t_VOID = r'void'
t_WHILE = r'while'

#precedence of the operators
precedence = (
   ('right', 'ASSIGN'),
   ('left', 'OR'),
   ('left', 'AND'),
   ('nonassoc', 'EQUAL', 'NOTEQUAL'),
   ('nonassoc', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL'),
   ('left', 'PLUS', 'MINUS'),
   ('left', 'MULTI', 'DIVIDE'),
   ('right', 'UMINUS', 'UPLUS', 'NOT', 'INCREMENT', 'DECREMENT'),
)

# Regular expression rules for simple tokens
t_ASSIGN  = r'='

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTI   = r'\*'
t_DIVIDE  = r'/'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'

t_AND = r'&&'
t_OR = r'\|\|'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='

t_NOT = r'!'

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LSQ  = r'\['
t_RSQ  = r'\]'
t_LBIG  = r'\{'
t_RBIG  = r'\}'
t_POINT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'


# A regular expression rule with some action code
def t_INT_CONST(t):
    r'\d+'
    t.value = int(t.value)    
    return t
def t_FLOAT_CONST(t):
    r'\d+.\d+(E[+-]*\d+)*'
    t.value = float(t.value)
    return t
def t_STRING_CONST(t):
    r'(\'.*\'|\".*\")'
    temp = (t.value)
    str = ""
    for i in range(1, len(temp) - 1):
        str += temp[i]
    print str
    t.value = str
# def t_NULL(t):
#     r'null'
#     t.value = int(t.value)
# def t_FALSE(t):
#     r'false'
#     t.value = bool(False)
# def t_TRUE(t):
#     r'true'
#     t.value = bool(True)
    
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t
    
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s' at line %s, the %sth character" %(t.value[0], t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)
