#paintProject.py
#Nicholas Culmone

from pygame import *
from random import *
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

#import FileDialog
    
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

init()

root = Tk() 
root.withdraw()

points = []

background = image.load("grass.jpg")
logo = image.load("logo.png")
wheel = image.load("wheel.png")
pencil = image.load("pencil.png")
eraser = image.load("eraser.jpg")
paintcan = image.load("paintcan.jpg")
polygon = image.load("polygon.png")
brush = image.load("brush.jpeg")
spray = image.load("spray.jpg")
dropper = image.load("dropper.jpg")
shapes = image.load("shapes.jpg")
stamp = image.load("stamp.jpg")
clear = image.load("clear.png")
back1 = image.load("background1.jpg")
back2 = image.load("background2.jpg")
back3 = image.load("background3.jpg")
sticker1 = image.load("steve.png")
sticker2 = image.load("creeper.png")
sticker3 = image.load("diamond.png")
sticker4 = image.load("pick.png")
sticker5 = image.load("gblock.png")
sticker6 = image.load("cake.png")
save = image.load("save.png")
folder = image.load("load.png")
disc1 = image.load("disc1.png")
disc2 = image.load("disc2.png")
disc3 = image.load("disc3.png")
disc4 = image.load("disc4.png")
disc5 = image.load("disc5.png")
disc6 = image.load("disc6.png")

sticker12 = image.load("steve2.png")
sticker22 = image.load("creeper2.png")
sticker32 = image.load("diamond2.png")
sticker42 = image.load("pick2.png")
sticker52 = image.load("gblock2.png")
sticker62 = image.load("cake2.png")
back12 = image.load("background12.jpg")
back22 = image.load("background22.jpg")
back32 = image.load("background32.jpg")

song1 = mixer.music.load("music/song1.mp3")
song2 = mixer.music.load("music/song2.mp3")
song3 = mixer.music.load("music/song3.mp3")
song4 = mixer.music.load("music/song4.mp3")
song5 = mixer.music.load("music/song5.mp3")
song6 = mixer.music.load("music/song6.mp3")

screen = display.set_mode((1024,768))
screen.fill((255,255,255))

screen.blit(background,(0,0))

draw.rect(screen,(200,200,200),(4,378,223,173))
draw.rect(screen,(0,0,0),(4,378,223,173),2)
draw.rect(screen,(255,255,255),(256,96,750,640))

for i in range(96,481,96):
    for j in range(10,166,73):
        draw.rect(screen,(255,255,255),(j,i,64,64))

tool = "pencil"

screen.blit(pencil,(15,390))
screen.blit(brush,(87,390))

width = 5

drawcolour = (0,0,0)

canvasrect = Rect(259,99,744,634)

colourrect = Rect(11,586,232,150)
pencilsrect = Rect(10,96,64,64)
erasersrect = Rect(83,96,64,64)
fillsrect = Rect(156,96,64,64)
polygonrect = Rect(10,192,64,64)
dropperrect = Rect(83,192,64,64)
sprayrect = Rect(156,192,64,64)
shapesrect = Rect(10,288,64,64)
stamprect = Rect(83,288,64,64)
musicrect = Rect(156,288,64,64)
saverect = Rect(53,30,40,40)
folderrect = Rect(126,30,40,40)

#Shapes
hollowrect = Rect(-10,-10,1,1)
filledrect = Rect(-10,-10,1,1)
linerect = Rect(-10,-10,1,1)
hollowcircle = Rect(-10,-10,1,1)
fillcircle = Rect(-10,-10,1,1)
#Pencils
pencilrect = Rect(10,384,64,64)
brushrect = Rect(83,384,64,64)
#Erasers
eraserrect = Rect(-10,-10,1,1)
clearrect = Rect(-10,-10,1,1)
#Fills
paintrect = Rect(-10,-10,1,1)
fillrect = Rect(-10,-10,1,1)
back1rect = Rect(-10,-10,1,1)
back2rect = Rect(-10,-10,1,1)
back3rect = Rect(-10,-10,1,1)
#Stickers
sticker1r = Rect(-10,-10,1,1)
sticker2r = Rect(-10,-10,1,1)
sticker3r = Rect(-10,-10,1,1)
sticker4r = Rect(-10,-10,1,1)
sticker5r = Rect(-10,-10,1,1)
sticker6r = Rect(-10,-10,1,1)
#Music
disc1r = Rect(-10,-10,1,1)
disc2r = Rect(-10,-10,1,1)
disc3r = Rect(-10,-10,1,1)
disc4r = Rect(-10,-10,1,1)
disc5r = Rect(-10,-10,1,1)
disc6r = Rect(-10,-10,1,1)


