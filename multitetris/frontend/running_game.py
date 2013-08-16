import pygame
from pygame.locals import *  # constants
from common import consts

blockpixsize = consts['block_element_size']

pygame.init()
fpsClock = pygame.time.Clock()  # FPS

window = pygame.display.set_mode((consts['window_width'], consts['window_height']), DOUBLEBUF)
pygame.display.set_caption("The game of Multitetris is running.")  # window title

fontObj = pygame.font.Font('freesansbold.ttf', 30)

semirandomColor = pygame.Color(123, 230, 58)
blockInnerColor = pygame.Color(192, 73, 239)
blockBorderColor = pygame.Color(23, 45, 32)

def BlockPos_to_PixPos(BPX, BPY):
    return (10 + BPX * blockpixsize, 200 + BPY * blockpixsize)

def DrawBlockElement(BlockPosX, BlockPosY):
    X, Y = BlockPos_to_PixPos(BlockPosX, BlockPosY)
    pygame.draw.rect(window, blockBorderColor, (X, Y, blockpixsize, blockpixsize))
    pygame.draw.rect(window, blockInnerColor, (1+X, 1+Y, blockpixsize-2, blockpixsize-2))

while True:
    window.fill(semirandomColor)
    for i in range(10):
        for j in range(10):
            DrawBlockElement(i, j)

    pygame.display.update()  # speak your mind!
    fpsClock.tick(consts['max_fps'])
