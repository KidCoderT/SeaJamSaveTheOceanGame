import pygame.image

from utils import *

SCREEN_WIDTH = pygame.display.Info().current_w * 0.8
SCREEN_HEIGHT = pygame.display.Info().current_h * 0.8

ocean_color_1 = pygame.Color(11, 134, 210)
ocean_color_2 = pygame.Color(21, 151, 229)

boat_image = scale_image(pygame.image.load("assets/boat.png"), 0.15)
trash_images = [
    scale_image(pygame.image.load("assets/trash1.png"), 0.08),  # 0
    scale_image(pygame.image.load("assets/trash2.png"), 0.08),  # 1
    scale_image(pygame.image.load("assets/trash3.png"), 0.08),  # 2
    scale_image(pygame.image.load("assets/trash4.png"), 0.08),  # 3
    scale_image(pygame.image.load("assets/trash5.png"), 0.08),  # 4
    scale_image(pygame.image.load("assets/trash6.png"), 0.08),  # 5
    scale_image(pygame.image.load("assets/trash7.png"), 0.08),  # 6
    scale_image(pygame.image.load("assets/trash8.png"), 0.08),  # 7
    scale_image(pygame.image.load("assets/trash9.png"), 0.08),  # 8
]
score_background_image = scale_image(pygame.image.load("assets/score_bg.png"), 0.4)

got_coin_anim_image = scale_image(pygame.image.load("assets/got coin anim img.png"), 0.2)

whirl_pool_image = scale_image(pygame.image.load("assets/whirlpool.png"), 0.15)

broken_boat_image = scale_image(pygame.image.load("assets/broken boat.png"), 0.15)

shop_background = scale_image(pygame.image.load("assets/shop_bg.png"), 0.2)

spicy_rice_font = pygame.font.Font("fonts/SpicyRice-Regular.ttf", 32)
spicy_rice_coin_font = pygame.font.Font("fonts/SpicyRice-Regular.ttf", 24)
spicy_rice_warning_font = pygame.font.Font("fonts/SpicyRice-Regular.ttf", 64)
spicy_rice_death_font = pygame.font.Font("fonts/SpicyRice-Regular.ttf", 62)
spicy_rice_death_subtitle_font = pygame.font.Font("fonts/SpicyRice-Regular.ttf", 20)

pause_image = pygame.image.load("assets/pause indicator and button.png")

lives_left_image = [
    scale_image(pygame.image.load("assets/3 life.png"), 0.1),
    scale_image(pygame.image.load("assets/2 life.png"), 0.1),
    scale_image(pygame.image.load("assets/1 life.png"), 0.1)
]
lives_background_image = scale_image(pygame.image.load("assets/lives bg.png"), 0.4)

sara = scale_image(pygame.image.load("assets/sara.png"), 2.5)
