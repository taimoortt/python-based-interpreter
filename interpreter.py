import sys
import ply.lex as lex
import ply.yacc as yacc
import copy
import parser
import lexer

general_scope_variables, struct_definitions, struct_objects = {}, {}, {} # Basic dictionaries to keep track of the variable environment seperateley for structs and simple variables
parent_env = [] # A dictionary of all the environment dcitionaries
parent_env.append(general_scope_variables)
identifiers = ['int', 'char', 'string', 'bool', 'double']


'''
Execute recives a list of commands i.e. multiple commands sperated by a semi colon and passes them to the run function one by one to execute them
'''
def execute(command_list):
	for command in command_list:
		run(command, general_scope_variables)

'''
Run function recives one command at a time. It determines the type of command based on the value at the 0th index in the tuple or the root of the tree.
Then it handles the functionality(tree) of that command accordingly in individual if-else blocks
'''
def run(tree, variables):
	# print('TREE: ', tree)
	op_type = tree[0]

	if(op_type == 'unary_op'):
		unary_op = tree[1]
		var_name = tree[2][1]
		var_info = access_variable(var_name, variables)
		var_type = var_info[0]
		if(var_type == 'int' or var_type == 'double'):
			var_value = var_info[1]
			if(unary_op == '++'):
				var_value += 1
				var_info[1] = var_value
				variables[var_name] = var_info
			elif(unary_op == '--'):
				var_value -= 1
				var_info[1] = var_value
				variables[var_name] = var_info
			elif(unary_op == '-'):
				var_value = -1 * var_value
				return var_value
		else:
			print("Unary operators cannot be applied on non-numerical objects")
			sys.exit()

	elif(op_type == 'arithmetic_op'):
		bin_op = tree[1]
		left_child = tree[2]
		right_child = tree[3]
		left_child = run(left_child, variables)
		right_child = run(right_child, variables)
		if(bin_op == '+'):
			return left_child + right_child
		elif(bin_op == '-'):
			return left_child - right_child
		elif(bin_op == '*'):
			return left_child * right_child
		elif(bin_op == '/'):
			return left_child / right_child
		elif(bin_op == '%'):
			return left_child % right_child
		elif(bin_op == '^'):
			return left_child ** right_child

	elif(op_type == 'conditional_op'):
		conditional_op = tree[1]
		if(conditional_op == 'not'):
			var_value = run(tree[2],variables)
			if(var_value == 'false'):
				var_value = False
			elif(var_value == 'true'):
				var_value = True
			return not(bool(var_value))

		left_child = tree[2]
		right_child = tree[3]
		left_child = run(left_child,variables)
		right_child = run(right_child,variables)

		if(conditional_op == 'and'):
			return bool(left_child and right_child)

		elif(conditional_op == 'or'):
			return bool(left_child or right_child)

		elif(conditional_op == '>='):
			if(left_child >= right_child):
				return True
			else:
				return False

		elif(conditional_op == '<='):
			if(left_child <= right_child):
				return True
			else:
				return False

		elif(conditional_op == '=='):
			if(left_child == right_child):
				return True
			else:
				return False

		elif(conditional_op == '>'):
			if(left_child > right_child):
				return True
			else:
				return False

		elif(conditional_op == '<'):
			if(left_child < right_child):
				return True
			else:
				return False

		elif(conditional_op == '!='):
			if(left_child != right_child):
				return True
			else:
				return False

	elif(op_type == 'number'):
		return tree[1]

	elif(op_type == 'string'):
		string = tree[1].replace('"', '')
		return string

	elif(op_type == 'char'):
		char = tree[1].replace('"', '')
		char = char[0]
		return char

	elif(op_type == 'bool'):
		if(tree[1] == 'true'):
			return True
		else:
			return False

	elif(op_type == 'print'):
		args = list(tree[1])
		printer(args, variables)

	elif(op_type == 'var access'):
		var_value = access_variable(tree[1], variables)
		if(var_value != None):
			var_value = var_value[1]
		return var_value

	elif(op_type == 'var dec'):
		declare_variable(tree[1], tree[2], variables)

	elif(op_type == 'var initialize'):
		done = initialize_variable(tree[1], tree[2], tree[3], variables)
		return done

	elif(op_type == 'var assign'):
		assign_variable(tree[1], tree[2], variables)

	elif(op_type == 'struct define'):
		struct_name = tree[1]
		attributes = tree[2]
		for declaration in attributes:
			define_struct(struct_name, declaration)

	elif(op_type == 'struct attribute initialize'):
		struct_name = tree[1]
		struct_attribute = tree[2]
		expression_to_assign = tree[3]
		initialize_struct_attribute(
			struct_name, struct_attribute, expression_to_assign, variables)

	elif (op_type == 'struct attribute access'):
		struct_name = tree[1]
		struct_attribute = tree[2]
		return access_struct_attribute(struct_name, struct_attribute)

	elif(op_type == 'loop'):
		operations = tree[1]
		condition = tree[2]
		handle_loop(operations, condition)


