classtable = {}  # initially empty dictionary of classes.
lastmethod = 0
lastconstructor = 0

# Class table.  Only user-defined classes are placed in the class table.
def lookup(table, key):
    if key in table:
        return table[key]
    else:
        return None

def addtotable(table, key, value):
    table[key] = value


def print_ast():
    for cid in classtable:
        c = classtable[cid]
        c.printout()
    print "-----------------------------------------------------------------------------"

<<<<<<< Updated upstream
temporary_cnt = 0
def generate_new_temporary():
    global temporary_cnt 
    temporary_cnt = temporary_cnt + 1
    return "t%d" %temporary_cnt 
def clear_temporary():
    global temporary_cnt
    temporary_cnt = 0

temporary_label = 0
def generate_new_label(s):
    global temporary_label
    temporary_label = temporary_label + 1
    if(s == None) :
        s = ""
    return "l%d_%s" %(temporary_label,s)
    
    
    
=======
>>>>>>> Stashed changes
def typecheck():
    global errorflag
    errorflag = False
    # add default constructors to all classes first!
    for cid in classtable:
        c = classtable[cid]
        if not c.builtin:
            c.add_default_constructor()
    for cid in classtable:
        c = classtable[cid]
        c.typecheck()
    return not errorflag
    

def initialize_ast():
    # define In class:
    cin = Class("In", None)
    cin.builtin = True     # this is a builtin class
    cout = Class("Out", None)
    cout.builtin = True     # this, too, is a builtin class

    scanint = Method('scan_int', cin, 'public', 'static', Type('int'))
    scanint.update_body(SkipStmt(None))    # No line number information for the empty body
    cin.add_method(scanint)
    
    scanfloat = Method('scan_float', cin, 'public', 'static', Type('float'))
    scanfloat.update_body(SkipStmt(None))    # No line number information for the empty body
    cin.add_method(scanfloat)

    printint = Method('print', cout, 'public', 'static', Type('void'))
    printint.update_body(SkipStmt(None))    # No line number information for the empty body
    printint.add_var('i', 'formal', Type('int'))   # single integer formal parameter
    cout.add_method(printint)
    
    printfloat = Method('print', cout, 'public', 'static', Type('void'))
    printfloat.update_body(SkipStmt(None))    # No line number information for the empty body
    printfloat.add_var('f', 'formal', Type('float'))   # single float formal parameter
    cout.add_method(printfloat)
    
    printboolean = Method('print', cout, 'public', 'static', Type('void'))
    printboolean.update_body(SkipStmt(None))    # No line number information for the empty body
    printboolean.add_var('b', 'formal', Type('boolean'))   # single boolean formal parameter
    cout.add_method(printboolean)
    
    printstring = Method('print', cout, 'public', 'static', Type('void'))
    printstring.update_body(SkipStmt(None))    # No line number information for the empty body
    printstring.add_var('b', 'formal', Type('string'))   # single string formal parameter
    cout.add_method(printstring)

    addtotable(classtable, "In", cin)
    addtotable(classtable, "Out", cout)

class Class:
    """A class encoding Classes in Decaf"""
    def __init__(self, classname, superclass):
        self.name = classname
        self.superclass = superclass
        self.fields = {}  # dictionary, keyed by field name
        self.constructors = []
        self.methods = []
<<<<<<< Updated upstream
        if(superclass != None) :
            self.wholeoffset = superclass.wholeoffset
        else :
            self.wholeoffset = 0
=======
>>>>>>> Stashed changes
        self.builtin = False

    def printout(self):
        if (self.builtin):
            return     # Do not print builtin classes
        
        print "-----------------------------------------------------------------------------"
        print "Class Name: {0}".format(self.name)
        sc = self.superclass
        if (sc == None):
            scname = ""
        else:
            scname = sc.name
        print "Superclass Name: {0}".format(scname)
<<<<<<< Updated upstream
        print "Wholeoffset: {0}".format(self.wholeoffset)
=======
>>>>>>> Stashed changes
        print "Fields:"
        for f in self.fields:
            (self.fields[f]).printout()
        print "Constructors:"
        for k in self.constructors:
            k.printout()
        print "Methods:"
        for m in self.methods:
            m.printout()

    def typecheck(self):
        global current_class
        if (self.builtin):
            return     # Do not type check builtin classes

        current_class = self

        # First check if there are overlapping overloaded constructors and methods
        n = len(self.constructors)
        for i in range(0,n):
            for j in range(i+1, n):
                at1 = self.constructors[i].argtypes()
                at2 = self.constructors[j].argtypes()
                if (not subtype_or_incompatible(at1, at2)):
                    t1 = ",".join([str(t) for t in at1])
                    t2 = ",".join([str(t) for t in at2])
                    signal_type_error("Overlapping types in overloaded constructors: `{0}' (line {2}) and `{1}'".format(t1,t2, self.constructors[i].body.lines), self.constructors[j].body.lines)

        n = len(self.methods)
        for i in range(0,n):
            for j in range(i+1, n):
                if (self.methods[i].name != self.methods[j].name):
                    # Check only overloaded methods
                    break
                at1 = self.methods[i].argtypes()
                at2 = self.methods[j].argtypes()
                if (not subtype_or_incompatible(at1, at2)):
                    t1 = ",".join([str(t) for t in at1])
                    t2 = ",".join([str(t) for t in at2])
                    signal_type_error("Overlapping types in overloaded methods: `{0}' (line {2}) and `{1}'".format(t1,t2, self.methods[i].body.lines), self.methods[j].body.lines)

        for k in self.constructors:
            k.typecheck()
            # ensure it does not have a return statement
            if (k.body.has_return() > 0):
                signal_type_error("Constructor cannot have a return statement", k.body.lines)
        for m in self.methods:
            m.typecheck()
            # ensure that non-void methods have a return statement on every path
            if (m.rtype.is_subtype_of(Type('void'))): 
                if (isinstance(m.body, BlockStmt)):
                    m.body.stmtlist.append(ReturnStmt(None,m.body.lines))
                else:
