#program submit
import sys
import string

#mode = "test"   # test mode input from file
mode = "submit"   # submit mode keyboard input
commands = ""
vari = []
value = []
def labelCheck(label,colon = False):
    #check label name validness
    #label the string to check; colon if the label end with colon
    if colon == True and label[len(label)-1] != ':':
        return False
    else:
        label = label[:len(label)-1]
    if len(label)==0:
        if label in string.lowercase:
            return True
        else:
            return False
    elif label[0] in string.lowercase:
        for digit in label[1:]:
            if not (digit.isdigit() or digit in string.lowercase or digit == '_'):
                return  False
    else:
        return False
    return  True

def inputProcess():
    #load the commands and check it's validity
    global commands
    global vari

    tempCommands = []

    #load commands
    if mode == "test":
        f = open("input1.txt")
        tempCommands = f.readlines()
        f.close()
    else:
        for line in sys.stdin:
            tempCommands.append(line)

    for i in range(0,len(tempCommands),1):
        #process of comment and combine lines
        if (tempCommands[i].find(';') != -1 ):
            tempCommands[i] = tempCommands[i].replace(';',' ; ')
            semcolonFlag = True
        else:
            semcolonFlag = False

        if (tempCommands[i].find('~') != -1 ):
            tempCommands[i] = tempCommands[i].replace('~',' ~ ')

        commands += tempCommands[i]
    if semcolonFlag == False:
        print("Error: command not ended with ;")
        exit()
    #split base on ' '
    commands = commands.split()

    i = 0
    opeNum = 0
    numNum = 0
    newline = 0
    variNum = 0
    while i < len(commands):
        # syntax check
        # since all operator has 2 input: #operater = #num + 1
        if newline == 0:
            if not labelCheck(commands[i]):
                print "Error: Variable name check fail"
                exit()
            else:
                if commands[i] not in vari:
                    vari.append(commands[i])
                newline += 1
        elif newline == 1:
            if not commands[i] == '=':
                print("Error: = not found")
                exit();
            else:
                newline = -1 #close the new line process
        elif commands[i] == ';':
            if opeNum +1 == numNum:
                newline = 0 # restart new line process
                opeNum = 0
                numNum = 0
            else:
                print("Error: operator number and operand number not match")
                exit()
        elif commands [i] == '~':
            if commands [i+1].isdigit():
                commands [i+1] = '-' + commands [i+1]
                numNum += 1
                i += 1
            else:
                print("Error: no number after \'~\'")
                exit()
        elif commands [i].isdigit():
            numNum += 1
        elif commands[i] in ['+','-','*','/','%']:
            opeNum += 1
        elif commands[i] in vari:
            numNum += 1
        else:
            print(commands[i],commands[i+1])
            print("Error: syntax wrong or use variable without initialize")
            exit()
        i += 1
    #print("syntax check success")

def compile():
    i=0
    lineStart = 0;
    lineEnd = 0;
    while lineStart < len(commands):
        # compile
        lineEnd = commands.index(";",lineStart)

        print("ildc "+str(vari.index(commands[lineStart])))  # x =

        for i in range(lineStart+2,lineEnd,1):
            # process of operand
            # process in forward order
            # skip the x =
            # note range (x,y,z)  is like i = x ; i < y ; i++
            # and the i++ in the circulate doesn't work
            if commands[i].isdigit():
                print("ildc "+ str(int(string.atof(commands[i]))))
            if commands[i] in vari:
                print("ildc " + str(vari.index(commands[i])))
                print("load")

        for i in range(lineEnd-1,lineStart-1,-1):
            # process of =-*/%
            # process in reverse order
            if commands[i] in ['+','-','*','/','%']:
                if commands[i] == '+':
                    print "iadd"
                if commands[i] == '-':
                    print "isub"
                if commands[i] == '*':
                    print "imul"
                if commands[i] == '/':
                    print "idiv"
                if commands[i] == '%':
                    print "imod"
        print ("store")
        lineStart = lineEnd + 1

inputProcess()
compile()