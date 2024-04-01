import pygame, time, random
from pygame.locals import *
                
# TUDO QUE ESTIVER COMENTADO É PARA A IMAGEM DO PLAYER QUE ESTOU COLOCANDO

def colision(x, y):
    return x[0] == y[0] and x[1] == y[1]

def onGridRandom():
    x = random.randint(0, 54)
    y = random.randint(0, 69)

    pos = (x*5, y*5)

    while True:
        if pos in player1_trail or pos in player2_trail:
            x = random.randint(0, 109)
            y = random.randint(0, 139)

            pos = (x*5, y*5)

        else:
            return pos


def lose():
    global points_player1, points_player2

    sound_die.play()
    time.sleep(1.5)
    screen.fill((0, 0, 0))


    if if_lose != "tie":
        font = pygame.font.SysFont(None, 48)
        lose_text = font.render("YOU LOSE!", True, (255, 0, 0))
        text_rect = lose_text.get_rect(center=(275, 200))
        screen.blit(lose_text, text_rect)


        if if_lose == "YELLOW":
            points_player1 += 1
            font = pygame.font.SysFont(None, 30)
            lose_text = font.render(if_lose , True, (255, 255, 0))
            text_rect = lose_text.get_rect(center=(275, 240))
            screen.blit(lose_text, text_rect)


        elif if_lose == "BLUE":
            points_player2 += 1
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
    global player1_pos, player1_direction, player1_trail, player2_direction, player2_pos, player2_trail, img_player, rotate_img1, rotate_img2

    player1_pos = [275, 600]
    player1_direction = UP
    rotate_img1 = pygame.transform.rotate(img_player, 0)
    player1_trail = []

    player2_pos = [275, 100]
    player2_direction = DOWN
    rotate_img2 = pygame.transform.rotate(img_player, 180)
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

explosion_size = (60, 60)
img_explosion_load = pygame.image.load("assets/img/explosion.png")
img_explosion = pygame.transform.scale(img_explosion_load, explosion_size)

img_size = (15, 40)
img_player = pygame.transform.scale(pygame.image.load("assets/img/player.png"), img_size)

# rotate_img1 = pygame.transform.rotate(img_player, 0)
# rotate_img2 = pygame.transform.rotate(img_player, 180)

player_color = (255, 255, 255)
player = pygame.Surface((5, 5))
player.fill(player_color)

color_trail1 = (0, 0, 255)
color_trail2 = (255, 255, 0)

players_speed1 = 5
players_speed2 = 5

player1_pos = [275, 600]
player1_direction = UP
player1_trail = []

player2_pos = [275, 100]
player2_direction = DOWN
player2_trail = []

points_player1 = 0
points_player2 = 0


"""  Powerups
1 - Uma vida a +
2 - Congelar o inimigo]
"""
powerUp_freezing = pygame.Surface((5, 5))
powerUp_freezing.fill((45, 180, 180))
powerUp_freezing_pos = (-10, -10)


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

sec = cont = 0

while not game_over:
    clock.tick(clock_tick)

    cont += 1
    if cont == clock_tick:
        sec += 1
        cont = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[K_UP] and player1_direction != DOWN:
        player1_direction = UP
        # rotate_img1 = pygame.transform.rotate(img_player, 0)
    elif keys[K_DOWN] and player1_direction != UP:
        player1_direction = DOWN
        # rotate_img1 = pygame.transform.rotate(img_player, 180)
    elif keys[K_LEFT] and player1_direction != RIGHT:
        player1_direction = LEFT
        # rotate_img1 = pygame.transform.rotate(img_player, 90)
    elif keys[K_RIGHT] and player1_direction != LEFT:
        player1_direction = RIGHT
        # rotate_img1 = pygame.transform.rotate(img_player, -90)

    if keys[K_w] and player2_direction != DOWN:
        player2_direction = UP
        # rotate_img2 = pygame.transform.rotate(img_player, 0)
    elif keys[K_s] and player2_direction != UP:
        player2_direction = DOWN
        # rotate_img2 = pygame.transform.rotate(img_player, 180)
    elif keys[K_a] and player2_direction != RIGHT:
        player2_direction = LEFT
        # rotate_img2 = pygame.transform.rotate(img_player, 90)
    elif keys[K_d] and player2_direction != LEFT:
        player2_direction = RIGHT
        # rotate_img2 = pygame.transform.rotate(img_player, -90)


    if player1_direction == UP:
        player1_pos[1] -= players_speed1
    elif player1_direction == DOWN:
        player1_pos[1] += players_speed1
    elif player1_direction == LEFT:
        player1_pos[0] -= players_speed1
    elif player1_direction == RIGHT:
        player1_pos[0] += players_speed1

    if player2_direction == UP:
        player2_pos[1] -= players_speed2
    elif player2_direction == DOWN:
        player2_pos[1] += players_speed2
    elif player2_direction == LEFT:
        player2_pos[0] -= players_speed2
    elif player2_direction == RIGHT:
        player2_pos[0] += players_speed2

    if player1_pos[0] < 0 or player1_pos[0] >= screen.get_width() or player1_pos[1] < 0 or player1_pos[1] >= screen.get_height():
        if_lose = "BLUE"
        lose()

    if player2_pos[0] < 0 or player2_pos[0] >= screen.get_width() or player2_pos[1] < 0 or player2_pos[1] >= screen.get_height():
        if_lose = "YELLOW"
        lose()

    if player1_pos in player1_trail[1:] or player1_pos in player2_trail:
        if_lose = "BLUE"
        lose()

    if player2_pos in player1_trail or player2_pos in player2_trail[1:]:
        if_lose = "YELLOW"
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
    
    if sec == 8:
        powerUp_freezing_pos = onGridRandom()
        sec = 0

    if colision(player1_pos, powerUp_freezing_pos):
        powerUp_freezing_pos = (-10, -10)


    # screen.blit(rotate_img1, rotate_img1.get_rect(center=player1_pos))
    # screen.blit(rotate_img2, rotate_img2.get_rect(center=player2_pos))
        
    screen.blit(player, player1_pos)
    screen.blit(player, player2_pos)
    # screen.blit(powerUp_freezing, powerUp_freezing_pos)

    pygame.display.update()

pygame.quit()

