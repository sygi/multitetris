import pygame
from pygame.locals import *
import json
import os

from .common import consts, colors
from . import connection


########################
# Globals
########################

mousex,mousey = 0,0
cur_screen = 'GAME'
SIZE = (consts.block_element_size, consts.block_element_size)
no_of_players = 7
arial_font = None
players_names = ["Player 1", "Player 2", "Player 3", "Player 4",
            "Player 5", "Player 6", "Player 7", "Player 8"]
cur_connection = None
board_topleft = (20, 30)
playersline_topleft = (20, 5)
playersline_height = 20

########################
# Drawing functions
########################

def draw_menu(display):
    """
    Menu screen
    """
    pass

def draw_box(display, color, screenpos):
    pygame.draw.rect(display, color,
                 (screenpos[0] + 1, screenpos[1] + 1) + (SIZE[0] - 1, SIZE[1] - 1), 0)

def draw_nicelinebox(display, color, innertopleft, innersizes, thicknesses, offset = [0, 0]):
    pygame.draw.rect(display, colors['line'],
                (innertopleft[0] + offset[0] - thicknesses[0],
                 innertopleft[1] + offset[1] - thicknesses[1],
                 innersizes[0] + 2 * thicknesses[0],
                 innersizes[1] + 2 * thicknesses[1]
                ), 2)

def draw_main_grid(display):
    # board
    draw_nicelinebox(display, colors['line'], board_topleft,
                [consts.columns_per_player * SIZE[0] * no_of_players, consts.number_of_rows * SIZE[1]], [2, 2])
    for i in range(no_of_players):
        draw_nicelinebox(display, colors['line'], playersline_topleft,
                [consts.columns_per_player * SIZE[0] - 3, 22], [2, 2], [consts.columns_per_player * SIZE[0] * i, 0])
        text_surface = arial_font.render(players_names[i], False, colors['text'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (playersline_topleft[0] + 5 + consts.columns_per_player * SIZE[0] * i + 10,
                         playersline_topleft[1] + 3)
        display.blit(text_surface, text_rect)
        

def draw_game(display):
    """
    Game screen
    """
    
    draw_main_grid(display)
    
    # process data from server and show bricks
    global cur_connection
    print cur_connection.state
    if cur_connection.state:
        for brick in cur_connection.state['bricks']:
            pos = screen_pos(brick['pos'])
            print pos + SIZE, brick['color']
            draw_box(display, brick['color'], pos + SIZE)


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
    return (board_topleft[0] + pos[0] * SIZE[0],
            board_topleft[1] + (consts.number_of_rows - pos[1] - 1) * SIZE[1] + 800)

########################
# Main loop
########################

def run(addr="localhost"):
    global arial_font, cur_connection
    
    cur_connection = connection.Connection(addr)
    
    pygame.init()
    fps_clock = pygame.time.Clock()  # FPS limiter
    
    arial_font = pygame.font.SysFont("arial", 17)
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
