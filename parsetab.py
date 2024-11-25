
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'stmtsleftORleftANDleftEQEQnonassocLESSGREATERLESSEQGREATEREQleftPLUSMINUSrightEXPONENTleftMULTIPLYDIVIDEMODrightNOTAND BOOLDEC CHARDEC COMMA COMMENT DECREMENT DIVIDE DO DOT DOUBLE DOUBLEDEC EQEQ EQUALS EXPONENT FALSE GREATER GREATEREQ INCREMENT INT INTDEC LBRACE LESS LESSEQ LPAR MINUS MOD MULTIPLY NAME NOT NOTEQ OR PLUS PRINT RBRACE RPAR SEMICOLON STRING STRINGDEC STRUCT TRUE WHILE\n\tstmts : stmt SEMICOLON stmts\n\t\n\tstmts : COMMENT\n\t\n\tstmts :\n\t\n\tstmt : expr\n\t\t\t| empty\n\t\t\t| var_dec\n\t\t\t| var_initialize\n\t\t\t| var_assign\n\t\t\t| var_access\n\t\t\t| function_call\n\t\t\t| loop\n\t\t\t| struct_definition\n\t\t\t| struct_attribute_initialize\n\t\t\t| unary_op\n\t\n\tstruct_definition : STRUCT NAME EQUALS LBRACE attribute_dec RBRACE\n\t\n\tattribute_dec : var_dec SEMICOLON attribute_dec\n\t\t\t\t\t\t\t  | var_initialize SEMICOLON attribute_dec\n\t\n\tattribute_dec : var_dec SEMICOLON\n\t\t\t\t\t\t\t  | var_initialize SEMICOLON\n\t\t\t\t\t\t\t  | empty\n\t\n\tvar_access : NAME\n\t\n\tstruct_access : NAME DOT NAME\n\t\n\tvar_assign : NAME EQUALS expr\n\t\n\tvar_dec : identifier NAME\n\t\n\tvar_initialize : identifier NAME EQUALS expr\n\t\t\t\t\t| identifier NAME EQUALS NAME\n\t\n\tidentifier : INTDEC\n\t\t\t\t\t   | DOUBLEDEC\n\t\t\t\t\t   | STRINGDEC\n\t\t\t\t\t   | BOOLDEC\n\t\t\t\t\t   | CHARDEC\n\t\t\t\t\t   | NAME\n\t\n\tstruct_attribute_initialize : NAME DOT NAME EQUALS expr\n\t\n\texpr : LPAR expr RPAR\n\t\n\texpr : unary_op\n\t\n\texpr : expr MULTIPLY expr\n\t\t\t\t\t| expr DIVIDE expr\n\t\t\t\t\t| expr PLUS expr\n\t\t\t\t\t| expr MINUS expr\n\t\t\t\t\t| expr MOD expr\n\t\t\t\t\t| expr EXPONENT expr\n\t\n\texpr : DOUBLE\n\t\t | INT\n\t\n\texpr : MINUS DOUBLE\n\t\t| MINUS INT\n\t\n\texpr : STRING\n\t\n\texpr : TRUE\n\t\t\t | FALSE\n\t\n\texpr : var_access\n\t\n\texpr : struct_access\n\t\n\texpr : empty\n\t\n\tunary_op : var_access INCREMENT\n\t\t\t\t| var_access DECREMENT\n\t\t\t\t| struct_access INCREMENT\n\t\t\t\t| struct_access DECREMENT\n\t\n\tunary_op : MINUS var_access\n\t\n\texpr : expr conditional_operators expr\n\t\n\texpr : NOT expr\n\t\n\tconditional_operators : EQEQ\n\t\t| LESS\n\t\t| GREATER\n\t\t| AND\n\t\t| OR\n\t\t| GREATEREQ\n\t\t| LESSEQ\n\t\t| NOTEQ\n\t\n\tloop : DO LBRACE stmts RBRACE WHILE LPAR expr RPAR\n\t\n\tfunction_call : PRINT LPAR opt_args RPAR\n\t\n\topt_args : expr moreargs\n\t\n\tmoreargs : COMMA expr moreargs\n\t\n\topt_args : empty\n\t\n\tmoreargs : empty\n\t\n\tempty :\n\t'
    
