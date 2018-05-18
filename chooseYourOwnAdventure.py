#By Joshua Wells
#CS 1400
#March 15 2018
#Choose your own adventure game
from random import randrange, random
import time, os, sys
from tkinter import *
from tkinter import ttk
from graphics import *
from math import pi, sin, cos



def main():
    name = input("What is your name? ")
    introduction(name)
    adventureIntro(name)

    root = Tk()
    root.title("Destiney")
    canvas = Canvas(root,width = 400, height = 300)
    canvas.grid()
    canvas.create_line(200,0, 200,300, fill='black')
    
    theChoice(name, root)

    choiceGraphic(root,canvas)
        
def introduction(name):
    print("Hello ", name, ", this game changes as your choices do, lets see")
    print("where you end up...")

def adventureIntro(name):
    print("Press enter to begin!")
    str(input())
    print("OK ", name,", your first test is to flip a coin, sometimes the")
    print("adventure chooses you :)")
    input("press enter to flip your coin!")
    coin = randrange(1,4)
#When done testing change coin == 1
    if coin == 0:
        print("Your coin landed tails...")
        print("You just died, press enter to exit")
        input()
        sys.exit()
    else:
        print("Your coin landed heads,")
        print("the adventure has chosen you!")

def theChoice(name, root):
    print("So",name,", do you want to attack a fort or hide from a witch?")
    print("Please click which one in the window called Destiney!")

def choiceGraphic(root, canvas):
    x=250
    y1=150
    y2=175
    wall = canvas.create_rectangle(225,y1, 250,300, fill='black')
    wall2 = canvas.create_rectangle(350,y1, 375,300, fill='black')
    
    roof = canvas.create_rectangle(250,y2, 350,200, fill='black')
    
    pari = canvas.create_rectangle(270,y1, 290,y2, fill='black')
    pari2 = canvas.create_rectangle(310,y1, 330,y2, fill='black')

    window1 = canvas.create_rectangle(265,225, 285,245)
    bar = canvas.create_line(270,225, 270,245)
    bar2 = canvas.create_line(275,225, 275,245)
    bar3 = canvas.create_line(280,225, 280,245)
    

    window2 = canvas.create_rectangle(335,225, 315,245)
    bar4 = canvas.create_line(320,225, 320,245)
    bar5 = canvas.create_line(325,225, 325,245)
    bar6 = canvas.create_line(330,225,330,245)
    
    door = canvas.create_rectangle(290,300, 310,270)
    doorline = canvas.create_line(300,270, 300,300)
    doorhandle1 = canvas.create_oval(296,285, 297,284)
    doorhandle1 = canvas.create_oval(305,285, 304,284)
    fortName = Button(master=root, text='Fort Mean Guys', font='18')
    fortName.place(x=225, y=50)
    
    chimney = canvas.create_polygon(115,300,115,300, 130,300,130,300, 120,220,120,220, 135,220,135,220, smooth=1)
    hut = canvas.create_polygon(25,300,25,300, 25,240, 175,240, 175,300,175,300, smooth=1, fill='maroon')
    roof = canvas.create_polygon(20,255,20,255, 100,240, 180,255,180,255, 100,220,100,220, smooth=1, fill='brown')
    door = canvas.create_polygon(90,270,90,270, 90,300,90,300, 110,300,110,300, 110,270,110,270, 100,255, smooth=1, fill='gray')
    handle = canvas.create_line(108,277, 106,280,106,275, 107,277 ,106,274,106,274, smooth=1)
    window = canvas.create_oval(55,260, 70,270, fill='#4f2126')
    
    hutName = Button(master=root, text='Witch\'s Evil Hut', font='18')
    hutName.place(x=25, y=50)

    fortName['command'] = lambda: fortgame(root, hutName, fortName)
    hutName['command'] = lambda: witchgame(root, hutName, fortName)

def fortgame(root, hutName, fortName):
    print("you have chosen the fort game!")
    fortName['state'] = DISABLED
    hutName['state'] = DISABLED
    root.destroy()
    fort()

def fort():
    root = Tk()
    root.title("Shoot the Fort!")
    canvas = Canvas(root, width= 1500, height= 500)
    canvas.grid()
    x=1250
    y1=250
    y2=275
    ground = canvas.create_line(0,400, 1500,400, fill='gray') 
    wall = canvas.create_rectangle(1225,y1, 1250,400, fill='black')
    wall2 = canvas.create_rectangle(1350,y1, 1375,400, fill='black')
    
    roof = canvas.create_rectangle(1250,y2, 1350,300, fill='black')
    
    pari = canvas.create_rectangle(1270,y1, 1290,y2, fill='black')
    pari2 = canvas.create_rectangle(1310,y1, 1330,y2, fill='black')

    window1 = canvas.create_rectangle(1265,325, 1285,345)
    bar = canvas.create_line(1270,325, 1270,345)
    bar2 = canvas.create_line(1275,325, 1275,345)
    bar3 = canvas.create_line(1280,325, 1280,345)
    

    window2 = canvas.create_rectangle(1335,325, 1315,345)
    bar4 = canvas.create_line(1320,325, 1320,345)
    bar5 = canvas.create_line(1325,325, 1325,345)
    bar6 = canvas.create_line(1330,325,1330,345)
    
    door = canvas.create_rectangle(1290,400, 1310,370)
    doorline = canvas.create_line(1300,370, 1300,400)
    doorhandle1 = canvas.create_oval(1296,385, 1297,384)
    doorhandle1 = canvas.create_oval(1305,385, 1304,384)

    flagpole = canvas.create_line(1200,400, 1200, 250)
    flag = canvas.create_polygon(1200,250, 1200,250, 1150,275, 1100,280, 1100,280, 1150,280, 1200,300, 1200,300, smooth=1)

    cannonhill = canvas.create_polygon(130,400,130,400, 180,400,180,400, 155,385,fill='green',smooth=1)
    cannon = canvas.create_polygon(150,390,150,390, 175,380,175,380, 173,370, 170,365, 170,365,145,380, smooth=1)
    cannonwheel = canvas.create_oval(155,395, 145,385, fill='brown')
    fuse = canvas.create_line(146,381, 140,385, 137,390,smooth=1)
    stand = canvas.create_polygon(162,380,168,378,168,378, 172,395,172,395, 166,395,166,395,fill='#996633', smooth=1)

    fifteen = Button(master = root, text='    15    ', font='18')
    fifteen.place(x=325, y=350)
    
    thirty = Button(master = root, text='    30    ', font='18')
    thirty.place(x=325, y=250)
    

    fortyfive = Button(master = root, text='    45    ', font='18')
    fortyfive.place(x=325, y=150)
    
    fifteen['command']= lambda: closer(canvas, fifteen, thirty, fortyfive)
    thirty['command']= lambda: miss(canvas, fifteen, thirty, fortyfive)
    fortyfive['command']= lambda: boom(canvas, fifteen, thirty, fortyfive)
    angleshot = Label(canvas, font='18', text="Angle of the cannon.")
    angleshot.place(x=325,y=50)

