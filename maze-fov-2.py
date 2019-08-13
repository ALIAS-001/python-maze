from random import shuffle,randint,seed
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
                if xx < x:
                    grid[y][x][0] = False
                    grid[yy][xx][1] = False
                if xx > x:
                    grid[y][x][1] = False
                    grid[yy][xx][0] = False
                if yy < y:
                    grid[y][x][2] = False
                    grid[yy][xx][3] = False
                if yy > y:
                    grid[y][x][3] = False
                    grid[yy][xx][2] = False
                recback(xx,yy,grid,gridx,gridy)
    return grid
def output(length, height, grid,char,end):
    check = [[],False]
#   can be optimized
    for x in char:
        check[0].append(x)
    change = [[-1,0],[1,0],[0,-1],[0,1]] #change in coordinates
    grid[check[0][1]][check[0][0]][4] = False
    for x in range(4):
        while not check[1]:
            if grid[check[0][1]][check[0][0]][x]:
                check[1] = True
            else:
                check[0][0] += change[x][0]
                check[0][1] += change[x][1]
                grid[check[0][1]][check[0][0]][4] = False
        for i,x in enumerate(char):
            check[0][i] = x
        check[1] = False
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
                if grid[i][n][1]:
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
                if grid[i][n][3]:
                    print("--+",end='')
                else:
                    print("  +",end='')
            else:
                if i == height-1:
                    print("--+",end='')
                elif i < height-1:
                    if not grid[i+1][n][4]:
                        if grid[i+1][n][2]:
                            print("--+",end='')
                        else:
                            print("  +",end='')
                    else:
                        print("  +",end='')
        print()
    return grid
#   initializer
length = int(input("length of maze: "))
height = int(input("height of maze: "))
seed_ = int(input("seed: "))
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

#   locations
#   [x][y]
start = [randint(0,length-1),randint(0,height-1)]
end = [randint(0,length-1),randint(0,height-1)]
maze = recback(start[0],start[1],maze,length,height)
#   constantly running
done = False
print("use WASD controls and enter to proceed")
#   start
while not done:
    output(length,height,maze,start,end)
    step = input("direction: ")
    if step == "debug":
        for i in maze:
            print(i)
        continue
    if step == "exit":
        print("terminated")
        done=True
    if step == 'a':
        if maze[start[1]][start[0]][0]:
            print("can't go there")
        else:
            start[0] -= 1
    elif step == 'd':
        if maze[start[1]][start[0]][1]:
            print("can't go there")
        else:
            start[0] += 1
    elif step == 'w':
        if maze[start[1]][start[0]][2]:
            print("can't go there")
        else:
            start[1] -= 1
    elif step == 's':
        if maze[start[1]][start[0]][3]:
            print("can't go there")
        else:
            start[1] += 1
    else:
        print("invalid input")
    if start == end:
        print("Congratulations, you've escaped")
        done = True