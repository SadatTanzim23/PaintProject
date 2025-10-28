
'''
Paint project
'''
from pygame import *
from random import *
from math import *

from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

root=Tk()
root.withdraw()#hides the small extra window

init()
font.init()
mixer.init()

width,height=1250,600#screen size
screen=display.set_mode((width,height))#displaying the screen
#some basic color
RED=(255,0,0)#color red
BLACK=(0,0,0)#color black
BLUE=(0,0,255)#color blue
GREEN=(0,255,0)#color green
WHITE=(255,255,255)#color white

#songs list
ost=["PythonGraphics/How to do images and text/Pics/Overtaken.mp3","PythonGraphics/How to do images and text/Pics/The very very strong world.mp3","PythonGraphics/How to do images and text/Pics/farewell.mp3"]

#Different fonts
arialf=font.SysFont("Arial", 25)
arialff=font.SysFont("Arial", 40)
comicFont=font.SysFont("Comic Sans Ms",20)
 
#Lists of backgrounds and stamps and stickers
bglist=["PythonGraphics/How to do images and text/Pics/bg1L.jpg","PythonGraphics/How to do images and text/Pics/bg2L.jpg","PythonGraphics/How to do images and text/Pics/bg3L.jpg","PythonGraphics/How to do images and text/Pics/bg4L.jpg","PythonGraphics/How to do images and text/Pics/bg5L.jpg"]#background list
bgclist=["PythonGraphics/How to do images and text/Pics/bg1.jpg","PythonGraphics/How to do images and text/Pics/bg2.jpg","PythonGraphics/How to do images and text/Pics/bg3.jpg","PythonGraphics/How to do images and text/Pics/bg4.jpg","PythonGraphics/How to do images and text/Pics/bg5.jpg"]#background list]
stlist=["PythonGraphics/How to do images and text/Pics/luffy.png","PythonGraphics/How to do images and text/Pics/nami.png","PythonGraphics/How to do images and text/Pics/usopp.png","PythonGraphics/How to do images and text/Pics/zoro.png","PythonGraphics/How to do images and text/Pics/luffy0.png"]#stamps
stklist=["PythonGraphics/How to do images and text/Pics/stick1.png","PythonGraphics/How to do images and text/Pics/stick2.png","PythonGraphics/How to do images and text/Pics/stick3.png","PythonGraphics/How to do images and text/Pics/stick4.png","PythonGraphics/How to do images and text/Pics/stick5.png"]#stickers

#lists for list of all the pictures including backgrounds thats an icon on the screen
picslist=["PythonGraphics/How to do images and text/Pics/background.png","PythonGraphics/How to do images and text/Pics/clear.png","PythonGraphics/How to do images and text/Pics/save.png","PythonGraphics/How to do images and text/Pics/load.png","PythonGraphics/How to do images and text/Pics/pencil.png","PythonGraphics/How to do images and text/Pics/eraser.png","PythonGraphics/How to do images and text/Pics/brush.png","PythonGraphics/How to do images and text/Pics/line.png","PythonGraphics/How to do images and text/Pics/spray.png","PythonGraphics/How to do images and text/Pics/rectangle.png","PythonGraphics/How to do images and text/Pics/circle.png","PythonGraphics/How to do images and text/Pics/triangle.png","PythonGraphics/How to do images and text/Pics/filled rect.png","PythonGraphics/How to do images and text/Pics/filled circle.png","PythonGraphics/How to do images and text/Pics/filled triangle.png","PythonGraphics/How to do images and text/Pics/poly.png","PythonGraphics/How to do images and text/Pics/stamp.png","PythonGraphics/How to do images and text/Pics/sticker.png","PythonGraphics/How to do images and text/Pics/undo.png","PythonGraphics/How to do images and text/Pics/redo.png"]
#list of all the picture posiions
picsposition=[(0,0),(1150,80),(1180,10),(1110,10),(15,160),(85,160),(155,160),(225,160),(15,230),(85,230),(155,230),(225,230),(15,300),(85,300),(155,300),(225,300),(15,370),(85,370),(155,370),(225,370)]
#loop of the all the images being loaded and displaying on the screen
for i in range(20):
    mage=image.load(picslist[i])
    screen.blit(mage,(picsposition[i]))