draw.rect(screen,drawcolour,(11,576,232,10))

draw.rect(screen,(0,0,0),(256,96,750,640),5)

for i in range(48,122,73):
    draw.rect(screen,(255,255,255),(i,25,50,50))
    draw.rect(screen,(0,0,0),(i,25,50,50),2)

for i in range(96,481,96):
    for j in range(10,166,73):
        draw.rect(screen,(0,0,0),(j,i,64,64),2)
draw.rect(screen,(255,0,0),(10,96,64,64),2)
draw.rect(screen,(0,0,255),(10,384,64,64),2)

screen.blit(logo,(311,0))
screen.blit(wheel,(11,586))
screen.blit(pencil,(18,100))
screen.blit(eraser,(86,102))
screen.blit(paintcan,(160,100))
screen.blit(polygon,(18,199))
screen.blit(dropper,(86,194))
screen.blit(spray,(160,199))
screen.blit(shapes,(16,293))
screen.blit(stamp,(92,295))
screen.blit(save,(53,30))
screen.blit(folder,(126,30))

running = True
while running:
    for e in event.get():
        draw.rect(screen,drawcolour,(11,576,232,10))
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:           
           copy = screen.copy()
           if e.button == 1:
               startmx = mx
               startmy = my
           if e.button == 4:
               width += 1
               startmx = mx
               startmy = my
               if width == 30:
                   width = 29
           if e.button == 5:
               width -= 1
               startmx = mx
               startmy = my
               if width == 0:
                   width = 1

    screen.set_clip(canvasrect)
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    
#-------------------------------------------------------------- 
#-------------------------------------------------------
    if mb[0] == 1 and pencilsrect.collidepoint((mx,my)):
        tool = "pencil"
        screen.set_clip(None)

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(255,255,255),(j,i,64,64))
                
        for i in range(96,289,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)

        screen.blit(pencil,(15,390))
        screen.blit(brush,(87,390))

        #Shapes
        hollowrect = Rect(-10,-10,1,1)
        filledrect = Rect(-10,-10,1,1)
        linerect = Rect(-10,-10,1,1)
        hollowcircle = Rect(-10,-10,1,1)
        fillcircle = Rect(-10,-10,1,1)
        #Erasers
        eraserrect = Rect(-10,-10,1,1)
        clearrect = Rect(-10,-10,1,1)
        #Pencils
        pencilrect = Rect(10,384,64,64)
        brushrect = Rect(83,384,64,64)
        #Fills
        paintrect = Rect(-10,-10,1,1)
        fillrect = Rect(-10,-10,1,1)
        back1rect = Rect(-10,-10,1,1)
        back2rect = Rect(-10,-10,1,1)
        back3rect = Rect(-10,-10,1,1)
        #Stickers
        sticker1r = Rect(-10,-10,1,1)
        sticker2r = Rect(-10,-10,1,1)
        sticker3r = Rect(-10,-10,1,1)
        sticker4r = Rect(-10,-10,1,1)
        sticker5r = Rect(-10,-10,1,1)
        sticker6r = Rect(-10,-10,1,1)
        #Music
        disc1r = Rect(-10,-10,1,1)
        disc2r = Rect(-10,-10,1,1)
        disc3r = Rect(-10,-10,1,1)
        disc4r = Rect(-10,-10,1,1)
        disc5r = Rect(-10,-10,1,1)
        disc6r = Rect(-10,-10,1,1)
               
        draw.rect(screen,(255,0,0),(10,96,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
        
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and brushrect.collidepoint((mx,my)):
        tool = "brush"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(83,384,64,64),2)
        screen.set_clip(canvasrect)

        
    elif mb[0] == 1 and pencilrect.collidepoint((mx,my)):
        tool = "pencil"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
        screen.set_clip(canvasrect)
#-------------------------------------------------------
        
    elif mb[0] == 1 and erasersrect.collidepoint((mx,my)):
        tool = "eraser"
        screen.set_clip(None)

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(255,255,255),(j,i,64,64))

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        
        for i in range(96,289,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)

        screen.blit(eraser,(15,390))
        screen.blit(clear,(94,393))

        #Shapes
        hollowrect = Rect(-10,-10,1,1)
        filledrect = Rect(-10,-10,1,1)
        linerect = Rect(-10,-10,1,1)
        hollowcircle = Rect(-10,-10,1,1)
        fillcircle = Rect(-10,-10,1,1)
        #Pencils
        pencilrect = Rect(-10,-10,1,1)
        brushrect = Rect(-10,-10,1,1)
        #Erasers
        eraserrect = Rect(10,384,64,64)
        clearrect = Rect(83,384,64,64)
        #Fills
        paintrect = Rect(-10,-10,1,1)
        fillrect = Rect(-10,-10,1,1)
        back1rect = Rect(-10,-10,1,1)
        back2rect = Rect(-10,-10,1,1)
        back3rect = Rect(-10,-10,1,1)
        #Stickers
        sticker1r = Rect(-10,-10,1,1)
        sticker2r = Rect(-10,-10,1,1)
        sticker3r = Rect(-10,-10,1,1)
        sticker4r = Rect(-10,-10,1,1)
        sticker5r = Rect(-10,-10,1,1)
        sticker6r = Rect(-10,-10,1,1)
        #Music
        disc1r = Rect(-10,-10,1,1)
        disc2r = Rect(-10,-10,1,1)
        disc3r = Rect(-10,-10,1,1)
        disc4r = Rect(-10,-10,1,1)
        disc5r = Rect(-10,-10,1,1)
        disc6r = Rect(-10,-10,1,1)
                        
        draw.rect(screen,(255,0,0),(83,96,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
        
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and clearrect.collidepoint((mx,my)):
        tool = "clear"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(83,384,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and eraserrect.collidepoint((mx,my)):
        tool = "eraser"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
        screen.set_clip(canvasrect)
#-------------------------------------------------------
        
    elif mb[0] == 1 and fillsrect.collidepoint((mx,my)):
        tool = "paintcan"
        screen.set_clip(None)

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(255,255,255),(j,i,64,64))

        screen.blit(back12,(10,480))
        screen.blit(back22,(83,480))
        screen.blit(back32,(156,480))
        screen.blit(paintcan,(15,390))

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        
        for i in range(96,289,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)

        #Shapes
        hollowrect = Rect(-10,-10,1,1)
        filledrect = Rect(-10,-10,1,1)
        linerect = Rect(-10,-10,1,1)
        hollowcircle = Rect(-10,-10,1,1)
        fillcircle = Rect(-10,-10,1,1)
        #Pencils
        pencilrect = Rect(-10,-10,1,1)
        brushrect = Rect(-10,-10,1,1)
        #Erasers
        eraserrect = Rect(-10,-10,1,1)
        clearrect = Rect(-10,-10,1,1)
        #Fills
        paintrect = Rect(10,384,64,64)
        fillrect = Rect(83,384,64,64)
        back1rect = Rect(10,480,64,64)
        back2rect = Rect(83,480,64,64)
        back3rect = Rect(156,480,64,64)
        #Stickers
        sticker1r = Rect(-10,-10,1,1)
        sticker2r = Rect(-10,-10,1,1)
        sticker3r = Rect(-10,-10,1,1)
        sticker4r = Rect(-10,-10,1,1)
        sticker5r = Rect(-10,-10,1,1)
        sticker6r = Rect(-10,-10,1,1)
        #Music
        disc1r = Rect(-10,-10,1,1)
        disc2r = Rect(-10,-10,1,1)
        disc3r = Rect(-10,-10,1,1)
        disc4r = Rect(-10,-10,1,1)
        disc5r = Rect(-10,-10,1,1)
        disc6r = Rect(-10,-10,1,1)
    
        draw.rect(screen,(0,0,255),(10,384,64,64),2)        
        draw.rect(screen,(255,0,0),(156,96,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and paintrect.collidepoint((mx,my)):
        tool = "paintcan"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and back1rect.collidepoint((mx,my)):
        tool = "back1"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(10,480,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and back2rect.collidepoint((mx,my)):
        tool = "back2"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(83,480,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and back3rect.collidepoint((mx,my)):
        tool = "back3"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(156,480,64,64),2)
        screen.set_clip(canvasrect)
#-------------------------------------------------------
        
    elif mb[0] == 1 and polygonrect.collidepoint((mx,my)):
        tool = "polygon"
        screen.set_clip(None)
        
        for i in range(96,289,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
                
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(255,255,255),(j,i,64,64))

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)        

        #Shapes
        hollowrect = Rect(-10,-10,1,1)
        filledrect = Rect(-10,-10,1,1)
        linerect = Rect(-10,-10,1,1)
        hollowcircle = Rect(-10,-10,1,1)
        fillcircle = Rect(-10,-10,1,1)
        #Pencils
        pencilrect = Rect(-10,-10,1,1)
        brushrect = Rect(-10,-10,1,1)
        #Erasers
        eraserrect = Rect(-10,-10,1,1)
        clearrect = Rect(-10,-10,1,1)
        #Fills
        paintrect = Rect(-10,-10,1,1)
        fillrect = Rect(-10,-10,1,1)
        back1rect = Rect(-10,-10,1,1)
        back2rect = Rect(-10,-10,1,1)
        back3rect = Rect(-10,-10,1,1)
        #Stickers
        sticker1r = Rect(-10,-10,1,1)
        sticker2r = Rect(-10,-10,1,1)
        sticker3r = Rect(-10,-10,1,1)
        sticker4r = Rect(-10,-10,1,1)
        sticker5r = Rect(-10,-10,1,1)
        sticker6r = Rect(-10,-10,1,1)
        #Music
        disc1r = Rect(-10,-10,1,1)
        disc2r = Rect(-10,-10,1,1)
        disc3r = Rect(-10,-10,1,1)
        disc4r = Rect(-10,-10,1,1)
        disc5r = Rect(-10,-10,1,1)
        disc6r = Rect(-10,-10,1,1)
                
        draw.rect(screen,(255,0,0),(10,192,64,64),2)
        screen.set_clip(canvasrect)
#-------------------------------------------------------
    
    elif mb[0] == 1 and dropperrect.collidepoint((mx,my)):
        tool = "dropper"
        screen.set_clip(None)

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(255,255,255),(j,i,64,64))

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        
        for i in range(96,289,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(255,0,0),(83,192,64,64),2)

        #Shapes
        hollowrect = Rect(-10,-10,1,1)
        filledrect = Rect(-10,-10,1,1)
        linerect = Rect(-10,-10,1,1)
        hollowcircle = Rect(-10,-10,1,1)
        fillcircle = Rect(-10,-10,1,1)
        #Pencils
        pencilrect = Rect(-10,-10,1,1)
        brushrect = Rect(-10,-10,1,1)
        #Erasers
        eraserrect = Rect(-10,-10,1,1)
        clearrect = Rect(-10,-10,1,1)
        #Fills
        paintrect = Rect(-10,-10,1,1)
        fillrect = Rect(-10,-10,1,1)
        back1rect = Rect(-10,-10,1,1)
        back2rect = Rect(-10,-10,1,1)
        back3rect = Rect(-10,-10,1,1)
        #Stickers
        sticker1r = Rect(-10,-10,1,1)
        sticker2r = Rect(-10,-10,1,1)
        sticker3r = Rect(-10,-10,1,1)
        sticker4r = Rect(-10,-10,1,1)
        sticker5r = Rect(-10,-10,1,1)
        sticker6r = Rect(-10,-10,1,1)
        #Music
        disc1r = Rect(-10,-10,1,1)
        disc2r = Rect(-10,-10,1,1)
        disc3r = Rect(-10,-10,1,1)
        disc4r = Rect(-10,-10,1,1)
        disc5r = Rect(-10,-10,1,1)
        disc6r = Rect(-10,-10,1,1)
                
        screen.set_clip(canvasrect)
#-------------------------------------------------------
        
    elif mb[0] == 1 and sprayrect.collidepoint((mx,my)):
        tool = "spray"
        screen.set_clip(None)

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(255,255,255),(j,i,64,64))

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        
        for i in range(96,289,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)

        #Shapes
        hollowrect = Rect(-10,-10,1,1)
        filledrect = Rect(-10,-10,1,1)
        linerect = Rect(-10,-10,1,1)
        hollowcircle = Rect(-10,-10,1,1)
        fillcircle = Rect(-10,-10,1,1)
        #Pencils
        pencilrect = Rect(-10,-10,1,1)
        brushrect = Rect(-10,-10,1,1)
        #Erasers
        eraserrect = Rect(-10,-10,1,1)
        clearrect = Rect(-10,-10,1,1)
        #Fills
        paintrect = Rect(-10,-10,1,1)
        fillrect = Rect(-10,-10,1,1)
        back1rect = Rect(-10,-10,1,1)
        back2rect = Rect(-10,-10,1,1)
        back3rect = Rect(-10,-10,1,1)
        #Stickers
        sticker1r = Rect(-10,-10,1,1)
        sticker2r = Rect(-10,-10,1,1)
        sticker3r = Rect(-10,-10,1,1)
        sticker4r = Rect(-10,-10,1,1)
        sticker5r = Rect(-10,-10,1,1)
        sticker6r = Rect(-10,-10,1,1)
        #Music
        disc1r = Rect(-10,-10,1,1)
        disc2r = Rect(-10,-10,1,1)
        disc3r = Rect(-10,-10,1,1)
        disc4r = Rect(-10,-10,1,1)
        disc5r = Rect(-10,-10,1,1)
        disc6r = Rect(-10,-10,1,1)
              
        draw.rect(screen,(255,0,0),(156,192,64,64),2)
        screen.set_clip(canvasrect)

#-------------------------------------------------------    
    elif mb[0] == 1 and shapesrect.collidepoint((mx,my)):
        screen.set_clip(None)

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(255,255,255),(j,i,64,64))

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
                
        for i in range(96,289,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
                
        draw.rect(screen,(255,0,0),(10,288,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
                
        draw.rect(screen,(0,0,0),(15,397,54,40),2)
        draw.rect(screen,(0,0,0),(88,397,54,40))         
        draw.line(screen,(0,0,0),(162,390),(215,430),4)
        draw.circle(screen,(0,0,0),(42,512),28,1)
        draw.circle(screen,(0,0,0),(115,512),28)

        #Shapes
        hollowrect = Rect(10,384,64,64)
        filledrect = Rect(83,384,64,64)
        linerect = Rect(156,384,64,64)
        hollowcircle = Rect(10,480,64,64)
        fillcircle = Rect(83,480,64,64)
        #Pencils
        pencilrect = Rect(-10,-10,1,1)
        brushrect = Rect(-10,-10,1,1)
        #Erasers
        eraserrect = Rect(-10,-10,1,1)
        clearrect = Rect(-10,-10,1,1)
        #Fills
        paintrect = Rect(-10,-10,1,1)
        fillrect = Rect(-10,-10,1,1)
        back1rect = Rect(-10,-10,1,1)
        back2rect = Rect(-10,-10,1,1)
        back3rect = Rect(-10,-10,1,1)
        #Stickers
        sticker1r = Rect(-10,-10,1,1)
        sticker2r = Rect(-10,-10,1,1)
        sticker3r = Rect(-10,-10,1,1)
        sticker4r = Rect(-10,-10,1,1)
        sticker5r = Rect(-10,-10,1,1)
        sticker6r = Rect(-10,-10,1,1)
        #Music
        disc1r = Rect(-10,-10,1,1)
        disc2r = Rect(-10,-10,1,1)
        disc3r = Rect(-10,-10,1,1)
        disc4r = Rect(-10,-10,1,1)
        disc5r = Rect(-10,-10,1,1)
        disc6r = Rect(-10,-10,1,1)

        tool = "hollowrect"

        screen.set_clip(canvasrect)

    elif mb[0] == 1 and hollowrect.collidepoint((mx,my)):
        tool = "hollowrect"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
        screen.set_clip(canvasrect)
        
    elif mb[0] == 1 and filledrect.collidepoint((mx,my)):
        tool = "filledrect"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(83,384,64,64),2)
        screen.set_clip(canvasrect)
        
    elif mb[0] == 1 and linerect.collidepoint((mx,my)):
        tool = "line"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(156,384,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and hollowcircle.collidepoint((mx,my)):
        tool = "hollowcirc"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(10,480,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and fillcircle.collidepoint((mx,my)):
        tool = "fillcirc"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(83,480,64,64),2)
        screen.set_clip(canvasrect)
#-------------------------------------------------------
    elif mb[0] == 1 and stamprect.collidepoint((mx,my)):
        screen.set_clip(None)
        
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(255,255,255),(j,i,64,64))

        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
                
        for i in range(96,289,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)

        draw.rect(screen,(255,0,0),(83,288,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
        
        screen.blit(sticker1,(27,386))
        screen.blit(sticker2,(100,392))
        screen.blit(sticker3,(166,391))
        screen.blit(sticker4,(18,487))
        screen.blit(sticker5,(94,487))
        screen.blit(sticker6,(165,491))
        
        #Shapes
        hollowrect = Rect(-10,-10,1,1)
        filledrect = Rect(-10,-10,1,1)
        linerect = Rect(-10,-10,1,1)
        hollowcircle = Rect(-10,-10,1,1)
        fillcircle = Rect(-10,-10,1,1)
        #Pencils
        pencilrect = Rect(-10,-10,1,1)
        brushrect = Rect(-10,-10,1,1)
        #Erasers
        eraserrect = Rect(-10,-10,1,1)
        clearrect = Rect(-10,-10,1,1)
        #Fills
        paintrect = Rect(-10,-10,1,1)
        fillrect = Rect(-10,-10,1,1)
        back1rect = Rect(-10,-10,1,1)
        back2rect = Rect(-10,-10,1,1)
        back3rect = Rect(-10,-10,1,1)
        #Stickers
        sticker1r = Rect(10,384,64,64)
        sticker2r = Rect(83,384,64,64)
        sticker3r = Rect(156,384,64,64)
        sticker4r = Rect(10,480,64,64)
        sticker5r = Rect(83,480,64,64)
        sticker6r = Rect(156,480,64,64)
        #Music
        disc1r = Rect(-10,-10,1,1)
        disc2r = Rect(-10,-10,1,1)
        disc3r = Rect(-10,-10,1,1)
        disc4r = Rect(-10,-10,1,1)
        disc5r = Rect(-10,-10,1,1)
        disc6r = Rect(-10,-10,1,1)
       
        screen.set_clip(canvasrect)
        tool = "sticker1"

    elif mb[0] == 1 and sticker1r.collidepoint((mx,my)):
        tool = "sticker1"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(10,384,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and sticker2r.collidepoint((mx,my)):
        tool = "sticker2"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(83,384,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and sticker3r.collidepoint((mx,my)):
        tool = "sticker3"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(156,384,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and sticker4r.collidepoint((mx,my)):
        tool = "sticker4"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(10,480,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and sticker5r.collidepoint((mx,my)):
        tool = "sticker5"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(83,480,64,64),2)
        screen.set_clip(canvasrect)

    elif mb[0] == 1 and sticker6r.collidepoint((mx,my)):
        tool = "sticker6"
        screen.set_clip(None)
        for i in range(384,481,96):
            for j in range(10,166,73):
                draw.rect(screen,(0,0,0),(j,i,64,64),2)
        draw.rect(screen,(0,0,255),(156,480,64,64),2)
        screen.set_clip(canvasrect)
#-------------------------------------------------------
##    elif mb[0] == 1 and musicrect.collidepoint((mx,my)):
##        screen.set_clip(None)
##        
##        for i in range(384,481,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(255,255,255),(j,i,64,64))
##
##        for i in range(384,481,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(0,0,0),(j,i,64,64),2)
##                
##        for i in range(96,289,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(0,0,0),(j,i,64,64),2)
##
##        draw.rect(screen,(255,0,0),(156,288,64,64),2)
##
##        screen.blit(disc1,(27,386))
##        screen.blit(disc2,(100,392))
##        screen.blit(disc3,(166,391))
##        screen.blit(disc4,(18,487))
##        screen.blit(disc5,(94,487))
##        screen.blit(disc6,(165,491))
##
##        #Shapes
##        hollowrect = Rect(-10,-10,1,1)
##        filledrect = Rect(-10,-10,1,1)
##        linerect = Rect(-10,-10,1,1)
##        hollowcircle = Rect(-10,-10,1,1)
##        fillcircle = Rect(-10,-10,1,1)
##        #Pencils
##        pencilrect = Rect(-10,-10,1,1)
##        brushrect = Rect(-10,-10,1,1)
##        #Erasers
##        eraserrect = Rect(-10,-10,1,1)
##        clearrect = Rect(-10,-10,1,1)
##        #Fills
##        paintrect = Rect(-10,-10,1,1)
##        fillrect = Rect(-10,-10,1,1)
##        back1rect = Rect(-10,-10,1,1)
##        back2rect = Rect(-10,-10,1,1)
##        back3rect = Rect(-10,-10,1,1)
##        #Stickers
##        sticker1r = Rect(-10,-10,1,1)
##        sticker2r = Rect(-10,-10,1,1)
##        sticker3r = Rect(-10,-10,1,1)
##        sticker4r = Rect(-10,-10,1,1)
##        sticker5r = Rect(-10,-10,1,1)
##        sticker6r = Rect(-10,-10,1,1)
##        #Music
##        disc1r = Rect(10,384,64,64)
##        disc2r = Rect(83,384,64,64)
##        disc3r = Rect(156,384,64,64)
##        disc4r = Rect(10,480,64,64)
##        disc5r = Rect(83,480,64,64)
##        disc6r = Rect(156,480,64,64)
##
##        screen.set_clip(canvasrect)
##
##    elif mb[0] == 1 and disc1r.collidepoint((mx,my)):
##        screen.set_clip(None)
##        for i in range(384,481,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(0,0,0),(j,i,64,64),2)
##        draw.rect(screen,(0,0,255),(10,384,64,64),2)
##        screen.set_clip(canvasrect)
##
##        mixer.music.play(song1)
##
##    elif mb[0] == 1 and disc2r.collidepoint((mx,my)):
##        screen.set_clip(None)
##        for i in range(384,481,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(0,0,0),(j,i,64,64),2)
##        draw.rect(screen,(0,0,255),(83,384,64,64),2)
##        screen.set_clip(canvasrect)
##
##        mixer.music.play(song2)
##
##    elif mb[0] == 1 and disc3r.collidepoint((mx,my)):
##        screen.set_clip(None)
##        for i in range(384,481,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(0,0,0),(j,i,64,64),2)
##        draw.rect(screen,(0,0,255),(156,384,64,64),2)
##        screen.set_clip(canvasrect)
##
##        mixer.music.play(song3)
##
##    elif mb[0] == 1 and disc4r.collidepoint((mx,my)):
##        screen.set_clip(None)
##        for i in range(384,481,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(0,0,0),(j,i,64,64),2)
##        draw.rect(screen,(0,0,255),(10,480,64,64),2)
##        screen.set_clip(canvasrect)
##
##        mixer.music.play(song4)
##
##    elif mb[0] == 1 and disc5r.collidepoint((mx,my)):
##        screen.set_clip(None)
##        for i in range(384,481,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(0,0,0),(j,i,64,64),2)
##        draw.rect(screen,(0,0,255),(83,480,64,64),2)
##        screen.set_clip(canvasrect)
##
##        mixer.music.play(song5)
##
##    elif mb[0] == 1 and disc6r.collidepoint((mx,my)):
##        screen.set_clip(None)
##        for i in range(384,481,96):
##            for j in range(10,166,73):
##                draw.rect(screen,(0,0,0),(j,i,64,64),2)
##        draw.rect(screen,(0,0,255),(156,480,64,64),2)
##        screen.set_clip(canvasrect)
##
##        mixer.music.play(song6)
#-------------------------------------------------------
    elif mb[0] == 1 and saverect.collidepoint((mx,my)):
        pic = screen.subsurface(canvasrect).copy()
        savefile = asksaveasfilename(parent=root,title="Save as")
        image.save(screen.subsurface(canvasrect),savefile+".png")

    elif mb[0] == 1 and folderrect.collidepoint((mx,my)):
        openfile = askopenfilename(parent=root,title="Open")
        openedfile = image.load(openfile)
        screen.blit(openedfile,(259,99))
        
#--------------------------------------------------------------        


    if mb[0] == 1 and colourrect.collidepoint((mx,my)):
        drawcolour = screen.get_at((mx,my))
        
    if mb[0] == 1 and canvasrect.collidepoint((mx,my)):

        if tool == "pencil": draw.line(screen,drawcolour,(oldmx,oldmy),(mx,my),2)
        elif tool == "eraser": draw.circle(screen,(255,255,255),(mx,my),width*2)
        elif tool == "paintcan": draw.rect(screen,drawcolour,(256,96,750,640))            
        elif tool == "polygon":
            points.append([mx,my])
            screen.set_at((mx,my),drawcolour)
        elif tool == "spray": screen.set_at((randint(mx-width,mx+width),randint(my-width,my+width)),drawcolour)
        elif tool == "dropper": drawcolour = screen.get_at((mx,my))
        elif tool == "line":
            screen.blit(copy,(0,0))
            draw.line(screen,drawcolour,(startmx,startmy),(mx,my),width)
        elif tool == "brush": draw.circle(screen,drawcolour,(mx,my),width)
        elif tool == "hollowrect":
            screen.blit(copy,(0,0))
            draw.rect(screen,drawcolour,(startmx,startmy,mx-startmx,my-startmy),width)
        elif tool == "filledrect":
            screen.blit(copy,(0,0))
            draw.rect(screen,drawcolour,(startmx,startmy,mx-startmx,my-startmy))
        elif tool == "hollowcirc":
            screen.blit(copy,(0,0))
            circ1 = Rect(startmx,startmy,mx-startmx,my-startmy)
            circ1.normalize()
            circ1.width += 2
            circ1.height += 2
            draw.ellipse(screen,drawcolour,(circ1),1)
        elif tool == "fillcirc":
            screen.blit(copy,(0,0))
            circ1 = Rect(startmx,startmy,mx-startmx,my-startmy)
            circ1.normalize()
            circ1.width += 2
            circ1.height += 2
            draw.ellipse(screen,drawcolour,(circ1))
        elif tool == "clear": draw.rect(screen,(255,255,255),(259,99,744,634))
        elif tool == "sticker1":
            screen.blit(copy,(0,0))
            screen.blit(sticker12,(mx-50,my-50))
        elif tool == "sticker2":
            screen.blit(copy,(0,0))
            screen.blit(sticker22,(mx-50,my-50))
        elif tool == "sticker3":
            screen.blit(copy,(0,0))
            screen.blit(sticker32,(mx-45,my-50))
        elif tool == "sticker4":
            screen.blit(copy,(0,0))
            screen.blit(sticker42,(mx-50,my-50))
        elif tool == "sticker5":
            screen.blit(copy,(0,0))
            screen.blit(sticker52,(mx-50,my-50))
        elif tool == "sticker6":
            screen.blit(copy,(0,0))
            screen.blit(sticker62,(mx-50,my-50))
        elif tool == "back1": screen.blit(back1,(259,99))
        elif tool == "back2": screen.blit(back2,(256,99))
        elif tool == "back3": screen.blit(back3,(259,99))

    if mb[2] == 1 and canvasrect.collidepoint((mx,my)) and points != []:
        if tool == "polygon":
            points.append(points[0])
            for i in range(len(points)-1):
                draw.line(screen,drawcolour,points[i],points[i+1],2)
            points = []

    screen.set_clip(None)            

    oldmx,oldmy = mx,my
     
       
    display.flip()
quit()
