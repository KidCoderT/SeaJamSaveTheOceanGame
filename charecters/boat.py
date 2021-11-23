import math
import random

import pygame.math

from constants import *


class Boat:

    def __init__(self, max_vel, rotation_vel):
        self.vel = 0
        self.angle = 0
        self.acceleration = 0.1
        self.particles = []
        self.died = False
        self.death_time = None
        self.whirlpool_pull_force_dividend = 0.03
        self.scale_amount = 0.15
        self.img = scale_image(boat_image, self.scale_amount)
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.x, self.y = ((SCREEN_WIDTH / 2) - (self.img.get_width() / 2), (SCREEN_HEIGHT / 2) - (self.img.get_height() / 2))

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
        self.img = scale_image(boat_image, self.scale_amount)
        self.x, self.y = ((SCREEN_WIDTH / 2) - (self.img.get_width() / 2), (SCREEN_HEIGHT / 2) - (self.img.get_height() / 2))
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

    def update_particles(self, boat_dead):
        if self.vel > 0.5 and not boat_dead:
            self.particles.append(
                [[self.x + (self.img.get_width() / 2), self.y + (self.img.get_height() / 2)],
                 [random.randint(0, 20) / 10 - 1, -2],
                 random.randint(int(self.vel) * 3, int(self.vel + 2) * 3) * 0.9])

    def move_to_whirlpool(self, whirlpool_cx, whirlpool_cy):
        force_x = float(whirlpool_cx - self.x) / 5
        force_y = float(whirlpool_cy - self.y) / 5

        self.x += (force_x) * self.whirlpool_pull_force_dividend
        self.y += (force_y) * self.whirlpool_pull_force_dividend
    
    def speed_level(self):
        return 1 if (self.max_vel == 3.0) else 2 if (self.max_vel == 3.5) else 3 if (self.max_vel == 4.0) else 4 if (self.max_vel == 4.5) else 5
    
    def rotation_level(self):
        return 1 if (self.rotation_vel == 3.0) else 2 if (self.rotation_vel == 3.5) else 3 if (self.rotation_vel == 4.0) else 4 if (self.rotation_vel == 4.5) else 5

    def scale_level(self):
        return 1 if (self.scale_amount == 0.15) else 2 if (self.scale_amount == 0.175) else 3 if (self.scale_amount == 0.2) else 4 if (self.scale_amount == 0.225) else 5