#Pictures of the small stuff like the arrows and all the music pictures
arrowup=image.load("PythonGraphics/How to do images and text/Pics/arrow up.png")
screen.blit(arrowup,(987,13))
screen.blit(arrowup,(823,13))
arrowdown=image.load("PythonGraphics/How to do images and text/Pics/arrow down.png")
screen.blit(arrowdown,(987,128))
screen.blit(arrowdown,(823,128))
larrow=image.load("PythonGraphics/How to do images and text/Pics/left arrow.png")
screen.blit(larrow,(338,532))
rarrow=image.load("PythonGraphics/How to do images and text/Pics/right arrow.png")
screen.blit(rarrow,(453,532))
song=image.load("PythonGraphics/How to do images and text/Pics/song.png")
screen.blit(song,(580,20))
play=image.load("PythonGraphics/How to do images and text/Pics/play.png")
screen.blit(play,(550,75))
pause=image.load("PythonGraphics/How to do images and text/Pics/pause.png")
screen.blit(pause,(610,75))
beforesong=image.load("PythonGraphics/How to do images and text/Pics/last.png")
screen.blit(beforesong,(490,75))
aftersong=image.load("PythonGraphics/How to do images and text/Pics/next.png")
screen.blit(aftersong,(670,75))

#All the rectangles on the screen each name describes which one it is
canvaRect=Rect(500,150,745,445)
toolRect=Rect(5,150,290,290)
toolnameRect=Rect(5,445,290,150)
#Defining all the tools
pencilRect=Rect(15,160,60,60)#+60 and 10 space
eraserRect=Rect(85,160,60,60)#+60 and 10 space
brushtoolRect=Rect(155,160,60,60)#+60 and 10 space
lineRect=Rect(225,160,60,60)#+60 and 10 space
spraypRect=Rect(15,230,60,60)#+60 and 10 space
rectRect=Rect(85,230,60,60)#+60 and 10 space
circleRect=Rect(155,230,60,60)#+60 and 10 space
triRect=Rect(225,230,60,60)#+60 and 10 space
frectRect=Rect(15,300,60,60)#+60 and 10 space
fcircleRect=Rect(85,300,60,60)#+60 and 10 space
ftriRect=Rect(155,300,60,60)#+60 and 10 space
polyRect=Rect(225,300,60,60)#+60 and 10 space
stampRect=Rect(15,370,60,60)#+60 and 10 space
stickerRect=Rect(85,370,60,60)#+60 and 10 space
undoRect=Rect(155,370,60,60)#+60 and 10 space
redoRect=Rect(225,370,60,60)#+60 and 10 space
saveRect=Rect(1180,10,60,60)#save rect
loadRect=Rect(1110,10,60,60)#load rect
refreshRect=Rect(1150,80,60,60)#rerfresh
bgsRect=Rect(900,25,200,100)#backgrounds
topbgRect=Rect(900,10,200,15)#top arrow for switching
bottombgRect=Rect(900,125,200,15)#bottom arrow for switching
stRect=Rect(780,25,100,100)#stamps
topstRect=Rect(780,10,100,15)#top arrow for switching
bottomstRect=Rect(780,125,100,15)#bottom arrow for switching
stkRect=Rect(350,490,100,100)#stickers
rightstkRect=Rect(335,490,15,100)#right side arrow for switching
leftstkRect=Rect(450,490,15,100)#left side arrow for switching
musicCircle=Rect(580,25,50,50)#Music logo
redRect=Rect(300,150,40,255)#red rgb color picker
greenRect=Rect(350,150,40,255)#green rgb color picker
blueRect=Rect(400,150,40,255)#blue rgb color picker
sizeRect=Rect(370,415,100,60)#the rect that the size is beign chosen from
sizepickerRect=Rect(450,150,30,255)#the slider thats picking the size
musicRect=Rect(470,10,270,130)#music box
ostRect=Rect(580,20,50,50)#music
beforeostRect=Rect(490,75,50,50)#next song
playRect=Rect(550,75,50,50)#playing
pauseRect=Rect(610,75,50,50)#pause
afterostRect=Rect(670,75,50,50)#song before

