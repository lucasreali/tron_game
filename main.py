import pygame
import time
import random
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_s, K_a, K_d, QUIT, KEYDOWN, K_SPACE

class Player:
    def __init__(self, pos, direction, color, speed, trail_color):
        self.pos = pos
        self.direction = direction
        self.color = color
        self.speed = speed
        self.trail_color = trail_color
        self.trail = []

    def move(self):
        if self.direction == K_UP:
            self.pos[1] -= self.speed
        elif self.direction == K_DOWN:
            self.pos[1] += self.speed
        elif self.direction == K_LEFT:
            self.pos[0] -= self.speed
        elif self.direction == K_RIGHT:
            self.pos[0] += self.speed

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((550, 700))
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.points_player1 = 0
        self.points_player2 = 0
        self.players_speed1 = 5
        self.players_speed2 = 5
        self.powerUp_freezing_pos = (-10, -10)
        self.sound_die = pygame.mixer.Sound("assets/sounds/die.mp3")
        self.sound_start = pygame.mixer.Sound("assets/sounds/start.mp3")
        self.sound_move = pygame.mixer.Sound("assets/sounds/move.mp3")
        self.sound_bg = pygame.mixer.Sound("assets/sounds/bg-music.mp3")
        self.clock_tick = 25
        self.sec = 0
        self.cont = 0
        self.if_lose = ""
        self.img_bg = pygame.image.load("assets/img/bg-tron.jpg")
        self.font = pygame.font.SysFont(None, 48)
        self.fontsys = pygame.font.SysFont(None, 25)

        self.player1 = Player([275, 600], K_UP, (255, 255, 255), self.players_speed1, (0, 0, 255))
        self.player2 = Player([275, 100], K_DOWN, (255, 255, 255), self.players_speed2, (255, 255, 0))

    def onGridRandom(self):
        x = random.randint(0, 54)
        y = random.randint(0, 69)
        pos = (x * 5, y * 5)

        while pos in self.player1.trail or pos in self.player2.trail:
            x = random.randint(0, 54)
            y = random.randint(0, 69)
            pos = (x * 5, y * 5)

        return pos

    def reset_game(self):
        self.player1 = Player([275, 600], K_UP, (255, 255, 255), self.players_speed1, (0, 0, 255))
        self.player2 = Player([275, 100], K_DOWN, (255, 255, 255), self.players_speed2, (255, 255, 0))
        self.if_lose = ""

    def lose(self):
        self.sound_die.play()
        time.sleep(1.5)
        self.screen.fill((0, 0, 0))

        if self.if_lose != "tie":
            lose_text = self.font.render("YOU LOSE!", True, (255, 0, 0))
            text_rect = lose_text.get_rect(center=(275, 200))
            self.screen.blit(lose_text, text_rect)

            if self.if_lose == "YELLOW":
                self.points_player1 += 1
                lose_text = self.font.render(self.if_lose, True, (255, 255, 0))
                text_rect = lose_text.get_rect(center=(275, 240))
                self.screen.blit(lose_text, text_rect)
            elif self.if_lose == "BLUE":
                self.points_player2 += 1
                lose_text = self.font.render(self.if_lose, True, (0, 0, 255))
                text_rect = lose_text.get_rect(center=(275, 240))
                self.screen.blit(lose_text, text_rect)
        elif self.if_lose == "tie":
            lose_text = self.font.render("A TIE", True, (255, 0, 255))
            text_rect = lose_text.get_rect(center=(275, 200))
            self.screen.blit(lose_text, text_rect)

        self.game_over = True
        button_text = self.font.render("Press SPACE", True, (255, 255, 225))
        button_rect = button_text.get_rect(center=(275, 375))
        self.screen.blit(button_text, button_rect)

        points_text = self.fontsys.render(f"Blue: {self.points_player1} | Yellow: {self.points_player2}", True,
                                          (255, 255, 255))
        points_rect = points_text.get_rect(center=(282, 450))
        self.screen.blit(points_text, points_rect)

        pygame.display.update()

        while self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.game_over = False
                        self.reset_game()

    def run(self):
        self.sound_start.play()
        time.sleep(1)
        self.sound_bg.play(-1)

        while not self.game_over:
            self.clock.tick(self.clock_tick)
            self.cont += 1
            if self.cont == self.clock_tick:
                self.sec += 1
                self.cont = 0

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[K_UP] and self.player1.direction != K_DOWN:
                self.player1.direction = K_UP
            elif keys[K_DOWN] and self.player1.direction != K_UP:
                self.player1.direction = K_DOWN
            elif keys[K_LEFT] and self.player1.direction != K_RIGHT:
                self.player1.direction = K_LEFT
            elif keys[K_RIGHT] and self.player1.direction != K_LEFT:
                self.player1.direction = K_RIGHT

            if keys[K_w] and self.player2.direction != K_DOWN:
                self.player2.direction = K_UP
            elif keys[K_s] and self.player2.direction != K_UP:
                self.player2.direction = K_DOWN
            elif keys[K_a] and self.player2.direction != K_RIGHT:
                self.player2.direction = K_LEFT
            elif keys[K_d] and self.player2.direction != K_LEFT:
                self.player2.direction = K_RIGHT

            self.player1.move()
            self.player2.move()

            if self.player1.pos[0] < 0 or self.player1.pos[0] >= self.screen.get_width() or \
               self.player1.pos[1] < 0 or self.player1.pos[1] >= self.screen.get_height():
                self.if_lose = "BLUE"
                self.lose()

            if self.player2.pos[0] < 0 or self.player2.pos[0] >= self.screen.get_width() or \
               self.player2.pos[1] < 0 or self.player2.pos[1] >= self.screen.get_height():
                self.if_lose = "YELLOW"
                self.lose()

            if self.player1.pos in self.player1.trail[1:] or self.player1.pos in self.player2.trail:
                self.if_lose = "BLUE"
                self.lose()

            if self.player2.pos in self.player1.trail or self.player2.pos in self.player2.trail[1:]:
                self.if_lose = "YELLOW"
                self.lose()

            if self.player1.pos == self.player2.pos:
                self.if_lose = "tie"
                self.lose()

            self.player1.trail.append(self.player1.pos[:])
            self.player2.trail.append(self.player2.pos[:])

            self.screen.blit(self.img_bg, (0, 0))

            for pos in self.player1.trail:
                pygame.draw.rect(self.screen, self.player1.trail_color, (pos[0], pos[1], 5, 5))

            for pos in self.player2.trail:
                pygame.draw.rect(self.screen, self.player2.trail_color, (pos[0], pos[1], 5, 5))

            if self.sec == 8:
                self.powerUp_freezing_pos = self.onGridRandom()
                self.sec = 0

            if self.player1.pos == self.powerUp_freezing_pos:
                self.powerUp_freezing_pos = (-10, -10)

            pygame.draw.rect(self.screen, self.player1.color, (*self.player1.pos, 5, 5))
            pygame.draw.rect(self.screen, self.player2.color, (*self.player2.pos, 5, 5))

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