<<<<<<< Updated upstream
                    m.body = BlockStmt([m.body, ReturnStmt(None,m.body.lines)], m.body.lines)
=======
                    m.body = BlockStmt([m.body, ReturnStmt(None,m.body.lines)], mbody.lines)
>>>>>>> Stashed changes
            else:
                if (m.body.has_return() < 2):
                    signal_type_error("Method needs a return statement on every control flow path", m.body.lines)

    def add_field(self, fname, field):
        self.fields[fname] = field
<<<<<<< Updated upstream
        field.offset = self.wholeoffset
        self.wholeoffset += 1
        
=======
>>>>>>> Stashed changes
    def add_constructor(self, constr):
        self.constructors.append(constr)
    def add_method(self, method):
        self.methods.append(method)

    def add_default_constructor(self):
        # check if a parameterless constructor already exists
        exists = False
        for c in self.constructors:
            if (len(c.vars.get_params()) == 0):
                exists = True
                break
        if (not exists):
            c = Constructor(self.name, 'public')
            c.update_body(SkipStmt(None))
            self.constructors.append(c)            

    def lookup_field(self, fname):
        return lookup(self.fields, fname)

    def is_subclass_of(self, other):
        if (self.name == other.name):
            return True
        elif (self.superclass != None):
<<<<<<< Updated upstream
            if (self.superclass == other):
                return True
            else:
                return self.superclass.is_subclass_of(other)
=======
             if (self.superclass == other):
                 return True
             else:
                 return self.superclass.is_subclass_of(other)
>>>>>>> Stashed changes
        return False
            
class Type:
    """A class encoding Types in Decaf"""
    def __init__(self, basetype, params=None, literal=False):
        if ((params == None) or (params == 0)):
            if (basetype in ['int', 'boolean', 'float', 'string', 'void', 'error', 'null']):
                self.kind = 'basic'
                self.typename = basetype
            elif (not literal):
                self.kind = 'user'
                self.baseclass = basetype
            else:
                self.kind = 'class_literal'
                self.baseclass = basetype
        else:
            if (params == 1):
                bt = basetype
            else:
                bt = Type(basetype, params=params-1)
            self.kind = 'array'
            self.basetype = bt

    def __str__(self):
        if (self.kind == 'array'):
            return 'array(%s)'%(self.basetype.__str__())
        elif (self.kind == 'user'):
            return 'user(%s)'%str(self.baseclass.name)
        elif (self.kind == 'class_literal'):
            return 'class_literal(%s)'%str(self.baseclass.name)
        else:
            return self.typename

    def __repr(self):
        return self.__str__()

    def is_subtype_of(self, other):
        if (self.kind == 'basic'):
            if other.kind == 'basic':
                if (self.typename == other.typename):
                    return True
                elif (self.typename == 'int') and (other.typename == 'float'):
                    return True
            elif (self.typename == 'null'):
                return (other.kind == 'user') or (other.kind == 'array')
        elif (self.kind == 'user'):
            if (other.kind == 'user'):
                return self.baseclass.is_subclass_of(other.baseclass)
        elif (self.kind == 'class_literal'):
            if (other.kind == 'class_literal'):
                return self.baseclass.is_subclass_of(other.baseclass)
        elif (self.kind == 'array') and (other.kind =='array'):
            return self.basetype.is_subtype_of(other.basetype)
        return False 

    def isint(self):
        return self.kind == 'basic' and self.typename == 'int'
        
    def isnumeric(self):
        return self.kind == 'basic' and (self.typename == 'int'
                                         or self.typename == 'float')
    def isboolean(self):
        return self.kind == 'basic' and self.typename == 'boolean'

    def isok(self):
        return not (self.kind == 'basic' and self.typename == 'error')
        

class Field:
    """A class encoding fields and their attributes in Decaf"""
    lastfield = 0
    def __init__(self, fname, fclass, visibility, storage, ftype):
        Field.lastfield += 1
        self.name = fname
        self.id = Field.lastfield
        self.inclass = fclass
        self.visibility = visibility
        self.storage = storage
        self.type = ftype

    def printout(self):
<<<<<<< Updated upstream
        print "FIELD {0}, {1}, {2}, {3}, {4}, {5}, {6}".format(self.id, self.name, self.inclass.name, self.visibility, self.storage, self.type, self.offset)
=======
        print "FIELD {0}, {1}, {2}, {3}, {4}, {5}".format(self.id, self.name, self.inclass.name, self.visibility, self.storage, self.type)
>>>>>>> Stashed changes

class Method:
    """A class encoding methods and their attributes in Decaf"""
    def __init__(self, mname, mclass, visibility, storage, rtype):
        global lastmethod
        self.name = mname
        lastmethod += 1
        self.id = lastmethod
        self.inclass = mclass
        self.visibility = visibility
        self.storage = storage
        self.rtype = rtype
        self.vars = VarTable()
        
    def update_body(self, body):
        self.body = body

    def add_var(self, vname, vkind, vtype):
        self.vars.add_var(vname, vkind, vtype)

    def printout(self):
        print "METHOD: {0}, {1}, {2}, {3}, {4}, {5}".format(self.id, self.name, self.inclass.name, self.visibility, self.storage, self.rtype)
        print "Method Parameters:",
        print ', '.join(["%d"%v.id for v in self.vars.get_params()])
        self.vars.printout()
        print "Method Body:"
        self.body.printout()

    def argtypes(self):
        return [v.type for v in self.vars.get_params()]

    def typecheck(self):
        global current_method
        current_method = self
        self.body.typecheck()
        
