import math
import random

import pygame.math

from constants import *


class Boat:
    IMG = boat_image
    START_POS = ((SCREEN_WIDTH / 2) - (IMG.get_width() / 2), (SCREEN_HEIGHT / 2) - (IMG.get_height() / 2))

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
        self.particles = []

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_and_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        boat_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(boat_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel
        self.move()

    def draw_particles(self, screen):
        for particle in self.particles:
            particle[2] -= 0.5
            particle[1][1] += 0.1
            pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)

    def update_particles(self):
        if self.vel > 0.5:
            self.particles.append(
                [[self.x + (boat_image.get_width() / 2), self.y + (boat_image.get_height() / 2)],
                 [random.randint(0, 20) / 10 - 1, -2],
                 random.randint(int(self.vel) * 3, int(self.vel + 2) * 3) * 0.9])

    def move_to_whirlpool(self, whirlpool_cx, whirlpool_cy, area_of_whirlpool):

        force_x = float(whirlpool_cx - self.x) / 5
        force_y = float(whirlpool_cy - self.y) / 5

        self.x += (force_x - self.vel) * 0.05
        self.y += (force_y - self.vel) * 0.05
