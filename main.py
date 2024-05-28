import pygame
import time
from pygame.locals import *
from copy import deepcopy

# Definição das direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Player:
    def __init__(self, position: list, color, direction, up_key, down_key, left_key, right_key):
        self.position = position
        self.color = color
        self.direction = direction
        self.trail = []
        self.up_key = up_key
        self.down_key = down_key
        self.left_key = left_key
        self.right_key = right_key

    
    def move(self, speed):
        if self.direction == UP:
            self.position[1] -= speed
        elif self.direction == DOWN:
            self.position[1] += speed
        elif self.direction == LEFT:
            self.position[0] -= speed
        elif self.direction == RIGHT:
            self.position[0] += speed

    def change_direction(self, key):
        if key == self.up_key and self.direction != DOWN:
            self.direction = UP
        elif key == self.down_key and self.direction != UP:
            self.direction = DOWN
        elif key == self.left_key and self.direction != RIGHT:
            self.direction = LEFT
        elif key == self.right_key and self.direction != LEFT:
            self.direction = RIGHT

class SoundManager:
    def __init__(self):
        self.sound_die = pygame.mixer.Sound("assets/sounds/die.mp3")
        self.sound_start = pygame.mixer.Sound("assets/sounds/start.mp3")
        self.sound_move = pygame.mixer.Sound("assets/sounds/move.mp3")
        self.sound_bg = pygame.mixer.Sound("assets/sounds/bg-music.mp3")

    def play_die(self):
        self.sound_die.play()
        self.sound_die.set_volume(0.4)
    
    def play_start(self):
        self.sound_start.play()
        self.sound_start.set_volume(0.4)

    def play_move(self):
        self.sound_move.play()
        self.sound_move.set_volume(0.3)
    
    def play_bg(self):
        self.sound_bg.play(-1)
        self.sound_bg.set_volume(0.3) 


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((550, 700))
        self.img_bg = pygame.image.load("assets/img/bg-tron.jpg")
        pygame.display.set_caption("Tron Game")

        self.clock = pygame.time.Clock()
        self.clock_tick = 25

        self.player_speed = 5
        self.points_player1 = 0
        self.points_player2 = 0
        self.game_over = False
        self.if_lose = ""

        self.sound_manager = SoundManager()

        self.player1 = Player([275, 600], (0, 0, 255), UP, K_UP, K_DOWN, K_LEFT, K_RIGHT)
        self.player2 = Player([275, 100], (255, 255, 0), DOWN, K_w, K_s, K_a, K_d)

    def reset_game(self):
        self.player1.position = [275, 600]
        self.player1.direction = UP
        self.player1.trail = []

        self.player2.position = [275, 100]
        self.player2.direction = DOWN
        self.player2.trail = []

    def lose(self):
        self.sound_manager.play_die()
        time.sleep(1.5)
        self.screen.fill((0, 0, 0))

        font = pygame.font.SysFont(None, 48)
        if self.if_lose != "tie":
            lose_text = font.render("YOU LOSE!", True, (255, 0, 0))
            text_rect = lose_text.get_rect(center=(275, 200))
            self.screen.blit(lose_text, text_rect)

            if self.if_lose == "YELLOW":
                self.points_player1 += 1
                lose_text = font.render(self.if_lose, True, (255, 255, 0))
                text_rect = lose_text.get_rect(center=(275, 240))
                self.screen.blit(lose_text, text_rect)

            elif self.if_lose == "BLUE":
                self.points_player2 += 1
                lose_text = font.render(self.if_lose, True, (0, 0, 255))
                text_rect = lose_text.get_rect(center=(275, 240))
                self.screen.blit(lose_text, text_rect)
        else:
            lose_text = font.render("A TIE", True, (255, 0, 255))
            text_rect = lose_text.get_rect(center=(275, 200))
            self.screen.blit(lose_text, text_rect)

        font = pygame.font.SysFont(None, 30)
        button_text = font.render("Press SPACE", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(275, 375))
        self.screen.blit(button_text, button_rect)

        font = pygame.font.SysFont(None, 25)
        points_text = font.render(f"Blue: {self.points_player1} | Yellow: {self.points_player2}", True, (255, 255, 255))
        points_rect = points_text.get_rect(center=(282, 450))
        self.screen.blit(points_text, points_rect)

        pygame.display.update()

        self.game_over = True
        while self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.game_over = False
                        self.reset_game()

    def run(self):
        self.sound_manager.play_start()
        time.sleep(1)
        self.sound_manager.play_bg()

        while not self.game_over:
            self.clock.tick(self.clock_tick)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == KEYDOWN:
                    self.sound_manager.play_move()
                    self.player1.change_direction(event.key)
                    self.player2.change_direction(event.key)

            self.player1.move(self.player_speed)
            self.player2.move(self.player_speed)

            if self.check_collision():
                continue

            self.screen.blit(self.img_bg, (0, 0))
            self.draw_trail(self.player1)
            self.draw_trail(self.player2)
            self.draw_player(self.player1)
            self.draw_player(self.player2)
            pygame.display.update()

        pygame.quit()

    def check_collision(self):
        if (self.player1.position[0] < 0 or self.player1.position[0] >= self.screen.get_width() or
            self.player1.position[1] < 0 or self.player1.position[1] >= self.screen.get_height()):
            self.if_lose = "BLUE"
            self.lose()
            return True

        if (self.player2.position[0] < 0 or self.player2.position[0] >= self.screen.get_width() or
            self.player2.position[1] < 0 or self.player2.position[1] >= self.screen.get_height()):
            self.if_lose = "YELLOW"
            self.lose()
            return True

        if self.player1.position in self.player1.trail or self.player1.position in self.player2.trail:
            self.if_lose = "BLUE"
            self.lose()
            return True

        if self.player2.position in self.player1.trail or self.player2.position in self.player2.trail:
            self.if_lose = "YELLOW"
            self.lose()
            return True

        if self.player1.position == self.player2.position:
            self.if_lose = "tie"
            self.lose()
            return True

        self.player1.trail.append(deepcopy(self.player1.position))
        self.player2.trail.append(deepcopy(self.player2.position))
        return False

    def draw_trail(self, player):
        for pos in player.trail:
            pygame.draw.rect(self.screen, player.color, (pos[0], pos[1], 5, 5))

    def draw_player(self, player):
        pygame.draw.rect(self.screen, player.color, (player.position[0], player.position[1], 5, 5))

if __name__ == "__main__":
    game = Game()
    game.run()