'''
Handle Loop is a function dedicated to the handling of the scope management of loops and to run the commands continuously until the conditon becomes false.
'''
def handle_loop(operations, condition):

	while(run(condition, parent_env[-1])):
		parent_env.append({})
		for command in operations:
			run(command, parent_env[-1])
		parent_env.pop()

'''
Access Struct Attributes checks if the struct has been defined and if the called upon instance of that struct has been declared. If yes, it allows us to access
the individual attributes of the struct.
'''

def access_struct_attribute(obj_name, attribute):
	if (obj_name in struct_objects.keys()):
		obj_info = struct_objects[obj_name]
		for defined_attributes in obj_info:
			if(list(defined_attributes.keys())[0] == attribute):
				x = defined_attributes[attribute]
				if(type(x) == type('a')):
					if(x in identifiers):
						print('ERROR!!! No value has been assigned to object', obj_name, 'attribute', attribute)
						sys.exit()
				return defined_attributes[attribute]

		print("ERROR!!! No attribute named", attribute, 'exists in object', obj_name)
		sys.exit()
	else:
		print("ERROR!!! No object named", obj_name, "exists")
		sys.exit()


'''
Initialize Struct Attirubute helps us to assign a value to each of the attricutes of a struct object once it has been delcared
'''

def initialize_struct_attribute(struct_name, attribute, expr, env):
	if(struct_name in struct_objects.keys()):
		value = run(expr, env)
		value_type = str(type(value))
		if(value_type == "<class 'str'>"):
			val_type = 'string'
		elif(value_type == "<class 'float'>"):
			val_type = 'double'
		elif(value_type == "<class 'int'>"):
			val_type = 'int'
		elif(value_type == "<class 'bool'>"):
			val_type = 'bool'
		error = True
		struct_info_list = struct_objects[struct_name]
		for kv_pairs in struct_info_list:
			if(list(kv_pairs.keys())[0] == attribute):
				var_type = kv_pairs[attribute]
				if(var_type == val_type):
					kv_pairs[attribute] = value
					struct_objects[struct_name] = struct_info_list
					error = False
				elif(type(value) == type(var_type)):
					kv_pairs[attribute] = value
					struct_objects[struct_name] = struct_info_list
					error = False
				if(error):
					print("ERROR!!! Incorrect variable type being assigned to struct attribute:", attribute)
					print(value_type, 'being assigned to a variable of', type(var_type))
					sys.exit()
				return
		print('No attribute called', attribute, 'in object', struct_name)
		sys.exit()
	else:
		print('ERROR!!! Object', struct_name, 'does not exist')
		sys.exit()


'''
Define struct takes in all the attributes of a newly defined struct and stores them in a dictionary to keep record of the struct which has been defined
'''

def define_struct(struct_name, declaration):

	if(struct_name in struct_definitions.keys()):
		current_variable_list = struct_definitions[struct_name]
		var_type = declaration[1]
		var_name = declaration[2]
		var_info = {var_name: var_type}
		current_variable_list.append(var_info)
		struct_definitions.update({struct_name: current_variable_list})
	else:
		var_type = declaration[1]
		var_name = declaration[2]
		var_info = {var_name: var_type}
		struct_definitions.update({struct_name: [var_info]})

