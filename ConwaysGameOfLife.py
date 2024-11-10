import time
import random
import os
#. = no life
# # = life

#init vars
databoard = []
booldata = []
temprepeatstorage = ["a","b","c"] # tempholders

#init boards
for i in range(52):
    emptyline = []
    boolline = []
    for j in range(52):
        if 1 <= i <= 50 and 1 <= j <= 50:
            x = random.randint(0, 2) # increase or decrease second parameter for decreased or increased life initialization
            if x == 1:
                emptyline.append("#")
            else:
                emptyline.append(".")
        else:
            emptyline.append(".")
        boolline.append(False)
    databoard.append(emptyline)
    booldata.append(boolline)

#check life
def checkcell(x,y):
    if databoard[x][y] == ".":
        return False
    elif databoard[x][y] == "#":
        return True
    
#scan to booldata
def scan():
    for i in range(1,51):
        for j in range(1,51):
            liveneighbors = 0
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if x == 0 and y == 0:
                        pass
                    elif checkcell(i+x, j+y):
                        liveneighbors += 1
            if databoard[i][j] == "#"  and liveneighbors < 2:
                booldata[i][j] = False
            if (databoard[i][j] == "#" and (liveneighbors == 2 or liveneighbors == 3)):
                booldata[i][j] = True
            if databoard[i][j] == "#"  and liveneighbors > 3:
                booldata[i][j] = False
            if databoard[i][j] == "." and liveneighbors == 3:
                booldata[i][j] = True 

#update databoard
def update():
    for i in range(1,51):
        for j in range(1,51):
            if booldata[i][j] == True:
                databoard[i][j] = "#"
            if booldata[i][j] == False:
                databoard[i][j] = "."

#printboard (prototype 1) --> prints too many times
def printboard1():
    clumpedstring = ""
    for i in range(1,51):
        clumpedstring += "\n"
        for j in range(1,51):
            clumpedstring += (databoard[i][j] + " ")
        
    print(clumpedstring,end='')
    print("\n")
    temprepeatstorage[0] = temprepeatstorage[1]
    temprepeatstorage[1] = temprepeatstorage[2]
    temprepeatstorage[2] = clumpedstring

#printboard (prototype 2)
def printboard2():
    # clear screen and move cursor to top left
    print("\033[2J\033[H", end='')
    for i in range(1, 51):
        for j in range(1, 51):
            print(databoard[i][j], end=' ')
        print()

#printboard (prototype 3)
def printboard3():
    # clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(1, 51):
        for j in range(1, 51):
            print(databoard[i][j], end=' ')
        print()

#printboard (prototype 4)
def printboard4():
    for i in range(52):  # Move the cursor up 51 lines --> ANSI cursor stuff
        print("\033[F", end='')

    for i in range(1, 51):
        line = ""
        for j in range(1, 51):
            line += databoard[i][j] + " "
        print(line)


            
# manual cell change

# databoard[30][30] = "#"
# databoard[32][30] = "#"
# databoard[31][29] = "#"

printboard1()

#ctrl + C to manually escape

while True:
    time.sleep(0.1) # comment out for instant end result fr fr
    #0.01 optimal speed for finishing + working, 0.1 best for seeing whats happening
    scan()
    update()
    printboard1()
    if temprepeatstorage[0] == temprepeatstorage[2]:
        break
