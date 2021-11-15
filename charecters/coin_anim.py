import pygame

from constants import *


class CoinGotAnimation:
    def __init__(self, x, y, points_to_be_earned):
        self.x = x
        self.y = y
        self.points_to_be_earned = points_to_be_earned
        self.image = got_coin_anim_image
        self.velocity = 1
        self.created_time = pygame.time.get_ticks()

    def draw(self, screen, font):
        screen.blit(self.image, (self.x, self.y))
        score_text = font.render(str(self.points_to_be_earned), "", (255, 255, 255))
        screen.blit(score_text, (self.x + 40, self.y))

    def update(self):
        self.y -= self.velocity