'''
Assign variable analyzes the tree which has been passed, and based on what type of value is being assigned, it enters and if-else branch.
It also checks whether the value being assigned is correct or not i.e int not being assigned to a string.
If a variable is being assigned to another variable, it checks whether that variable has already been defined or not. i.e. if a = b; checks if a and b already defined
'''

def assign_variable(name, value, variables):
	value = list(value)
	if(name in variables.keys()):
		variable_info = variables[name]
		variable_id = variable_info[0]

		if(value[0] == 'number'):
			if(variable_id == 'int'):
				variable_info = [variable_id, int(value[1])]
				variables[name] = variable_info
			elif(variable_id == 'double'):
				variable_info = [variable_id, float(value[1])]
				variables[name] = variable_info
			else:
				print('ERROR!!! Cannot assign a',
					  value[0], 'value to a', variable_id, 'variable')
			sys.exit()

		elif(value[0] == 'string'):
			if(variable_id == 'string'):
				variable_info = [variable_id, str(value[1])]
				variables[name] = variable_info
			elif(variable_id == 'char'):
				variable_info = [variable_id, str(value[1][1])]
				variables[name] = variable_info

			else:
				print('ERROR!!! Cannot assign a',
					  value[0], 'value to a', variable_id, 'variable')
				sys.exit()

		elif(value[0] == 'bool'):
			if(variable_id == 'bool'):
				if(value[1] == 'true'):
					value[1] = True
				else:
					value[1] = False
				variable_info = [variable_id, value[1]]
				variables[name] = variable_info
			else:
				print('ERROR!!! Cannot assign a',
					  value[0], 'value to a', variable_id, 'variable')
				sys.exit()

		elif(value[0] == 'var access'):
			var_value = access_variable(value[1], variables)
			var_type = var_value[0]
			var_value = var_value[1]
			current_variable_info = variables[name]
			current_id = current_variable_info[0]
			if(var_type == current_id):
				if(current_id == 'string'):
					var_info = [var_type, str(var_value)]
				elif(current_id == 'char'):
					var_info = [var_type, str(var_value)]
				elif(current_id == 'int'):
					var_info = [var_type, int(var_value)]
				elif(current_id == 'double'):
					var_info = [var_type, float(var_value)]
				elif(current_id == 'bool'):
					if(var_value=='true'):
						var_value = True
					else:
						var_value = False
					var_info = [var_type, var_value]

				variables[name] = var_info
			else:
				print('ERROR!!! Cannot assign a', var_type,
					  'variable to a', current_id, 'object')
				sys.exit()

		elif(value[0] == 'struct attribute access'):
			struct_val = access_struct_attribute(value[1], value[2])
			val_type = str(type(struct_val))
			val_type = val_type[8:-2]
			if(val_type == 'float'):
				val_type = 'double'
			if(val_type == 'str'):
				val_type = 'string'
			if(val_type == variable_id):
				variables[name] = struct_val
			else:
				print("ERROR!!! Cannot assign a", val_type,
					  "value to a ", variable_id, "object")
				sys.exit()

		elif(value[0] == 'arithmetic_op'):
			x = run(value,variables)
			if(variable_id == 'int'):
				try:
					x = int(x)
				except:
					print("Invalid Operation")
					sys.exit()
			elif(variable_id == 'double'):
				try:
					x = float(x)
				except:
					print("Invalid Operation")
					sys.exit()
			elif(variable_id == 'string'):
				x = str(x)
			product = [variable_id, x]
			variables[name] = product

		elif(value[0] == 'unary_op'):
			if(value[1] == '-'):
				var_info = access_variable(value[2][1], variables)
				var_val = var_info[1]
				var_val = -1*var_val
				new_info = [var_info[1], var_val]
			variables[name] = new_info

	else:
		print('ERROR!!! Undeclared variable', name)
		sys.exit()

