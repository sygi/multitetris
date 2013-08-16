import pygame
from pygame.locals import *  # constants
from common import consts

pygame.init()
fpsClock = pygame.time.Clock()  # FPS

windowSurfaceObj = pygame.display.set_mode((consts.window_width, consts.window_height))
pygame.display.set_caption("Multitetris")  # window title

fontObj = pygame.font.Font('freesansbold.ttf', 30)

semirandomColor = pygame.Color(123, 230, 58)

while True:
    windowSurfaceObj.fill(semirandomColor)

    pygame.display.update()  # speak your mind!
    fpsClock.tick(60)
