# Yacc example

# Get the token map from the lexer.  This is required.

from decaflexer import tokens
from decaflexer import precedence

def p_pp_print(p):
    'pp : program'
#     print p[1]
    
## program
def p_program(p):
    'program : '
def p_program_with_class(p):
    'program : program class_decl'    

## class_decl 
def p_class_decl1_no_extends(p):
    'class_decl1 : CLASS ID LBIG'
def p_class_decl1_extends(p):
    'class_decl1 : CLASS ID EXTENDS ID LBIG'
def p_class_decl2(p):
    'class_decl2 : class_decl1 class_body_decl'
def p_class_decl2_more(p):
    'class_decl2 : class_decl2 class_body_decl'
def p_class_decl(p):
    'class_decl : class_decl2 RBIG'

## class_body_decl
def p_class_body_decl_field(p):
    'class_body_decl : field_decl'
def p_class_body_decl_method(p):
    'class_body_decl : method_decl'
def p_class_body_decl_constructor(p):
    'class_body_decl : constructor_decl'

## field_decl
def p_field_decl(p):
    'field_decl : modifier var_decl'
    
## modifier 
def p_modifier_first_public(p):
    'modifier_first : PUBLIC'
def p_modifier_first_private(p):
    'modifier_first : PRIVATE'
def p_modifier_no(p):
    'modifier : modifier_first'
def p_modifier_have(p):
    'modifier : modifier_first STATIC'
    
## var_decl
def p_var_decl(p):
    'var_decl : type variables SEMICOLON'
    p[0] = 'var_decl'

## type                        need
def p_type_int(p): 
    'type : INT'
def p_type_float(p):
    'type : FLOAT'
def p_type_boolean(p):
    'type : BOOLEAN'
def p_type_id(p):
    'type : ID'
    
## variables
def p_variables(p):
    'variables : variable'
    p[0] = "variables"
def p_variables_more(p):
    'variables : variables COMMA variable'
    p[0] = "variables"

## variable
def p_variable(p):
    'variable : ID'
    p[0] = "variable"
def p_variable_array(p):
    'variable : variable LSQ RSQ'
    p[0] = "variable"
    
## method_decl
def p_method_decl1_type(p):
    'method_decl1 : modifier type ID LPAREN'
def p_method_decl1_void(p):
    'method_decl1 : modifier VOID ID LPAREN'
def p_method_decl_formals(p):
    'method_decl : method_decl1 formals RPAREN block'
def p_method_decl_no(p):
    'method_decl : method_decl1 RPAREN block'

## constructor_decl
def p_constructor_decl_no(p):
    'constructor_decl : modifier ID LPAREN RPAREN block'
def p_constructor_decl_formals(p):
    'constructor_decl : modifier ID LPAREN formals RPAREN block'

## formals 
def p_formals_single(p):
    'formals : formal_param'
def p_formals_more(p):
    'formals : formals COMMA formal_param'

## formal_param
def p_formal_param(p):
    'formal_param : type variable'
    
## block
def p_block1_first(p):
    'block1 : LBIG'
    p[0] = "block";
def p_block1_end(p):
    'block1 : block1 stmt'
    p[0] = p[2]
def p_block(p):
    'block : block1 RBIG'
    p[0] = p[1]

## stmt
#### summary
def p_stmt_summary(p):
    'stmt : noncompleteif_stmt'
    p[0] = "non_complete_if"
def p_stmt_summary1(p):
    'stmt : other_stmt'
    p[0] = "other"
#### noncompleteif_stmt
###### if
def p_noncompleteif_if(p):
    'noncompleteif_stmt : IF LPAREN expr RPAREN stmt'
    p[0] = "non_complete_if"
###### ifelse
def p_noncompleteif_ifelse(p):
    'noncompleteif_stmt : IF LPAREN expr RPAREN other_stmt ELSE noncompleteif_stmt'
    p[0] = "non_complete_ifelse"
###### while
def p_noncompleteif__while(p): 
    'noncompleteif_stmt : WHILE LPAREN expr RPAREN noncompleteif_stmt'
    p[0] = "non_complete_while"
###### for
def p_noncompleteif_for(p):
    'noncompleteif_stmt : forbasic noncompleteif_stmt'
    p[0] = "non_complete_for"
