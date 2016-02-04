import sys
import re

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
    if mode == "test":
        f = open("input1.txt")
        tempCommands = f.readlines()
        f.close()
    else:
        for line in sys.stdin:   #problem with sys don't know why
            commands.append (line)

    for i in range(0,len(tempCommands),1):
        #replace all '\n' with ' ', delete comments and combine commands
        if tempCommands[i].index('\n'):

            commands += ' '
            spaceCount = 1
            for j in range(1,tempCommands[i].index('\n')-1,1):
                if tempCommands[i][j] == ' ' and spaceCount ==0 :
                    commands += ' '
                else:
                    commands += tempCommands[i][j]
                    spaceCount = 0

    for i in range(0,len(commands)):
        # delete extra ' '
        pass


inputProcess()
print(commands)