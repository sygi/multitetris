import pygame
from pygame.locals import *  # constants
from common import *


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
    pass

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

# Controls
mousex,mousey = 0,0

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

while True:
    window.fill(colors['semirandom'])
    for i in range(10):
        for j in range(10):
            draw_block_element(i, j)

pygame.quit()
