# AST table

idConstructorNum = 1
idMethodNum = 1
idFieldNum = 1
idVaribleNum = 1
classList = {'':''}
outputSteam = ''

class Class:
    def __init__(self, name, superClassName, decl):
        self.name = name
        self.superClassName = superClassName
        global  curClassName
        constructors = {'':''}
        methods = {'':''}
        fields = {'':''}
        for item in decl:
            if type(item) == Constructor:
                item.containingClass = name
                self.constructors[item.id] = item
            elif type(item) == Method:
                item.containingClass = name
                self.methods[item.name] = item
            elif type(item) == Field:
                item.containingClass = name
                self.field[item.name] = item
    def output(self):
        s = "Class Name: %s\n", self.name
        s += "Super Class Name: %s\n", self.superClassName
        s += "Fileds: \n"
        for item in self.fields:
            s += item.output()
        s += "Constructors: \n"
        for item in self.constructors:
            s += item.output()
        s += "Methods: \n"
        for item in self.methods:
            s += item.output()
        s += "--------------------------------------------------------------\n"
        return s


class Constructor:
    def __init__(self, mod, name, paramList, block ):
        global  idConstructorNum
        self.id = idConstructorNum
        idConstructorNum += 1    # each Constructor has identical ID
        self.visibility = mod[0]          # public / private
        self.parameters = paramList    # seq of variable
        self.variableTable = ()  # table of variable
        self.contructorBody = () # statement

    def output(self):
        s = "Constructor: %d, %s\n", self.id, self.visibility
        s += "Constructor Parameters: \n"
        for item in self.parameters:
            s += item.output()
        s += "Variable Table: \n"
        for item in self.variableTable:
            s += item.output()
        s += "Constructor Body: \n"
        for item in self.contructorBody:
            s += item.output()
        return s



class Method:
    def __init__(self, mod, type, name, paramList, block):
        self.variNum = 0;
        self.name = name
        global idMethodNum
        self.id = idMethodNum
        idMethodNum += 1
        self.containingClass = ''                # name of class
        self.visibility = mod[0]             # public / private
        self.applicability  = mod[1]         # static or non-static
        self.parameters = paramList         # seq of variable
        self.returnValue =''        # type / emp (void)
        self.varibleTable = {'':''}
        self.methodBody = {'':''}        # statement

    def output(self):
        s = "%d, %s, %s, %s, %s, %s\n", self.id, self.name, self.containingClass, self.visibility, self.applicability, self.returnValue
        s += "Method Parameters: \n"
        for item in self.parameters:
            s += item.output
        s += "Variable Table: \n"
        for item in self.varibleTable:
            s += item.output
        s += "Method Body: \n"
        for item in self.methodBody:
            s += item.output
        return s



class Field:
    def __init__(self, vis, app, name):
        self.variNum = 0;
        self.name = name
        global  idFieldNum
        self.id = idFieldNum
        idFieldNum += 1
        self.typ = ''
        self.containingClass
        self.visibility          # public / private
        self.applicability

    def output(self):
        s = "%d, %s, %s, %s, instance, %s\n", self.id, self.name, self.containingClass, self.visibility, self.applicability, self.returnValue
        return  s



class Variable :
    def __init__(self, name):
        self.name = name
        self.id = ''                 # unique in constructor or method
        self.kind =''              # formal / local
        self.type =''
        self.baseType = ''

    # def __init__(self, type, name, args):
    #     self.name = name
    #     self.id = idVaribleNum  # unique in constructor or method
    #     self.kind               # formal / local
    #     self.type = type

    def output(self):
        s = "%d, %s, %s, %s\n", self.id , self.name, self.kind, self.type
        return s



class Type:                     # array or elementary
    def __init__(self, type):         # one of int, float, boolean, or string; or class name
        self.type = type


# Statement Group

class Statement:
    def __init__(self):
        self.lineStart           # index of start and end
        self.lineEnd             # to be added to code



class If_Stmt(Statement):
    def __init__(self, ifStmt,thenStmt, elseStmt):
        self.ifStmt = ifStmt           # expression
        self.thenStmt  =thenStmt         # Statement
        self.elseStmt  =elseStmt         # Statement

    def output(self):
        s = "If %s, then %s", self.ifStmt, self.thenStmt
        if self.elseStmt != []:
            s += ", else %s"
        return s



class While_stmt(Statement):
    def __init__(self,loopCondition, body):
        self.loopCondition = loopCondition   # expression
        self.body = body              # statement#
    def output(self):
        s = "While %s, Body: %s", self.loopCondition, self.body
        return s