def closer(canvas, fortyfive, thirty, fifteen):
    close = Label(canvas, font='18', text="Wow, that fort was a lot closer than I thought, we hit it! \ngood thing they didn't see us till we did!")
    close.place(x=750, y=100)
    fortyfive['state']=DISABLED
    thirty['state']=DISABLED
    fifteen['state']=DISABLED
    blam(canvas)
    win = Label(canvas, font='60', text='YOU WON!')
    win.place(x=700,y=200)
    cannonball(canvas)

#TODO fix cannonball animation
def cannonball(canvas):
    x=155
    y=380
    cannonball = []
    count = 0
    frames = 0.0
    while x < 1275:
        count += 1
        cannonball = [x,y,x+5,y-5]
        if count % 1 == 0:
            frames += 1
            canvas.create_oval(cannonball)
            x= x + 25
            y= (y-5.5*frames) + frames**1.5
            
        

def blam(canvas):
    k = []
    kaboom = randomlines(k, 4000)
    r= []
    kapow = randomlines(r, 4500)
    x=[]
    bablam = randomlines(x, 2000)

    canvas.create_oval(1275,350, 1300,325, fill="gray")
    canvas.create_line(kaboom, fill="red")
    canvas.create_line(kapow, fill="orange")
    canvas.create_line(bablam, fill="black")
    
    
def randomlines(kaboom, points):
    count = 0
    y=150
    x=1150
    while points > count:
        angle = random()*2*pi
        if y + 5*sin(angle) > 150 and x + 5*cos(angle) > 1150 and x + 5*cos(angle) < 1450 and y + 5*sin(angle) < 400:
            x = x + 5*cos(angle)
            y = y + 5*sin(angle)
            kaboom.append(x)
            kaboom.append(y)
            count += 1
    return kaboom

def miss(canvas, fifteen, thirty, fortyfive):
    missed = Label(canvas, font='18', text="You shot right over their heads... and they shot you! You died.")
    missed.place(x=750, y=100)
    fortyfive['state']=DISABLED
    thirty['state']=DISABLED
    fifteen['state']=DISABLED
    sys.exit()


def boom(canvas, fifteen, thirty, fortyfive):
    fail = Label(canvas, font='18', text="Your cannon just exploded! Guess you get what you pay for, next time buy it new.")
    fail.place(x=750, y=100)
    fortyfive['state']=DISABLED
    thirty['state']=DISABLED
    fifteen['state']=DISABLED
    kablam(canvas)
    sys.exit()

def kablam(canvas):
    q= []
    kaboom = lineList(q, 300)
    c= []
    kapow = lineList(c, 400)
    r= []
    blam = lineList(r, 200)
    
    canvas.create_line(blam, fill= "black")
    canvas.create_line(kaboom, fill = "red")
    canvas.create_line(kapow, fill = "orange")

def lineList(kaboom, times):
    count=0
    y=340
    x=125
    while times > count:
        angle = random()*2*pi
        if y + 5*sin(angle) > 340 and x + 5*cos(angle) > 125 and x + 5*cos(angle) < 195 and y + 5*sin(angle) < 395:
            x = x + 5*cos(angle)
            y = y + 5*sin(angle)
            kaboom.append(x)
            kaboom.append(y)
            count += 1
    return kaboom

def witchgame(root, hutName, fortName):
    print("You have chosen the witch's hut game!")
    fortName['state'] = DISABLED
    hutName['state'] = DISABLED
    root.destroy()
    frog()

def frog():
    print("You are a frog hiding from a witch. She needs to use you in her potion.")
    strategy = input("Do you choose to hide under the caldron, inside the sink or hop out the window? \n(type caldron, sink or window)")
    if strategy == 'caldron':
        print("She lit the fire to heat up her caldron, you died!")
        sys.exit()
    elif strategy == 'sink':
        print("Turns out she washes her ingredients in the sink \nbefore she uses them. She found you and you were\nmade into a potion that causes a mild rash.")
        sys.exit()
    elif strategy == 'window':
        print("It's a good thing she leaves her window open! You escaped and never \nfound out that you used to be a human.")
    else:
        print("your entry was incorrect!")
        input("press enter to exit.")
        sys.exit()

if __name__ == '__main__':
    main()
    
    
