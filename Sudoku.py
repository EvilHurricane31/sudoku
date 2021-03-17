try:
    import pyglet
except:
    import pip
    pip.main(["install", "pyglet"])
    import pyglet
from pyglet import *
from boardCheck import *
import math
from pyglet import shapes
from pyglet.window import key as k
from pyglet.window import mouse as m
from pyglet import clock
from time import sleep
from math import *
import os
from pyglet.clock import *

Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "#", "F"]

N = Numbers[0]

oldNum = Numbers[0]

size = 810
spacing = 90
locationX = 0
locationY = 0
find = 0

red = 0
green = 0
blue = 0

Min = True

FPs = False

def GAME(board, savedboard, Red, Green, Blue, chances, randomColor):
    global red
    global green
    global blue
    CurintGameBoard = [
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

    red = Red
    green = Green
    blue = Blue

    if chances != False:
        NumPerChance = chances
    else:
        NumPerChance = 25

    if board == False:
        Build(NumPerChance)
        Push(GameBoard, CurintGameBoard)
    else:
        Push(board, GameBoard)
        CurintGameBoard = savedboard

    def callback(dt):
        global red
        global green
        global blue
        global Min
        resize(window.width, window.height)
        try:
            image = pyglet.image.load("imgs//" + str(N) + ".cur")
        except:
            image = pyglet.image.load("APtest//imgs//" + str(N) + ".cur")
        cursor = pyglet.window.ImageMouseCursor(image, 16, 8)
        window.set_mouse_cursor(cursor)    
        if randomColor == True:
            if Min == True:
                if red == 255:
                    if green == 255:
                        if blue == 255:
                            Min = False
                        else:
                            blue+=1
                    else:
                        green+=1
                else:
                    red+=1
            else:
                if blue == 0:
                    if green == 0:
                        if red == 20:
                            Min = True
                        else:
                            red-=1
                    else:
                        green-=1
                else:
                    blue-=1
        if FPs == True:
            fps = round(pyglet.clock.get_fps(), 0)
            print(fps, end="\r")
        

    clock.schedule_interval(callback, 1/120.0)

    #lines

    #window
    window = pyglet.window.Window(resizable=True)
    window.set_minimum_size(270, 270)
    keys = k.KeyStateHandler()
    window.push_handlers(keys)

    @window.event
    def on_resize(width, height):
        resize(width, height)

    def resize(width, hieght):
        global size
        global spacing
        global find
        global locationX
        global locationY
        if width > hieght:
            size = hieght
            find = width
            locationX = abs((size//2)-find//2)
        if hieght > width:
            size = width
            find = hieght
            locationY = abs((size//2)-find//2)
        spacing = size/9

    #draw board
    @window.event
    def on_draw():
        window.clear()
        top = shapes.Line(x=0+locationX, y=(spacing*9)+locationY, x2=(spacing*9)+locationX, y2=(spacing*9)+locationY, width=5, color=(red, green, blue))
        right = shapes.Line(x=(spacing*9)+locationX, y=0+locationY, x2=(spacing*9)+locationX, y2=(spacing*9)+locationY, width=5, color=(red, green, blue))
        bottom = shapes.Line(x=0+locationX, y=0+locationY, x2=(spacing*9)+locationX, y2=0+locationY, width=5, color=(red, green, blue))
        left = shapes.Line(x=0+locationX, y=0+locationY, x2=0+locationX, y2=(spacing*9)+locationY, width=5, color=(red, green, blue))
        line1  = shapes.Line(x=0+locationX, y=spacing+locationY, x2=size+locationX, y2=spacing+locationY, width=1, color=(red, green, blue))
        line2  = shapes.Line(x=0+locationX, y=(spacing*2)+locationY, x2=size+locationX, y2=(spacing*2)+locationY, width=1, color=(red, green, blue))
        line3  = shapes.Line(x=0+locationX, y=(spacing*3)+locationY, x2=size+locationX, y2=(spacing*3)+locationY, width=5, color=(red, green, blue))
        line4  = shapes.Line(x=0+locationX, y=(spacing*4)+locationY, x2=size+locationX, y2=(spacing*4)+locationY, width=1, color=(red, green, blue))
        line5  = shapes.Line(x=0+locationX, y=(spacing*5)+locationY, x2=size+locationX, y2=(spacing*5)+locationY, width=1, color=(red, green, blue))
        line6  = shapes.Line(x=0+locationX, y=(spacing*6)+locationY, x2=size+locationX, y2=(spacing*6)+locationY, width=5, color=(red, green, blue))
        line7  = shapes.Line(x=0+locationX, y=(spacing*7)+locationY, x2=size+locationX, y2=(spacing*7)+locationY, width=1, color=(red, green, blue))
        line8  = shapes.Line(x=0+locationX, y=(spacing*8)+locationY, x2=size+locationX, y2=(spacing*8)+locationY, width=1, color=(red, green, blue))
        line9  = shapes.Line(x=spacing+locationX, y=0+locationY, x2=spacing+locationX, y2=size+locationY, width=1, color=(red, green, blue))
        line10 = shapes.Line(x=(spacing*2)+locationX, y=0+locationY, x2=(spacing*2)+locationX, y2=size+locationY, width=1, color=(red, green, blue))
        line11 = shapes.Line(x=(spacing*3)+locationX, y=0+locationY, x2=(spacing*3)+locationX, y2=size+locationY, width=5, color=(red, green, blue))
        line12 = shapes.Line(x=(spacing*4)+locationX, y=0+locationY, x2=(spacing*4)+locationX, y2=size+locationY, width=1, color=(red, green, blue))
        line13 = shapes.Line(x=(spacing*5)+locationX, y=0+locationY, x2=(spacing*5)+locationX, y2=size+locationY, width=1, color=(red, green, blue))
        line14 = shapes.Line(x=(spacing*6)+locationX, y=0+locationY, x2=(spacing*6)+locationX, y2=size+locationY, width=5, color=(red, green, blue))
        line15 = shapes.Line(x=(spacing*7)+locationX, y=0+locationY, x2=(spacing*7)+locationX, y2=size+locationY, width=1, color=(red, green, blue))
        line16 = shapes.Line(x=(spacing*8)+locationX, y=0+locationY, x2=(spacing*8)+locationX, y2=size+locationY, width=1, color=(red, green, blue))
        top.draw()
        right.draw()
        bottom.draw()
        left.draw()
        line1.draw()
        line2.draw()
        line3.draw()
        line4.draw()
        line5.draw()
        line6.draw()
        line7.draw()
        line8.draw()
        line9.draw()
        line10.draw()
        line11.draw()
        line12.draw()
        line13.draw()
        line14.draw()
        line15.draw()
        line16.draw()
        setup()

    def setup():
        for i in range(9):
            for j in range(9):
                if CurintGameBoard[i][j] != "#":
                    num(j, i, CurintGameBoard[i][j], False)

    def num(X, Y, Num, Fps):
        number = pyglet.text.Label(Num, font_size=spacing//2, x=locationX+(spacing*0.25)+(X*spacing), y=locationY+(spacing*0.25)+(Y*spacing), color=(red, green, blue, 255))
        number.draw()

    def save():
        try:
            file = str(len(os.listdir("saves//")))
            saveFile = open("saves//"+file+".txt", "w")
        except:
            file = str(len(os.listdir("APtest//saves//")))
            saveFile = open("APtest//saves//"+file+".txt", "w")
        saveFile.write(str(GameBoard) + "\n" + str(CurintGameBoard))
        saveFile.close()

    def fullscreen():
        if window.fullscreen == False:
            window.set_fullscreen(True)
        else:
            window.set_fullscreen(False)
            resize(window.width, window.height)

    #user imput
    @window.event
    def on_key_press(symbol, modifiers):
        global N
        global FPs
        if symbol == k._1:
            N = Numbers[0]
        if symbol == k._2:
            N = Numbers[1]
        if symbol == k._3:
            N = Numbers[2]
        if symbol == k._4:
            N = Numbers[3]
        if symbol == k._5:
            N = Numbers[4]
        if symbol == k._6:
            N = Numbers[5]
        if symbol == k._7:
            N = Numbers[6]
        if symbol == k._8:
            N = Numbers[7]
        if symbol == k._9:
            N = Numbers[8]
        if symbol == k._0:
            N = Numbers[9]
        if symbol == k.R:
            Push(GameBoard, CurintGameBoard)
        if symbol == k.S:
            save()
        if symbol == k.N:
            reset()
            Build(NumPerChance)
            Push(GameBoard, CurintGameBoard)
        if symbol == k.F:
            fullscreen()
        if symbol == k.ESCAPE:
            #save()
            pyglet.app.exit()
        if symbol == k.F4:
            if FPs == True:
                FPs = False
            else:
                FPs = True
            print(FPs)

    def checkdone(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == "#":
                    return False
        return True

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global N
        global oldNum
        if button == m.LEFT:
            if x >= 0+locationX and x <= (spacing*1)+locationX:
                X = 0
            elif x >= (spacing*1)+locationX+1 and x <= (spacing*2)+locationX:
                X = 1
            elif x >= (spacing*2)+locationX+1 and x <= (spacing*3)+locationX:
                X = 2
            elif x >= (spacing*3)+locationX+1 and x <= (spacing*4)+locationX:
                X = 3
            elif x >= (spacing*4)+locationX+1 and x <= (spacing*5)+locationX:
                X = 4
            elif x >= (spacing*5)+locationX+1 and x <= (spacing*6)+locationX:
                X = 5
            elif x >= (spacing*6)+locationX+1 and x <= (spacing*7)+locationX:
                X = 6
            elif x >= (spacing*7)+locationX+1 and x <= (spacing*8)+locationX:
                X = 7
            elif x >= (spacing*8)+locationX+1 and x <= (spacing*9)+locationX:
                X = 8
            else:
                X = 0
            if y >= 0+locationY and y <= (spacing*1)+locationY:
                Y = 0
            elif y >= (spacing*1)+locationY+1 and y <= (spacing*2)+locationY:
                Y = 1
            elif y >= (spacing*2)+locationY+1 and y <= (spacing*3)+locationY:
                Y = 2
            elif y >= (spacing*3)+locationY+1 and y <= (spacing*4)+locationY:
                Y = 3
            elif y >= (spacing*4)+locationY+1 and y <= (spacing*5)+locationY:
                Y = 4
            elif y >= (spacing*5)+locationY+1 and y <= (spacing*6)+locationY:
                Y = 5
            elif y >= (spacing*6)+locationY+1 and y <= (spacing*7)+locationY:
                Y = 6
            elif y >= (spacing*7)+locationY+1 and y <= (spacing*8)+locationY:
                Y = 7
            elif y >= (spacing*8)+locationY+1 and y <= (spacing*9)+locationY:
                Y = 8
            else:
                Y = 0
        if N != "F":
            oldNum = N
            if GameBoard[Y][X] == "#":
                if N != "#":
                    CurintGameBoard[Y][X] = N
                    splitBoard(CurintGameBoard, GridBoard)
                    if boardCheckMove(CurintGameBoard, X, Y, GridBoard) == False:
                        CurintGameBoard[Y][X] = "#"
                        N = Numbers[10]
                else:
                    CurintGameBoard[Y][X] = "#"
        else:
            N = oldNum
        if checkdone(CurintGameBoard) == True:
            print("board full!\npress N on your keyboard for a new board and thanks for playing")

    #start
    pyglet.app.run()

#GAME(False, False, 0, 0, 0, 25, True)