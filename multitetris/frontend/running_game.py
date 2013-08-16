import pygame
from pygame.locals import * # constants

pygame.init()
fps_clock = pygame.time.Clock() # FPS

display = pygame.display.set_mode((const_windowwidth, const_windowgeight))
pygame.display.set_caption("Multitetris") # window title

fontObj = pygame.font.Font('freesansbold.ttf', 30)

semirandomColor = pygame.Color(123, 230, 58)

while True:
    windowSurfaceObj.fill(semirandomColor)
	
    pygame.display.update() # speak your mind!
    fpsClock.tick(60)
