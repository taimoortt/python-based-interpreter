import sys
import ply.lex as lex
import ply.yacc as yacc
import lexer


tokens = lexer.tokens
start = 'stmts'

precedence = (
	('left', 'OR'),
	('left', 'AND'),
	('left', 'EQEQ'),
	('nonassoc', 'LESS', 'GREATER', 'LESSEQ',
	 'GREATEREQ'),  # Nonassociative operators
	('left', 'PLUS', 'MINUS'),
	('right', 'EXPONENT'),
	('left', 'MULTIPLY', 'DIVIDE', 'MOD'),
	('right', 'NOT')
)


def p_stmts(p):
	'''
	stmts : stmt SEMICOLON stmts
	'''
	p[0] = [p[1]] + p[3]


def p_comments(p):
	'''
	stmts : COMMENT
	'''
	return


def p_stmts_terminal(p):
	'''
	stmts :
	'''
	p[0] = []


def p_stmt(p):
	'''
	stmt : expr
			| empty
			| var_dec
			| var_initialize
			| var_assign
			| var_access
			| function_call
			| loop
			| struct_definition
			| struct_attribute_initialize
			| unary_op
	'''
	p[0] = p[1]


def p_struct_definition(p):
	'''
	struct_definition : STRUCT NAME EQUALS LBRACE attribute_dec RBRACE
	'''
	p[0] = ('struct define', p[2], p[5])


def p_multiple_attribute(p):
	'''
	attribute_dec : var_dec SEMICOLON attribute_dec
							  | var_initialize SEMICOLON attribute_dec
	'''
	if(p[3] == None):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]


def p_attribute_dec(p):
	'''
	attribute_dec : var_dec SEMICOLON
							  | var_initialize SEMICOLON
							  | empty
	'''
	if(p[1] != None):
		p[0] = [p[1]]
	else:
		return

# --------------------------------------------------------VAR ACCESS--------------------------------------------------------------------------------------


def p_var_access(p):
	'''
	var_access : NAME
	'''
	p[0] = ('var access', p[1])


def p_var_struct_access(p):
	'''
	struct_access : NAME DOT NAME
	'''
	p[0] = ('struct attribute access', p[1], p[3])

# ------------------------------------------------------VAR ASSIGNMENT--------------------------------------------------------------------------------------


def p_var_assign(p):
	'''
	var_assign : NAME EQUALS expr
	'''
	p[0] = ('var assign', p[1], p[3])

# ------------------------------------------------------VAR DECLARATION-------------------------------------------------------------------------------------


def p_var_dec(p):
	'''
	var_dec : identifier NAME
	'''
	p[0] = ('var dec', p[1], p[2])

# -----------------------------------------------------VAR INITIALIZATION-----------------------------------------------------------------------------------


def p_var_initialize(p):
	'''
	var_initialize : identifier NAME EQUALS expr
					| identifier NAME EQUALS NAME
	'''
	p[0] = ('var initialize', p[1], p[2], p[4])


def p_identifier(p):
	'''
	identifier : INTDEC
					   | DOUBLEDEC
					   | STRINGDEC
					   | BOOLDEC
					   | CHARDEC
					   | NAME
	'''
	p[0] = p[1]
	# The name allows the declaration of Struct objects.While interpreting,
	# check for initial identifiers, if it falls into else,assume a struct object


def p_struct_attribute_initialize(p):
	'''
	struct_attribute_initialize : NAME DOT NAME EQUALS expr
	'''
	p[0] = ('struct attribute initialize', p[1], p[3], p[5])

# ---------------------------------------------------------EXPRESSIONS---------------------------------------------------------------------------------------


def p_nested_expr(p):
	'''
	expr : LPAR expr RPAR
	'''
	p[0] = p[2]


def p_expr_unary_op(p):
	'''
	expr : unary_op
	'''
	p[0] = p[1]


def p_expr_binop(p):
	'''
	expr : expr MULTIPLY expr
					| expr DIVIDE expr
					| expr PLUS expr
					| expr MINUS expr
					| expr MOD expr
					| expr EXPONENT expr
	'''
	p[0] = ('arithmetic_op', p[2], p[1], p[3])


def p_expr_positive_numbers(p):
	'''
	expr : DOUBLE
		 | INT
	'''
	p[0] = ('number', p[1])


def p_expr_negative_numbers(p):
	'''
	expr : MINUS DOUBLE
		| MINUS INT
	'''

	p[0] = ('number', p[2]*-1)


def p_expr_string(p):
	'''
	expr : STRING
	'''
	p[0] = ('string', p[1])


def p_expr_bool(p):
	'''
	expr : TRUE
			 | FALSE
	'''
	p[0] = ('bool', p[1])


def p_expr_var(p):
	'''
	expr : var_access
	'''
	p[0] = p[1]


def p_expr_struct_var(p):
	'''
	expr : struct_access
	'''
	p[0] = p[1]


def p_expr_empty(p):
	'''
	expr : empty
	'''
	return


def p_unary_operation(p):
	'''
	unary_op : var_access INCREMENT
				| var_access DECREMENT
				| struct_access INCREMENT
				| struct_access DECREMENT
	'''
	p[0] = ('unary_op', p[2], p[1])


def p_unary_operation_negative(p):
	'''
	unary_op : MINUS var_access
	'''
	p[0] = ('unary_op', p[1], p[2])


def p_expr_conditional(p):
	'''
	expr : expr conditional_operators expr
	'''
	p[0] = ('conditional_op', p[2], p[1], p[3])


def p_expr_not(p):
	'''
	expr : NOT expr
	'''
	p[0] = ('conditional_op', p[1], p[2])


def p_conditional_operators(p):
	'''
	conditional_operators : EQEQ
		| LESS
		| GREATER
		| AND
		| OR
		| GREATEREQ
		| LESSEQ
		| NOTEQ
	'''
	p[0] = p[1]
# --------------------------------------------------------DO WHILE LOOP---------------------------------------------------------------------------------------


def p_loop(p):
	'''
	loop : DO LBRACE stmts RBRACE WHILE LPAR expr RPAR
	'''
	p[0] = ('loop', p[3], p[7])

# ---------------------------------------------------------PRINTING-----------------------------------------------------------------------------------------


def p_print(p):
	'''
	function_call : PRINT LPAR opt_args RPAR
	'''
	p[0] = ('print', p[3])


def p_optargs(p):
	'''
	opt_args : expr moreargs
	'''
	if(p[2] != None):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[1]


def p_moreargs(p):
	'''
	moreargs : COMMA expr moreargs
	'''
	if p[3] != None:
		p[0] = (p[2] + p[3])
	else:
		p[0] = (p[2])


def p_optargs_empty(p):
	'''
	opt_args : empty
	'''
	return


def p_moreargs_empty(p):
	'''
	moreargs : empty
	'''
	return

# --------------------------------------------------------MISCELLANEOUS-------------------------------------------------------------------------------------


def p_empty(p):
	'''
	empty :
	'''
	pass


def p_error(p):
	if p:
		print("Syntax error at token", p.type)
		sys.exit()
	else:
		pass

