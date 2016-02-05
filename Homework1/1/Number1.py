import sys
import string

mode = "test"   # test mode input from file
#mode = "submit"   # submit mode keyboard input

commands = ""
stack = []
store = [1000]
jumpRegister = [] # note 2 num is used as a group

def inputProcess():
    #load the commands and check it's validity
    global commands
    global jumpRegister
    tempCommands = []
    if mode == "test":
        f = open("input2.txt")
        tempCommands = f.readlines()
        f.close()
    else:
        for line in sys.stdin:   #problem with sys don't know why
            tempCommands.append (line)

    for i in range(0,len(tempCommands),1):
        #process of comment and return
        if tempCommands[i].find('\n') or tempCommands[i].find('#'):
            # the line above is stupid, don't know better way to do it
            commands += ' '
            if (tempCommands[i].find('#') == -1 ):
                if tempCommands[i].find('\n') == -1:
                    temp=len(tempCommands[i])
                else:
                    temp=tempCommands[i].find('\n')
            else:
                temp=tempCommands[i].find( '#' )
            commands += tempCommands[i][:temp]
    commands = commands.split()

    for i in range(0,len(commands)-1,1):
        #input grammar chack if fails, exit
        if commands[i] in ['ildc',                       #Fellowed by num
                          ]:
            for j in range(0,len(commands[i+1])-1):
                    if (commands[i+1][j].isdigit())==False:
                        print("Error: not argument for command")
                        exit();
        elif commands[i] in [
                           'iadd','isub','imul','idiv'
                           'pop','dup','swap'
                           'load','store','pop'            #Related to store
                          ]:
            pass
        elif commands[i] in [
                           'jz','jnz', 'jmp'                  #Fellowed by label
                          ]:
            flag = True
            if commands[i+1][0] in range('a','z') == False:
                flag = False
            else:
                for j in range(1,len(commands[i+1]-1)):
                    if (commands[i+1][j].isalpha() or commands[i+1][j] in range(0,9) or commands[i+1][j] == '_') == False:
                        flag = False
                        break
            if flag == False:
                print("Error:label not match requirement")
                exit()
            if max(commands.Find(commands[i+1],0,i)+':') == -1:
                print("Error:Jump to Label not find")
                exit()
            i += 1
        else:
            temp = max(commands.Index(commands[i],0,i),commands.Find(commands[i],i+1,len(commands)-1))
            # the other one
            if commands[temp]+':' == commands[i]  and commands[temp-1] in ['jz','jnz', 'jmp' ] and commands[i][len(commands[i])-1]:
                print('Error:label not called')

#'ildc',                       #Fellowed by num
#'iadd','isub','imul','idiv'
#'pop','dup','swap'
#'jz','jnz',                   #Fellowed by label
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