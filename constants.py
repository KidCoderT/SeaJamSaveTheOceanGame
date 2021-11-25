import pygame.image

from utils import *

SCREEN_WIDTH = pygame.display.Info().current_w * 0.8
SCREEN_HEIGHT = pygame.display.Info().current_h * 0.8

ocean_color_1 = pygame.Color(11, 134, 210)
ocean_color_2 = pygame.Color(21, 151, 229)

boat_image = pygame.image.load("assets/boat.png")
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

shop_background = scale_image(pygame.image.load("assets/shop_bg.png"), 0.18)
shop_item_hitbox = scale_image(pygame.image.load("assets/image.png"), 0.18)
shop_speed_item = [
    [scale_image(pygame.image.load("assets/boat_speed/Lv1.png"), 0.18), 50],
    [scale_image(pygame.image.load("assets/boat_speed/Lv2.png"), 0.18), 120],
    [scale_image(pygame.image.load("assets/boat_speed/Lv3.png"), 0.18), 200],
    [scale_image(pygame.image.load("assets/boat_speed/Lv4.png"), 0.18), 250],
    [scale_image(pygame.image.load("assets/boat_speed/Lv5.png"), 0.18), 0]
]
shop_rotation_item = [
    [scale_image(pygame.image.load("assets/boat_rotation/Lv1.png"), 0.18), 20],
    [scale_image(pygame.image.load("assets/boat_rotation/Lv2.png"), 0.18), 50],
    [scale_image(pygame.image.load("assets/boat_rotation/Lv3.png"), 0.18), 120],
    [scale_image(pygame.image.load("assets/boat_rotation/Lv4.png"), 0.18), 200],
    [scale_image(pygame.image.load("assets/boat_rotation/Lv5.png"), 0.18), 0]
]
shop_size_item = [
    [scale_image(pygame.image.load("assets/boat_size/Lv1.png"), 0.18), 120],
    [scale_image(pygame.image.load("assets/boat_size/Lv2.png"), 0.18), 200],
    [scale_image(pygame.image.load("assets/boat_size/Lv3.png"), 0.18), 250],
    [scale_image(pygame.image.load("assets/boat_size/Lv4.png"), 0.18), 300],
    [scale_image(pygame.image.load("assets/boat_size/Lv5.png"), 0.18), 0]
]

spicy_rice_font = pygame.font.Font("fonts/SpicyRiceFont/SpicyRice-Regular.ttf", 32)
spicy_rice_coin_font = pygame.font.Font("fonts/SpicyRiceFont/SpicyRice-Regular.ttf", 24)
spicy_rice_warning_font = pygame.font.Font("fonts/SpicyRiceFont/SpicyRice-Regular.ttf", 64)
spicy_rice_info_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 15)
spicy_rice_death_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 80)
spicy_rice_death_subtitle_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 20)
death_screen_title_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 80)
death_screen_subtitle_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 20)
death_screen_button_font = pygame.font.Font("fonts/BungeeFont/Bungee-Regular.ttf", 24)
death_screen_button_on_hover_font = pygame.font.Font("fonts/BungeeFont/Bungee-Regular.ttf", 30)
death_screen_info_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 15)

pause_image = pygame.image.load("assets/pause.png")

lives_left_image = [
    scale_image(pygame.image.load("assets/3 life.png"), 0.1),
    scale_image(pygame.image.load("assets/2 life.png"), 0.1),
    scale_image(pygame.image.load("assets/1 life.png"), 0.1)
]
lives_background_image = scale_image(pygame.image.load("assets/lives bg.png"), 0.4)

# sara = scale_image(pygame.image.load("assets/sara.png"), 2.5)

goo_image_list = [
    scale_image(pygame.image.load("assets/goo/Goo.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-1.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-2.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-3.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-4.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-5.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-6.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-7.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-8.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-9.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-10.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-11.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-12.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-13.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-14.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-15.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-16.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-17.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-18.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-19.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-20.png"), 0.17),
    scale_image(pygame.image.load("assets/goo/Goo-21.png"), 0.17)
]
