
import pygame
from pygame.locals import * # constants

pygame.init()
fpsClock = pygame.time.Clock() # FPS

const_maxwindowwidth = 20 * 10 * 5 # maxplayers * columnsperplayer * blockelementsize
const_maxwindowgeight = 50 * 5 + 300 # rowsperplayer * blockelementsize + whatever

windowSurfaceObj = pygame.display.set_mode((const_maxwindowwidth, const_maxwindowgeight))
pygame.display.set_caption("The game of Multitetris is running.") # window title

fontObj = pygame.font.Font('freesansbold.ttf', 30)

semirandomColor = pygame.Color(123, 230, 58)

while True:
    windowSurfaceObj.fill(semirandomColor)
	
    pygame.display.update() # speak your mind!
    fpsClock.tick(60)
