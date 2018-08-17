import pygame
import sys
from pygame.locals import *
from custom_color import palette

pygame.init()
pygame.display.set_caption("Mafia Bridge")

size = width, height = 1024,576
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
objects = list()

def clearObjects():
    global objects
    objects[:] = []

def makeFont(string, x, y, size=1, color="black"):
    global objects

    fontObj= pygame.font.Font("SeoulNamsanB.otf", (width*size)//100)

    stringSurfaceObj = fontObj.render(string, True, palette[color])
    stringRectObj = stringSurfaceObj.get_rect()
    stringRectObj.center = (x, y)
    objects.append((stringSurfaceObj, stringRectObj))

def main():
    previousStage, stage = -1, 0
    fps, realFps = 30, 0
    flipFlag = False

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
                    makeFont("Mafia Bridge", width//2, height//3, size=10)
            elif stage == 1:
                pass
            elif stage == 2:
                pass
            for obj in objects:
                screen.blit(obj[0], obj[1])
            if flipFlag:
                flipFlag = False
                pygame.display.flip()
            clock.tick(fps)
            #event handler
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                elif event.type == KEYDOWN:
                    print("key:", event.key)
                elif event.type == MOUSEMOTION:
                    pass
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            pygame.quit()
            sys.exit()

main()
