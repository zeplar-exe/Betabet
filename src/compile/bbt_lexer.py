import ply.lex as lex

tokens = [
                                                     # OPERATORS 
'PLUS' ,        # +
'MINUS' ,       # -
'MULTIPLY',     # *
'DIVIDE',       # /
'MODULO',       # %

'NOT',          # !
'EQUALS',       # =

                                                     # COMPARATORS 
'LT',           # <
'GT',           # >
'LTE',          # <=
'GTE',          # >=
'DOUBLEEQUAL',  # ==
'NE',           # !=
'AND',          # &
'OR' ,          # |                                                
                                                      # BRACKETS 

'LPAREN',       # (
'RPAREN',       # )
'LBRACE',       # [
'RBRACE',       # ]
'BLOCKSTART',   # {
'BLOCKEND',     # }
                                                    # DATA TYPES

'INTEGER',      # int
'int',
'FLOAT',       # flt
'float',
'double',
'NORM_STRING',       # nstr
'CHAR_STRING',       # cstr
'string',   
'FUNCTION',       # func
'BOOLEAN',         # bool
'bool',
'boolean',

'COMMENT',  # ##
'MULTILINE_COMMENT_START',   # #_
'MULTILINE_COMMENT_END',   # _#

                                                    # Keywords
'IF',     # if
'ELSE',     # else
'WHILE',     # while
'WHEN',     # when
'IS',     # is
'USE',     # use

                                                    # Misc
'KEY',     # var
'ARGUMENT',     # arg
'COLON',       # :
'COMMA',       # ,

]

# Operators
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_MULTIPLY   = r'\*'
t_DIVIDE  = r'\/'
t_MODULO = r'\%'
t_NOT = r'\!'
t_EQUALS = r'\='

# Brackets
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_BLOCKSTART = r'\{'
t_BLOCKEND = r'\}'

# Comparators
t_GT = r'\>'
t_LT = r'\<'
t_LTE = r'\<\='
t_GTE = r'\>\='
t_DOUBLEEQUAL = r'\=\='
t_NE = r'\!\='
t_AND = r'\&'
t_OR = r'\|'

# Datatypes
t_int = r'int'
t_float = r'float'
t_double = r'double'
t_string = r'string'
t_bool = r'bool'
t_boolean = r'boolean'

t_COMMENT = r'\#\#.*'      
t_MULTILINE_COMMENT_START = r'\#\_ [^\_\#]*'
t_MULTILINE_COMMENT_END = r'\_\#'
t_ignore  = ' \t'

# Keywords
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_WHEN = r'when'
t_IS = r'is'
t_USE = r'use'

# Misc
t_COLON = r':'
t_COMMA = r','

def t_FUNCTION(foo):
    r'(\w+)(?=\s+:)'
    return foo

def t_KEY(foo):
    r'(\w+)(?=\s+=)'
    return foo

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t  

def t_BOOLEAN(t):
    r'(true)|(false)'
    
    if t.value == "true":
        t.value = True
    elif t.value == "false":
        t.value = False

    return t

def t_NORM_STRING(string):
    r'"([^"\n]|(\\"))*"'
    string.value = str(string.value)
    return string

def t_CHAR_STRING(string):
    r"'([^'\n]|(\\'))*'"
    string.value = str(string.value)
    return string

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Unexpected character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

script = '''
bool x = true
autoVariable = 2
'''

lexer.input(script)

# Tokenize
for token in lexer:
    print(token)