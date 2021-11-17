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
pygame.display.set_icon(pygame.image.load("assets/icon.ico"))
screen_width, screen_height = (SCREEN_WIDTH, SCREEN_HEIGHT)
game_display = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
shop_display = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

ocean = Ocean(ocean_color_1, ocean_color_2, 5)
boat = Boat(3, 3)
clock = pygame.time.Clock()
trashes = [Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash()]
coin_anim_sprites = []
score = 25
whirlpool = None
screen_offset = [0, 0]
last_time_taken_to_increase_trash_amount = pygame.time.get_ticks()
wait_time_to_increase_trash_amount = 5000
last_time_taken_to_create_whirlpool = pygame.time.get_ticks()
whirl_pool_spawn_time = 10000
paused = False
lives = 3

border_mask = pygame.mask.from_surface(
    pygame.transform.scale(pygame.image.load("assets/border.png"), (SCREEN_WIDTH + 16, SCREEN_HEIGHT + 30)))

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

    if not paused:
        ocean.draw_and_update(game_display)

        if whirlpool is not None and not whirlpool.should_warn():
            whirlpool.draw(game_display)

            shrunk_whirlpool_mask = pygame.mask.from_surface(scale_image(whirlpool.image, 0.25))

            if not boat.died:
                if boat.mask.overlap(shrunk_whirlpool_mask, (int(whirlpool.x - boat.x), int(whirlpool.y - boat.y))):
                    lives -= 1
                    boat.img = None
                    boat.died = True
                    boat.death_time = pygame.time.get_ticks()
                else:
                    boat.move_to_whirlpool(whirlpool.x, whirlpool.y)

            if whirlpool.y >= SCREEN_HEIGHT + whirl_pool_image.get_height() + 10:
                whirlpool = None
                last_time_taken_to_create_whirlpool = pygame.time.get_ticks()
                whirl_pool_spawn_time -= 100
            else:
                whirlpool.update()

        if whirlpool is None:
            screen_offset[0] = 0
            screen_offset[1] = 0
        else:
            screen_offset[0] = random.randint(0, 8) - 4
            screen_offset[1] = random.randint(0, 8) - 4

        if not boat.died and boat.img is not None:
            boat.draw_particles(game_display)

        if pygame.time.get_ticks() - last_time_taken_to_increase_trash_amount > wait_time_to_increase_trash_amount:
            last_time_taken_to_increase_trash_amount = pygame.time.get_ticks()
            wait_time_to_increase_trash_amount += 2500
            trashes.append(Trash())

        for trash in trashes:
            trash.draw_and_update(game_display)

            if trash.has_crossed_edge():
                trashes.remove(trash)
                trashes.append(Trash())

            if whirlpool is not None:
                if whirlpool.mask.overlap(trash.mask, (int(whirlpool.x - trash.x), int(whirlpool.y - trash.y))):
                    trashes.remove(trash)
                    trashes.append(Trash())

            if not boat.died and boat.collide(trash.mask, trash.x, trash.y) and trashes.count(trash) != 0:
                score += trash.trash_points
                coin_anim_sprites.append(CoinGotAnimation(trash.x, trash.y, trash.trash_points))
                trashes.remove(trash)
                trashes.append(Trash())

        if whirlpool is not None and whirlpool.should_warn():
            whirlpool.warn(game_display, spicy_rice_warning_font)

        if not boat.died:
            boat.draw(game_display)

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

            if boat.collide(border_mask) is not None:
                boat.bounce()

        for coin in coin_anim_sprites:
            coin.draw(game_display, spicy_rice_coin_font)
            coin.update()

            now = pygame.time.get_ticks()
            if now - coin.created_time >= 500:
                coin_anim_sprites.remove(coin)

        if pygame.time.get_ticks() - last_time_taken_to_create_whirlpool > max(5000,
                                                                               whirl_pool_spawn_time) and score > 25 and whirlpool is None and not boat.died:
            whirlpool = WhirlPool()
            last_time_taken_to_create_whirlpool = pygame.time.get_ticks()

        if lives == 0:
            running = False
            continue

        boat.update_particles(boat.died)

    screen.blit(pygame.transform.scale(game_display, (SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1)), screen_offset)

    if boat.died:
        time_left = pygame.time.get_ticks() - boat.death_time
        death_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        death_screen.set_alpha(200)
        death_screen.fill((178, 0, 0))

        death_text = spicy_rice_death_font.render("You Died!", False, (255, 0, 0))
        death_screen.blit(death_text, (
            (SCREEN_WIDTH / 2) - (death_text.get_width() / 2),
            (SCREEN_HEIGHT / 2) - (death_text.get_height() / 2) - 70))

        respawn_time_in_amount = (pygame.time.get_ticks() - boat.death_time) // 1000

        respawn_time_text = spicy_rice_death_font.render(f"Respawning!", False, (255, 0, 0))
        death_screen.blit(respawn_time_text, (
            (SCREEN_WIDTH / 2) - (respawn_time_text.get_width() / 2),
            (SCREEN_HEIGHT / 2) - (respawn_time_text.get_height() / 2) + 70))

        screen.blit(pygame.transform.scale(death_screen, (SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1)), (0, 0))

        if time_left >= 5000 and whirlpool is None:
            boat.reset()
            boat.img = boat.IMG
            boat.died = False
            last_time_taken_to_create_whirlpool = pygame.time.get_ticks()

    if paused:
        transparent_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        transparent_surface.set_alpha(128)
        transparent_surface.fill((255, 255, 255))
        screen.blit(pygame.transform.scale(transparent_surface, (SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1)), (0, 0))
        screen.blit(pause_image, (
            (SCREEN_WIDTH * 1.1) / 2 - pause_image.get_width() / 2,
            (SCREEN_HEIGHT * 1.1) / 2 - pause_image.get_height() / 2))

    screen.blit(score_background_image, (-2, -2))
    score_text = spicy_rice_font.render(str(score), "", pygame.Color(255, 255, 255))
    screen.blit(score_text, (110 - ((score_text.get_width() / 2) + 15), 15))

    lives_image_index = 3 - lives

    screen.blit(lives_background_image, (SCREEN_WIDTH + 2, -2))
    screen.blit(lives_left_image[lives_image_index],
                (SCREEN_WIDTH + 10, 5))

    pygame.display.update()

pygame.quit()
sys.exit()
