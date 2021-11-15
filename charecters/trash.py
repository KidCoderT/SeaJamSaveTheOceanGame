import random

from constants import *

trash_types = ["bottle", "tray", "barrel"]


class Trash:
    def __init__(self, wait_time=random.randint(1000, 3000)):
        self.is_start_left = True if random.randint(1, 2) == 1 else False
        self.is_start_right = True if not self.is_start_left else False
        self.x = -25 if self.is_start_left else SCREEN_WIDTH + 25
        self.y = random.randint(30, SCREEN_HEIGHT - 30)
        self.angle = 0
        self.left_angle = random.randint(315, 350)
        self.right_angle = random.randint(10, 45)
        self.change_angle_by = random.randint(-10, 10) / 10
        self.created_time = pygame.time.get_ticks()
        self.cool_down_time_done = False
        self.wait_time = wait_time
        choice = random.randint(1, 20)
        if choice < 13:
            self.trash_type = trash_types[0]
            self.trash_points = 1
            self.image = trash_images[0]
            self.velocity = random.randint(2, 5) if self.is_start_left else random.randint(-5, -2)
        elif 12 < choice < 18:
            self.trash_points = 2
            self.trash_type = trash_types[1]
            self.image = trash_images[1]
            self.velocity = random.randint(1, 4) if self.is_start_left else random.randint(-6, -3)
        else:
            self.trash_points = 3
            self.trash_type = trash_types[2]
            self.image = trash_images[2]
            self.velocity = random.randint(1, 3) if self.is_start_left else random.randint(-6, -1)

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

    def has_crossed_edge(self):
        if self.x < -25:
            return True
        elif self.x > SCREEN_WIDTH + 25:
            return True
        return False
