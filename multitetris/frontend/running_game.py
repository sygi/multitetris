import pygame
from pygame.locals import *
import json
import os

from .common import consts
from . import connection

########################
# Globals
########################

mousex,mousey = 0,0
cur_screen = 'GAME'
SIZE = (15, 15)
cur_connection = None

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

def draw(display):
    """
    Main draw function
    """
    if   cur_screen == 'MENU'   : draw_menu(display)
    elif cur_screen == 'GAME'   : draw_game(display)
    elif cur_screen == 'ABOUT'  : draw_about(display)
    elif cur_screen == 'LOADING': draw_loading(display)
    elif cur_screen == 'JOIN'   : draw_join(display)
    else:
        raise Exception('Unknown screen name!')
    pass

########################
# Controls
########################

def on_key_LEFT():
    if cur_connection:
        cur_connection.move('L')

def on_key_RIGHT():
    if cur_connection:
        cur_connection.move('R')

def on_key_UP():
    if cur_connection:
        cur_connection.move('U')

def on_key_DOWN():
    if cur_connection:
        cur_connection.move('D')

########################
# Helper functions
########################

def screen_pos(pos):
    return (pos[0] * SIZE[0],
            consts.window_height - pos[1] * SIZE[1])

########################
# Main loop
########################
def run(addr="localhost"):
    cur_connection = connection.Connection(addr)

    pygame.init()
    fps_clock = pygame.time.Clock()  # FPS limiter

    display = pygame.display.set_mode((
        consts.window_width, consts.window_height))
    pygame.display.set_caption("Multitetris")
    pygame.key.set_repeat(500, 500)  # (delay, interval) - how many KEYDOWN events when holding a key, in ms

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
                elif event.key == K_LEFT:
                    on_key_LEFT()
                elif event.key == K_RIGHT:
                    on_key_RIGHT()
                elif event.key == K_UP:
                    on_key_UP()
                elif event.key == K_DOWN:
                    on_key_DOWN()

        draw(display)

        pygame.display.flip()
        fps_clock.tick(20)

    pygame.quit()
    os._exit(0)

if __name__ == '__main__':
    run()