class Constructor:
    """A class encoding constructors and their attributes in Decaf"""
    def __init__(self, cname, visibility):
        global lastconstructor
        self.name = cname
        lastconstructor += 1
        self.id = lastconstructor
        self.visibility = visibility
        self.vars = VarTable()
        
    def update_body(self, body):
        self.body = body

    def add_var(self, vname, vkind, vtype):
        self.vars.add_var(vname, vkind, vtype)

    def printout(self):
        print "CONSTRUCTOR: {0}, {1}".format(self.id, self.visibility)
        print "Constructor Parameters:",
        print ', '.join(["%d"%v.id for v in self.vars.get_params()])
        self.vars.printout()
        print "Constructor Body:"
        self.body.printout()

    def argtypes(self):
        return [v.type for v in self.vars.get_params()]
        
    def typecheck(self):
        self.body.typecheck()

class VarTable:
    """ Table of variables in each method/constructor"""
    def __init__(self):
        self.vars = {0:{}}
        self.lastvar = 0
        self.lastblock = 0
        self.levels = [0]

    def enter_block(self):
        self.lastblock += 1
        self.levels.insert(0, self.lastblock)
        self.vars[self.lastblock] = {}

    def leave_block(self):
        self.levels = self.levels[1:]
        # where should we check if we can indeed leave the block?

    def add_var(self, vname, vkind, vtype):
        self.lastvar += 1
        c = self.levels[0]   # current block number
        v = Variable(vname, self.lastvar, vkind, vtype)
        vbl = self.vars[c]  # list of variables in current block
        vbl[vname] = v
    
    def _find_in_block(self, vname, b):
        if (b in self.vars):
            # block exists
            if (vname in self.vars[b]):
                return self.vars[b][vname]
        # Otherwise, either block b does not exist, or vname is not in block b
        return None

    def find_in_current_block(self, vname):
        return self._find_in_block(vname, self.levels[0])

    def find_in_scope(self, vname):
        for b in self.levels:
            v = self._find_in_block(vname, b)
            if (v != None):
                return v
            # otherwise, locate in enclosing block until we run out
        return None

    def get_params(self):
        outermost = self.vars[0]  # 0 is the outermost block
        vars = [outermost[vname] for vname in outermost if outermost[vname].kind=='formal']
        vars_ids = [(v.id,v) for v in vars]  # get the ids as well, so that we can order them
        vars_ids.sort()
        return [v for (i,v) in vars_ids]   # in their order of definition!

    def printout(self):
        print "Variable Table:"
        for b in range(self.lastblock+1):
            for vname in self.vars[b]:
                v = self.vars[b][vname]
                v.printout()
        

class Variable:
    """ Record for a single variable"""
    def __init__(self, vname, id, vkind, vtype):
        self.name = vname
        self.id = id
        self.kind = vkind
        self.type = vtype

    def printout(self):
        print "VARIABLE {0}, {1}, {2}, {3}".format(self.id, self.name, self.kind, self.type)
    

class Stmt(object): 
    """ Top-level (abstract) class representing all statements"""

class IfStmt(Stmt):
    def __init__(self, condition, thenpart, elsepart, lines):
        self.lines = lines
        self.condition = condition
        self.thenpart = thenpart
        self.elsepart = elsepart
        self.__typecorrect = None

    def printout(self):
        print "If(",
        self.condition.printout()
        print ", ",
        self.thenpart.printout()
        print ", ",
        self.elsepart.printout()
        print ")"

    def typecheck(self):
        if (self.__typecorrect == None):
            b = self.condition.typeof()
            if (not b.isboolean()):
                signal_type_error("Type error in If statement's condition: boolean expected, found {0}".format(str(b)), self.lines)
                self.__typecorrect = False
            self.__typecorrect = b.isboolean() and self.thenpart.typecheck() and self.elsepart.typecheck()
        return self.__typecorrect

    def has_return(self):
        # 0 if none, 1 if at least one path has a return, 2 if all paths have a return
        r = self.thenpart.has_return() + self.elsepart.has_return()
        if (r == 4):
            return 2
        elif (r > 0):
            return 1
        else:
            return 0

class WhileStmt(Stmt):
    def __init__(self, cond, body, lines):
        self.lines = lines
        self.cond = cond
        self.body = body
        self.__typecorrect = None

    def printout(self):
        print "While(",
        self.cond.printout()
        print ", ",
        self.body.printout()
        print ")"

    def typecheck(self):
        if (self.__typecorrect == None):
            b = self.cond.typeof()
            if (not b.isboolean()):
                signal_type_error("Type error in While statement's condition: boolean expected, found {0}".format(str(b)), self.lines)
                self.__typecorrect = False
            self.__typecorrect = b.isboolean() and self.body.typecheck()
        return self.__typecorrect

    def has_return(self):
        # 0 if none, 1 if at least one path has a return, 2 if all paths have a return
        if (self.body.has_return() > 0):
            return 1
        else:
            return 0

