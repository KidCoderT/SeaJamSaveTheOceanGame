import math
import random

import pygame.draw

from constants import *


class WhirlPool:
    def __init__(self):
        self.velocity = 95
        self.image = whirl_pool_image
        self.x = random.randint(100, SCREEN_WIDTH - 100)
        self.y = 0 - self.image.get_height() - 10
        self.node_pos = [random.randint(100, SCREEN_WIDTH - 100), SCREEN_HEIGHT + self.image.get_height() + 10]
        self.created_time = pygame.time.get_ticks()
        self.x_distance, self.y_distance = (self.node_pos[0]-self.x, self.node_pos[1]-self.y)
        self.angle = 0

    def warn(self, screen, font):
        # pygame.draw.line(screen, (1, 61, 141), (self.x, self.y), (self.node_pos[0], self.node_pos[1]), 7)
        text = font.render("WHIRLPOOLS ALERT!!!!", "", pygame.Color(255, 0, 0))
        screen.blit(text, ((SCREEN_WIDTH / 2) - (text.get_width() / 2), SCREEN_HEIGHT - 100))

    def should_warn(self):
        now = pygame.time.get_ticks()
        if now - self.created_time < 2000:
            return True
        return False

    def draw(self, screen):
        true_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(true_image, (self.x - true_image.get_width()/2, self.y - true_image.get_height()/2))

    def update(self):
        self.x += self.x_distance / self.velocity
        self.y += self.y_distance / self.velocity
        self.angle += 5
