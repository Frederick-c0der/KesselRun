import pgzrun
import random
laserlist=[]
WIDTH=800
xwing=Actor('xwingpixel', (300, 550))
tiefighter=Actor('tiefighterpixel', (random.randint(0,800),0))
HEIGHT=600
def draw():
    screen.fill("black")
    xwing.draw()
    for i in range(len(laserlist)):
        laserlist[i].draw()
    tiefighter.draw()
def update():
    global laser
    global laserlist
    tiefighter.y+=3
    if keyboard.left:
        xwing.x-=3
    if keyboard.right:
        xwing.x+=3
    if tiefighter.y>=600:
        tiefighter.y=0
        tiefighter.x=random.randint(0,800)
    for i in range(len(laserlist)):
        laserlist[i].y-=3
        if tiefighter.colliderect(laserlist[i]):
            tiefighter.y=0
            tiefighter.x=random.randint(0,800)
            laserlist.remove(laserlist[i])
def on_key_down(key):
    if key == keys.SPACE:
        laser=Actor('laser', (xwing.x,xwing.y))
        laserlist.append(laser)
pgzrun.go()