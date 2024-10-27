import pgzrun
import random
laserlist=[]
WIDTH=800
r2=Rect(0,0, 800,80)
xwing=Actor('xwingpixel', (300, 550))
falcon=Actor('falconpixel', (300, 550))
ywing=Actor('ywing', (300, 525))
podracer=Actor('podracer', (300, 500))
venator=Actor('venator', (300, 575))
finishedgame=Actor('finishedgame', (0,0))
tiefighter=Actor('tiefighterpixel', (random.randint(0,800),0))
HEIGHT=600
level=0
win=False
Score=0
ships=[xwing, falcon, ywing, podracer,venator]
over=False
def draw():
    screen.blit("stars", (0,0))
    tiefighter.draw()
    ships[level].draw()
    screen.draw.filled_rect(r2, "black")
    screen.draw.textbox(str(Score), r2, color="white")
    for i in range(len(laserlist)):
        laserlist[i].draw()
    if over == True:
        screen.clear()
        screen.draw.textbox("Game Over!", r2, color="white")
    if win == True:
        screen.clear()
        screen.draw.textbox("You won!", r2, color="white")
def update():
    global laser
    global laserlist   
    global Score
    global over
    global level
    global win
    if level==0:
        tiefighter.y+=3
    elif level==1:
        tiefighter.y+=3.2
    elif level>=2:
        tiefighter.y+=3.6
    if keyboard.left:
        ships[level].x-=3
    if keyboard.right:
        ships[level].x+=3
    if tiefighter.y>=600:
        tiefighter.y=0
        tiefighter.x=random.randint(0,800)
    for laser in laserlist:
        laser.y-=3
        if tiefighter.colliderect(laser):
            tiefighter.y=0
            tiefighter.x=random.randint(0,800)
            laserlist.remove(laser)
            if Score >= 10:
                if level == 4:
                    win=True
                else:    
                    level+=1
            else:
                Score+=10
    if tiefighter.colliderect(ships[level]):
        ships[level].x+=1000
        over=True
def on_key_down(key):
    if key == keys.SPACE:
        laser=Actor('laser', (ships[level].x,ships[level].y))
        laserlist.append(laser)
pgzrun.go()