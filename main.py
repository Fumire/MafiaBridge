import pygame
from pygame.locals import *
from custom_color import palette

def main():
    pygame.init()
    
    size = width, height = 1024,576
    previous_stage, stage = -1, 0
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mafia Bridge")

    fontObjBig = pygame.font.Font("SeoulNamsanB.otf",width//16)
    fontObjNormal = pygame.font.Font("SeoulNamsanB.otf",width//32)
    fontObjSmall = pygame.font.Font("SeoulNamsanB.otf",width//64)

    pygame.mouse.set_visible(True)
    while True:
        try:
            screen.fill(palette["blue"])
            if stage == 0:
                pass
            elif stage == 1:
                pass
            elif stage == 2:
                pass
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
