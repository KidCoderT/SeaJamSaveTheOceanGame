import pygame.image
from pygame.transform import scale

from utils import *

SCREEN_WIDTH = pygame.display.Info().current_w * 0.8
SCREEN_HEIGHT = pygame.display.Info().current_h * 0.8

ocean_color_1 = pygame.Color(11, 134, 210)
ocean_color_2 = pygame.Color(21, 151, 229)

game_name = "SAVE THE OCEAN!"

boat_image = pygame.image.load("assets/boat.png")
trash_images = [
    scale_image(pygame.image.load("assets/trashes/trash1.png"), 0.08),  # 0
    scale_image(pygame.image.load("assets/trashes/trash2.png"), 0.08),  # 1
    scale_image(pygame.image.load("assets/trashes/trash3.png"), 0.08),  # 2
    scale_image(pygame.image.load("assets/trashes/trash4.png"), 0.08),  # 3
    scale_image(pygame.image.load("assets/trashes/trash5.png"), 0.08),  # 4
    scale_image(pygame.image.load("assets/trashes/trash6.png"), 0.08),  # 5
    scale_image(pygame.image.load("assets/trashes/trash7.png"), 0.08),  # 6
    scale_image(pygame.image.load("assets/trashes/trash8.png"), 0.08),  # 7
    scale_image(pygame.image.load("assets/trashes/trash9.png"), 0.08),  # 8
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
warning_font = pygame.font.Font("fonts/BungeeFont/Bungee-Regular.ttf", 64)
info_font = pygame.font.Font("fonts/BungeeFont/Bungee-Regular.ttf", 15)
spicy_rice_death_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 80)
spicy_rice_death_subtitle_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 20)
death_screen_title_font = pygame.font.Font("fonts/BungeeFont/Bungee-Regular.ttf", 80)
death_screen_subtitle_font = pygame.font.Font("fonts/BungeeFont/Bungee-Regular.ttf", 20)
death_screen_button_font = pygame.font.Font("fonts/BungeeFont/Bungee-Regular.ttf", 24)
death_screen_button_on_hover_font = pygame.font.Font("fonts/BungeeFont/Bungee-Regular.ttf", 30)
death_screen_info_font = pygame.font.Font("fonts/FingerPaintFont/FingerPaint-Regular.ttf", 15)

pause_image = pygame.image.load("assets/pause.png")

lives_left_image = [
    scale_image(pygame.image.load("assets/lives/3 life.png"), 0.1),
    scale_image(pygame.image.load("assets/lives/2 life.png"), 0.1),
    scale_image(pygame.image.load("assets/lives/1 life.png"), 0.1)
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

pause_btn = [
    scale_image(pygame.image.load("assets/pause_btn.png"), 0.35),
    scale_image(pygame.image.load("assets/pause_btn_hover.png"), 0.35)
]

shop_btn = [
    scale_image(pygame.image.load("assets/shop_btn.png"), 0.35),
    scale_image(pygame.image.load("assets/shop_btn_hover.png"), 0.35)
]

unpause_btn = [
    scale_image(pygame.image.load("assets/play_btn.png"), 0.35),
    scale_image(pygame.image.load("assets/play_btn_hover.png"), 0.35)
]

close_shop_btn = [
    scale_image(pygame.image.load("assets/close_shop_btn.png"), 0.35),
    scale_image(pygame.image.load("assets/close_shop_btn_hover.png"), 0.35)
]

shop_title_and_coins_banner = scale_image(pygame.image.load("assets/shop_title_and_coins.png"), 0.18)

death_sounds = [
    pygame.mixer.Sound("assets/sfx/Death.wav"),
    pygame.mixer.Sound("assets/sfx/Death2.wav"),
    pygame.mixer.Sound("assets/sfx/Death3.wav")
]

click_sounds = pygame.mixer.Sound("assets/sfx/click.wav")

pickup_sound = pygame.mixer.Sound("assets/sfx/Pickup.wav")
pickup_sound.set_volume(0.1)

whirlpool_sound = pygame.mixer.Sound("assets/sfx/whirlpool.wav")

not_enough_coins_sound = pygame.mixer.Sound("assets/sfx/not_enough_coins.wav")
not_enough_coins_sound.set_volume(0.2)

purchased_sound = pygame.mixer.Sound("assets/sfx/purchased.wav")
