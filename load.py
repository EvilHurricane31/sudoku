from Sudoku import GAME
import os
try: 
    import ast
except:
    import pip
    pip.main(["install", "ast"])
    import ast

Saves = []

def GetAllSaves():
    global Saves
    try:
        Saves = os.listdir("saves//")
    except:
        Saves = os.listdir("APtest//saves//")
    return Saves
    
def menu(Saves):
    coun = len(list(Saves))
    for i in range(coun):
        print(Saves[i])
    print("type whatt file to play")
    print("leave out the .txt")
    playerboard = int(input(''))
    try:
        Wfile = open("saves//" + Saves[playerboard], "r")
    except:
        Wfile = open("APtest//saves//" + Saves[playerboard], "r")
    boards = Wfile.read().split("\n")
    baseBoard = ast.literal_eval(boards[0])
    player = ast.literal_eval(boards[1])
    GAME(baseBoard, player, 255, 255, 255, False, False)
    
def run():
    files = GetAllSaves()
    selceted = menu(files)

print("new game or load game")
game = str(input(""))
if game == "new":
    GAME(False, False, 255, 255, 255, 25, False)
elif game == "RAINBOW!":
    GAME(False, False, 20, 0, 0, 25, True)
else:
    run()
