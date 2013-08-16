import pygame
from pygame.locals import *  # constants
from common import consts, config

blockpixsize = consts['block_element_size']
dmsg = '' # debug msg

pygame.init()
fpsClock = pygame.time.Clock()  # FPS

windowSurface = pygame.display.set_mode((consts['window_width'], consts['window_height']), DOUBLEBUF)
pygame.display.set_caption("The game of Multitetris is running.")  # window title

fontObj = pygame.font.Font('freesansbold.ttf', 15)

semirandomColor = pygame.Color(123, 230, 58)
blockInnerColor = pygame.Color(192, 73, 239)
blockBorderColor = pygame.Color(23, 45, 32)
debugFontColor = pygame.Color(250, 250, 250)

def blockPos_to_pixPos(BPX, BPY):
    # Blocks should be displayed in a grid in "virtual window" placed somewhere in game window, currently starting from (10,200)
    return (10 + BPX * blockpixsize, 200 + BPY * blockpixsize)

def draw_block_element(BlockPosX, BlockPosY):
    # Draw a block element in a block's array
    X, Y = blockPos_to_pixPos(BlockPosX, BlockPosY)
    pygame.draw.rect(windowSurface, blockBorderColor, (X, Y, blockpixsize, blockpixsize), )
    pygame.draw.rect(windowSurface, blockInnerColor, (1+X, 1+Y, blockpixsize-2, blockpixsize-2))

def on_quit_request():
    # If a player signals his will to quit
    # shall we return to the menu, or quit immediately?
    pygame.quit()
    sys.exit()
    

while True:
    windowSurface.fill(semirandomColor)
    
    # draw an array of blocks, 10x10
    for i in range(10):
        for j in range(10):
            draw_block_element(i, j)
    
    # Events!
    for event in pygame.event.get():
        if event.type == QUIT:
            on_quit_request()
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                dmsg = 'key down!'
            if event.key == K_ESCAPE:
                dmsg = 'they try to escape!'
                pygame.event.post(pygame.event.Event(QUIT))
    
    # Debug!
    dmsgSurface = fontObj.render(dmsg, False, debugFontColor)
    dmsgRect = dmsgSurface.get_rect()
    dmsgRect.topleft = (10, consts['window_height'] - 25)
    windowSurface.blit(dmsgSurface, dmsgRect)
    
    pygame.display.update()  # speak your mind!
    fpsClock.tick(config['max_fps'])
