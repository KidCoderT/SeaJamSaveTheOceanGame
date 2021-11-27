import math
import random

import pygame.draw

from constants import *

class WhirlPool:
    def __init__(self):
        self.image = scale_image(whirl_pool_image, random.uniform(1.0, 1.6))
        self.velocity = random.uniform(300, 400)
        self.x = random.uniform(100, SCREEN_WIDTH - 100)
        self.y = 0 - self.image.get_height() - 10
        self.node_pos = [random.uniform(100, SCREEN_WIDTH - 100), SCREEN_HEIGHT + self.image.get_height() + 10]
        self.created_time = pygame.time.get_ticks()
        self.x_distance, self.y_distance = (self.node_pos[0] - self.x, self.node_pos[1] - self.y)
        self.angle = 0
        self.mask = pygame.mask.from_surface(self.image)

    def warn(self, screen, font):
        # pygame.draw.line(screen, (1, 61, 141), (self.x, self.y), (self.node_pos[0], self.node_pos[1]), 7)
        text = font.render("WHIRLPOOL ALERT!!!!", "", pygame.Color(255, 0, 0))
        screen.blit(text, ((SCREEN_WIDTH / 2) - (text.get_width() / 2), SCREEN_HEIGHT - 100))

    def should_warn(self):
        now = pygame.time.get_ticks()
        if now - self.created_time < 2000:
            return True
        return False

    def draw(self, screen):
        true_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(true_image, (self.x - true_image.get_width() / 2, self.y - true_image.get_height() / 2))

    def update(self):
        self.x += self.x_distance / self.velocity
        self.y += self.y_distance / self.velocity
        self.angle += 5
        self.mask = pygame.mask.from_surface(self.image)

class DeadlyAcidicGoo:
    def __init__(self):
        self.image = scale_image(random.choice(goo_image_list), random.uniform(1.0, 1.5))
        self.x = random.choice([-10 - self.image.get_width(), (SCREEN_WIDTH*1.1) + 10 + self.image.get_width()])
        self.y = random.randint(50, int(SCREEN_HEIGHT) - 50)
        self.mask = pygame.mask.from_surface(scale_image(self.image, 0.4))
        self.velocity = random.uniform(-2, -6) if self.x > 0 else random.uniform(2, 6)

    def update(self):
        self.x += self.velocity
        self.mask = pygame.mask.from_surface(scale_image(self.image, 0.7))
