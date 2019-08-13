from random import shuffle,randint,seed
import os
    # author:               Caleb Chan
    # purpose:              generate a maze that the user can't fully see
    # date of compleation:  7/14/2019
#   functions
def recback(x,y,grid,gridx,gridy):
    if 0 <= x < gridx and 0 <= y < gridy:
        grid[y][x][4] = True
        d = [(x-1,y),(x,y+1),(x,y-1),(x+1,y)]
        shuffle(d)
        for (xx,yy) in d:
            if 0 <= xx < gridx and 0 <= yy < gridy:
                if grid[yy][xx][4]:
                    continue
                if xx < x:              # left
                    grid[y][x][0] = False
                    grid[yy][xx][2] = False
                if xx > x:              # right
                    grid[y][x][2] = False
                    grid[yy][xx][0] = False
                if yy < y:              # up
                    grid[y][x][3] = False
                    grid[yy][xx][1] = False
                if yy > y:              # down
                    grid[y][x][1] = False
                    grid[yy][xx][3] = False
                recback(xx,yy,grid,gridx,gridy)
    return grid
def output(length, height, grid,char,end):
    check = [[],False]
    for x in char:
        check[0].append(x)
    change = [-1,1] #change in coordinates
    grid[check[0][1]][check[0][0]][4] = False
    while not check[1]:		#check left
        if grid[check[0][1]][check[0][0]][0]:
            check[1] = True
        else:
            check[0][0] += change[0]
            grid[check[0][1]][check[0][0]][4] = False
    for i,x in enumerate(char):	#reset
        check[0][i] = x
    check[1] = False
    while not check[1]:		#check down
        if grid[check[0][1]][check[0][0]][1]:
            check[1] = True
        else:
            check[0][1] += change[1]
            grid[check[0][1]][check[0][0]][4] = False
    for i,x in enumerate(char):	#reset
        check[0][i] = x
    check[1] = False
    while not check[1]:		#check right
        if grid[check[0][1]][check[0][0]][2]:
            check[1] = True
        else:
            check[0][0] += change[1]
            grid[check[0][1]][check[0][0]][4] = False		
    for i,x in enumerate(char):	#reset
        check[0][i] = x
    check[1] = False
    while not check[1]:		#check up?
        if grid[check[0][1]][check[0][0]][3]:
            check[1] = True
        else:
            check[0][1] += change[0]
            grid[check[0][1]][check[0][0]][4] = False
    print('+',end='')
    print("--+"*length,end='')
    print()
    for i in range(height):
        print('|',end='')
        for n in range(length):
            if not grid[i][n][4]:
                if i == char[1] and n == char[0]:
                    print("<>",end='')
                elif i == end[1] and n == end[0]:
                    print("{}",end='')
                else:
                    print("  ",end='')
            else:
                print("  ",end='')
            # wall output
            if not grid[i][n][4]:
                if grid[i][n][2]:
                    print('|',end='')
                else:
                    print(' ',end='')
            else:
                if n == length-1:
                    print('|',end='')
                elif n+1 < length:
                    if not grid[i][n+1][4]:
                        if grid[i][n+1][0]:
                            print('|',end='')
                        else:
                            print(' ',end='')
                    else:
                        print(' ',end='')
        print()
        print('+',end='')
        for n in range(length):
            if not grid[i][n][4]:
                if grid[i][n][1]:
                    print("--+",end='')
                else:
                    print("  +",end='')
            else:
                if i == height-1:
                    print("--+",end='')
                elif i < height-1:
                    if not grid[i+1][n][4]:
                        if grid[i+1][n][3]:
                            print("--+",end='')
                        else:
                            print("  +",end='')
                    else:
                        print("  +",end='')
        print()
    return grid
#   start of code
#   initializer
def main():
    steps = 0
    length = int(input("length:"))
    height = int(input("height:"))
    seed_ = int(input("seed:"))
    seed(a=seed_)
    maze = [[None for i in range(length)] for n in range(height)]
    #   Node attributes
    for i in range(height):
        for n in range(length):
            maze[i][n] = [True for x in range(5)]
            if n == 0:              #left
                maze[i][n][0] = True
            if n == length-1:       #right
                maze[i][n][1] = True
            if i == 0:              #up
                maze[i][n][2] = True
            if i == height-1:       #down
                maze[i][n][3] = True
            maze[i][n][4] = False   #visible
    #   random locations
    #   [x][y]
    start = [randint(0,length-1),randint(0,height-1)]       #   corrdinate array
    end = [randint(0,length-1),randint(0,height-1)]
    maze = recback(start[0],start[1],maze,length,height)    #   recursive backtrack randomization
    #   constantly running
    #   start
    maze[start[1]][start[0]][4] = False 
    done = False
    print("use WASD controls and enter to proceed")
    #   start
    while not done:
        maze = output(length,height,maze,start,end)
        step = input("direction: ")
        steps += 1
        if step == "exit":
            done = True
            print("Terminated")
        elif step == "debug":
            for i in maze:
                print(i)
            continue
        elif step == 'a':
            if maze[start[1]][start[0]][0]:
                print("can't go there")
            else:
                start[0] -= 1
        elif step == 'd':
            if maze[start[1]][start[0]][2]:
                print("can't go there")
            else:
                start[0] += 1
        elif step == 'w':
            if maze[start[1]][start[0]][3]:
                print("can't go there")
            else:
                start[1] -= 1
        elif step == 's':
            if maze[start[1]][start[0]][1]:
                print("can't go there")
            else:
                start[1] += 1
        else:
            print("invalid input")
        if start == end:
            print("Congratulations, you've escaped")
            print("you took {} steps".format(steps))
            done = True
main()
os.system('pause')