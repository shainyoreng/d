import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

pygame.init()


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    tab_case = []
    x = -1*sizeBtwn
    y = -1*sizeBtwn
    for count1 in range(rows):
        x = x + sizeBtwn
        y = -1*sizeBtwn
        for count2 in range(rows):
            y = y + sizeBtwn
            tab_case.append((x,y))

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
    
    try:
        return tab_case
    except:
        pass

def redrawWindow(surface,data,take_from):
    global rows, width, s
    font = pygame.font.Font(None, int(width/rows/2))
    surface.fill((0,0,0))
    drawGrid(width,rows, surface)
    sizeBtwn = width // rows
    x = -1*sizeBtwn
    count=0
    for a in range(rows):
        x+=sizeBtwn
        y= -1*sizeBtwn
        for b in range(rows):
            y+=sizeBtwn
            if data[count][1]=="neutral":
                pass
            if data[count][1]=="player1":
                if a*rows+b == take_from:
                    pygame.draw.rect(surface,(255,255,0),(x+sizeBtwn/4,y+sizeBtwn/4,sizeBtwn/2,sizeBtwn/3),int(sizeBtwn/2))
                    surface.blit(font.render(str(data[count][0]), True, (0,0,0), (255,255,0)) ,(x+sizeBtwn/6,y+sizeBtwn/4.5))
                else:
                    pygame.draw.rect(surface,(0,255,255),(x+sizeBtwn/4,y+sizeBtwn/4,sizeBtwn/2,sizeBtwn/3),int(sizeBtwn/2))
                    surface.blit(font.render(str(data[count][0]), True, (0,0,0), (0,255,255)) ,(x+sizeBtwn/6,y+sizeBtwn/4.5))
            if data[count][1]=="player2":
                if a*rows+b == take_from:
                    pygame.draw.rect(surface,(255,255,0),(x+sizeBtwn/4,y+sizeBtwn/4,sizeBtwn/2,sizeBtwn/2),int(sizeBtwn/2))
                    surface.blit(font.render(str(data[count][0]), True, (0,0,0), (255,255,0)) ,(x+sizeBtwn/6,y+sizeBtwn/4))
                else:
                    pygame.draw.rect(surface,(255,0,0),(x+sizeBtwn/4,y+sizeBtwn/4,sizeBtwn/2,sizeBtwn/3),int(sizeBtwn/2))
                    surface.blit(font.render(str(data[count][0]), True, (0,0,0), (255,0,0)) ,(x+sizeBtwn/6,y+sizeBtwn/4))

            count+=1

    pygame.display.update()


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def AIalgoritem(forturn):
	global data, squrea
	allDataSaves = [[data]]
	for e in range(forturn):
		allDataSaves.append([])
		for i in range(allDataSaves[e]):
			squres =[]
			for squrea in range(squres.count(turn)):
				squres.append(squrea[1])
			
			
			
			
		