#Creating the actual thing on the screen
draw.rect(screen,WHITE,canvaRect)
draw.rect(screen,BLACK,canvaRect,2)
draw.rect(screen,BLUE,toolRect,2)
draw.rect(screen,(33,194,235),toolnameRect)
draw.rect(screen,RED,sizeRect,2)

tool=""#tool
rct=""#rect

#colors list
rgb=[RED,GREEN,BLUE]
sliders=[150,150,150]#sliders starting position
brushSlider=[150]

#variables
r=0
g=0
b=0
br=0
color=(r,g,b)
showcolorRect=Rect(300,415,60,60)
draw.rect(screen,color,showcolorRect,2)

#loading all backgrounds
bglist1=[]#the actual pictures will be stored in this list
for name in bglist:
    pic=image.load(name)
    bglist1.append(pic)
bgclist1=[]
for name in bgclist:
    pic=image.load(name)
    bgclist1.append(pic)
pos=0
screen.blit(bglist1[pos].subsurface(0,0,200,100),(900,25))
n=len(bglist1)

#loading all stamps
stlist1=[]#the actual pictures will be stored in this list
for name in stlist:
    pic=image.load(name)
    stlist1.append(pic)
posm=0
screen.blit(stlist1[posm].subsurface(0,0,100,100),(780,25))
m=len(stlist1)

#loading all stickers
stklist1=[]#the actual pictures will be stored in this list
for name in stklist:
    pic=image.load(name)
    stklist1.append(pic)
posmm=0
screen.blit(stklist1[posm].subsurface(0,0,100,100),(350,490))
mm=len(stklist1)

#loading the music
posx=0
mixer.init()
mixer.music.load(ost[posx])
mixer.music.play()
x=len(ost[posx])

#random variable
count=0
ttt=0
t=10
    
running=True
screenCap=screen.subsurface(canvaRect).copy()#canvas only

#undo redo
ur=[]#undo and redo
sclist=[screenCap]#screenshot

