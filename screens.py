import pygame, sys
from constants import *

def main_menu_screen(screen):
	run_game = True
	exited = False
	circle_radius = 0
	should_grow = True
	mouse_pressed = False
	while not exited:
		screen.fill((20, 125, 205))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exited = True
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pressed = True
			else:
				mouse_pressed = False
		
		boat = pygame.transform.rotate(scale_image(pygame.image.load("assets/boat.png"), 0.8), 330)
		boat_cx, boat_cy = ((SCREEN_WIDTH*1.1) - ((SCREEN_WIDTH*1.1)/4), (SCREEN_HEIGHT*1.1)/2)
		pygame.draw.circle(screen, ocean_color_1, (boat_cx, boat_cy), circle_radius + 100)
		pygame.draw.circle(screen, ocean_color_2, (boat_cx, boat_cy), circle_radius)
		if should_grow:
			circle_radius += 1
		else:
			circle_radius -= 1

		if circle_radius > 230:
			circle_radius = 230
			should_grow = False
		elif circle_radius < 100:
			circle_radius = 100
			should_grow = True

		screen.blit(boat, (boat_cx - boat.get_width()/2, boat_cy - boat.get_height()/2))

		game_title_text = death_screen_title_font.render(game_name, "", (255, 255, 255))
		screen.blit(game_title_text, (100, ((SCREEN_HEIGHT*1.1)/5) * 2.25 - game_title_text.get_height() - 10))

		mx, my = pygame.mouse.get_pos()

		mx, my = pygame.mouse.get_pos()

		# Continue Button
		continue_btn_x, continue_btn_y = (115, ((SCREEN_HEIGHT*1.1)/5) * 2.25)
		continue_button = pygame.Rect(continue_btn_x, continue_btn_y, 400, 50)
		if continue_button.collidepoint((mx, my)):
			pygame.draw.rect(screen, (255, 255, 255), (continue_btn_x - 2.5, continue_btn_y - 2.5, 405, 55))
			if mouse_pressed:
				exited = True
		pygame.draw.rect(screen, (0, 18, 35), continue_button)

		if continue_button.collidepoint((mx, my)):
			continue_button_text = death_screen_button_on_hover_font.render("PLAY!", "", (255, 255, 255))
			screen.blit(continue_button_text, ((continue_btn_x + 200) - (continue_button_text.get_width()/2), (continue_btn_y + 25) - (continue_button_text.get_height()/2)))
		else:
			continue_button_text = death_screen_button_font.render("PLAY!", "", (255, 255, 255))
			screen.blit(continue_button_text, ((continue_btn_x + 200) - (continue_button_text.get_width()/2), (continue_btn_y + 25) - (continue_button_text.get_height()/2)))

		# Exit Button
		exit_btn_x, exit_btn_y = (115, continue_btn_y + 50 + 10)
		exit_button = pygame.Rect(exit_btn_x, exit_btn_y, 400, 50)
		if exit_button.collidepoint((mx, my)):
			pygame.draw.rect(screen, (255, 255, 255), (exit_btn_x - 2.5, exit_btn_y - 2.5, 405, 55))
			if mouse_pressed:
				run_game = False
				exited = True
		pygame.draw.rect(screen, (0, 18, 35), exit_button)

		if exit_button.collidepoint((mx, my)):
			exit_button_text = death_screen_button_on_hover_font.render("EXIT!", "", (255, 255, 255))
			screen.blit(exit_button_text, ((exit_btn_x + 200) - (exit_button_text.get_width()/2), (exit_btn_y + 25) - (exit_button_text.get_height()/2)))
		else:
			exit_button_text = death_screen_button_font.render("EXIT!", "", (255, 255, 255))
			screen.blit(exit_button_text, ((exit_btn_x + 200) - (exit_button_text.get_width()/2), (exit_btn_y + 25) - (exit_button_text.get_height()/2)))
		
		pygame.display.update()
	
	return run_game

