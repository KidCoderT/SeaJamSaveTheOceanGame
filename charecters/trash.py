import random

from constants import *


class Trash:
    def __init__(self, wait_time=random.randint(1000, 3000)):
        self.is_start_left = True if random.randint(1, 2) == 1 else False
        self.is_start_right = True if not self.is_start_left else False
        self.x = -25 if self.is_start_left else SCREEN_WIDTH + 25
        self.y = random.uniform(30, SCREEN_HEIGHT - 30)
        self.angle = 0
        self.left_angle = random.randint(315, 350)
        self.right_angle = random.randint(10, 45)
        self.change_angle_by = random.randint(-10, 10) / 10
        self.created_time = pygame.time.get_ticks()
        self.cool_down_time_done = False
        self.wait_time = wait_time
        choice = random.randint(1, 50)
        if choice <= 30:
            self.trash_points = 1
            self.image = trash_images[random.randint(0, 2)]
            self.velocity = random.uniform(1.0, 3.0) if self.is_start_left else random.uniform(-3.0, -1.0)
        elif 30 < choice <= 40:
            self.trash_points = 2
            self.image = trash_images[random.randint(3, 4)]
            self.velocity = random.uniform(2.0, 4.0) if self.is_start_left else random.uniform(-4.0, -2.0)
        elif 40 < choice < 45:
            self.trash_points = 3
            self.image = trash_images[random.randint(5, 6)]
            self.velocity = random.uniform(2.5, 4.5) if self.is_start_left else random.uniform(-4.5, -2.5)
        else:
            self.trash_points = 4
            self.image = trash_images[random.randint(7, 8)]
            self.velocity = random.uniform(5.0, 7.0) if self.is_start_left else random.uniform(-7.0, -5.0)
        self.mask = pygame.mask.from_surface(pygame.transform.rotate(self.image, self.angle))

    def draw_and_update(self, screen):
        if not self.cool_down_time_done:
            now = pygame.time.get_ticks()
            if now - self.created_time >= self.wait_time:
                self.cool_down_time_done = True

        if self.cool_down_time_done:
            blit_and_rotate_center(screen, self.image, (self.x, self.y), self.angle)

            self.rotate()
            self.update()

    def rotate(self):
        self.angle += self.change_angle_by

    def update(self):
        if random.randint(1, 5) > 2:
            self.x += self.velocity
        else:
            self.x += self.velocity - 2
        self.mask = pygame.mask.from_surface(pygame.transform.rotate(self.image, self.angle))

    def has_crossed_edge(self):
        if self.x < -25:
            return True
        elif self.x > SCREEN_WIDTH + 25:
            return True
        return False
