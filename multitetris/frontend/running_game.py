import pygame
from pygame.locals import *  # constants
from common import *

########################
# Menu screen
########################

def draw_menu():
    pass

########################
# Game screen
########################

def draw_game():
    pass

########################
# About screen
########################

def draw_about():
    pass

########################
# Loading screen
########################

def draw_loading():
    pass

########################
# Join screen
########################

def draw_join():
    pass

########################
# Main draw funtion
########################

def draw():
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
<<<<<<< HEAD
        if event.type == QUIT:
=======
        if   event.type == QUIT:
>>>>>>> e842a9d13875580565c66faf167d260a8f9bb61a
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
