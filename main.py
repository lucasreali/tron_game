# Objetivo de criar um jogo do tron para TDE

import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode([500, 700])

name = "Tron Game"
pygame.display.set_caption(name)

# ico = pygame.image.load("colocar aq o link do icone")
# pygame.display.set_icon(ico)


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3



clock_tick = 20
clock = pygame.time.Clock()

player_pos = [(300, 300)]
player_surface = pygame.Surface((10, 10))
player_surface.fill((255, 255, 255))

my_direction = UP

while True:
    clock.tick(clock_tick)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    screen.fill([0, 0, 0])

    pygame.display.update()