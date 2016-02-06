import sys
import string

#mode = "test"   # test mode input from file
mode = "submit"   # submit mode keyboard input

commands = ""
stack = []
store = [1000]

def labelCheck(label,colon = False):
    #check label name validness
    #label the string to check; colon if the label end with colon
    if colon == True and label[len(label)-1] != ':':
        return False
    else:
        label = label[:len(label)-1]
    if label[0] in string.lowercase:
        for digit in label[1:]:
            if not (digit.isdigit() or digit in string.lowercase or digit == '_'):
                return  False
    else:
        return False
    return  True

def inputProcess():
    #load the commands and check it's validity
    global commands
    global jumpRegister
    tempCommands = []

    #load commands
    if mode == "test":
        f = open("input2.txt")
        tempCommands = f.readlines()
        f.close()
    else:
        for line in sys.stdin:
            tempCommands.append(line)

    for i in range(0,len(tempCommands),1):
        #process of comment and combine lines
        if (tempCommands[i].find('#') == -1 ):
            if tempCommands[i].find('\n') == -1:
                temp=len(tempCommands[i])
            else:
                temp=tempCommands[i].find('\n')
        else:
            temp=tempCommands[i].find( '#' )
        commands += tempCommands[i][:temp]
        commands += ' '

    #split base on ' '
    commands = commands.split()
    print(commands)

    i=0
    while i < len(commands):
        #input grammar chack if fails, exit
        print(i,commands[i])
        if commands[i] in ['ildc',                       #Fellowed by num
                          ]:
            if commands[i+1].isdigit() == False:
                print("Error: ildc + num wrong")
                exit()
            i += 1
        elif commands[i] in [
                           'iadd','isub','imul','idiv'
                           'pop','dup','swap',
                           'load','store','pop'            #Related to store
                          ]:
            pass
        elif commands[i] in [
                           'jz','jnz', 'jmp'                  #Fellowed by label
                          ]:
            if labelCheck(commands[i+1],False):
                if not (commands.count(commands[i+1]+':') == 1):
                    #print(commands.count(commands[i+1]+':'),commands[i+1]+':',commands[4])
                    print("Error: no where to jump to")
                    exit()
            else:
                print("label check failed 1")
                exit()
            i += 1
        elif not labelCheck(commands[i],True):
            if (commands.count(commands[i][:len(commands[i])-1]) == 1):
                print("Error: no matching jump command")
                exit()
            else:
                print(commands[i][:len(commands[i])-1])
                print(commands.count(commands[:len(commands[i])-1]))

                print("label check failed 2")
                exit()
        i += 1
#end of funciton input Process

#semantics
#'ildc',                       #Fellowed by num
#'iadd','isub','imul','idiv'
#'pop','dup','swap'
#'jz','jnz','jump',                   #Fellowed by label
#'load','store'                #Related to store
def calcProcess():
    i=0
    while i < len(commands):
        keyWord = commands[i]
        if keyWord == 'ildc':
            stack.append(string.atof(commands[i+1]))
            i += 1
        elif keyWord == 'iadd':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)

        elif keyWord == 'isub':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif keyWord == 'imul':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif keyWord == 'idiv':
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)

        elif keyWord == 'pop':
            a = stack.pop()
        elif keyWord == 'dup':
            a = stack.pop()
            stack.append(a)
            stack.append(a)
        elif keyWord == 'swap':
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            stack.append(b)

        elif keyWord == 'jz':
            if stack.pop() == 0:
                i = commands.index(commands[i+1]+":")
        elif keyWord == 'jnz':
            if stack.pop() != 0:
                i = commands.index(commands[i+1]+":")
        elif keyWord == 'jmp':
            i = commands.index(commands[i+1]+":")
        elif keyWord == 'load':
            a = stack.pop()
            store[a] = a
            ##might be wrong
        elif keyWord == 'store':
            a = stack.pop()
            b = stack.pop()
            store[b] = a
        i += 1

inputProcess()
calcProcess()
print(int(stack.pop()))