import pygame
from pygame.locals import *

def lose():
    pygame.quit()

pygame.init()
screen = pygame.display.set_mode((550, 700))

name = "Tron Game"
pygame.display.set_caption(name)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

clock_tick = 25
clock = pygame.time.Clock()

player_pos = [300, 300]
player_surface = pygame.Surface((5, 5))
player_surface.fill((255, 255, 255))

my_direction = UP
player_speed = 5
trail = []


while True:
    clock.tick(clock_tick)

    for event in pygame.event.get():
        if event.type == QUIT:
            lose()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            elif event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            elif event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            elif event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if my_direction == UP:
        player_pos[1] -= player_speed
    elif my_direction == DOWN:
        player_pos[1] += player_speed
    elif my_direction == LEFT:
        player_pos[0] -= player_speed
    elif my_direction == RIGHT:
        player_pos[0] += player_speed

    if player_pos[0] < 0 or player_pos[0] >= screen.get_width() or player_pos[1] < 0 or player_pos[1] >= screen.get_height():
        running = False

    trail.append(player_pos[:])

    for pos in trail:
        pygame.draw.rect(screen, (0, 0, 255), (pos[0], pos[1], 5, 5))

    screen.blit(player_surface, player_pos)
    pygame.display.update()

pygame.quit()