_lr_action_items = {'COMMENT':([0,34,68,],[3,3,3,]),'$end':([0,1,3,34,70,],[-3,0,-2,-3,-1,]),'LPAR':([0,15,23,26,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,65,67,68,80,91,94,100,107,],[15,15,15,67,15,15,15,15,15,15,15,15,-59,-60,-61,-62,-63,-64,-65,-66,15,15,15,15,15,15,107,15,]),'DOUBLE':([0,15,16,23,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,65,67,68,80,91,94,107,],[17,17,57,17,17,17,17,17,17,17,17,17,-59,-60,-61,-62,-63,-64,-65,-66,17,17,17,17,17,17,17,]),'INT':([0,15,16,23,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,65,67,68,80,91,94,107,],[18,18,58,18,18,18,18,18,18,18,18,18,-59,-60,-61,-62,-63,-64,-65,-66,18,18,18,18,18,18,18,]),'MINUS':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[16,38,-51,-49,-35,16,-42,-43,-46,-47,-48,-50,16,-21,16,16,16,16,16,16,16,16,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,38,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,16,16,16,-36,-37,-38,-39,-40,-41,38,-34,16,38,-22,38,-51,-22,-21,38,16,16,38,38,16,38,]),'STRING':([0,15,23,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,65,67,68,80,91,94,107,],[19,19,19,19,19,19,19,19,19,19,19,-59,-60,-61,-62,-63,-64,-65,-66,19,19,19,19,19,19,19,]),'TRUE':([0,15,23,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,65,67,68,80,91,94,107,],[20,20,20,20,20,20,20,20,20,20,20,-59,-60,-61,-62,-63,-64,-65,-66,20,20,20,20,20,20,20,]),'FALSE':([0,15,23,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,65,67,68,80,91,94,107,],[21,21,21,21,21,21,21,21,21,21,21,-59,-60,-61,-62,-63,-64,-65,-66,21,21,21,21,21,21,21,]),'NOT':([0,15,23,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,65,67,68,80,91,94,107,],[23,23,23,23,23,23,23,23,23,23,23,-59,-60,-61,-62,-63,-64,-65,-66,23,23,23,23,23,23,23,]),'SEMICOLON':([0,2,4,5,6,7,8,9,10,11,12,13,14,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,68,71,72,73,74,75,76,77,78,80,81,82,88,89,90,91,92,98,103,104,108,114,],[-73,34,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-24,-73,-73,-36,-37,-38,-39,-40,-41,-57,-34,-73,-23,-22,-22,-21,-25,-73,-68,-33,109,110,-15,-67,]),'MULTIPLY':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,35,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,35,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,35,35,-40,35,35,-34,-73,35,-22,35,-51,-22,-21,35,-73,-73,35,35,-73,35,]),'DIVIDE':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,36,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,36,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,36,36,-40,36,36,-34,-73,36,-22,36,-51,-22,-21,36,-73,-73,36,36,-73,36,]),'PLUS':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,37,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,37,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,37,-34,-73,37,-22,37,-51,-22,-21,37,-73,-73,37,37,-73,37,]),'MOD':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,39,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,39,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,39,39,-40,39,39,-34,-73,39,-22,39,-51,-22,-21,39,-73,-73,39,39,-73,39,]),'EXPONENT':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,40,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,40,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,40,40,-40,40,40,-34,-73,40,-22,40,-51,-22,-21,40,-73,-73,40,40,-73,40,]),'EQEQ':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,42,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,42,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,42,-34,-73,42,-22,42,-51,-22,-21,42,-73,-73,42,42,-73,42,]),'LESS':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,43,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,43,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,43,-34,-73,43,-22,43,-51,-22,-21,43,-73,-73,43,43,-73,43,]),'GREATER':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,44,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,44,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,44,-34,-73,44,-22,44,-51,-22,-21,44,-73,-73,44,44,-73,44,]),'AND':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,45,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,45,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,45,-34,-73,45,-22,45,-51,-22,-21,45,-73,-73,45,45,-73,45,]),'OR':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,46,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,46,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,46,-34,-73,46,-22,46,-51,-22,-21,46,-73,-73,46,46,-73,46,]),'GREATEREQ':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,47,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,47,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,47,-34,-73,47,-22,47,-51,-22,-21,47,-73,-73,47,47,-73,47,]),'LESSEQ':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,48,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,48,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,48,-34,-73,48,-22,48,-51,-22,-21,48,-73,-73,48,48,-73,48,]),'NOTEQ':([0,4,5,9,14,15,17,18,19,20,21,22,23,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,71,72,73,74,75,76,77,78,80,81,82,84,85,88,89,90,91,94,98,99,107,111,],[-73,49,-51,-49,-35,-73,-42,-43,-46,-47,-48,-50,-73,-21,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,49,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-73,-73,-36,-37,-38,-39,-40,-41,49,-34,-73,49,-22,49,-51,-22,-21,49,-73,-73,49,49,-73,49,]),'NAME':([0,15,16,23,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,65,66,67,68,79,80,91,94,97,101,107,109,110,],[25,56,60,56,64,-32,69,-27,-28,-29,-30,-31,25,56,56,56,56,56,56,56,-59,-60,-61,-62,-63,-64,-65,-66,56,82,56,25,88,89,56,56,101,-32,56,101,101,]),'PRINT':([0,34,68,],[26,26,26,]),'DO':([0,34,68,],[27,27,27,]),'STRUCT':([0,34,68,],[28,28,28,]),'INTDEC':([0,34,68,97,109,110,],[29,29,29,29,29,29,]),'DOUBLEDEC':([0,34,68,97,109,110,],[30,30,30,30,30,30,]),'STRINGDEC':([0,34,68,97,109,110,],[31,31,31,31,31,31,]),'BOOLDEC':([0,34,68,97,109,110,],[32,32,32,32,32,32,]),'CHARDEC':([0,34,68,97,109,110,],[33,33,33,33,33,33,]),'RBRACE':([3,34,68,70,86,97,102,105,109,110,112,113,],[-2,-3,-3,-1,96,-73,108,-20,-18,-19,-16,-17,]),'INCREMENT':([9,22,25,54,56,82,88,89,],[50,61,-21,50,-21,-22,-22,-21,]),'DECREMENT':([9,22,25,54,56,82,88,89,],[51,62,-21,51,-21,-22,-22,-21,]),'RPAR':([15,17,18,19,20,21,22,23,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,71,72,73,74,75,76,77,78,83,84,85,88,93,94,95,99,106,107,111,],[-73,-42,-43,-46,-47,-48,-50,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,78,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-36,-37,-38,-39,-40,-41,-57,-34,92,-73,-51,-22,-69,-73,-72,-73,-70,-73,114,]),'COMMA':([17,18,19,20,21,22,23,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,67,71,72,73,74,75,76,77,78,84,85,88,94,99,],[-42,-43,-46,-47,-48,-50,-73,-73,-73,-73,-73,-73,-73,-73,-59,-60,-61,-62,-63,-64,-65,-66,-52,-53,-35,-49,-51,-21,-44,-45,-56,-21,-54,-55,-58,-73,-36,-37,-38,-39,-40,-41,-57,-34,94,-51,-22,-73,94,]),'EQUALS':([25,64,69,82,],[65,80,87,91,]),'DOT':([25,56,89,],[66,79,79,]),'LBRACE':([27,87,],[68,97,]),'WHILE':([96,],[100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmts':([0,34,68,],[1,70,86,]),'stmt':([0,34,68,],[2,2,2,]),'expr':([0,15,23,34,35,36,37,38,39,40,41,65,67,68,80,91,94,107,],[4,52,63,4,71,72,73,74,75,76,77,81,84,4,90,98,99,111,]),'empty':([0,15,23,34,35,36,37,38,39,40,41,65,67,68,80,84,91,94,97,99,107,109,110,],[5,55,55,5,55,55,55,55,55,55,55,55,85,5,55,95,55,55,105,95,55,105,105,]),'var_dec':([0,34,68,97,109,110,],[6,6,6,103,103,103,]),'var_initialize':([0,34,68,97,109,110,],[7,7,7,104,104,104,]),'var_assign':([0,34,68,],[8,8,8,]),'var_access':([0,15,16,23,34,35,36,37,38,39,40,41,65,67,68,80,91,94,107,],[9,54,59,54,9,54,54,54,54,54,54,54,54,54,9,54,54,54,54,]),'function_call':([0,34,68,],[10,10,10,]),'loop':([0,34,68,],[11,11,11,]),'struct_definition':([0,34,68,],[12,12,12,]),'struct_attribute_initialize':([0,34,68,],[13,13,13,]),'unary_op':([0,15,23,34,35,36,37,38,39,40,41,65,67,68,80,91,94,107,],[14,53,53,14,53,53,53,53,53,53,53,53,53,14,53,53,53,53,]),'struct_access':([0,15,23,34,35,36,37,38,39,40,41,65,67,68,80,91,94,107,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'identifier':([0,34,68,97,109,110,],[24,24,24,24,24,24,]),'conditional_operators':([4,52,63,71,72,73,74,75,76,77,81,84,90,98,99,111,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'opt_args':([67,],[83,]),'moreargs':([84,99,],[93,106,]),'attribute_dec':([97,109,110,],[102,112,113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stmts","S'",1,None,None,None),
  ('stmts -> stmt SEMICOLON stmts','stmts',3,'p_stmts','parser.py',25),
  ('stmts -> COMMENT','stmts',1,'p_comments','parser.py',32),
  ('stmts -> <empty>','stmts',0,'p_stmts_terminal','parser.py',46),
  ('stmt -> expr','stmt',1,'p_stmt','parser.py',53),
  ('stmt -> empty','stmt',1,'p_stmt','parser.py',54),
  ('stmt -> var_dec','stmt',1,'p_stmt','parser.py',55),
  ('stmt -> var_initialize','stmt',1,'p_stmt','parser.py',56),
  ('stmt -> var_assign','stmt',1,'p_stmt','parser.py',57),
  ('stmt -> var_access','stmt',1,'p_stmt','parser.py',58),
  ('stmt -> function_call','stmt',1,'p_stmt','parser.py',59),
  ('stmt -> loop','stmt',1,'p_stmt','parser.py',60),
  ('stmt -> struct_definition','stmt',1,'p_stmt','parser.py',61),
  ('stmt -> struct_attribute_initialize','stmt',1,'p_stmt','parser.py',62),
  ('stmt -> unary_op','stmt',1,'p_stmt','parser.py',63),
  ('struct_definition -> STRUCT NAME EQUALS LBRACE attribute_dec RBRACE','struct_definition',6,'p_struct_definition','parser.py',70),
  ('attribute_dec -> var_dec SEMICOLON attribute_dec','attribute_dec',3,'p_multiple_attribute','parser.py',77),
  ('attribute_dec -> var_initialize SEMICOLON attribute_dec','attribute_dec',3,'p_multiple_attribute','parser.py',78),
  ('attribute_dec -> var_dec SEMICOLON','attribute_dec',2,'p_attribute_dec','parser.py',88),
  ('attribute_dec -> var_initialize SEMICOLON','attribute_dec',2,'p_attribute_dec','parser.py',89),
  ('attribute_dec -> empty','attribute_dec',1,'p_attribute_dec','parser.py',90),
  ('var_access -> NAME','var_access',1,'p_var_access','parser.py',104),
  ('struct_access -> NAME DOT NAME','struct_access',3,'p_var_struct_access','parser.py',111),
  ('var_assign -> NAME EQUALS expr','var_assign',3,'p_var_assign','parser.py',120),
  ('var_dec -> identifier NAME','var_dec',2,'p_var_dec','parser.py',129),
  ('var_initialize -> identifier NAME EQUALS expr','var_initialize',4,'p_var_initialize','parser.py',138),
  ('var_initialize -> identifier NAME EQUALS NAME','var_initialize',4,'p_var_initialize','parser.py',139),
  ('identifier -> INTDEC','identifier',1,'p_identifier','parser.py',146),
  ('identifier -> DOUBLEDEC','identifier',1,'p_identifier','parser.py',147),
  ('identifier -> STRINGDEC','identifier',1,'p_identifier','parser.py',148),
  ('identifier -> BOOLDEC','identifier',1,'p_identifier','parser.py',149),
  ('identifier -> CHARDEC','identifier',1,'p_identifier','parser.py',150),
  ('identifier -> NAME','identifier',1,'p_identifier','parser.py',151),
  ('struct_attribute_initialize -> NAME DOT NAME EQUALS expr','struct_attribute_initialize',5,'p_struct_attribute_initialize','parser.py',160),
  ('expr -> LPAR expr RPAR','expr',3,'p_nested_expr','parser.py',169),
  ('expr -> unary_op','expr',1,'p_expr_unary_op','parser.py',176),
  ('expr -> expr MULTIPLY expr','expr',3,'p_expr_binop','parser.py',183),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr_binop','parser.py',184),
  ('expr -> expr PLUS expr','expr',3,'p_expr_binop','parser.py',185),
  ('expr -> expr MINUS expr','expr',3,'p_expr_binop','parser.py',186),
  ('expr -> expr MOD expr','expr',3,'p_expr_binop','parser.py',187),
  ('expr -> expr EXPONENT expr','expr',3,'p_expr_binop','parser.py',188),
  ('expr -> DOUBLE','expr',1,'p_expr_positive_numbers','parser.py',195),
  ('expr -> INT','expr',1,'p_expr_positive_numbers','parser.py',196),
  ('expr -> MINUS DOUBLE','expr',2,'p_expr_negative_numbers','parser.py',203),
  ('expr -> MINUS INT','expr',2,'p_expr_negative_numbers','parser.py',204),
  ('expr -> STRING','expr',1,'p_expr_string','parser.py',212),
  ('expr -> TRUE','expr',1,'p_expr_bool','parser.py',219),
  ('expr -> FALSE','expr',1,'p_expr_bool','parser.py',220),
  ('expr -> var_access','expr',1,'p_expr_var','parser.py',227),
  ('expr -> struct_access','expr',1,'p_expr_struct_var','parser.py',234),
  ('expr -> empty','expr',1,'p_expr_empty','parser.py',241),
  ('unary_op -> var_access INCREMENT','unary_op',2,'p_unary_operation','parser.py',248),
  ('unary_op -> var_access DECREMENT','unary_op',2,'p_unary_operation','parser.py',249),
  ('unary_op -> struct_access INCREMENT','unary_op',2,'p_unary_operation','parser.py',250),
  ('unary_op -> struct_access DECREMENT','unary_op',2,'p_unary_operation','parser.py',251),
  ('unary_op -> MINUS var_access','unary_op',2,'p_unary_operation_negative','parser.py',258),
  ('expr -> expr conditional_operators expr','expr',3,'p_expr_conditional','parser.py',265),
  ('expr -> NOT expr','expr',2,'p_expr_not','parser.py',272),
  ('conditional_operators -> EQEQ','conditional_operators',1,'p_conditional_operators','parser.py',279),
  ('conditional_operators -> LESS','conditional_operators',1,'p_conditional_operators','parser.py',280),
  ('conditional_operators -> GREATER','conditional_operators',1,'p_conditional_operators','parser.py',281),
  ('conditional_operators -> AND','conditional_operators',1,'p_conditional_operators','parser.py',282),
  ('conditional_operators -> OR','conditional_operators',1,'p_conditional_operators','parser.py',283),
  ('conditional_operators -> GREATEREQ','conditional_operators',1,'p_conditional_operators','parser.py',284),
  ('conditional_operators -> LESSEQ','conditional_operators',1,'p_conditional_operators','parser.py',285),
  ('conditional_operators -> NOTEQ','conditional_operators',1,'p_conditional_operators','parser.py',286),
  ('loop -> DO LBRACE stmts RBRACE WHILE LPAR expr RPAR','loop',8,'p_loop','parser.py',294),
  ('function_call -> PRINT LPAR opt_args RPAR','function_call',4,'p_print','parser.py',303),
  ('opt_args -> expr moreargs','opt_args',2,'p_optargs','parser.py',310),
  ('moreargs -> COMMA expr moreargs','moreargs',3,'p_moreargs','parser.py',320),
  ('opt_args -> empty','opt_args',1,'p_optargs_empty','parser.py',330),
  ('moreargs -> empty','moreargs',1,'p_moreargs_empty','parser.py',337),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',346),
]