while running:
    count+=1
    draw.circle(screen,color,(330,445),25)#color picked under the sliders
    for evt in event.get():
        if evt.type==QUIT:
            running=False

        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:#left click
                if canvaRect.collidepoint(evt.pos):
                    sx, sy = evt.pos
                #backgrounds
                if topbgRect.collidepoint(mx,my):
                    pos=(pos+1)%n
                    print(pos)
                if bottombgRect.collidepoint(mx,my):
                    pos=(pos+n-1)%n

                #stamps
                if topstRect.collidepoint(mx,my):
                    posm=(posm+1)%m
                    print(posm)
                if bottomstRect.collidepoint(mx,my):
                    posm=(posm+m-1)%m

                #stickers
                if rightstkRect.collidepoint(mx,my):
                    posmm=(posmm+1)%mm
                    print(posmm)
                if leftstkRect.collidepoint(mx,my):
                    posmm=(posmm+mm-1)%mm

                #music
                if afterostRect.collidepoint(mx,my):
                    posx=(posx+1)%len(ost)
                    print(posx)
                    mixer.music.load(ost[posx])
                    mixer.music.play()
                if beforeostRect.collidepoint(mx,my):
                    print(posx)
                    posx=(posx+x-1)%len(ost)
                    mixer.music.load(ost[posx])
                    mixer.music.play()
                if playRect.collidepoint(mx,my):
                    mixer.music.play()
                if pauseRect.collidepoint(mx,my):
                    mixer.music.pause()

                #Colors
                if redRect.collidepoint(mx,my):
                    sliders[0]=my
                    r=my-150
                if greenRect.collidepoint(mx,my):
                    sliders[1]=my
                    g=my-150
                if blueRect.collidepoint(mx,my):
                    sliders[2]=my
                    b=my-150
                if sizepickerRect.collidepoint(mx,my):
                    brushSlider[0]=my
                    br=my-150
                color=(r,g,b)#color of what the
                brsize=(br)#brush size
                
                #the loop for how save works and functions
                if saveRect.collidepoint(mx,my) :
                    tool="save"
                    fname=filedialog.asksaveasfilename(defaultextension=".png")
                    if fname != "":
                        image.save(screen.subsurface(canvaRect),fname)
                    #You will need to add the code that actually saves the picture
                #the loop for how to load a pic
                if loadRect.collidepoint(mx,my) :
                    tool="load"
                    fname=filedialog.askopenfilename()
                    if fname!="":
                        il = image.load(fname).convert_alpha()
                        il = transform.scale(il, (canvaRect.width, canvaRect.height))
                        screen.blit(il, canvaRect.topleft)
                    print(fname)
                #Clear the screen
                if refreshRect.collidepoint(mx,my) :
                    tool="refresh"
                    screen.set_clip(None)
                    draw.rect(screen,WHITE, canvaRect)

        if evt.type==MOUSEBUTTONUP:#when the mouse is released
            screenCap=screen.subsurface(canvaRect).copy()
            if canvaRect.collidepoint(mx,my):
                sclist.append(screenCap)
            if canvaRect.collidepoint(evt.pos):
                sx1, sy1 = evt.pos

                                        
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    #tools being created
    tools=[pencilRect,eraserRect,brushtoolRect,lineRect,spraypRect,rectRect,circleRect,triRect,frectRect,fcircleRect,ftriRect,polyRect,stampRect,stickerRect,undoRect,redoRect]
    tol=["pencil","eraser","brush","line","spray","rect","circle","triangle","filled rect","filled circle","filled triangle","polygon","stamp","sticker","undo","redo"]
    toolfn=["Pencil","Eraser","Brush","Line","Spray paint","Rectangle","Circle","Triangle","Filled Rectangel","Filled Circle","Filled triangle","Polygon", "Stamp","Sticker","Undo","Redo"]
    #Tool function description
    toolfnd=["Use the pencil tool to draw","Use the eraser tool to erase","Use this tool to draw with the","Use this tool to draw a line","Use this tool to spray on the","Use this tool to draw a","Use this tool to draw a circle on","Use this tool to draw a Triangle","Use this tool to draw a filled","Use this tool to draw a filled","Use this tool to draw a filled","Use this tool to draw a polygon","Use this tool to stamp the","Use this tool to stamp the","Press this to undo the last","Press this to redo the last"]
    toolfnd2=["on the canvas","what is on the canvas","size thats picked","from a point to another","canvas where ever you wish","rectangle on the canvas"," on the canvas","the canvas","rectangle on the canvas","circle on the canvas","triangle on the canvas","on the canvas","stamp on the canvas","sticker on the canvas","command on the canvas","command on the canvas"]
    #loop for drawing the tools
    for i in range(16):
        draw.rect(screen,GREEN,tools[i],2)

    #Tools outside the tools rects
    #save load and refresh
    slrn=[saveRect,loadRect,refreshRect]
    slr=["save","load","refresh"]
    slrfn=["Save","Load","Refresh"]
    slrfnd=["Use this tool to save progress","Use this tool to load an image","Use this tool to clear the canvas"]

    #Rects other hen the tools insdie
    rects=[saveRect,loadRect,refreshRect,bgsRect,topbgRect,bottombgRect,stRect,topstRect,bottomstRect,stkRect,rightstkRect,leftstkRect]
    #loop for drawing the tools and other rects that are outside the rect
    for i in range(12):
        draw.rect(screen,GREEN,rects[i],2)

    draw.rect(screen,BLACK,sizepickerRect)
    draw.rect(screen,WHITE,(450,brushSlider[0],30,10))

    #Doing the colors
    for j in range(3):
        draw.rect(screen,rgb[j],(j*50+300,150,40,255))
        draw.rect(screen,BLACK,(j*50+300,sliders[j],40,10))
    screen.blit(image.load(picslist[0]).subsurface(300,405,180,10),(300,405))
    brush=str(br)+""
    #draw.rect(screen, BLACK,(395,425,60,40))
    screen.blit(image.load(picslist[0]).subsurface(392,425,60,40),(392,425))
    bbr=arialff.render(brush,True,BLACK)
    screen.blit(bbr,(392,425))
     
    #showing the backgrounds, stamps, and stickers
    #background
    screen.blit(bglist1[pos].subsurface(0,0,200,100),(900,25))
    #stamp
    screen.blit(image.load(picslist[0]).subsurface(780,25,100,100),(780,25))
    screen.blit(stlist1[posm].subsurface(0,0,100,100),(780,25))
    screen.blit(stlist1[posm],(780,25))
    #ticker
    draw.rect(screen,BLACK,(350,490,100,100))
    screen.blit(stklist1[posmm].subsurface(0,0,100,100),(350,490))

