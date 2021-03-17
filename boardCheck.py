import random
from random import choice
from solve import solve

Failed = 0

def reset():
    global Failed
    Failed = 0

List = list

GridBoard = [
    ["A", "A", "A", "B", "B", "B", "C", "C", "C"], 
    ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
    ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
    ["D", "D", "D", "E", "E", "E", "F", "F", "F"], 
    ["D", "D", "D", "E", "E", "E", "F", "F", "F"], 
    ["D", "D", "D", "E", "E", "E", "F", "F", "F"], 
    ["G", "G", "G", "H", "H", "H", "I", "I", "I"], 
    ["G", "G", "G", "H", "H", "H", "I", "I", "I"],
    ["G", "G", "G", "H", "H", "H", "I", "I", "I"]
]

A = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
B = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
C = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
D = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
E = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
F = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
G = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
H = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
I = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]

GameBoard = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

blank = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def Push(baceBoard, PlayerBoard):
    for i in range(9):
        for j in range (9):
            PlayerBoard[i][j] = baceBoard[i][j]

def CheckQuo(setBoard, x, y):
    global List
    if setBoard[y][x] == "A":
        List = A
    if setBoard[y][x] == "B":
        List = B
    if setBoard[y][x] == "C":
        List = C
    if setBoard[y][x] == "D":
        List = D
    if setBoard[y][x] == "E":
        List = E
    if setBoard[y][x] == "F":
        List = F
    if setBoard[y][x] == "G":
        List = G
    if setBoard[y][x] == "H":
        List = H
    if setBoard[y][x] == "I":
        List = I

def splitBoard(board, setBoard):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    k = 0
    for i in range (9):
        for j in range (9):
            if setBoard[i][j] == "A":
                A[a] = board[i][j]
                a = a + 1
            if setBoard[i][j] == "B":
                B[b] = board[i][j]
                b = b + 1
            if setBoard[i][j] == "C":
                C[c] = board[i][j]
                c = c + 1
            if setBoard[i][j] == "D":
                D[d] = board[i][j]
                d = d + 1
            if setBoard[i][j] == "E":
                E[e] = board[i][j]
                e = e + 1
            if setBoard[i][j] == "F":
                F[f] = board[i][j]
                f = f + 1
            if setBoard[i][j] == "G":
                G[g] = board[i][j]
                g = g + 1
            if setBoard[i][j] == "H":
                H[h] = board[i][j]
                h = h + 1
            if setBoard[i][j] == "I":
                I[k] = board[i][j]
                k = k + 1

def boardCheckMove(board, x, y, setBoard):
    global List
    check = 0
    CheckQuo(setBoard, x, y)
    move = board[y][x]
    for i in range (9):
        if i != x:
            if board[y][i] == move:
                return False 
    for i in range (9):
        if i != y:
            if board[i][x] == move:
                return False
    for i in range (9):
        if List[i] != "#":
            if List[i] == move:
                check = check + 1
                if check == 2:
                    return False
    return True

def Build(NumChance):
    global Failed
    k = 0
    building = 0
    for i in range(9):
        for j in range(9):
            board = False
            chance = random.randint(1, 100)
            if chance <= NumChance:
                while board == False:
                    num = random.choice(numbers)
                    GameBoard[i][j] = num
                    splitBoard(GameBoard, GridBoard)
                    if boardCheckMove(GameBoard, j, i, GridBoard) == True:
                        break
                    else:
                        board = False
                        k += 1 
                        if k == 10:
                            Failed += 1
                            print("Failed ", Failed)
                            if Failed > 994:
                                print("lower percent")
                                return False
                            else:
                                Build(NumChance)
            else:
                GameBoard[i][j] = "#"
            building = building + 1
    Push(GameBoard, blank)
    buildInt(blank)
    if solve(blank) != True:
        Failed += 1
        if Failed > 994:
            print("lower percent")
            return False
        else:
            Build(NumChance)

def buildInt(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != "#":
                board[i][j] = int(board[i][j])
            else:
                board[i][j] = 0

def Ui():
    print("how many boards would you like to genrate?")
    NumOfBoard = int(input(''))
    print("what is the chance of number space you would like?")
    ChanceOfNum = int(input(''))
    for i in range(NumOfBoard):
        Build(ChanceOfNum)
        print(GameBoard)

#Build(25)