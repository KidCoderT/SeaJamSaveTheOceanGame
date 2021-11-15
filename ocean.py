import pygame
from constants import *


class Ocean:
    def __init__(self, color_1, color_2, repeat_count):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color = self.color_1
        self.lerp_backwards = False
        self.lerp_amount_list = []
        self.lerp_index = 0
        self.setup_lerp_list(repeat_count)

    def setup_lerp_list(self, repeat_count):
        for number in range(10):
            for i in range(repeat_count):
                self.lerp_amount_list.append((number + 1) / 10)

    def draw_and_update(self, screen):
        self.color = self.color_1.lerp(
            self.color_2, self.lerp_amount_list[self.lerp_index])
        screen.fill(self.color)

        if self.lerp_index == len(self.lerp_amount_list) - 1:
            self.lerp_backwards = True
        elif self.lerp_index == 0:
            self.lerp_backwards = False

        if not self.lerp_backwards:
            self.lerp_index += 1
        else:
            self.lerp_index -= 1

