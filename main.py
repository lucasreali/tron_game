import pygame
from pygame.locals import *

def lose():
    global running
    running = False

pygame.init()
screen = pygame.display.set_mode((550, 700))

name = "Tron Game"
pygame.display.set_caption(name)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

players_color = (255, 255, 255)

color_trail1 = (0, 0, 255)
color_trail2 = (255, 255, 0)

clock_tick = 25
clock = pygame.time.Clock()

player1_pos = [275, 600]
player1_direction = UP
player1_speed = 5
player1_trail = []

player2_pos = [275, 100]
player2_direction = DOWN
player2_speed = 5
player2_trail = []

running = True

while running:
    clock.tick(clock_tick)

    for event in pygame.event.get():
        if event.type == QUIT:
            lose()

    keys = pygame.key.get_pressed()
    if keys[K_UP] and player1_direction != DOWN:
        player1_direction = UP
    elif keys[K_DOWN] and player1_direction != UP:
        player1_direction = DOWN
    elif keys[K_LEFT] and player1_direction != RIGHT:
        player1_direction = LEFT
    elif keys[K_RIGHT] and player1_direction != LEFT:
        player1_direction = RIGHT

    if keys[K_w] and player2_direction != DOWN:
        player2_direction = UP
    elif keys[K_s] and player2_direction != UP:
        player2_direction = DOWN
    elif keys[K_a] and player2_direction != RIGHT:
        player2_direction = LEFT
    elif keys[K_d] and player2_direction != LEFT:
        player2_direction = RIGHT

    if player1_direction == UP:
        player1_pos[1] -= player1_speed
    elif player1_direction == DOWN:
        player1_pos[1] += player1_speed
    elif player1_direction == LEFT:
        player1_pos[0] -= player1_speed
    elif player1_direction == RIGHT:
        player1_pos[0] += player1_speed

    if player2_direction == UP:
        player2_pos[1] -= player2_speed
    elif player2_direction == DOWN:
        player2_pos[1] += player2_speed
    elif player2_direction == LEFT:
        player2_pos[0] -= player2_speed
    elif player2_direction == RIGHT:
        player2_pos[0] += player2_speed

    if player1_pos[0] < 0 or player1_pos[0] >= screen.get_width() or player1_pos[1] < 0 or player1_pos[1] >= screen.get_height():
        lose()

    if player2_pos[0] < 0 or player2_pos[0] >= screen.get_width() or player2_pos[1] < 0 or player2_pos[1] >= screen.get_height():
        lose()

    if player1_pos in player1_trail or player1_pos in player2_trail:
        lose()

    if player2_pos in player1_trail or player2_pos in player2_trail:
        lose()

    player1_trail.append(player1_pos[:])
    player2_trail.append(player2_pos[:])

    for pos in player1_trail:
        pygame.draw.rect(screen, color_trail1, (pos[0], pos[1], 5, 5))

    for pos in player2_trail:
        pygame.draw.rect(screen, color_trail2, (pos[0], pos[1], 5, 5))

    # Desenhar os jogadores
    pygame.draw.rect(screen, players_color, (player1_pos[0], player1_pos[1], 5, 5))
    pygame.draw.rect(screen, players_color, (player2_pos[0], player2_pos[1], 5, 5))

    pygame.display.update()

pygame.quit()
