import pygame
from pygame.locals import *
import socket
import json

from .common import consts

########################
# Globals
########################

mousex,mousey = 0,0
cur_screen = 'MENU'
bricks = []
SIZE = (15, 15)

########################
# Drawing functions
########################

def draw_menu(display):
    """
    Menu screen
    """
    pass


def draw_game(display):
    """
    Game screen
    """
    line_color = (100, 100, 100)
    blockpixsize = consts.block_element_size

    state = read_state()

    display.fill((123, 230, 58))
    pass


def draw_about(display):
    """
    About screen
    """
    pass


def draw_loading(display):
    """
    Loading screen
    """
    pass


def draw_join(display):
    """
    Join screen
    """
    pass

########################
# Helper functions
########################

def screen_pos(pos):
    return (pos[0] * SIZE[0],
            consts.window_height - pos[1] * SIZE[1])

def read_state():
    return json.loads(sockf.readline())

########################
# Main loop
########################
def run():
    global sock, sockf
    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sockf = sock.makefile('r+')

    pygame.init()
    fps_clock = pygame.time.Clock()  # FPS limiter

    display = pygame.display.set_mode((
        consts.window_width, consts.window_height))
    pygame.display.set_caption("Multitetris")

    quit_request = False

    while not quit_request:
        display.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                quit_request = True
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_request = True

        draw_game(display)

        pygame.display.flip()
        fps_clock.tick(20)

    pygame.quit()

if __name__ == '__main__':
    run()
