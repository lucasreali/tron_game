import pygame, time
from pygame.locals import *

def lose():
    global game_over

    sound_die.play()
    time.sleep(2)

    # screen.fill((0, 0, 0))
    screen.blit(img_bg, (0, 0))

    if if_lose != "tie":
        font = pygame.font.SysFont(None, 48)
        lose_text = font.render("YOU LOSE!", True, (255, 0, 0))
        text_rect = lose_text.get_rect(center=(275, 200))
        screen.blit(lose_text, text_rect)

        if if_lose == "YELLOW":
            font = pygame.font.SysFont(None, 30)
            lose_text = font.render(if_lose , True, (255, 255, 0))
            text_rect = lose_text.get_rect(center=(275, 240))
            screen.blit(lose_text, text_rect)
        elif if_lose == "BLUE":
            font = pygame.font.SysFont(None, 30)
            lose_text = font.render(if_lose, True, (0, 0, 255))
            text_rect = lose_text.get_rect(center=(275, 240))
            screen.blit(lose_text, text_rect)
    
    elif if_lose == "tie":
        font = pygame.font.SysFont(None, 48)
        lose_text = font.render("A TIE", True, (255, 0, 255))
        text_rect = lose_text.get_rect(center=(275, 200))
        screen.blit(lose_text, text_rect)


    game_over = True
    button_text = font.render("Press SPACE", True, (255, 255, 225))
    button_rect = button_text.get_rect(center=(275, 375))
    screen.blit(button_text, button_rect)

    fontsys = pygame.font.SysFont(None, 25)

    points_text = fontsys.render(f"Blue: {points_player1} | Yellow: {points_player2}", True, (255, 255, 255))
    points_rect = points_text.get_rect(center=(282, 450))
    screen.blit(points_text, points_rect)

    pygame.display.update()

    while game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game_over = False
                    reset_game()

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
img_bg = pygame.image.load("assets/img/bg-tron.jpg")

name = "Tron Game"
pygame.display.set_caption(name)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

player_color = (255, 255, 255)
player = pygame.Surface((5, 5))
player.fill(player_color)

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

sound_die = pygame.mixer.Sound("assets/sounds/die.mp3")
sound_start = pygame.mixer.Sound("assets/sounds/start.mp3")
sound_move = pygame.mixer.Sound("assets/sounds/move.mp3")
sound_bg = pygame.mixer.Sound("assets/sounds/bg-music.mp3")

clock_tick = 25
clock = pygame.time.Clock()

if_lose = ""

game_over = False

sound_start.play()
time.sleep(1)

sound_bg.play(-1)

while not game_over:
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
        if_lose = "BLUE"
        points_player2 += 1
        lose()

    if player2_pos[0] < 0 or player2_pos[0] >= screen.get_width() or player2_pos[1] < 0 or player2_pos[1] >= screen.get_height():
        if_lose = "YELLOW"
        points_player1 += 1
        lose()

    if player1_pos in player1_trail or player1_pos in player2_trail:
        if_lose = "BLUE"
        points_player2 += 1
        lose()

    if player2_pos in player1_trail or player2_pos in player2_trail:
        if_lose = "YELLOW"
        points_player1 += 1
        lose()

    if player1_pos == player2_pos:
        if_lose = "tie"
        lose()

    player1_trail.append(player1_pos[:])
    player2_trail.append(player2_pos[:])

    screen.blit(img_bg, (0, 0))

    for pos in player1_trail:
        pygame.draw.rect(screen, color_trail1, (pos[0], pos[1], 5, 5))

    for pos in player2_trail:
        pygame.draw.rect(screen, color_trail2, (pos[0], pos[1], 5, 5))

    screen.blit(player, player1_pos)
    screen.blit(player, player2_pos)

    pygame.display.update()

pygame.quit()
