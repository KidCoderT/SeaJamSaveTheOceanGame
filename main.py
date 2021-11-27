import sys
import pygame

pygame.init()
pygame.mixer.init()

from game import *
from screens import death_screen, main_menu_screen

screen = pygame.display.set_mode((SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1))
pygame.display.set_caption(game_name)
pygame.display.set_icon(pygame.image.load("assets/icon.ico"))

should_replay = False
while True:
	if not should_replay:
		can_play_game = main_menu_screen(screen)
		if not can_play_game:
			break
		elif can_play_game == "howtoplay":
			print("okay")
	else:
		should_replay = False

	trashes_collected = run_game(screen)
	should_continue = death_screen(screen, 55)

	if not should_continue:
		break
	
	if should_continue == "replay":
		should_replay = True

pygame.quit()
sys.exit()
