import pygame
from pygame.locals import *  # constants
from common import *

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


def draw_game():
    """
    Game screen
    """
    pass


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
blockpixsize = consts['block_element_size']
dmsg = '' # debug msg

pygame.init()
fps_clock = pygame.time.Clock()  # FPS limiter

display = pygame.display.set_mode((consts['window_width'], consts['window_height']), DOUBLEBUF)
pygame.display.set_caption("Multitetris")

fontObj = pygame.font.Font('freesansbold.ttf', 30)
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

    pygame.display.update()
    fps_clock.tick(config['max_fps'])


def block_pos_to_pix_pos(x, y):
    return 10 + x * blockpixsize, 200 + y * blockpixsize


def draw_block_element(x, y):
    x, y = block_pos_to_pix_pos(x, y)
    pygame.draw.rect(window, colors['block-border'], (x, y, blockpixsize, blockpixsize))
    pygame.draw.rect(window, colors['block-inner'], (x+1, y+1, blockpixsize-2, blockpixsize-2))

pygame.quit()
