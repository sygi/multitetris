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
    	if   event.type == QUIT:
    		quit_request = True
    	elif event.type == MOUSEMOTION:
    		mousex, mousey = event.pos
    	elif event.type == KEYDOWN:
    		if event.key == K_ESCAPE:
    			quit_request = True
    pygame.display.update()
    fps_clock.tick(60)

pygame.quit()