#songs list and loop 
    songlist=[beforeostRect,playRect,pauseRect,afterostRect]
    draw.rect(screen,RED,musicRect,2)
    screen.set_clip(None)
    #loop for the rects of the music 
    for i in range(4):
        if songlist[i].collidepoint(mx,my):
            draw.rect(screen,RED,songlist[i],2)
            if mb[0]:
                draw.rect(screen,BLUE,songlist[i],2)
        else:
            draw.rect(screen,GREEN,songlist[i],2)

    #selecting the tool
    screen.set_clip(None)
    for i in range(16):
        if tools[i].collidepoint(mx,my):
            tn=toolfn[i]#tn=tool name
            draw.rect(screen, (33,194,235),(5,445,290,150))
            toolname=arialf.render(tn,True,BLACK)
            screen.blit(toolname,(5,445))
            ######discription
            tnd=toolfnd[i]#toolnd=tool name discription
            toolnamed=arialf.render(tnd,True,BLACK)
            screen.blit(toolnamed,(5,485))
            ######discription part 2
            tnd2=toolfnd2[i]
            toolnamed2=arialf.render(tnd2,True,BLACK)
            screen.blit(toolnamed2,(5,525))
            draw.rect(screen,RED,tools[i],2)
            if mb[0]:
                draw.rect(screen,BLUE,tools[i],2)
                tool=tol[i]
        elif not tool == tol[i]:
            draw.rect(screen,GREEN,tools[i],2)
 

    screen.set_clip(None)
    #save load and refresh
    for i in range(3):
        if slrn[i].collidepoint(mx,my):
            slr=slrfn[i]#tn=tool name
            draw.rect(screen, (33,194,235),(5,445,290,150))
            slrname=arialf.render(slr,True,BLACK)
            screen.blit(slrname,(5,445))
            slrd=slrfnd[i]#toolnd=tool name discription
            slrnamed=arialf.render(slrd,True,BLACK)
            screen.blit(slrnamed,(5,485))
            if mb[0]:
                draw.rect(screen,BLUE,slrn[i],2)
                tool=slr[i]
        elif not tool == slr[i]:
            draw.rect(screen,GREEN,slrn[i],2)

    screen.set_clip(None)
    #rects that are outside the tools rect
    for i in range(12):
        if rects[i].collidepoint(mx,my) :
            draw.rect(screen,RED,rects[i],2)
            if mb[0]:
                draw.rect(screen,BLUE,rects[i],2)
        else:
            draw.rect(screen,GREEN,rects[i],2)
            
####Redo and Undo
    screen.set_clip(canvaRect)
    if undoRect.collidepoint(mx,my) and mb[0] and len(sclist)>1:
        draw.rect(screen,RED,undoRect,2)
        ur.append(sclist[-1])
        sclist.pop()
        screen.blit(sclist[-1],(canvaRect))
        time.wait(69)
    if redoRect.collidepoint(mx,my) and mb[0] and len(ur)>0:
        draw.rect(screen,RED,redoRect,2)
        sclist.append(ur[-1])
        ur.pop()
        screen.blit(sclist[-1],(canvaRect))
        time.wait(69)
        