#### other_stmt 
###### complete_if
def p_other_stmt_complete_if(p):
    'other_stmt : IF LPAREN expr RPAREN other_stmt ELSE other_stmt'
    p[0] = "complete";
###### while
def p_other_stmt_complete_while(p): 
    'other_stmt : WHILE LPAREN expr RPAREN other_stmt'
    p[0] = "while"
###### for
def p_forbasic1_no(p):
    'forbasic1 : FOR LPAREN SEMICOLON'
def p_forbasic1_have(p):
    'forbasic1 : FOR LPAREN stmt_expr SEMICOLON'
def p_forbasic2_no(p):
    'forbasic2 : forbasic1 SEMICOLON'
def p_forbasic2_have(p):
    'forbasic2 : forbasic1 expr SEMICOLON'
def p_forbasic_no(p):
    'forbasic : forbasic2 RPAREN'
def p_forbasic_have(p):
    'forbasic : forbasic2 stmt_expr RPAREN'
def p_other_stmt_for(p):
    'other_stmt : forbasic other_stmt'
    p[0] = 'for'
###### return
def p_other_stmt_return_no(p):
    'other_stmt : RETURN SEMICOLON'
    p[0] = 'return'
def p_other_stmt_return_have(p):
    'other_stmt : RETURN expr SEMICOLON'
    p[0] = 'return'
###### stmt_expr
def p_other_stmt_stmt_expr(p): 
    'other_stmt : stmt_expr SEMICOLON'
    p[0] = "stmt_expr"
###### break
def p_other_stmt_break(p):
    'other_stmt : BREAK'
    p[0] = "break"
###### continue
def p_other_stmt_continue(p):
    'other_stmt : CONTINUE'
    p[0] = "continue"
###### block
def p_other_stmt_block(p):
    'other_stmt : block'
    p[0] = 'block'
###### var_decl 
def p_other_stmt_var_decl(p):
    'other_stmt : var_decl'
    p[0] = 'var_decl'    
###### SEMICOLON
def p_stmt_semicolon(p):
    'other_stmt : SEMICOLON'
    p[0] = "semi"
  
## literal
def p_literal_int(p):
    'literal : INT_CONST'
    p[0] = p[1]
def p_literal_float(p):
    'literal : FLOAT_CONST'
    p[0] = p[1]
def p_literal_string(p):
    'literal : STRING_CONST'
    p[0] = p[1]
def p_literal_null(p):
    'literal : NULL'
    p[0] = p[1]
def p_literal_true(p):
    'literal : TRUE'
    p[0] = p[1]
def p_literal_false(p):
    'literal : FALSE'
    p[0] = p[1]
      
## primary
#### iteral
def p_primary_literal(p):
    'primary : literal'
    p[0] = p[1]
#### this
def p_primary_this(p):
    'primary : THIS'
    p[0] = 0
#### super
def p_primary_super(p):
    'primary : SUPER'
    p[0] = 0
#### paren
def p_primary_paren(p):
    'primary : LPAREN expr RPAREN'
    p[0] = p[2]
#### new
def p_primary_pnew1(p):
    'pnew1 : NEW ID'
    p[0] = p[2]
def p_primary_pnew(p):
    'pnew : pnew1 LPAREN RPAREN'
    p[0] = p[1]
def p_primary_pnew_arg(p):
    'pnew : pnew1 LPAREN arguments RPAREN'
    p[0] = p[1]
def p_primary_summary(p):
    'primary : pnew'
    p[0] = p[1]
#### lhs
def p_primary_lhs(p):
    'primary : lhs'
    p[0] = p[1]
#### method_invocation
def p_primary_method_invocation(p):
    'primary : method_invocation'
    p[0] = p[1]
    
## arguments
def p_argument_init(p):
    'arguments : expr'
    p[0] = p[1]
def p_argument_follow(p):
    'arguments : arguments COMMA expr'
    p[0] = p[1]
      
## lhs                         need
def p_lhs_field(p):
    'lhs : field_access'
    p[0] = 0
def p_lhs_array(p):
    'lhs : array_access'
    p[0] = 0
  
## field_access                need
def p_field_access(p):
    'field_access : primary POINT ID'
    p[0] = 0