class ForStmt(Stmt):
    def __init__(self, init, cond, update, body, lines):
        self.lines = lines
        self.init = init
        self.cond = cond
        self.update = update
        self.body = body
        self.__typecorrect = None

    def printout(self):
        print "For(",
        if (self.init != None):
            self.init.printout()
        print ", ",
        if (self.cond != None):
            self.cond.printout()
        print ", ",
        if (self.update != None):
            self.update.printout()
        print ", ",
        self.body.printout()
        print ")"

    def typecheck(self):
        if (self.__typecorrect == None):
            a = True
            if (self.init != None):
                a = a and self.init.typeof().isok()
            if (self.update != None):
                a = a and self.update.typeof().isok()
            if (self.cond != None):
                b = self.cond.typeof()
                if (not b.isboolean()):
                    signal_type_error("Type error in For statement's condition: boolean expected, found {0}".format(str(b)), self.lines)
                    a = False
            a = a and self.body.typecheck()
            self.__typecorrect = a
        return self.__typecorrect
        
    def has_return(self):
        # 0 if none, 1 if at least one path has a return, 2 if all paths have a return
        if (self.body.has_return() > 0):
            return 1
        else:
            return 0


class ReturnStmt(Stmt):
    def __init__(self, expr, lines):
        self.lines = lines
        self.expr = expr
        self.__typecorrect = None

    def printout(self):
        print "Return(",
        if (self.expr != None):
            self.expr.printout()
        print ")"

    def typecheck(self):
        global current_method
        if (self.__typecorrect == None):
            if (self.expr == None):
                argtype = Type('void')
            else:
                argtype = self.expr.typeof()
            self.__typecorrect = argtype.is_subtype_of(current_method.rtype)
            if (argtype.isok() and (not self.__typecorrect)):
                signal_type_error("Type error in Return statement: {0} expected, found {1}".format(str(current_method.rtype), str(argtype)), self.lines)
        return self.__typecorrect

    def has_return(self):
        return 2
    
class BlockStmt(Stmt):
    def __init__(self, stmtlist, lines):
        self.lines = lines
        self.stmtlist = [s for s in stmtlist if (s != None) and (not isinstance(s, SkipStmt))]
        self.__typecorrect = None

    def printout(self):
        print "Block(["
        if (len(self.stmtlist) > 0):
            self.stmtlist[0].printout()
        for s in self.stmtlist[1:]:
            print ", ",
            s.printout()
        print "])"

    def typecheck(self):
        if (self.__typecorrect == None):
            self.__typecorrect = all([s.typecheck() for s in self.stmtlist])
        return self.__typecorrect

    def has_return(self):
        rs = [s.has_return() for s in self.stmtlist]
        if (2 in rs):
            return 2
        elif (1 in rs):
            return 1
        else:
            return 0

class BreakStmt(Stmt):
    def __init__(self, lines):
        self.lines = lines
        self.__typecorrect = True

    def printout(self):
        print "Break"

    def typecheck(self):
        return self.__typecorrect

    def has_return(self):
        return 0
        
class ContinueStmt(Stmt):
    def __init__(self, lines):
        self.lines = lines
        self.__typecorrect = True

    def printout(self):
        print "Continue"

    def typecheck(self):
        return self.__typecorrect

    def has_return(self):
        return 0
        
    
class ExprStmt(Stmt):
    def __init__(self, expr, lines):
        self.lines = lines
        self.expr = expr
        self.__typecorrect = None

    def printout(self):
        print "Expr(",
        self.expr.printout()
        print ")"

    def typecheck(self):
        if (self.__typecorrect == None):
            if (self.expr.typeof().kind == 'error'):
                self.__typecorrect = False
            else:
                self.__typecorrect = True
        return self.__typecorrect

    def has_return(self):
        return 0
        
    
class SkipStmt(Stmt):
    def __init__(self, lines):
        self.lines = lines
        self.__typecorrect = True

    def printout(self):
        print "Skip"

    def typecheck(self):
        return self.__typecorrect

    def has_return(self):
        return 0
        

    
class Expr(object):
    '''Class representing all expressions in Decaf'''
    def __repr__(self):
        return "Unknown expression"
    def printout(self):
        print self, 


class ConstantExpr(Expr):
    def __init__(self, kind, arg=None, lines=None):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.kind = kind
        if (kind=='int'):
            self.int = arg
        elif (kind == 'float'):
            self.float = arg
        elif (kind == 'string'):
            self.string = arg
        self.__typeof = None
<<<<<<< Updated upstream
        self.rcode = []
        self.at = ""
        self.t = ""
=======
>>>>>>> Stashed changes

            
    def __repr__(self):
        s = "Unknown"
        if (self.kind == 'int'):
            s = "Integer-constant(%d)"%self.int
        elif (self.kind == 'float'):
            s = "Float-constant(%g)"%self.float
        elif (self.kind == 'string'):
            s = "String-constant(%s)"%self.string
        elif (self.kind == 'Null'):
            s = "Null"
        elif (self.kind == 'True'):
            s = "True"
        elif (self.kind == 'False'):
            s = "False"
        return "Constant({0})".format(s)

    def typeof(self):
        if (self.__typeof == None):
            if (self.kind == 'int'):
                self.__typeof = Type('int')
            elif (self.kind == 'float'):
                self.__typeof = Type('float')
            elif (self.kind == 'string'):
                self.__typeof = Type('string')
            elif (self.kind == 'Null'):
                self.__typeof = Type('null')
            elif (self.kind == 'True'):
                self.__typeof = Type('boolean')
            elif (self.kind == 'False'):
                self.__typeof = Type('boolean')
        return self.__typeof