class For_stmt(Statement):
    def __init__(self, intializer, condition, update, body):
        self.intializer = intializer       # expression
        self.condition = condition        # expression
        self.update = update           # expression
        self.body = body            # statement
    def output(self):
        s = "For( %s, %s, %s) Body: %s", self.intializer, self.condition, self.update, self.body
        return s



class Return_stmt(Statement):
    def __init__(self,returnValue):
        self.returnValue = returnValue    # expression
    def output(self):
        s = "Return %s", self.returnValue
        return s



class Expr_stmt(Statement):
    def __init__(self, expression):
        self.expression        # expression
    def output(self):
        s = "Expression: (  ",
        for item in self.expression:
            s += item.output
        s += "   )\n"
        return  s



class Block_stmt(Statement):
    def __init__(self, stmt):
        self.stmt = stmt         # statement seq
    def output(self):
        s = "Block([\n"
        for item in self.stmt:
            s += item.output
        s += "\n )]\n"
        return  s


class Break_stmt(Statement):
    def __init__(self):
        pass
    def output(self):
        return "Break"



class Continue_stmt(Statement):
    def __init__(self):
        pass
    def output(self):
        return "Continue"



class Skip_stmt(Statement):
    def __init__(self):
        pass                   # empty else part
    def output(self):
        return "Skip"


# Expression Group
class Expression:
    def __init__(self):
        self.lineStart
        self.lineEnd


class Constant_expr (Expression):
    def __init__(self, string):
        self.info = string                  # Integer / Float / String / Null
        if (string in ['true', 'false', 'null']):
            self.type = 'bool'
        else:
            self.type = string
    def output(self):
        s = "Type: %s, Info: %s", self.type, self.info
        return s



class Var_expr (Expression):
    def __init__(self):
        self.id
    def output(self):
        s = "Varibable ID: %d", self.id
        return s



class Unary_expr (Expression):
    def __init__(self, operand, operator):
        self.operand = operand                # +25 -25
        self.operator = operator
    def output(self):
        s = "Unary: %c%d", self.operand, self.operator
        return  s



class Binary_expr (Expression):
    def __init__(self, operand1, operator, operand2):
        self.operand1 = operand1              # expression
        self.operand2 = operand2             # expression
        self.operator = operator            # add, sub, mul, div, and, or, eq, neq, lt, leq, gt, and geq

    def output(self):
        s =  "Binary: %d %s %d", self.operand1, self.operator, self.operand2
        return s



class Assign_expr (Expression):
    def __init__(self, left, right):
        self.left = left                 # expression
        self.right = right                # expression

    def output(self):
        s = self.left.output + self.right.output
        return s



class Auto_expr (Expression):       # x++
    def __init__(self, operand, autoIncre, post):
        self.operand = operand      # expression
        self.autoIncre  = autoIncre   #inc /  dec
        self.post  = post        #post  /  pre

    def output(self):
        if self == "post":
            s = "%s %s", self.autoIncre, self.operand
        else:
            s = "%s %s", self.operand, self.autoIncre
        return s


class FieldAccess_expr (Expression):

    def __init__(self,name):
        self.base = ''         # expression
        self.name = name         # string

    def output(self):
        s = "%s.%s", self.base, self.name
        return  s


class MethodCall_expr (Expression):
    def __init__(self, base, name, argu2Call ):
        self.base  = base        #expr
        self.name  = name        #string
        self.argu2Call  = argu2Call  #seq of expr  / emp

    def output(self):
        s = "%s.%s ("
        s += self.argu2Call.output;
        s += " )"
        return s


class NewObject_expr(Expression):
    def __init__(self, className, argument):
        self.className = className  # string
        self.argument  = argument   # seq of expression / emp

    def output(self):
        s = "%s %s", self.className, self.argument
        return  s



class This_expr (Expression):
    def __init__(self):
        pass

    def output(self):
        s = "this"
        return s


class Super_expr(Expression):
    def __init__(self):
        pass


class ClassReference(Expression):
    def __init__(self):
        self.className       # class name


class ArrayAccess_expr(Expression):
    def __init__(self, base, index):
        self.base = base           # expression
        self.index = index        # expression


class NewArray_expr (Expression):
    def __init__(self, type, dim):
        self.type = type
        self.dimesion = dim       # array

# new int[25][][] should be represented by an new array expression
# of base type array(array(int)), with array dimension 25