import random
import sys
import pygame

pygame.init()

from constants import *
from charecters.boat import Boat
from charecters.trash import Trash
from charecters.coin_anim import CoinGotAnimation
from charecters.whirlpool import WhirlPool
from ocean import Ocean

screen = pygame.display.set_mode((SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1))
pygame.display.set_caption("Clean the Ocean")
screen_width, screen_height = (SCREEN_WIDTH, SCREEN_HEIGHT)
display = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

ocean = Ocean(ocean_color_1, ocean_color_2, 5)
boat = Boat(7, 3)
clock = pygame.time.Clock()
trashes = [Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash()]
coin_anim_sprites = []
score = 50
whirlpool = None
screen_offset = [0, 0]
last_time_taken_to_increase_trash_amount = pygame.time.get_ticks()
wait_time_to_increase_trash_amount = 5000
last_time_taken_to_create_whirlpool = pygame.time.get_ticks()

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ocean.draw_and_update(display)

    if whirlpool is not None and not whirlpool.should_warn():
        whirlpool.draw(display)

        for trash in trashes:
            trash_mask = pygame.mask.from_surface(pygame.transform.rotate(trash.image, trash.angle))
            whirlpool_mask = pygame.mask.from_surface(whirlpool.image)

            if whirlpool_mask.overlap(trash_mask, (int(whirlpool.x - trash.x), int(whirlpool.y - trash.y))):
                trashes.remove(trash)
                trashes.append(Trash())

        if whirlpool.y >= SCREEN_HEIGHT + whirl_pool_image.get_height() + 10:
            whirlpool = None
        else:
            whirlpool.update()

    if whirlpool is None:
        screen_offset[0] = 0
        screen_offset[1] = 0
    else:
        screen_offset[0] = random.randint(0, 8) - 4
        screen_offset[1] = random.randint(0, 8) - 4

    boat.draw_particles(display)

    if pygame.time.get_ticks() - last_time_taken_to_increase_trash_amount > wait_time_to_increase_trash_amount:
        last_time_taken_to_increase_trash_amount = pygame.time.get_ticks()
        wait_time_to_increase_trash_amount += 2500
        trashes.append(Trash())

    for trash in trashes:
        trash.draw_and_update(display)

        if trash.has_crossed_edge():
            trashes.remove(trash)
            trashes.append(Trash())

        trash_mask = pygame.mask.from_surface(pygame.transform.rotate(trash.image, trash.angle))

        if boat.collide(trash_mask, trash.x, trash.y):
            score += trash.trash_points
            coin_anim_sprites.append(CoinGotAnimation(trash.x, trash.y, trash.trash_points))
            trashes.remove(trash)
            trashes.append(Trash())

    if whirlpool is not None and whirlpool.should_warn():
        whirlpool.warn(display, spicy_rice_warning_font)

    boat.draw(display)

    for coin in coin_anim_sprites:
        coin.draw(display, spicy_rice_coin_font)
        coin.update()

        now = pygame.time.get_ticks()
        if now - coin.created_time >= 500:
            coin_anim_sprites.remove(coin)

    display.blit(score_background_image, (-2, -2))
    score_text = spicy_rice_font.render(str(score), "", pygame.Color(255, 255, 255))
    display.blit(score_text, (110 - ((score_text.get_width() / 2) + 15), 15))

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        boat.rotate(left=True)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        boat.rotate(right=True)

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        moved = True
        boat.move_forward()
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        moved = True
        boat.move_backward()

    if not moved:
        boat.reduce_speed()

    if pygame.time.get_ticks() - last_time_taken_to_create_whirlpool > 10000 and score > 50 and whirlpool is None:
        whirlpool = WhirlPool()
        last_time_taken_to_create_whirlpool = pygame.time.get_ticks()

    boat.update_particles()

    screen.blit(pygame.transform.scale(display, (SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1)), screen_offset)

    pygame.display.update()

pygame.quit()
sys.exit()