<<<<<<< Updated upstream
    
    def codegen(self):
        code = ["Unknown"]
        if (self.kind == 'int'):
            self.t = generate_new_temporary()
            code=["    move_immed_i %s,%d" %(self.t,self.int)]
        elif (self.kind == 'float'):
            self.t = generate_new_temporary()
            code = ["    move_immed_f %s,%d" %(self.t,self.float)]
        elif (self.kind == 'string'):
            code = ["    Simplified: has no string constants"]
        elif (self.kind == 'Null'):
            self.t = generate_new_temporary()
            code = ["    move_immed_i %s,%d" %(self.t,0)]
        elif (self.kind == 'True'):
            self.t = generate_new_temporary()
            code = ["    move_immed_i %s,%d" %(self.t, 1)]
        elif (self.kind == 'False'):
            self.t = generate_new_temporary()
            code = ["    move_immed_i %s,%d" %(self.t,0)]
        self.rcode = code 

class VarExpr(Expr):
    def __init__(self, var, lines):
=======
            

class VarExpr(Expr):
    def __init__(self, var, lines):
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.var = var
        self.__typeof = None
    def __repr__(self):
        return "Variable(%d)"%self.var.id

    def typeof(self):
        if (self.__typeof == None):
            self.__typeof = self.var.type
        return self.__typeof