'''
Initialize Variable initializes a variable which was previously only declared but not given an exact value
It checks whether a variable by that name has been defined. And whether the value it is being initialized with is correct or not
'''

def initialize_variable(identifier, name, value, variables):
	if(identifier not in identifiers):
		print('Object class', identifier, 'not defined')
	if(name not in variables.keys()):
		value = list(value)
		if(value[0] == 'arithmetic_op'):
			x = run(value,variables)
			if(identifier == 'int'):
				try:
					x = int(x)
					value = ['int', x]
				except:
					print("Invalid Operation")
					sys.exit()
			elif(identifier == 'double'):
				try:
					x = float(x)
					value = ['double', x]
				except:
					print("Invalid Operation")
					sys.exit()
			elif(identifier == 'string'):
				x = str(x)
				value = ['string', x]
			variables.update({name: value})

		elif(value[0] == 'unary_op'):
			if(value[1] == '-'):
				var_info = access_variable(value[2][1],variables)
				var_val = var_info[1]
				var_val = -1*var_val
				new_info = [var_info[0], var_val]
			variables[name] = new_info

		elif(value[0] == 'var access'):
			var_value = access_variable(value[1],variables)
			if(var_value == None):
				return False
			var_type = var_value[0]
			var_value = var_value[1]

			if(var_type == identifier):
				if(identifier == 'string'):
					var_info = [var_type, str(var_value)]
				elif(identifier == 'int'):
					var_info = [var_type, int(var_value)]
				elif(identifier == 'double'):
					var_info = [var_type, float(var_value)]
				elif(identifier == 'bool'):
					if(var_value == 'false'):
						var_info = [var_type, False]
					else:
						var_info = [var_type, True]
					
				variables[name] = var_info
			else:
				print('ERROR!!! Cannot assign a', var_type,
					  'variable to a', identifier, 'object')
				sys.exit()

		elif(value[0] == 'struct attribute access'):
			value_of_struct = access_struct_attribute(value[1], value[2])
			val_type = str(type(value_of_struct))
			val_type = val_type[8:-2]
			if(val_type == 'float'):
				val_type = 'double'
			if(val_type == 'str'):
				val_type = 'string'
			if(val_type == identifier):
				variables[name] = [str(val_type), value_of_struct]
			else:
				print("ERROR!!! Cannot assign a", val_type,
					  "value to a ", identifier, "object")
				sys.exit()
				# return False
			# print(variables)

		elif(identifier == 'int'):
			if(value[0] == 'number'):
				value[0] = 'int'
				variables.update({name: value})
			else:
				print('ERROR!!! Cannot assign a non integer value to an integer object')
				sys.exit()
				# return False

		elif (identifier == 'double'):
			if(value[0] == 'number'):
				value[0] = 'double'
				variables.update({name: value})
			else:
				print('ERROR!!! Cannot assign a non double value to a double object')
				sys.exit()
				# return False

		elif(identifier == 'string'):
			if(value[0] == 'string'):
				value[1] = value[1].replace('"', '')
				variables.update({name: value})
			else:
				print('ERROR!!! Cannot assign a non string value to a string object')
				sys.exit()
				# return False

		elif(identifier == 'bool'):
			if(value[0] == 'bool'):
				if(value[1]=='false'):
					value[1] = False
				else:
					value[1] = True
				variables.update({name: value})
			else:
				print('Invalid arguments passed for bool object')
				sys.exit()
				# return False

		elif(identifier == 'char'):
			if(value[0] == 'string'):
				value[0] = 'char'
				value[1] = value[1].replace('"', '')
				value[1] = value[1][0]
				variables.update({name: value})
			else:
				print('ERROR!!! Cannot assign a non string value to a string object')
				sys.exit()
				return False

		return True
	else:
		print('RedeclarationError. Variable', name, 'already defined')
		sys.exit()
		# return False


'''
Declares a variable of the said type and appends it to our variable environment after assigning it default values.
'''

