# AST table

idConstructorNum = 0
idMethodNum = 0
idFieldNum = 0
idVaribleNum = 0

class Expr: pass

class Class:
    def __init__(self, name, superClassName):
        self.name = name
        self.superClassName = superClassName
        constructors = ()
        methods = ()
        fields = ()

class Constructor:
    def __init__(self):
        global  idConstructorNum
        self. id = idConstructorNum
        idConstructorNum += 1    # each Constructor has identical ID
        self.visibility          # public / private
        self.parameters = ()     # seq of variable
        self.variableTable = ()  # table of variable
        self.contructorBody = () # statement

class Method:
    def __init__(self, name):
        self.name = name
        global  idMethodNum
        self.id = idMethodNum
        idMethodNum += 1
        self.containingClass     # name of class
        self.visibility          # public / private
        self.applicability       # static or non-static
        self.parameters          # seq of variable
        self.returnValue         # type / emp (void)
        self.varibleTable
        self.methodBody          # statement

class Field:
    def __init__(self, name):
        self.name = name
        global  idFieldNum
        self.id = idFieldNum
        idFieldNum += 1
        self.containingClass
        self.visibility          # public / private
        self.applicability       # static or non-static
        self.type
# might put it in the constructor or method late

class VariableTable :
    def __init__(self, name):
        self.name = name
        self.id = idVaribleNum  # unique in constructor or method
        self.kind               # formal / local
        self.type

class Type:                     # array or elementary
    def __init__(self):         # one of int, float, boolean, or string; or class name
        pass


# Statement Group

class Statement:
    def __init__(self):
        self.lineStart           # index of start and end
        self.lineEnd

class If_Stmt(Statement):
    def __init__(self):
        self.ifStmt             # expression
        self.thenStmt           # Statement
        self.elseStmt           # Statement

class While_stmt(Statement):
    def __init__(self):
        self.LoopCondition     # expression
        self.body              # statement#

class For_stmt(Statement):
    def __init__(self):
        self.intializer        # expression
        self.condition         # expression
        self.update            # expression
        self.body              # statement

class Return_stmt(Statement):
    def __init__(self):
        self.returnValue       # expression

class Expr_stmt(Statement):
    def __init__(self):
        self.expression        # expression

class Block_stmt(Statement):
    def __init__(self):
        self.stmt = ()         # statement seq

class Break_stmt(Statement):
    def __init__(self):
        pass

class Continue_stmt(Statement):
    def __init__(self):
        pass

class Skip_stmt(Statement):
    def __init__(self):
        pass                   # empty else part



# Expression Group
class Expression:
    def __init__(self):
        self.lineStart
        self.lineEnd

class Constant_expr (Expression):
    def __init__(self):
        self.type                   # Integer / Float / String / Null
        self.info

class Var_expr (Expression):
    def __init__(self):
        self.id

class Unary_expr (Expression):
    def __init__(self):
        self.operand                # +25 -25
        self.operator

class Binary_expr (Expression):
    def __init__(self):
        self.operand1               # expression
        self.operand2               # expression
        self.operator               # add, sub, mul, div, and, or, eq, neq, lt, leq, gt, and geq

class Assign_expr (Expression):
    def __init__(self):
        self.left                   # expression
        self.right                  # expression

class Auto_expr (Expression):       # x++
    def __init__(self):
        self.operand       # expression
        self.autoIncre     #incre /  decre
        self.post          #post  /  pre

class FieldAccess_expr (Expression):
    def __init__(self):
        self.base          # expression
        self.name          # string

class MethodCall_expr (Expression):
    def __init__(self):
        self.base         #expr
        self.base         #string
        self.argu2Call    #seq of expr  / emp

class NewObject_expr(Expression):
    def __init__(self):
        self.className   # string
        self.argument    # seq of expression / emp

class This_expr (Expression):
    def __init__(self):
        pass

class Super_expr(Expression):
    def __init__(self):
        pass

class ClassReference(Expression):
    def __init__(self):
        self.className       # class name

class ArrayAccess_expr(Expression):
    def __init__(self):
        self.base           # expression
        self.index          # expression

class NewArray_expr (Expression):
    def __init__(self):
        self.type
        self.dimesion       # array

# new int[25][][] should be represented by an new array expression
# of base type array(array(int)), with array dimension 25




