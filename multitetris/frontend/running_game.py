import pygame
from pygame.locals import *  # constants
from common import *

#import sys
#sys.path.append('../backend')
#import mock

########################
# Globals
########################

mousex,mousey = 0,0
cur_screen = 'MENU'

def draw_menu():
    """
    Menu screen
    """
    pass


def draw_game(display):
    """
    Game screen
    """
    lineColor = pygame.Color(100, 100, 100)
    blockpixsize = consts['block_element_size']
    
    def draw_the_table():
        for k in range(0, 600, 60):
            pygame.draw.line(windowSurface, (100, 100, 101), ( consts['window_width']-consts['tab_width'], k ), (consts['window_width'], k ))
            pygame.draw.line(windowSurface, (100, 100, 101), ( consts['window_width']-consts['tab_width'], 0 ), (consts['window_width']-consts['tab_width'], consts['window_height'] ))
    
    def draw_the_bricks(board):
        def blockPos_to_pixPos(BPX, BPY):
            # Blocks should be displayed in a grid in "virtual window" placed somewhere in game window, currently starting from (10,200)
            return (10 + BPX * blockpixsize, 200 + BPY * blockpixsize)
        def draw_block_element((BlockPosX, BlockPosY), color):
            # Draw a block element in a block's array
            X, Y = blockPos_to_pixPos(BlockPosX, BlockPosY)
            pygame.draw.rect(display, colors['block_border'], (X, Y, blockpixsize, blockpixsize), 1)
            pygame.draw.rect(display, color, (1+X, 1+Y, blockpixsize-2, blockpixsize-2), 0)
        def draw_a_brick(pos, type = "duck", color = colors['block_inner']):
            pass
        
        def draw_the_grid():
            for i in range(consts['number_of_rows']*blockpixsize):
                for j in range(consts['columns_per_player']*blockpixsize):
                    X, Y = blockPos_to_pixPos(i, j)
                    pygame.draw.rect(display, colors['block_border'], (X, Y, blockpixsize, blockpixsize), 1)
        
        # finally, do sth
        for (pos, sth) in board:
            draw_a_brick(pos)
        
        draw_the_grid()
        # end of draw_the_blocks()
    
    display.fill(colors['semirandom'])
    board = []
    draw_the_bricks(board)
    # end of draw_game()


def draw_about():
    """
    About screen
    """
    pass


def draw_loading():
    """
    Loading screen
    """
    pass


def draw_join():
    """
    Join screen
    """
    pass

def draw():
    """
    Main draw function
    """
    if cur_screen == 'MENU': draw_menu()
    if cur_screen == 'GAME': draw_game()
    if cur_screen == 'ABOUT': draw_about()
    if cur_screen == 'LOADING': draw_loading()
    if cur_screen == 'JOIN': draw_join()

########################
# PyGame init
########################
dmsg = '' # debug msg

pygame.init()
fps_clock = pygame.time.Clock()  # FPS limiter

display = pygame.display.set_mode((consts['window_width'], consts['window_height']), DOUBLEBUF)
pygame.display.set_caption("Multitetris")

quit_request = False

########################
# Main loop
########################
while not quit_request:
    display.fill(pygame.Color(0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            quit_request = True
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit_request = True
    
    draw_game(display)
    
    pygame.display.update()
    fps_clock.tick(config['max_fps'])

pygame.quit()
