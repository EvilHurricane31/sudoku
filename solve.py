try:
    import numpy as np
except:
    import pip
    pip.main(["install", "numpy"])
    import numpy as np

checkboard0 = 0

def possible(y,x,n, grid):
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve(grid):
    global checkboard0
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n,grid):
                        grid[y][x] = n
                        if checkboard0 != 1000:
                            checkboard0 += 1
                            solve(grid)
                            grid[y][x] = 0
                        else:
                            #print(np.matrix(grid))
                            return True
                return False
    #print(np.matrix(grid))
    return True