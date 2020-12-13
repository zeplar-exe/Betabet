import ply.lex as lex

tokens = [
                                                     # OPERATORS #
'PLUS' ,        # +
'MINUS' ,       # -
'MULTIPLY',     # *
'DIVIDE',       # /
'MODULO',       # %

'NOT',          # !
'EQUALS',       # =

                                                     # COMPARATORS #
'LT',           # <
'GT',           # >
'LTE',          # <=
'GTE',          # >=
'DOUBLEEQUAL',  # ==
'NE',           # !=
'AND',          # &
'OR' ,          # |                                                
                                                      # BRACKETS #

'LPAREN',       # (
'RPAREN',       # )
'LBRACE',       # [
'RBRACE',       # ]
'BLOCKSTART',   # {
'BLOCKEND',     # }
                                                    # DATA TYPES#

'INTEGER',      # int
'FLOAT',       # flt
'STRING',       # str
'FUNCTION',       # func

'COMMENT',  # ##
'MULTILINE_COMMENT_START',   # #_
'MULTILINE_COMMENT_END',   # _#

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
t_COMMENT = r'\#\#.*'      
t_MULTILINE_COMMENT_START = r'\#\_ [^\_\#]*'
t_MULTILINE_COMMENT_END = r'\_\#'
t_ignore  = ' \t'

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t  

def t_STRING(t):
    r'"([^"\n]|(\\"))*"$'
    t.value = str(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Unexpected character '%s'" % t.value[0])
    t.lexer.skip(1)

reserved_keys = {
    # Keywords
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'when' : 'WHEN',
    'is' : 'IS',
    'use' : 'USE',

    # Datatypes
    'int' : "INT",
    'char' : "CHAR",
    'string' : "STRING",
    'double' : "DOUBLE",
    'float' : "FLOAT",
}

tokens.append('ID')
tokens += list(reserved_keys)

lexer = lex.lex()

data = '''
[25/(3*40) + {300-20} -16.5]
{(300-250)<(400-500)}
20 & 30 | 50
5 + 90
## This is a single-line comment
#_ This is a multi-line comment 
boi 
im so smart lol
hehe
dumb
_#
"This is a double-quote string"
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
for token in lexer:
    print(token)
