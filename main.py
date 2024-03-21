import pygame
from pygame.locals import *

def lose():
    global game_over

    screen.fill((0, 0, 0))

    font = pygame.font.SysFont(None, 48)
    lose_text = font.render("YOU LOSE!", True, (255, 0, 0))
    text_rect = lose_text.get_rect(center=(275, 200))
    screen.blit(lose_text, text_rect)

    game_over = True
    button_text = font.render("Press SPACE", True, (255, 255, 225))
    button_rect = button_text.get_rect(center=(275, 375))
    screen.blit(button_text, button_rect)

    fontsys = pygame.font.SysFont(None, 25)

    points_text = fontsys.render(f"Blue: {points_player1} | Yellow: {points_player2}", True, (255, 255, 255))
    points_rect = points_text.get_rect(center=(270, 450))
    screen.blit(points_text, points_rect)

    pygame.display.update()

    while game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    screen.fill((0, 0, 0))
                    reset_game()
                    game_over = False

def reset_game():
    global player1_direction, player1_pos, player1_direction, player1_trail, player2_direction, player2_pos, player2_trail
    player1_pos = [275, 600]
    player1_direction = UP
    player1_trail = []

    player2_pos = [275, 100]
    player2_direction = DOWN
    player2_trail = []


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

players_speed = 5

player1_pos = [275, 600]
player1_direction = UP
player1_trail = []

player2_pos = [275, 100]
player2_direction = DOWN
player2_trail = []

points_player1 = 0
points_player2 = 0

clock_tick = 25
clock = pygame.time.Clock()


while True:
    clock.tick(clock_tick)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

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
        player1_pos[1] -= players_speed
    elif player1_direction == DOWN:
        player1_pos[1] += players_speed
    elif player1_direction == LEFT:
        player1_pos[0] -= players_speed
    elif player1_direction == RIGHT:
        player1_pos[0] += players_speed

    if player2_direction == UP:
        player2_pos[1] -= players_speed
    elif player2_direction == DOWN:
        player2_pos[1] += players_speed
    elif player2_direction == LEFT:
        player2_pos[0] -= players_speed
    elif player2_direction == RIGHT:
        player2_pos[0] += players_speed

    if player1_pos[0] < 0 or player1_pos[0] >= screen.get_width() or player1_pos[1] < 0 or player1_pos[1] >= screen.get_height():
        points_player2 += 1
        lose()

    if player2_pos[0] < 0 or player2_pos[0] >= screen.get_width() or player2_pos[1] < 0 or player2_pos[1] >= screen.get_height():
        points_player1 += 1
        lose()

    if player1_pos in player1_trail or player1_pos in player2_trail:
        points_player2 += 1
        lose()

    if player2_pos in player1_trail or player2_pos in player2_trail:
        points_player1 += 1
        lose()

    if player1_pos == player2_pos:
        lose()

    player1_trail.append(player1_pos[:])
    player2_trail.append(player2_pos[:])

    for pos in player1_trail:
        pygame.draw.rect(screen, color_trail1, (pos[0], pos[1], 5, 5))

    for pos in player2_trail:
        pygame.draw.rect(screen, color_trail2, (pos[0], pos[1], 5, 5))

    pygame.draw.rect(screen, players_color, (player1_pos[0], player1_pos[1], 5, 5))
    pygame.draw.rect(screen, players_color, (player2_pos[0], player2_pos[1], 5, 5))

    pygame.display.update()

pygame.quit()
