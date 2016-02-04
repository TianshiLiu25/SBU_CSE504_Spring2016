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
        #process of comment and return
        if tempCommands[i].find('\n') or tempCommands[i].find('#'):
            # the line above is stupid, don't know better way to do it
            commands += ' '
            spaceCount = 1
            for j in range(1,max(tempCommands[i].find('\n'), tempCommands[i].find('#')),1):
                #copy and eliminate extra ' '
                #However, this part might doesn't matter at all because of split
                if (tempCommands[i][j] == ' ' or tempCommands[i][j] == ' ')and spaceCount ==0 :
                    commands += ' '
                else:
                    commands += tempCommands[i][j]
                    spaceCount = 0
    commands = commands.split()

    for i in range(0,len(commands)-1,1):
        #input grammar chack if fails, exit
        if commands[i] in ['ildc',                       #Fellowed by num
                          ]:
            if ~commands[i+1].isnumeric():
                print("error")
                exit()
        elif commands[i] in [
                           'iadd','isub','imul','idiv'
                           'pop','dup','swap'
                           'load','store'                #Related to store
                          ]:
        elif commands[i] in [
                           'jz','jnz',                   #Fellowed by label
                          ]:
            errorflag = 0
            if ~commands[i+1][0]
        elif 

inputProcess()
print(commands)