def death_screen(screen, trashes_collected):
	run_game = True
	exited = False
	circle_radius = 0
	should_grow = True
	mouse_pressed = False
	while not exited:
		screen.fill((250, 79, 76))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exited = True
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pressed = True
			else:
				mouse_pressed = False
		
		broken_boat = scale_image(pygame.image.load("assets/broken boat.png"), 0.8)
		boat_cx, boat_cy = ((SCREEN_WIDTH*1.1) - ((SCREEN_WIDTH*1.1)/4), (SCREEN_HEIGHT*1.1)/2)
		pygame.draw.circle(screen, (221, 66, 64), (boat_cx, boat_cy), circle_radius + 100)
		pygame.draw.circle(screen, (216, 52, 49), (boat_cx, boat_cy), circle_radius)
		if should_grow:
			circle_radius += 1
		else:
			circle_radius -= 1

		if circle_radius > 230:
			circle_radius = 230
			should_grow = False
		elif circle_radius < 100:
			circle_radius = 100
			should_grow = True

		screen.blit(broken_boat, (boat_cx - broken_boat.get_width()/2, boat_cy - broken_boat.get_height()/2))

		you_died_text = death_screen_title_font.render("Game Over!", "", (255, 255, 255))
		screen.blit(you_died_text, (100, ((SCREEN_HEIGHT*1.1)/5) * 1.37))
		you_died_subtitle_text = death_screen_subtitle_font.render(f"You collected {trashes_collected} trashes!", "", (255, 255, 255))
		screen.blit(you_died_subtitle_text, (120, ((SCREEN_HEIGHT*1.1)/5) * 1.4 + you_died_text.get_height()))

		mx, my = pygame.mouse.get_pos()

		mx, my = pygame.mouse.get_pos()

		# Replay Button
		replay_btn_x, replay_btn_y = (115, ((SCREEN_HEIGHT*1.1)/5) * 2.2)
		replay_button = pygame.Rect(replay_btn_x, replay_btn_y, 400, 50)
		if replay_button.collidepoint((mx, my)):
			pygame.draw.rect(screen, (255, 255, 255), (replay_btn_x - 2.5, replay_btn_y - 2.5, 405, 55))
			if mouse_pressed:
				run_game = "replay"
				exited = True
		pygame.draw.rect(screen, (0, 18, 35), replay_button)

		if replay_button.collidepoint((mx, my)):
			replay_button_text = death_screen_button_on_hover_font.render("REPLAY!", "", (255, 255, 255))
			screen.blit(replay_button_text, ((replay_btn_x + 200) - (replay_button_text.get_width()/2), (replay_btn_y + 25) - (replay_button_text.get_height()/2)))
		else:
			replay_button_text = death_screen_button_font.render("REPLAY!", "", (255, 255, 255))
			screen.blit(replay_button_text, ((replay_btn_x + 200) - (replay_button_text.get_width()/2), (replay_btn_y + 25) - (replay_button_text.get_height()/2)))

		# Main Menu Button
		main_menu_btn_x, main_menu_btn_y = (115, replay_btn_y + 50 + 10)
		main_menu_button = pygame.Rect(main_menu_btn_x, main_menu_btn_y, 400, 50)
		if main_menu_button.collidepoint((mx, my)):
			pygame.draw.rect(screen, (255, 255, 255), (main_menu_btn_x - 2.5, main_menu_btn_y - 2.5, 405, 55))
			if mouse_pressed:
				exited = True
		pygame.draw.rect(screen, (0, 18, 35), main_menu_button)

		if main_menu_button.collidepoint((mx, my)):
			main_menu_button_text = death_screen_button_on_hover_font.render("MAIN MENU!", "", (255, 255, 255))
			screen.blit(main_menu_button_text, ((main_menu_btn_x + 200) - (main_menu_button_text.get_width()/2), (main_menu_btn_y + 25) - (main_menu_button_text.get_height()/2)))
		else:
			main_menu_button_text = death_screen_button_font.render("MAIN MENU!", "", (255, 255, 255))
			screen.blit(main_menu_button_text, ((main_menu_btn_x + 200) - (main_menu_button_text.get_width()/2), (main_menu_btn_y + 25) - (main_menu_button_text.get_height()/2)))

		# Exit Button
		exit_btn_x, exit_btn_y = (115, main_menu_btn_y + 50 + 10)
		exit_button = pygame.Rect(exit_btn_x, exit_btn_y, 400, 50)
		if exit_button.collidepoint((mx, my)):
			pygame.draw.rect(screen, (255, 255, 255), (exit_btn_x - 2.5, exit_btn_y - 2.5, 405, 55))
			if mouse_pressed:
				run_game = False
				exited = True
		pygame.draw.rect(screen, (0, 18, 35), exit_button)

		if exit_button.collidepoint((mx, my)):
			exit_button_text = death_screen_button_on_hover_font.render("EXIT!", "", (255, 255, 255))
			screen.blit(exit_button_text, ((exit_btn_x + 200) - (exit_button_text.get_width()/2), (exit_btn_y + 25) - (exit_button_text.get_height()/2)))
		else:
			exit_button_text = death_screen_button_font.render("EXIT!", "", (255, 255, 255))
			screen.blit(exit_button_text, ((exit_btn_x + 200) - (exit_button_text.get_width()/2), (exit_btn_y + 25) - (exit_button_text.get_height()/2)))
		
		msg = "This is a game By the KCT. And this is his first ever game created with python and pygame for the SeaJam game jam which also happens to be my very first game jam so I really hope this game was good and thank you for playing it."
		draw_text_multilined(screen, msg, (255, 255, 255), (105, exit_btn_y + 50 + 10, 500, 500), death_screen_info_font)
		
		pygame.display.update()
	
	return run_game