##    #background showing--v--
    if bgsRect.collidepoint(mx,my) and mb[0]:
        screen.blit(bgclist1[pos],(500,150))
        screen.blit(bglist1[pos].subsurface(0,0,200,100),(900,25))
        
    screen.set_clip(canvaRect)###Make sure this is TEMPORARY   
    if canvaRect.collidepoint(mx,my) and mb[0]:
        #if the tools are activated this starts
        if tool=="pencil" :
            draw.line(screen,color,(omx,omy),(mx,my),1)
            if br<1:
                br=1
            draw.rect(screen,RED,pencilRect,2)
        if tool=="eraser":
            dx = mx - omx  # horiz. distance    (run)
            dy = my - omy  # vertical distance  (rise)
            dist = (dx ** 2 + dy ** 2) ** (1 / 2)
            for i in range(1, int(dist)):  # 1,2,3,4,....
                cx = omx + i * dx / dist  # run
                cy = omy + i * dy / dist  # rise
                draw.circle(screen, WHITE, (cx, cy), br // 2)
            if br<5:
                br=5
        if tool=="brush":
            dx = mx - omx  # horiz. distance    (run)
            dy = my - omy  # vertical distance  (rise)
            dist = (dx ** 2 + dy ** 2) ** (1 / 2)
            for i in range(1, int(dist)):  # 1,2,3,4,....
                cx = omx + i * dx / dist  # run
                cy = omy + i * dy / dist  # rise
                draw.circle(screen, color, (cx, cy), br // 2)
            if br<5:
                br=5
            draw.rect(screen,RED,brushtoolRect,2)
        if tool=="line":
            screen.blit(screenCap,(500,150))
            draw.line(screen,color,(sx,sy),(mx,my),2)
            draw.rect(screen,RED,lineRect,2)
        if tool=="spray":
            for i in range(5):
                rx=randint(-t,t)
                ry=randint(-t,t)
                sd=sqrt((rx ** 2 + ry ** 2) ** (1 / 2))#square distance
                if sd<br/2:
                    draw.circle(screen,color,(mx-rx,my-ry),2)
                    draw.rect(screen,RED,spraypRect,2)
                if br<5:
                    br=5
        if tool=="rect":
            screen.blit(screenCap,(500,150))
            rrect=Rect((sx,sy,mx-sx,my-sy))
            rrect.normalize()
            draw.rect(screen,color,rrect,2)
        if tool=="circle":
            screen.blit(screenCap,(500,150))
            cir=Rect((sx,sy,mx-sx,my-sy))
            cir.normalize()
            draw.ellipse(screen,color,cir,2)
        if tool=="triangle":
            screen.blit(screenCap,(500,150))
            draw.polygon(screen,color,[(sx,sy),(sx-(mx-sx),my),(mx,my)],2)
        if tool=="filled rect":
            screen.blit(screenCap,(500,150))
            rrect=Rect((sx,sy,mx-sx,my-sy))
            rrect.normalize()
            draw.rect(screen,color,rrect)
        if tool=="filled circle":
            screen.blit(screenCap,(500,150))
            cir=Rect((sx,sy,mx-sx,my-sy))
            cir.normalize()
            draw.ellipse(screen,color,cir)
        if tool=="filled triangle":
            screen.blit(screenCap,(500,150))
            draw.polygon(screen,color,[(sx,sy),(sx-(mx-sx),my),(mx,my)])
        if tool=="polygon":
            if ttt==0:
                screen.blit(screenCap,(500,150))
                draw.line(screen,color,(sx,sy),(mx,my),2)
                print(sx,sy)
                ttt=1
            elif ttt==1:
                screen.blit(screenCap,(500,150))
                draw.line(screen,color,(sx1,sy1),(mx,my),2)
        if tool=="stamp":
            w=image.load(stlist[posm]).get_width()
            h=image.load(stlist[posm]).get_height()
            screen.blit(image.load(stlist[posm]),(mx-w//2,my-h//2))
        if tool=="sticker":
            w=image.load(stklist[posmm]).get_width()
            h=image.load(stklist[posmm]).get_height()
            screen.blit(image.load(stklist[posmm]),(mx-w//2,my-h//2))
        if tool != "polygon":
            ttt=0
        if len(ur)!=0:
            ur=[]
        
    screen.set_clip(None)

    omx,omy=mx,my

    print(len(sclist))
    print(len(ur))
   
    display.flip()
            
quit()
