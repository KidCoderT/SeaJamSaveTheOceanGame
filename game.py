import random
import sys

from constants import *
from charecters.boat import Boat
from charecters.trash import Trash
from charecters.coin_anim import CoinGotAnimation
from charecters.enemies import WhirlPool, DeadlyAcidicGoo
from ocean import Ocean

def run_game(screen):
    game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    ocean = Ocean(ocean_color_1, ocean_color_2, 5)
    boat = Boat(3, 3)
    clock = pygame.time.Clock()
    trashes_list = [Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash(), Trash()]
    goops_list = []
    coin_anim_sprites = []
    coins = 0
    trashes_collected = 0
    whirlpool = None
    screen_offset = [0, 0]
    last_time_taken_to_increase_trash_amount = pygame.time.get_ticks()
    wait_time_to_increase_trash_amount = 5000
    last_time_taken_to_create_whirlpool = pygame.time.get_ticks()
    whirl_pool_spawn_time = 10000
    paused = False
    shop_opened = False
    lives = 3
    death_done_wait_time = 0
    death_subtitle = ""
    died_by_goop = False
    last_time_to_update_whirlpool_pull_power_on_player = pygame.time.get_ticks()
    wait_time_to_update_whirlpool_pull_power_on_player = 20000
    mouse_clicked = False
    shop_msg = []
    new_goop_creation_wait_time = random.randint(2, 5) * 1000
    new_goop_creation_last_time_counted = pygame.time.get_ticks()

    border_mask = pygame.mask.from_surface(
        pygame.transform.scale(pygame.image.load("assets/border.png"), (SCREEN_WIDTH + 16, SCREEN_HEIGHT + 30)))

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_k:
                    shop_opened = not shop_opened
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_clicked = False

        if not paused and not shop_opened:
            ocean.draw_and_update(game_surface)

            if whirlpool is not None and not whirlpool.should_warn():
                whirlpool.draw(game_surface)

                if not boat.died:

                    converted_boat_image = pygame.transform.rotate(boat.img, boat.angle).convert_alpha()
                    whirlpool_image = scale_image(whirlpool.image.copy(), 0.25).convert_alpha()

                    whirlpool_mask = pygame.mask.from_surface(whirlpool_image)
                    whirlpool_rect = whirlpool_image.get_rect(center=(whirlpool.x, whirlpool.y))
                    boat_rect = converted_boat_image.get_rect(center=(boat.x, boat.y))

                    offset = (whirlpool_rect.x - boat_rect.x), (whirlpool_rect.y - boat_rect.y)

                    if whirlpool_mask.overlap(whirlpool_mask, offset):
                        lives -= 1
                        boat.img = None
                        boat.died = True
                        boat.death_time = pygame.time.get_ticks()
                        death_done_wait_time = 0
                        death_subtitle = "You got sucked into the whirlpool be careful they have a very strong " \
                                "pull force. "
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
                boat.draw_particles(game_surface)

            if pygame.time.get_ticks() - last_time_taken_to_increase_trash_amount > wait_time_to_increase_trash_amount:
                last_time_taken_to_increase_trash_amount = pygame.time.get_ticks()
                wait_time_to_increase_trash_amount += 2500
                trashes_list.append(Trash())

            if pygame.time.get_ticks() - last_time_to_update_whirlpool_pull_power_on_player > wait_time_to_update_whirlpool_pull_power_on_player:
                last_time_to_update_whirlpool_pull_power_on_player = pygame.time.get_ticks()
                wait_time_to_update_whirlpool_pull_power_on_player -= 100
                boat.whirlpool_pull_force_dividend += 0.009
            
            for goop in goops_list:
                game_surface.blit(goop.image, (goop.x - goop.image.get_width() / 2, goop.y - goop.image.get_height() / 2))

                if not boat.died:
                    if boat.collide(goop.mask, goop.x, goop.y) is not None or died_by_goop:
                        died_by_goop = True
                        if death_done_wait_time == 0:
                            boat.img = broken_boat_image
                            boat.broken = True
                            death_done_wait_time = pygame.time.get_ticks()
                        else:
                            if pygame.time.get_ticks() - death_done_wait_time >= 800:
                                lives -= 1
                                boat.img = None
                                boat.died = True
                                boat.death_time = pygame.time.get_ticks()
                                death_done_wait_time = 0
                                death_subtitle = "You got Stuck in the acidic goop melting your boat. Be Carefull!"
                                died_by_goop = False

                if goop.x <= -30 - goop.image.get_width() or goop.x >= (SCREEN_WIDTH*1.1) + 30 + goop.image.get_width():
                    goops_list.remove(goop)
                else:
                    goop.update()

            for trash in trashes_list:
                trash.draw_and_update(game_surface)

                if trash.has_crossed_edge():
                    trashes_list.remove(trash)
                    trashes_list.append(Trash())

                if whirlpool is not None:
                    if whirlpool.mask.overlap(trash.mask, (int(whirlpool.x - trash.x), int(whirlpool.y - trash.y))):
                        trashes_list.remove(trash)
                        trashes_list.append(Trash())

                if not boat.died and boat.collide(trash.mask, trash.x, trash.y) and trashes_list.count(trash) != 0:
                    coins += trash.trash_points
                    trashes_collected += 1
                    coin_anim_sprites.append(CoinGotAnimation(trash.x, trash.y, trash.trash_points))
                    trashes_list.remove(trash)
                    trashes_list.append(Trash())

            if whirlpool is not None and whirlpool.should_warn():
                whirlpool.warn(game_surface, spicy_rice_warning_font)

            if not boat.died:
                boat.draw(game_surface)

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

                if not (-15 < boat.y < SCREEN_HEIGHT - 15):
                    if death_done_wait_time == 0:
                        boat.img = broken_boat_image
                        boat.broken = True
                        death_done_wait_time = pygame.time.get_ticks()
                    else:
                        if pygame.time.get_ticks() - death_done_wait_time >= 800:
                            lives -= 1
                            boat.img = None
                            boat.died = True
                            boat.death_time = pygame.time.get_ticks()
                            death_done_wait_time = 0
                            death_subtitle = "The whirlpool flung you off to the side and we lost connection to the " \
                                            "boat, be careful!!"

                elif boat.y > (SCREEN_HEIGHT - (boat.img.get_height()/3) * 2) or boat.y < (boat.img.get_height()/3) * -2:
                    if death_done_wait_time == 0:
                        boat.img = broken_boat_image
                        death_done_wait_time = pygame.time.get_ticks()
                    else:
                        if pygame.time.get_ticks() - death_done_wait_time >= 800:
                            lives -= 1
                            boat.img = None
                            boat.died = True
                            boat.death_time = pygame.time.get_ticks()
                            death_done_wait_time = 0
                            death_subtitle = "The whirlpool flung you off onto our border destroying the boat in the process, be careful!!"

            for coin in coin_anim_sprites:
                coin.draw(game_surface, spicy_rice_coin_font)
                coin.update()

                now = pygame.time.get_ticks()
                if now - coin.created_time >= 500:
                    coin_anim_sprites.remove(coin)

            if pygame.time.get_ticks() - last_time_taken_to_create_whirlpool > max(5000,
                                                                                whirl_pool_spawn_time) and trashes_collected > 10 and whirlpool is None and not boat.died:
                whirlpool = WhirlPool()
                last_time_taken_to_create_whirlpool = pygame.time.get_ticks()
            
            if pygame.time.get_ticks() - new_goop_creation_last_time_counted > new_goop_creation_wait_time and trashes_collected > 20:
                goops_list.append(DeadlyAcidicGoo())
                new_goop_creation_last_time_counted = pygame.time.get_ticks()
                new_goop_creation_wait_time = random.randint(2, 5) * 1000

            if lives == 0:
                running = False
                continue

            boat.update_particles(boat.died)

        screen.blit(pygame.transform.scale(game_surface, (SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1)), screen_offset)

        if boat.died:
            time_left = pygame.time.get_ticks() - boat.death_time
            death_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            death_screen.set_alpha(200)
            death_screen.fill((178, 0, 0))

            text_color = (240, 180, 180)

            death_text = spicy_rice_death_font.render("You Died! Wait Respawning!", False, text_color)
            death_screen.blit(death_text, (
                (SCREEN_WIDTH / 2) - (death_text.get_width() / 2),
                (SCREEN_HEIGHT / 2) - (death_text.get_height() / 2) - 10))

            death_subtitle_text = spicy_rice_death_subtitle_font.render(death_subtitle, False, text_color)
            death_screen.blit(death_subtitle_text, (
                (SCREEN_WIDTH / 2) - (death_subtitle_text.get_width() / 2),
                (SCREEN_HEIGHT / 2) + (death_subtitle_text.get_height() + 25)))

            screen.blit(pygame.transform.scale(death_screen, (SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1)), (0, 0))

            if time_left >= 2300 and whirlpool is None:
                boat.reset()
                boat.img = scale_image(boat_image, boat.scale_amount)
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
        
        if shop_opened:
            real_width = (SCREEN_WIDTH * 1.1)
            real_height = (SCREEN_HEIGHT * 1.1)
            items_y = ((real_height/2) - (shop_item_hitbox.get_height()/2)) + 90
            item_1x = (real_width/2) - shop_item_hitbox.get_width() - 125
            item_2x = (real_width/2) - (shop_item_hitbox.get_width()/2)
            item_3x = (real_width/2) + 125
            screen.blit(shop_background, ((real_width/2) - (shop_background.get_width()/2), (real_height/2) - (shop_background.get_height()/2)))
            
            mouse_pos = pygame.mouse.get_pos()

            # Speed item
            if ((item_1x <= mouse_pos[0] <= item_1x + shop_item_hitbox.get_width()) and (items_y <= mouse_pos[1] <= items_y + shop_item_hitbox.get_height())):
                screen.blit(scale_image(shop_item_hitbox, 1.02), (item_1x-2.5, items_y-2))
                screen.blit(shop_speed_item[boat.speed_level()-1][0], (item_1x, items_y))

                if mouse_clicked and boat.speed_level() < 5:
                    if shop_speed_item[boat.speed_level()-1][1] <= coins:
                        coins -= shop_speed_item[boat.speed_level()-1][1]
                        boat.max_vel += 0.5
                    else:
                        shop_msg.append([spicy_rice_warning_font.render("Not enough coins", "", pygame.Color(255, 0, 0)), pygame.time.get_ticks()])
                    mouse_clicked = False
            else:
                screen.blit(shop_speed_item[boat.speed_level()-1][0], (item_1x, items_y))
            
            # Rotation item
            if ((item_2x <= mouse_pos[0] <= item_2x + shop_item_hitbox.get_width()) and (items_y <= mouse_pos[1] <= items_y + shop_item_hitbox.get_height())):
                screen.blit(scale_image(shop_item_hitbox, 1.02), (item_2x-2, items_y-2))
                screen.blit(shop_rotation_item[boat.rotation_level()-1][0], (item_2x, items_y))

                if mouse_clicked and boat.rotation_level() < 5:
                    if shop_rotation_item[boat.rotation_level()-1][1] <= coins:
                        coins -= shop_rotation_item[boat.rotation_level()-1][1]
                        boat.rotation_vel += 0.5
                    else:
                        shop_msg.append([spicy_rice_warning_font.render("Not enough coins", "", pygame.Color(255, 0, 0)), pygame.time.get_ticks()])
                    mouse_clicked = False
            else:
                screen.blit(shop_rotation_item[boat.rotation_level()-1][0], (item_2x, items_y))

            # Size item
            if ((item_3x <= mouse_pos[0] <= item_3x + shop_item_hitbox.get_width()) and (items_y <= mouse_pos[1] <= items_y + shop_item_hitbox.get_height())):
                screen.blit(scale_image(shop_item_hitbox, 1.02), (item_3x-2.5, items_y-2))
                screen.blit(shop_size_item[boat.scale_level()-1][0], (item_3x, items_y))

                if mouse_clicked and boat.scale_level() < 5:
                    if shop_rotation_item[boat.scale_level()-1][1] <= coins:
                        coins -= shop_rotation_item[boat.scale_level()-1][1]
                        boat.scale_amount = round(boat.scale_amount + 0.025, 3)
                        boat.img = scale_image(boat_image, boat.scale_amount)
                    else:
                        shop_msg.append([spicy_rice_warning_font.render("Not enough coins", "", pygame.Color(255, 0, 0)), pygame.time.get_ticks()])
                    mouse_clicked = False
            else:
                screen.blit(shop_size_item[boat.scale_level()-1][0], (item_3x, items_y))

        screen.blit(score_background_image, (-2, -3))
        score_text = spicy_rice_font.render(str(coins), "", pygame.Color(255, 255, 255))
        screen.blit(score_text, (110 - ((score_text.get_width() / 2) + 15), 10))
        trashes_collected_text = spicy_rice_font.render(str(trashes_collected), "", pygame.Color(255, 255, 255))
        screen.blit(trashes_collected_text, (110 - ((trashes_collected_text.get_width() / 2) + 15), 75))

        lives_image_index = 3 - lives

        screen.blit(lives_background_image, (((SCREEN_WIDTH * 1.1) - lives_background_image.get_width()) + 10, -2))
        screen.blit(lives_left_image[lives_image_index],
                    (((SCREEN_WIDTH * 1.1) - lives_left_image[lives_image_index].get_width()) - 5, 3))
        
        for msg in shop_msg:
            if pygame.time.get_ticks() - msg[1] > 800:
                shop_msg.remove(msg)
            else:
                screen.blit(msg[0], ((SCREEN_WIDTH*1.1)/2 - (msg[0].get_width()/2) - random.randint(-10, 10), (SCREEN_HEIGHT*1.1)/2 - (msg[0].get_height()/2)  - random.randint(-10, 10)))

        info_text = spicy_rice_info_font.render("press P to pause/unpause", "", pygame.Color(255, 255, 255))
        screen.blit(info_text, (10, (SCREEN_HEIGHT * 1.1) - 10 - info_text.get_height()))

        info_text = spicy_rice_info_font.render("press K to open/close the store", "", pygame.Color(255, 255, 255))
        screen.blit(info_text, ((SCREEN_WIDTH * 1.1) - 5 - info_text.get_width(), (SCREEN_HEIGHT * 1.1) - 5 - info_text.get_height()))

        pygame.display.update()
    
    return trashes_collected
