# AST table

idConstructorNum = 1
idMethodNum = 1
idFieldNum = 1
idVaribleNum = 1


class Class:

    constructors = {}
    methods = {}
    fields = {}
    name = ''
    superClassName = ''

    def __init__(self, name, superclass, decl):
        self.name = name
        self.superClassName = superclass
        # print ">>>>>>>>>>>>>"
        # print self.name
        # print self.fields
        # print self.constructors
        # print self.methods
        # print ">>>>>>>>>>>>>"
        # without the fellowing code, field, constructor, method just inhert
        # previous one, are ya kidding....
        self.fields = {}
        self.constructors = {}
        self.methods = {}
        if decl:
            for item in decl:
                if type(item) is Constructor:
                    item.containingClass = name
                    self.constructors[item.id] = item
                elif type(item) is Method:
                    item.containingClass = name
                    self.methods[item.name] = item
                elif type(item) == Field:
                    item.containingClass = name
                    self.fields[item.name] = item
                else:
                    print "Error: no mathcing class in field, constructor, method\n"
        # print ">>>>>>>>>>>>>"
        # print self.name
        # print self.fields
        # print self.constructors
        # print self.methods
        # print ">>>>>>>>>>>>>"
        # error with initialize here

    def output(self):
        s = "Class Name: %s\n" % self.name
        s += "Super Class Name: %s\n" % self.superClassName
        s += "Fields: \n"

        if self.fields:
            for item in self.fields:
                s += self.fields[item].output()
        s += "Constructors: \n"
        if self.constructors:
            for item in self.constructors:
                s += self.constructors[item].output()
        s += "Methods: \n"
        if self.methods:
            for item in self.methods:
                s += self.methods[item].output()
        s += "--------------------------------------------------------------\n"
        return s


class Constructor(object):

    id = -1
    visibility = ''          # public / private
    parameters = []          # seq of variable
    variableTable = []       # table of variable
    contructorBody = []     # statement

    def __init__(self, mod, name, paramList, block ):
        global  idConstructorNum
        self.id = idConstructorNum
        idConstructorNum += 1    # each Constructor has identical ID
        self.visibility = mod[0]          # public / private
        self.parameters = paramList    # seq of variable
        self.contructorBody = block

    def output(self):
        s = "    Constructor: %d, %s\n"% (self.id, self.visibility)
        s += "    Constructor Parameters: \n"
        if self.parameters:
            for item in self.parameters:
                s += self.parameters[item].output()
        s += "    Variable Table: \n"
        if self.variableTable:
            for item in self.variableTable:
                s += self.variableTable[item].output()
        s += "    Constructor Body: \n"
        if self.contructorBody:
            s +=  self.contructorBody.output()
        return s


class Method(object):

    variNum = 0
    name = ''
    id = -1
    containingClass = ''                # name of class
    visibility = ''             # public / private
    applicability  = ''         # static or non-static
    parameters = []         # seq of variable
    returnValue = ''        # type / emp (void)
    varibleTable = {}
           # statement

    def __init__(self, mod, type, name, paramList, block):
        self.name = name
        global idMethodNum
        self.id = idMethodNum
        idMethodNum += 1
        self.containingClass = ''                # name of class
        self.visibility = mod[0]             # public / private
        self.applicability = mod[1]         # static or non-static
        self.parameters = paramList         # seq of variable
        self.methodBody = block
        self.returnValue = type

    def output(self):
        s = "    %d, %s, %s, %s, %s, %s\n"% (self.id, self.name, self.containingClass, self.visibility, self.applicability, self.returnValue)
        s += "    Method Parameters: \n"
        if self.parameters:
            for item in self.parameters:
                s += "    "
                s += item.output()
        s += "    Variable Table: \n"
        if self.varibleTable:
            for item in self.varibleTable:
                s += self.varibleTable[item].output()
        s += "    Method Body: \n"

        self.methodBody.output()
        return s


class Field(object):

    variNum = 0
    name = ''
    id = idFieldNum
    type = ''
    containingClass = ''
    visibility = ''         # public / private
    applicability = ''
    #variableList = []

    def __init__(self, vis, app, name, type):
        self.variNum = 0
        self.name = name
        global idFieldNum
        self.id = idFieldNum
        idFieldNum += 1
        self.type = type
        self.visibility = vis
        self.applicability = app

    def output(self):
        s = "    %d, %s, %s, %s, %s, %s\n" %(self.id, self.name, self.containingClass, self.visibility, self.applicability, self.type)
        return s


class Variable :
    name = ''
    id = -1                 # unique in constructor or method
    kind = ''              # formal / local
    type = ''
    baseType = ''
    def __init__(self, name):
        self.name = name
        self.id = -1                 # unique in constructor or method
        self.kind = ''              # formal / local
        self.type = ''
        self.baseType = ''

    def output(self):
        s = "%d, %s, %s, %s\n" %(self.id, self.name, self.kind, self.type)
        return s


class Type:                     # array or elementary
    type = ''
    def __init__(self, type):         # one of int, float, boolean, or string or class name
        self.type = type

# Statement Group

class Statement:

    lineStart = -1
    lineEnd = -1

    def __init__(self):
        self.lineStart           # index of start and end
        self.lineEnd             # to be added to code


class IfStmt(Statement):

    ifStmt = []
    thenStmt = []
    elseStmt = []

    def __init__(self, ifStmt,thenStmt, elseStmt):
        self.ifStmt = ifStmt           # expression
        self.thenStmt = thenStmt         # Statement
        self.elseStmt = elseStmt         # Statement

    def output(self):
        s = "If %s, then %s"% (self.ifStmt, self.thenStmt)
        if self.elseStmt != []:
            s += ", else %s"
        return s



