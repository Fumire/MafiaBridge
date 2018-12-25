import pygame
import sys
from pygame.locals import *
from variable import *

pygame.init()
pygame.display.set_caption("Mafia Bridge")

size = width, height = 1024, 576
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
objects = list()
pos = (0, 0)
player = list()

playerHands = list()
fields = list()
playerScore = list()

def clearObjects():
    global objects
    objects[:] = list()

def makeFont(string, x, y, size=1, color="black"):
    global objects

    fontObj= pygame.font.Font("SeoulNamsanB.otf", int(width*size)//100)

    stringSurfaceObj = fontObj.render(string, True, palette[color])
    stringRectObj = stringSurfaceObj.get_rect()
    stringRectObj.center = (int(x*width), int(y*height))
    objects.append((stringSurfaceObj, stringRectObj))

def makeRect(x, y, w, h, color="red"):
    pygame.draw.rect(screen, palette[color], [int(width*x), int(height*y), int(width*w), int(height*h)])

def makeRectFont(string, x, y, w, h, fontSize=1, colorRect="red", colorFont="blue"):
    makeFont(string, x, y, fontSize, colorFont)
    makeRect(x-w/2, y-h/2, w, h, colorRect)

def checkPos(x1, y1, x2, y2):
    x1, x2 = x1-x2/2, x1+x2/2; y1, y2 = y1-y2/2, y1+y2/2;
    x1 *= width; x2 *= width; y1 *= height; y2 *= height;
    return (pos[0]>x1) and (pos[0]<x2) and (pos[1]>y1) and (pos[1]<y2)

def setPlayer(number=5):
    global player
    name = chooseName(number)
    color = chooseColor(number)
    player[:] = []
    for i in range(number):
        player.append((name[i], color[i]))

def main():
    global pos

    previousStage, stage = -1, 0
    fps, realFps = 30, 0
    flipFlag = False
    tmp = 0

    pygame.mouse.set_visible(True)
    while True:
        try:
            screen.fill(palette["white"])
            if stage == 0:
                if previousStage != 0:
                    flipFlag = True
                    previousStage = 0
                    print("stage 0")

                    clearObjects()
                    makeFont("Mafia Bridge", 1/2, 1/3, size=15)
                    makeFont("Press anywhere", 1/2, 3/4, size=5)
            elif stage == 1:
                if previousStage != 1:
                    flipFlag = True
                    previousStage = 1
                    print("stage 1")

                    clearObjects()
                    setPlayer()
                    for i in range(5):
                        makeFont("Player " + str(i+1), 1/5, (i+1)/7, size=5)
                        makeFont(player[i][0], 4/5, (i+1)/7, size=5, color=player[i][1])
                    makeRectFont("Change", 1/5, 6/7, 1/9, 1/14, fontSize=3)
                    makeRectFont("Next", 4/5, 6/7, 1/9, 1/14, fontSize=3)
            elif stage == 2:
                if previousStage != 2:
                    flipFlag = True
                    previousStage = 2
                    print("stage 2")

                    clearObjects()

            for obj in objects: screen.blit(obj[0], obj[1])
            if flipFlag:
                flipFlag = False
                pygame.display.flip()
            clock.tick(fps)

            #event handler
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print("Position:", pos)
                    if stage == 0: stage = 1
                    if stage == 1:
                        if checkPos(1/5, 6/7, 1/9, 1/14):
                            setPlayer()
                            previousStage = None
                        if checkPos(4/5, 6/7, 1/9, 1/14): stage = 2
                elif event.type == KEYDOWN:
                    print("key:", event.key)
                elif event.type == MOUSEMOTION:
                    pass
                elif event.type == QUIT:
                    print("Press Exit")
                    pygame.quit()
                    sys.exit()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            pygame.quit()
            sys.exit()

main()