def main():
    global width, rows,data,squrea
    width = 700
    addinturn=1
    rows = 5
    win = pygame.display.set_mode((width, width))
    tab_case = drawGrid(width,rows, win)
    flag = True
    clock = pygame.time.Clock()
    sizeBtwn = width // rows
    take_from = -1


    data = []
    for i in range(pow(rows,2)):
        data.append([0,"neutral"])
    
    start_places = {
1:"player1", 2:"player1", 3:"player1",
6:"player1",7:"player1",8:"player1"
,16:"player2",17:"player2",18:"player2",
21:"player2",22:"player2",23:"player2"}
    for e in range(len(data)):
        if e in start_places.keys():
            data[e][0]+=1
            data[e][1] = start_places[e]
    turn_click = 0
    turn = "player1"
    while flag:
        for event in pygame.event.get():
            pygame.time.delay(30)
            clock.tick(200)


            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            notfaild = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(tab_case)):
                    if pygame.mouse.get_pos()[0]>tab_case[i][0]and pygame.mouse.get_pos()[0]<tab_case[i][0]+sizeBtwn \
                    and pygame.mouse.get_pos()[1]>tab_case[i][1]and pygame.mouse.get_pos()[1]<tab_case[i][1]+sizeBtwn:

                        if turn_click == 0:
                            if data[i][1] == turn:
                                if not data[i][0]==0:
                                    turn_click = 1
                                    take_from = i
                                    # message_box("ssdasfas",(data[i], str(i)))
                                    break
                                else:
                                	pass
                                    #message_box("help","you  can't you cubes with zero inside!")
                            else:
                            	pass
                                #message_box("help","you can use just your cubes. you can't use "+data[i][1]+" cubes!")

                        if turn_click == 1:
                            if data[i][1] == turn:
                                if i != take_from:
                                    data[i][0] +=data[take_from][0]
                                    data[take_from][0]=0
                                    notfaild=True
                                else:
                                    take_from = -1
                                    turn_click = 0

                            elif data[i][1] == "neutral":
                                if i==take_from + rows or i==take_from - rows or i==take_from+1 or i==take_from-1:
                                    data[i][0] +=data[take_from][0]
                                    data[take_from][0] = 0
                                    data[i][1] = turn
                                    notfaild=True
                                else:
                                	pass
                                    #message_box("help","you can't use your cubes to distance then more then une, diagonals does not count!")
                            
                            else:
                                if i <rows:
                                    if i != 0:
                                        if i + rows ==take_from or i + 1 ==take_from or i - 1 ==take_from:
                                            if data[take_from][0] - data[i][0] >0:
                                                data[i][1] = turn
                                                data[i][0] = data[take_from][0] - data[i][0]
                                                data[take_from][0] = 0

                                            else:
                                                data[i][0] = data[i][0] - data[take_from][0]
                                                data[take_from][0] = 0
                                            notfaild=True

                                        else:
                                        	pass
                                            #message_box("help","you can't use your cubes to distance then more then une, diagonals does not count!")
                                    else:
                                        if i + rows ==take_from or i + 1 ==take_from:
                                            if data[take_from][0] - data[i][0] >0:
                                                data[i][1] = turn
                                                data[i][0] = data[take_from][0] - data[i][0]
                                                data[take_from][0] = 0

                                            else:
                                                data[i][0] = data[i][0] - data[take_from][0]
                                                data[take_from][0] = 0
                                            notfaild=True

                                        else:
                                        	pass
                                            #message_box("help","you can't use your cubes to distance then more then une, diagonals does not count!")

                                elif i >rows*(rows-1)-1:
                                    if i != pow(rows,2)-1:
                                        if i - rows ==take_from or i + 1 ==take_from or i - 1 ==take_from:
                                            if data[take_from][0] - data[i][0] >0:
                                                data[i][1] = turn
                                                data[i][0] = data[take_from][0] - data[i][0]
                                                data[take_from][0] = 0

                                            else:
                                 
                                                data[i][0] = data[i][0] - data[take_from][0]
                                                data[take_from][0] = 0
                                            notfaild=True

                                        else:
                                        	pass
                                            #message_box("help","you can't use your cubes to distance then more then une, diagonals does not count!")

                                    else:
                                        if i - rows ==take_from or i -1 ==take_from:
                                            if data[take_from][0] - data[i][0] >0:
                                                data[i][1] = turn
                                                data[i][0] = data[take_from][0] - data[i][0]
                                                data[take_from][0] = 0

                                            else:
                                                data[i][0] = data[i][0] - data[take_from][0]
                                                data[take_from][0] = 0
                                            notfaild=True

                                        else:
                                        	pass
                                            #message_box("help","you can't use your cubes to distance then more then une, diagonals does not count!")

                                else:
                                    if i + rows ==take_from or i - rows ==take_from or i + 1 ==take_from or i -1 ==take_from:
                                        if data[take_from][0] - data[i][0] >0:
                                            data[i][1] = turn
                                            data[i][0] = data[take_from][0] - data[i][0]
                                            data[take_from][0] = 0

                                        else:
                                            data[i][0] = data[i][0] - data[take_from][0]
                                            data[take_from][0] = 0
                                        notfaild=True

                                    else:
                                    	pass
                                        #message_box("help","you can't use your cubes to distance then more then une, diagonals does not count!")

                            

                            if notfaild:
                                turn_click = 0
                                take_from = -1
                                redrawWindow(win,data,take_from)
                                pygame.time.delay(400)
                                for e in range(len(data)):
                                    if data[e][1] == turn:
                                        print(e)
                                        if e <rows:
                                            if e != 0:
                                                if data[ e + rows][1] !=turn or data[e + 1][1] !=turn or data[e - 1][1] !=turn:
                                                    data[e][0]+=addinturn
                                            else:
                                                if data[ e + rows][1] !=turn or data[e + 1][1] !=turn:
                                                    data[e][0]+=addinturn

                                        elif e >rows*(rows-1)-1:
                                            if e != pow(rows,2)-1:
                                                if data[e - rows][1] !=turn or data[e - 1][1] !=turn or data[e + 1][1] !=turn:
                                                    data[e][0]+=addinturn  
                                            else:
                                                if data[e - rows][1] !=turn or data[e - 1][1] !=turn:
                                                    data[e][0]+=addinturn

                                        else:
                                            if data[e + rows][1] !=turn or data[e - rows][1] !=turn or data[e + 1][1] !=turn or data[e - 1][1] !=turn:
                                                data[e][0]+=addinturn

                                if turn == "player1":
                                    turn = "player2"
                                else:
                                    turn = "player1"

                                font = pygame.font.Font(None, 42)
                                squres =[]
                                for squrea in data:
                                	squres.append(squrea[1])
                                if squres.count("player1") ==0:
                                    win.blit(font.render("player 2 win", True, (0,0,0), (255,255,0)) ,(width/2,width/2))
                                    pygame.display.update()
                                if squres.count("player2") ==0:
                                    win.blit(font.render("player 1 win", True, (0,0,0), (255,255,0)) ,(width/2,width/2))
                                    pygame.display.update()

                        print(turn)
        redrawWindow(win,data,take_from)

main()