class WhileStmt(Statement):

    loopCondition = []
    body = []

    def __init__(self,loopcondition, body):
        self.loopCondition = loopcondition   # expression
        self.body = body              # statement#

    def output(self):
        s = "While %s, Body: %s" % (self.loopCondition, self.body)
        return s


class ForStmt(Statement):

    intializer = []       # expression
    condition = []        # expression
    update = []           # expression
    body = []            # statement

    def __init__(self, intializer, condition, update, body):
        self.intializer = intializer       # expression
        self.condition = condition        # expression
        self.update = update           # expression
        self.body = body            # statement
    def output(self):
        s = "For( %s, %s, %s) Body: %s" %(self.intializer, self.condition, self.update, self.body)
        return s



class ReturnStmt(Statement):

    returnValue = []

    def __init__(self,returnValue):
        self.returnValue = returnValue    # expression
    def output(self):
        s = "Return %s"% self.returnValue
        return s


class ExprStmt(Statement):

    expression = []

    def __init__(self, expression):
        self.expression        # expression

    def output(self):
        s = "Expression: (  ",
        for item in self.expression:
            s += item.output
        s += "   )\n"
        return  s


class BlockStmt(Statement):

    stmt = []

    def __init__(self, stmt):
        self.stmt = stmt         # statement seq

    def output(self):
        s = "Block(["
        print self.stmt
        if self.stmt:
            for item in self.stmt:
                s += "\n    "
                print "****%s" %item
                s += item.output()
        s += "\n )]\n"
        return s


class BreakStmt(Statement):

    def __init__(self):
        pass

    @staticmethod
    def output(self):
        return "Break"


class ContinueStmt(Statement):

    def __init__(self):
        pass

    @staticmethod
    def output(self):
        return "Continue"


class SkipStmt(Statement):

    def __init__(self):
        pass                   # empty else part

    @staticmethod
    def output(self):
        return "Skip"


# Expression Group
class Expression:
    lineStart = -1
    lineEnd = -1

    # def __init__(self):
    #     self.lineStart
    #     self.lineEnd


class ConstantExpr (Expression):

    info = []
    type = ''

    def __init__(self, info, type):
        self.info = info                  # Integer / Float / String / Null
        self.type = type

    def output(self):
        s = "%s(%s)"% (self.type, self.info)
        return s


class VarExpr (Expression):

    id = []

    def __init__(self, id):
        self.id = id

    def output(self):
        s =''
        if id:
            s = "Declare Variable: # "
            for item in self.id:
                s += " %s," %item
        return s


class UnaryExpr (Expression):

    operand = ''
    operator = ''

    def __init__(self, operand, operator):
        self.operand = operand                # +25 -25
        self.operator = operator

    def output(self):
        s = "Unary: %c%d" % (self.operand, self.operator)
        return s


class BinaryExpr (Expression):

    operand1 = ''
    operand2 = ''
    operator = ''

    def __init__(self, operand1, operator, operand2):
        self.operand1 = operand1              # expression
        self.operand2 = operand2             # expression
        self.operator = operator            # add, sub, mul, div, and, or, eq, neq, lt, leq, gt, and geq

    def output(self):
        s = "Binary: %d %s %d" % (self.operand1, self.operator, self.operand2)
        return s


class AssignExpr (Expression):
    left = ''
    right = ''

    def __init__(self, left, right):
        self.left = left                 # expression
        self.right = right                # expression

    def output(self):
        print self.left.output()
        print self.right.output()
        s = "Assign:( %s, %s)" %( self.left.output() , self.right.output())
        return s


class AutoExpr (Expression):       # x++

    operand = ''
    autoIncre = ''
    post = ''

    def __init__(self, operand, autoIncre, post):
        self.operand = operand       # expression
        self.autoIncre = autoIncre   # increase/decrease
        self.post = post             # post/pre

    def output(self):
        if self == "post":
            s = "%s %s" % (self.autoIncre, self.operand)
        else:
            s = "%s %s" % (self.operand, self.autoIncre)
        return s


class FieldAccessExpr (Expression):

    def __init__(self,name):
        self.base = 'This'         # expression
        self.name = name         # string

    def output(self):
        s = "Field-Access: (%s, %s)"% (self.base, self.name)
        return  s


class MethodCallExpr (Expression):
    def __init__(self, base, name, argu2Call ):
        self.base  = base        #expr
        self.name  = name        #string
        self.argu2Call  = argu2Call  #seq of expr  / emp

    def output(self):
        s = "%s.%s (" %(self.base, self.name)
        s += self.argu2Call.output
        s += " )"
        return s


class NewObjectExpr(Expression):
    def __init__(self, className, argument):
        self.className = className  # string
        self.argument  = argument   # seq of expression / emp

    def output(self):
        s = "%s %s"% (self.className, self.argument)
        return s



class ThisExpr (Expression):
    def __init__(self):
        pass

    def output(self):
        s = "This"
        return s


class SuperExpr(Expression):
    def __init__(self):
        pass


class ClassReference(Expression):
    className = ''

    def __init__(self):
        self.className       # class name


class ArrayAccessExpr(Expression):
    base = ''
    index = ''

    def __init__(self, base, index):
        self.base = base           # expression
        self.index = index        # expression


class NewArrayExpr (Expression):

    type = ''
    dimension = ''

    def __init__(self, typ, dim):
        self.type = typ
        self.dimension = dim       # array

# new int[25][][] should be represented by an new array expression
# of base type array(array(int)), with array dimension 25