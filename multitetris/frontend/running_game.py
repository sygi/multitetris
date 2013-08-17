import pygame
from pygame.locals import *
import socket
import json

from .common import consts, colors

SIZE = (consts.block_element_size, consts.block_element_size)

board_topleft = (22, 32)
playersline_topleft = (20, 5)
playersline_height = 20

pygame.init()
#fontObj = pygame.font.Font("freesansbold.ttf", 10)
fontObj = pygame.font.SysFont("arial", 17)

no_of_players = 7
players_names = ["Player 1", "Player 2", "Player 3", "Player 4",
            "Player 5", "Player 6", "Player 7", "Player 8"]

def screen_pos(pos):
    return (board_topleft[0] + pos[0] * SIZE[0],
            board_topleft[1] + (consts.number_of_rows - pos[1] - 1) * SIZE[1])

def read_state():
    return json.loads(sockf.readline())

def draw_box(display, color, screenpos):
    pygame.draw.rect(display, color,
                 (screenpos[0] + 1, screenpos[1] + 1) + (SIZE[0] - 1, SIZE[1] - 1), 0)

def draw_main_grid(display):
    # board
    pygame.draw.rect(display, colors['line'],
                (board_topleft[0] - 2,
                 board_topleft[1] - 2,
                 consts.columns_per_player * SIZE[0] * no_of_players + 4,
                 consts.number_of_rows * SIZE[1] + 4
                ), 2)
    # players_line
    pygame.draw.rect(display, colors['line'],
                (playersline_topleft[0],
                 playersline_topleft[1],
                 consts.columns_per_player * SIZE[0] * no_of_players + 4,
                 25
                ), 2)
    for i in range(no_of_players):
        pygame.draw.rect(display, colors['line'],
                (playersline_topleft[0] + 1 + consts.columns_per_player * SIZE[0] * i,
                 playersline_topleft[1] + 2,
                 2,
                 25
                ), 1)
        text_surface = fontObj.render(players_names[i], False, colors['text'])
        text_rect = text_surface.get_rect()
        text_rect.topleft = (playersline_topleft[0] + 5 + consts.columns_per_player * SIZE[0] * i + 10,
                         playersline_topleft[1] + 3)
        display.blit(text_surface, text_rect)
        

def draw_game(display):
    draw_main_grid(display)
    state = read_state()
    print state

    for brick in state['bricks']:
        pos = screen_pos(brick['pos'])
        print pos + SIZE, brick['color']
        draw_box(display, brick['color'], pos + SIZE)


def run():
    global sock, sockf
    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sockf = sock.makefile('r+')

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
