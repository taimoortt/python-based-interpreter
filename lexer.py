import sys
import ply.lex as lex

# -------------------------------------TOKENS---------------------------------------

reserved = {
	'do': 'DO',
	'while': 'WHILE',
	'false' : 'FALSE',
	'true' : 'TRUE',
	'and' : 'AND',
	'or' : 'OR',
	'not' : 'NOT',
	'int' : 'INTDEC',
	'double' : 'DOUBLEDEC',
	'bool' : 'BOOLDEC',
	'string' : 'STRINGDEC',
	'char' : 'CHARDEC',
	'print' : 'PRINT',
	'struct' : 'STRUCT'
}

tokens = [
	'INT', 'DOUBLE', 'STRING', 
	'NAME', 'COMMENT', 'DOT',
	'INCREMENT', 'DECREMENT',  
	'PLUS', 'MINUS', 'DIVIDE', 'MULTIPLY', 'EQUALS', 'MOD','EXPONENT',
	'LESS', 'GREATER','EQEQ', 'GREATEREQ', 'LESSEQ','NOTEQ',
	'LPAR', 'RPAR', 'LBRACE', 'RBRACE',
	'SEMICOLON', 'COMMA'

] + list(reserved.values())

# Declaring Tokens through regular expressions
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_EQEQ = r"\=\="
t_LESS = r'\<'
t_GREATER = r'\>'
t_GREATEREQ = r'\>\='
t_LESSEQ = r'\<\='
t_NOTEQ = r'\!\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EXPONENT = r'\^'
t_EQUALS = r'\='
t_MOD = r'\%'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_STRING = r'\".*?\"'
t_DOT = r'\.'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_ignore = ' \t\v\r'

# We declare empty space as a token and t_ignore will tell PLY to ignore this token
# t is a Python 4-tuple with the following attributes:
# t.type
# t.value
# t.lineno
# t.lexpos --> index of the token relative to the start of input text

# Expressions longer than 1 character in length need to be concatenated and hence are defined through functions

def t_NAME(t):
	# The second character re ensures that a name cannot start with a number
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'NAME')
	return t

def t_COMMENT(t):
	r'\#.*'
	pass

def t_DOUBLE(t):
	r'\d+\.\d+'
	# Any float with any number of integers before and after every decimal
	t.value = float(t.value)
	return t

def t_INT(t):
	r'\d+'  # Any integers of length > 1
	t.value = int(t.value)
	return t

def t_error(t):
	t.lexer.skip(1)