class UnaryExpr(Expr):
    def __init__(self, uop, expr, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.uop = uop
        self.arg = expr
        self.__typeof = None
    def __repr__(self):
        return "Unary({0}, {1})".format(self.uop, self.arg)

    def typeof(self):
        if (self.__typeof == None):
            argtype = self.arg.typeof()
            self.__typeof = Type('error')
            if (self.uop == 'uminus'):
<<<<<<< Updated upstream
                if ((argtype.isnumeric())) :
=======
                if ((argtype.isnumeric()):
>>>>>>> Stashed changes
                    self.__typeof = argtype
                elif (argtype.kind != 'error'):
                    # not already in error
                    signal_type_error("Type error in unary minus expression: int/float expected, found {0}".format(str(argtype)), self.arg.lines)
            elif (self.uop == 'neg'):
                if (argtype.isboolean()):
                    self.__typeof = argtype
                elif (argtype.kind != 'error'):
                    # not already in error
                    signal_type_error("Type error in unary negation expression: boolean expected, found {0}".format(str(argtype)), self.arg.lines)
        return self.__typeof
<<<<<<< Updated upstream
                    
=======

    def codegen(self):
        code = []
        self.t = generate_new_temporary()
        if (self.uop == 'uminus'):
            arg.codegen()
            code.append("move_immed_i %s,%d\n" % self.t % 0)
            code.append("isub %s,%s,%s" % self.t % self.t % self.t)
        elif (self.uop == 'neg'):
            arg.codegen()
            code.append("move_immed_i %s,%d\n" % self.t % 1)
            code.append("isub %s,%s,%s" % self.t % self.t % self.t)
        self.rcode = code

>>>>>>> Stashed changes
def signal_bop_error(argpos, bop, argtype, arg, possible_types, ptype_string):
    if (argtype.kind not in (['error'] + possible_types)):
        # not already in error
        signal_type_error("Type error in {0} argument of binary {1} expression: {2} expected, found {3}".format(argpos, bop, ptype_string, str(argtype)), arg.lines)
        
class BinaryExpr(Expr):
    def __init__(self, bop, arg1, arg2, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.bop = bop
        self.arg1 = arg1
        self.arg2 = arg2
        self.__typeof = None
    def __repr__(self):
        return "Binary({0}, {1}, {2})".format(self.bop,self.arg1,self.arg2)            

    def typeof(self):
        if (self.__typeof == None):
            arg1type = self.arg1.typeof()
            arg2type = self.arg2.typeof()
            self.__typeof = Type('error')
            if (self.bop in ['add', 'sub', 'mul', 'div']):
                if (arg1type.isint()) and (arg2type.isint()):
                    self.__typeof = arg1type
                elif (arg1type.isnumeric()) and (arg2type.isnumeric()): 
                    self.__typeof = Type('float')
                else:
                    if (arg1type.isok() and arg2type.isok()):
                        signal_bop_error('first', self.bop, arg1type, self.arg1,
                                         ['int', 'float'], 'int/float')
                        signal_bop_error('second', self.bop, arg2type, self.arg2,
                                         ['int', 'float'], 'int/float')
                    
            elif (self.bop in ['lt', 'leq', 'gt', 'geq']):
                if ((arg1type.isnumeric()) and (arg2type.isnumeric())): 
                    self.__typeof = Type('boolean')
                else:
                    if (arg1type.isok() and arg2type.isok()):
                        signal_bop_error('first', self.bop, arg1type, self.arg1,
                                         ['int', 'float'], 'int/float')
                        signal_bop_error('second', self.bop, arg2type, self.arg2,
                                         ['int', 'float'], 'int/float')
                    
            elif (self.bop in ['and', 'or']):
                if ((arg1type.isboolean()) and (arg2type.isboolean())):
                    self.__typeof = Type('boolean')
                else:
                    if (arg1type.isok() and arg2type.isok()):
                        signal_bop_error('first', self.bop, arg1type, self.arg1,
                                         ['boolean'], 'boolean')
                        signal_bop_error('second', self.bop, arg2type, self.arg2,
                                         ['boolean'], 'boolean')
            else:
                # equality/disequality
                if ((arg1type.isok()) and (arg2type.isok())):
                    if ((arg1type.is_subtype_of(arg2type)) or (arg2type.is_subtype_of(arg1type))):
                        self.__typeof = Type('boolean')
                    else:
                        signal_type_error('Type error in arguments of binary {0} expression: compatible types expected, found {1} and {2}'.format(self.bop, str(arg1type), str(arg2type)), self.lines)
                       
        return self.__typeof

<<<<<<< Updated upstream
class AssignExpr(Expr):
    def __init__(self, lhs, rhs, lines):
=======
    def codegen(self):
        code = []
        self.t = generate_new_temporary()
        self.arg1.codegen()
        self.arg2.codegen()
        if (self.bop == '+'):
            code = ["iadd %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == '-'):
            code = ["isub %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == '*'):
            code = ["imul %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == '/'):
            code = ["idiv %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == '%'):
            code = ["imod %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == '>'):
            code = ["igt %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == '>='):
            code = ["igeq %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == '<'):
            code = ["ilt %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == '<='):
            code = ["ileq %s,%s,%s" % self.t % self.arg1.codegen() % self.arg2.codegen()]
        elif (self.bop == 'and'):
            endlabel = generate_new_label("binary_end")
            falselabel = generate_new_label("binary_false")
            code = ["beq %s,%d,%s" % self.arg1.codegen() % 0 % falselabel]
            code.append("beq %s,%d,%s" % self.arg2.codegen() % 0 % falselabel)
            code.append("move_immed_i %s,1" % self.t)
            code.append("jmp %s" % endlabel)
            code.append("%s:" % falselabel)
            code.append("move_immed_i %s,0" % self.t)
            code.append("%s:" % endlabel)
        elif (self.bop == 'or'):
            endlabel = generate_new_label("binary_end")
            truelabel = generate_new_label("binary_true")
            code = ["beq %s,%d,%s" % self.arg1.codegen() % 1 % truelabel]
            code.append("beq %s,%d,%s" % self.arg2.codegen() % 1 % truelabel)
            code.append("move_immed_i %s,0" % self.t)
            code.append("jmp %s" % endlabel)
            code.append("%s:" % truelabel)
            code.append("move_immed_i %s,1" % self.t)
            code.append("%s:" % endlabel)
        code.append("\n")
        return code
class AssignExpr(Expr):
    def __init__(self, lhs, rhs, lines):
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.lhs = lhs
        self.rhs = rhs
        self.__typeof = None
    def __repr__(self):
        return "Assign({0}, {1}, {2}, {3})".format(self.lhs, self.rhs, self.lhs.typeof(), self.rhs.typeof())

    def typeof(self):
        if (self.__typeof == None):
            lhstype = self.lhs.typeof()
            rhstype = self.rhs.typeof()
            if (lhstype.isok() and rhstype.isok()):
                if (rhstype.is_subtype_of(lhstype)):
                    self.__typeof = rhstype
                else:
                    self.__typeof = Type('error')
                    signal_type_error('Type error in assign expression: compatible types expected, found {0} and {1}'.format(str(lhstype), str(rhstype)), self.lines)
            else:
                self.__typeof = Type('error')
        return self.__typeof
    
class AutoExpr(Expr):
    def __init__(self, arg, oper, when, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.arg = arg
        self.oper = oper
        self.when = when
        self.__typeof = None
    def __repr__(self):
        return "Auto({0}, {1}, {2})".format(self.arg, self.oper, self.when)

    def typeof(self):
        if (self.__typeof == None):
            argtype = self.arg.typeof()
            if (argtype.isnumeric()):
                self.__typeof = argtype
            else:
                self.__typeof = Type('error')
                if (argtype.isok()):
                    signal_type_error('Type error in auto expression: int/float expected, found {0}'.format(str(argtype)), self.lines)
        return self.__typeof

<<<<<<< Updated upstream
=======
    def codegen(self):
        code = []
        self.arg.codegen()
        oneAdd = generate_new_temporary()
        code.append("move_immed_i %s,%d" %(oneAdd,1))
        if (self.when == 'pre' & & self.oper == 'inc'):
            code.extend(arg.rCode)
            code.append("iadd %s,%s,%s" % (self.arg.t, self.arg.t, oneAdd))
        elif (self.when == 'pre' & & self.oper == 'dec'):
            code.extend(arg.rCode)
            code.append("isub %s,%s,%s" % (self.arg.t, self.arg.t, oneAdd))
        elif (self.when == 'post' & & self.oper == 'inc'):
            code.append("iadd %s,%s,%s" % (self.arg.t, self.arg.t, oneAdd))
            code.extend(arg.rCode)
        elif (self.when == 'post' & & self.oper == 'dec'):
            code.append("isub %s,%s,%s" % (self.arg.t, self.arg.t, oneAdd))
            code.extend(arg.rCode)
        self.code = code
        return code

>>>>>>> Stashed changes
def find_applicable_methods(acc, baseclass, mname, argtypes):
    ms = []
    for m in baseclass.methods:
        if ((m.name == mname) and (m.storage == acc)):
            params = m.vars.get_params()
            paramtypes = [v.type for v in params]
            if ((len(paramtypes) == len(argtypes)) and
                all([(a.is_subtype_of(p)) for (a,p) in (zip(argtypes, paramtypes))])):
                # if every arg is a subtype of corresponding parameter
                ms.append((m, paramtypes))
    
    return ms

def find_applicable_constructors(baseclass, argtypes):
    cs = []
    for c in baseclass.constructors:
        params = c.vars.get_params()
        paramtypes = [v.type for v in params]
        if ((len(paramtypes) == len(argtypes)) and
            all([(a.is_subtype_of(p)) for (a,p) in (zip(argtypes, paramtypes))])):
            # if every arg is a subtype of corresponding parameter
            cs.append((c, paramtypes))
    
    return cs

def most_specific_method(ms):
    mst = None
    result = None
    for (m, t) in ms:
        if (mst == None):
            mst = t
            result = m
        else:
            if all([a.is_subtype_of(b) for (a,b) in zip(mst, t)]):
                # current most specific type is at least as specific as t
                continue
            elif all([b.is_subtype_of(a) for (a,b) in zip(mst, t)]):
                # current t is at least as specific as the most specific type 
                mst = t
                result = m
            else:
                # t is no more specific than mst, nor vice-versa
                return (None, (mst, result, t, m))
                break
    return (result, None)
        
def subtype_or_incompatible(tl1, tl2):
    #  True iff tl1 is a subtype of tl2 or tl2 is a subtype of tl1, or the two type lists are incompatible
    n = len(tl1)
    if (len(tl2) != n):
        return True

    # is tl1 a subtype of tl2?  return False if any incompatible types are found
    subt = True
    for i in range(0,n):
        t1 = tl1[i]
        t2 = tl2[i]
        if (not t1.is_subtype_of(t2)):
            subt = False
            if (t2.is_subtype_of(t1)):
                # tl2 may be a subtype of tl1, so we need to wait to check that
                break
            else:
                # types are incompatible
                return True
    if (subt):
        return True
    # Check the other direction
    for i in range(0,n):
        t1 = tl1[i]
        t2 = tl2[i]
        if (not t2.is_subtype_of(t1)):
            return False
    # tl2 is a subtype of tl1
    return True    

def resolve_method(acc, baseclass, mname, argtypes, current, lineno):
    original_baseclass = baseclass
    while (baseclass != None):
        ms = find_applicable_methods(acc, baseclass, mname, argtypes)
        (m, errorc) = most_specific_method(ms)
        if ((len(ms) > 0) and 
            (m != None) and ( (m.visibility == 'public') or (baseclass == current) )):
            return m
        elif (len(ms) > 0) and (m == None):
            # there were applicable methods but no unique one.
            (t1, m1, t2, m2) = errorc
            signal_type_error("Ambiguity in resolving overloaded method {0}: methods with types '{1}' and '{2}' in class {3}".format(mname, str(t1), str(t2), baseclass.name), lineno)
            return None
        else:
            baseclass = baseclass.superclass
    # search for mname failed,
    signal_type_error("No accessible method with name {0} in class {1}".format(mname, original_baseclass.name), lineno)
    return None

def resolve_constructor(baseclass, current, argtypes, lineno):
    cs = find_applicable_constructors(baseclass, argtypes)
    (c, errorc) = most_specific_method(cs)
    if ((len(cs) > 0) and 
        (c != None) and ( (c.visibility == 'public') or (baseclass == current) )):
        return c
    elif (len(cs) > 0) and (c == None):
        # there were applicable constructors but no unique one.
        (t1, c1, t2, c2) = errorc
        signal_type_error("Ambiguity in resolving overloaded constructor {0}: constructors with types '{1}' and '{2}'}".format(baseclass.name, str(t1), str(t2)), lineno)
        return None
    else:
        signal_type_error("No accessible constructor for class {0}".format(baseclass.name), lineno)
        return None
    

def resolve_field(acc, baseclass, fname, current):
    while (baseclass != None):
        f = baseclass.lookup_field(fname)
        if ((f != None) and (f.storage == acc)
            and ( (f.visibility == 'public') or (baseclass == current) )):
            return f
        else:
            baseclass = baseclass.superclass
    # search for fname failed,
    return None

class FieldAccessExpr(Expr):
    def __init__(self, base, fname, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.base = base
        self.fname = fname
        self.__typeof = None
        self.field = None
        
    def __repr__(self):
        return "Field-access({0}, {1}, {2})".format(self.base, self.fname, self.field.id)

    def typeof(self):
        if (self.__typeof == None):
            # resolve the field name first
            btype = self.base.typeof()
            if btype.isok():
                if btype.kind not in ['user', 'class_literal']:
                    signal_type_error("User-defined class/instance type expected, found {0}".format(str(btype)), self.lines)
                    self.__typeof = Type('error')
                else:
                    if btype.kind == 'user':
                        # user-defined instance type:
                        acc = 'instance'
                    else:
                        # user-defined class type
                        acc = 'static'

                    baseclass =  btype.baseclass
                    j = resolve_field(acc, baseclass, self.fname, current_class)
                    if (j == None):
                        signal_type_error("No accessible field with name {0} in class {1}".format(self.fname, baseclass.name), self.lines)
                        self.__typeof = Type('error')
                    else:
                        self.field = j
                        self.__typeof = j.type
                        
        return self.__typeof
    
class MethodInvocationExpr(Expr):
    def __init__(self, field, args, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.base = field.base
        self.mname = field.fname
        self.args = args
        self.method = None
        self.__typeof = None
    def __repr__(self):
        return "Method-call({0}, {1}, {2})".format(self.base, self.mname, self.args)

    def typeof(self):
        if (self.__typeof == None):
            # resolve the method name first
            btype = self.base.typeof()
            if btype.isok():
                if btype.kind not in ['user', 'class_literal']:
                    signal_type_error("User-defined class/instance type expected, found {0}".format(str(btype)), self.lines)
                    self.__typeof = Type('error')
                else:
                    if btype.kind == 'user':
                        # user-defined instance type:
                        acc = 'instance'
                    else:
                        # user-defined class type
                        acc = 'static'

                    baseclass =  btype.baseclass
                    argtypes = [a.typeof() for a in self.args]
                    if (all([a.isok() for a in argtypes])):
                        j = resolve_method(acc, baseclass, self.mname, argtypes, current_class, self.lines)
                        
                        if (j == None):
                            self.__typeof = Type('error')
                        else:
                            self.method = j
                            self.__typeof = j.rtype
                    else:
                        self.__typeof = Type('error')
<<<<<<< Updated upstream
        return self.__typeof 
        
    
class NewObjectExpr(Expr):
    def __init__(self, cref, args, lines):
=======
        return self.__typeof
    
class NewObjectExpr(Expr):
    def __init__(self, cref, args, lines):
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.classref = cref
        self.args = args
        self.__typeof = None
    def __repr__(self):
        return "New-object({0}, {1})".format(self.classref.name, self.args)

    def typeof(self):
        if (self.__typeof == None):
            # resolve the constructor name first
            argtypes = [a.typeof() for a in self.args]
            if (all([a.isok() for a in argtypes])):
                j = resolve_constructor(current_class, self.classref, argtypes, self.lines)
                if (j == None):
                    self.__typeof = Type('error')
                else:
                    self.constructor = j
                    self.__typeof = Type(self.classref)
            else:
                # type error in some argument; already signaled before
                self.__typeof = Type('error')
        return self.__typeof
    
    
class ThisExpr(Expr):
    global current_class
    def __init__(self, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.__typeof = None
    def __repr__(self):
        return "This"
    def typeof(self):
        if (self.__typeof == None):
            self.__typeof = Type(current_class)
        return self.__typeof
        
class SuperExpr(Expr):
    global current_class
    def __init__(self, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.__typeof = None
    def __repr__(self):
        return "Super"

    def typeof(self):
        if (self.__typeof == None):
            if (current_class.superclass != None):
                self.__typeof = Type(current_class.superclass)
            else:
                self.__typeof = Type('error')
                signal_type_error("Type error in Super expression: class {0} has no superclass".format(str(current_class)), self.lines)
        return self.__typeof
    
    
class ClassReferenceExpr(Expr):
    def __init__(self, cref, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.classref = cref
        self.__typeof = None
    def __repr__(self):
        return "ClassReference({0})".format(self.classref.name)

    def typeof(self):
        if (self.__typeof == None):
            self.__typeof = Type(self.classref, literal=True)
        return self.__typeof
    
class ArrayAccessExpr(Expr):
    def __init__(self, base, index, lines):
<<<<<<< Updated upstream
=======
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.base = base
        self.index = index
        self.__typeof = None
    def __repr__(self):
        return "Array-access({0}, {1})".format(self.base, self.index)

    def typeof(self):
        if (self.__typeof == None):
            if (not self.index.typeof().isint()):
                signal_type_error("Type error in index of Array Index expression: integer expected, found {0}".format(str(self.index.typeof())), self.index.lines)
                mytype = Type('error')
            if (self.base.typeof().kind != 'array'):
                signal_type_error("Type error in base of Array Index expression: array type expected, found {0}".format(str(self.base.typeof())), self.base.lines)
                mytype = Type('error')
            else:
                mytype = self.base.typeof().basetype
            self.__typeof = mytype
        return self.__typeof
                
<<<<<<< Updated upstream

class NewArrayExpr(Expr):
    def __init__(self, basetype, args, lines):
=======
                

class NewArrayExpr(Expr):
    def __init__(self, basetype, args, lines):
        self.lcode = []
        self.rcode = []
>>>>>>> Stashed changes
        self.lines = lines
        self.basetype = basetype
        self.args = args
        self.__typeof = None
<<<<<<< Updated upstream
        self.t = ""
        self.lcode = []
        self.rcode = []
        self.at = ""
        self.mem = ""
        
    def __repr__(self):
        s = "New-array({0}, {1})".format(self.basetype, self.args)
        self.codegen()
        for i in self.rcode:
            s += "\n"
            s += i
        return s
        
=======
    def __repr__(self):
        return "New-array({0}, {1})".format(self.basetype, self.args)
>>>>>>> Stashed changes

    def typeof(self):
        if (self.__typeof == None):
            mytype = Type(self.basetype, len(self.args))
            for a in self.args:
                if (not a.typeof().isok()):
                    # previous error, so mark and pass
                    mytype = Type('error')
                    break
                if (not a.typeof().isint()):
                    # int arg type expected
                    signal_type_error("Type error in argument to New Array expression: int expected, found {0}".format(str(a.typeof())), a.lines)
                    mytype = Type('error')
                    break
            self.__typeof = mytype
        return self.__typeof
<<<<<<< Updated upstream
    
    def recur(self, args, taddr):
        if(len(args) == 0) : 
            return []
        label1 = generate_new_label("alloc_begin")
        label2 = generate_new_label("alloc_end")
        args[0].codegen();
        ans = args[0].rcode
        ans.append("    halloc %s %s" %(taddr, args[0].t))
        if(len(args)>1):
            i = generate_new_temporary()
            ans.append("    move %s %s" %(i, args[0].t))
            jud = generate_new_temporary()
            zero = generate_new_temporary()
            one = generate_new_temporary()
            ans.append("    move_immed_i %s %d"%(one,1))
            ans.append("    move_immed_i %s %d" %(zero,0))
            ans.append("    igt %s %s %s" %(jud,i,zero))
            ans.append("    bz %s %s" %(jud, label2))
            ans.append("#begin of alloc an array")
            ans.append("%s:" % label1)
            ans.append("    isub %s %s %s"%(i,i,one))
            nxt_taddr = generate_new_temporary()
            ans.append("    move %s %s" %(nxt_taddr,taddr))
            ans.append("    iadd %s %s %s" %(nxt_taddr,nxt_taddr,i))
            ans.extend(self.recur(args[1:], nxt_taddr))
            ans.append("    bz %s %s" %(i, label2))
            ans.append("    jmp %s" %label1)
            ans.append("#end of alloc an array")
            ans.append("%s:" %label2)
        return ans
        
        
    def codegen(self):
        self.t = self.at = generate_new_temporary()
        self.lcode = []
        self.rcode = self.recur(self.args, self.t)
    
=======

>>>>>>> Stashed changes

def signal_type_error(string, lineno):
    global errorflag
    print "{1}: {0}".format(string, lineno)
    errorflag = True