def declare_variable(identifier, name, variables):
	if(name not in variables.keys() or struct_objects.keys()):
		if(identifier == 'int'):
			variables.update({name: ['int', None]})

		elif (identifier == 'double'):
			variables.update({name: ['double', None]})

		elif(identifier == 'string'):
			variables.update({name: ['string', None]})

		elif(identifier == 'bool'):
			variables.update({name: ['bool', None]})

		elif(identifier == 'char'):
			variables.update({name: ['char', None]})

		elif(identifier in struct_definitions.keys()):
			attributes = copy.deepcopy(struct_definitions[identifier])
			struct_objects.update({name: attributes})

		else:
			print('ERROR!!! No object class', identifier, 'defined')
			sys.exit()

	else:
		print("ERROR!!! Object", name, "already exists")
		sys.exit()

'''
Following two functions access the variable from the environement(based on scope) we are currently in and returns the value if it exists. Else gives an error
'''

def access_variable(name, variables):
	if(name in variables.keys()):
		return variables[name]
	else:
		return find_in_scope(name, variables)

def find_in_scope(variable, env):
	counter = 0
	counter = len(parent_env)-1

	while(counter>=0):
		if(variable in parent_env[counter].keys()):
			return parent_env[counter][variable]
		else:
			counter-=1
	if(counter < 0):
		print('ERROR!!! Variable', variable, 'has not been defined')
		sys.exit()
		# return None

'''
Based on the command, does certain string manipulation to print the given arguments. Sets the end flag to tab instead of default newline to allow for comma
seperated values to be printed in the same line
'''
def printer(args, variables):
	number_of_args = len(args)
	i = 0

	while(i < number_of_args):
		var_type = args[i]
		var = args[i+1]
		if(var_type == 'string'):
			var = var.replace('"', '')
			print(var, end=" ")
		elif(var_type == 'char'):
			var = var.replace('"', '')
			print(var, end=" ")
		elif(var_type == 'number'):
			if(var == int(var)):
				print(int(var), " ", end=(' '))
			else:
				print(var, end = ' ')
		elif(var_type == 'bool'):
			print(var, end=" ")
		elif(var_type == 'var access'):
			var_info = access_variable(var, variables)
			var_value = var_info[1]
			if(type(var_value) == type(1.0)):
				if(var_value == int(var_value)):
					print(int(var_value), end=" ")
					i += 2
					continue
			print(var_value, end=" ")
		elif(var_type == 'struct attribute access'):
			struct_val = access_struct_attribute(var, args[i+2])
			if(struct_val == None):
				return
			print(struct_val, end=' ')
			i += 1
		elif (var_type == 'arithmetic_op'):
			calculate = [var_type, var, args[i+2], args[i+3]]
			x = run(calculate,variables)
			if(x == None):
				return
			if(x == int(x)):
				print(int(x), end=" ")
			else:
				print(x, end=' ')
			i += 2
		elif(var_type == 'conditional_op'):
			if(var == 'not'):
				calculate = [var_type, var, args[i+2]]
				x = run(calculate,variables)
				print(x, end=' ')
				i += 1
			else:
				calculate = [var_type, var, args[i+2], args[i+3]]
				x = run(calculate,variables)
				print(x, end=' ')
				i += 2
		i += 2

	print()

print('Welcome to the MyYAPL Interpreter!')

if len(sys.argv) < 2:
	print('\nPlease enter a file name as an argument.')
	print('e.g: python3 interpreter.py expressions.txt')
else:
	print('Output:')

	code = ' '
	with open(sys.argv[1]) as file:
		for line in file.readlines():
			code += line

	

	jslexer = lex.lex(module=lexer)
	jslexer.input(code)
	jsparser = yacc.yacc(module=parser)
	jsast = jsparser.parse(code, lexer=jslexer)

	try:
		execute(jsast)
	except TypeError as error:
		print('TypeError')
	except ZeroDivisionError as error:
		print('ZeroDivisionError')
	except ValueError as error:
		print('ValueError')
	except Exception as error:
		error = str(error)
		print(error)