def p_field_access_1(p):
    'field_access : ID'
    p[0] = 0
      
## array_access                need
def p_array_access(p):
    'array_access : primary LSQ expr RSQ'
    p[0] = 0

## method_invocation 
def p_method_invocation_noarg(p):
    'method_invocation : field_access LPAREN RPAREN'
    p[0] = 0
def p_method_invocation_arg(p):
    'method_invocation : field_access LPAREN arguments RPAREN'
    p[0] = 0
    
## expression
#### arith_op
def p_expr_arith_add(p):
    'expr : expr PLUS expr'
    p[0] = p[1] + p[3]
def p_expr_arith_minus(p): 
    'expr : expr MINUS expr'
    p[0] = p[1] - p[3]
def p_expr_arith_multi(p):
    'expr : expr MULTI expr'
    p[0] = p[1] * p[3]
def p_expr_airth_divede(p):
    'expr : expr DIVIDE expr'
    p[0] = p[1] / p[3]
#### bool_op
def p_expr_bool_and(p):
    'expr : expr AND expr'
    p[0] = bool(p[1] and p[3])
def p_expr_bool_or(p):
    'expr : expr OR expr'
    p[0] = bool(p[1] or p[3])
def p_expr_bool_equal(p):
    'expr : expr EQUAL expr'
    p[0] = bool(p[1] == p[3])
def p_expr_bool_notequal(p):
    'expr : expr NOTEQUAL expr'
    p[0] = bool(p[1] != p[3])
def p_expr_bool_less(p):
    'expr : expr LESS expr'
    p[0] = bool(p[1] < p[3])
def p_expr_bool_greater(p):
    'expr : expr GREATER expr'
    p[0] = bool(p[1] > p[3])
def p_expr_bool_lessequal(p):
    'expr : expr LESSEQUAL expr'
    p[0] = bool(p[1] <= p[3])
def p_expr_bool_greaterequal(p):
    'expr : expr GREATEREQUAL expr'
    p[0] = bool(p[1] >= p[3])
#### primary
def p_expr_primary(p):
    'expr : primary'
    p[0] = p[1]
#### assign
def p_expr_assign(p):
    'expr : assign'
    p[0] = p[1]
#### newarray
def p_expr_newarray(p):
    'expr : newarray'
    p[0] = p[1]
#### unary
def p_expr_uminus(p):
    'expr : MINUS expr %prec UMINUS'
    p[0] = -p[2]
def p_expr_uplus(p):
    'expr : PLUS expr %prec UPLUS'
    p[0] = p[2]
def p_expr_not(p):
    'expr : NOT expr %prec NOT'
    p[0] = not bool(p[2])
  
 
## newarray
def p_newarray_p(p):
    "newarray : newarrayp"
def p_newarray_w(p):
    "newarray : newarrayw"
def p_newarrayw_follow(p):
    "newarrayw : newarrayw LSQ RSQ"
def p_newarrayw_first(p):
    "newarrayw : newarrayp LSQ RSQ"
def p_newarrayp_first(p):
    "newarrayp : NEW type LSQ INT_CONST RSQ"
def p_newarrayp_follow(p):
    "newarrayp : newarrayp LSQ INT_CONST RSQ"
          
## assign
def p_assign_normal(p):
    'assign : lhs ASSIGN expr'
    p[0] = p[3]
    p[1] = p[3]
def p_assign_dadd(p):
    'assign : lhs INCREMENT'
    p[0] = p[1];
    p[1] = p[1] + 1;
def p_assign_bdadd(p):
    'assign : INCREMENT lhs'
    p[0] = p[2] + 1;
    p[2] = p[2] + 1;
def p_assign_dminus(p):
    'assign : lhs DECREMENT'
    p[0] = p[1];
    p[1] = p[1] - 1;
def p_assign_bdminus(p):
    'assign : DECREMENT lhs'
    p[0] = p[2] - 1;
    p[2] = p[2] - 1;    
    
## stmt_expr
def p_stmt_expr_assign(p):
    'stmt_expr : assign'
    p[0] = p[1]
def p_stmt_expr_method_invocation(p):
    'stmt_expr : method_invocation'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! " ), 

# Build the parser
