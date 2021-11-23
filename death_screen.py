import pygame, sys
from constants import *

def show_death_screen(screen, trashes_collected):
	run_game = True
	exited = False
	circle_radius = 0
	should_grow = True
	mouse_pressed = False
	while not exited:
		screen.fill((240, 79, 76))

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
		screen.blit(you_died_text, (100, ((SCREEN_HEIGHT*1.1)/5) * 1.5))
		you_died_subtitle_text = death_screen_subtitle_font.render(f"You collected {trashes_collected} trashes!", "", (255, 255, 255))
		screen.blit(you_died_subtitle_text, (120, ((SCREEN_HEIGHT*1.1)/5) * 1.5 + you_died_text.get_height() - 20))

		mx, my = pygame.mouse.get_pos()

		mx, my = pygame.mouse.get_pos()

		# Continue Button
		continue_btn_x, continue_btn_y = (115, ((SCREEN_HEIGHT*1.1)/5) * 2.2)
		continue_button = pygame.Rect(continue_btn_x, continue_btn_y, 400, 50)
		if continue_button.collidepoint((mx, my)):
			pygame.draw.rect(screen, (255, 255, 255), (continue_btn_x - 2.5, continue_btn_y - 2.5, 405, 55))
			if mouse_pressed:
				exited = True
		pygame.draw.rect(screen, (0, 18, 35), continue_button)

		if continue_button.collidepoint((mx, my)):
			continue_button_text = death_screen_button_on_hover_font.render("CONTINUE!", "", (255, 255, 255))
			screen.blit(continue_button_text, ((continue_btn_x + 200) - (continue_button_text.get_width()/2), (continue_btn_y + 25) - (continue_button_text.get_height()/2)))
		else:
			continue_button_text = death_screen_button_font.render("CONTINUE!", "", (255, 255, 255))
			screen.blit(continue_button_text, ((continue_btn_x + 200) - (continue_button_text.get_width()/2), (continue_btn_y + 25) - (continue_button_text.get_height()/2)))

		# Exit Button
		exit_btn_x, exit_btn_y = (115, ((SCREEN_HEIGHT*1.1)/5) * 2.5)
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
		
		msg = "This is a game By Tejas. And this is his first ever game created with python and pygame for the SeaJam game jam which also happens to be my very first game jam so I really hope this game was good and thank you for playing it."
		draw_text(screen, msg, (255, 255, 255), (105, ((SCREEN_HEIGHT*1.1)/5) * 2.85, 500, 500), death_screen_info_font)
		
		pygame.display.update()
	
	return run_game