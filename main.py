import sys
import pygame

pygame.init()
pygame.mixer.init()

from game import *
from screens import death_screen, main_menu_screen

screen = pygame.display.set_mode((SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1))
pygame.display.set_caption(game_name)
pygame.display.set_icon(pygame.image.load("assets/icon.ico"))

pygame.mixer.music.load("assets/sfx/main_theme.wav")
pygame.mixer.music.play(-1)

highscore = get_highscore()

should_replay = False
while True:
	if not should_replay:
		can_play_game = main_menu_screen(screen, highscore)
		if not can_play_game:
			break
		elif can_play_game == "howtoplay":
			print("okay")
	else:
		should_replay = False

	trashes_collected = run_game(screen)
	if trashes_collected > highscore:
		new_highscore(trashes_collected)
		highscore = get_highscore()
		should_continue = death_screen(screen, trashes_collected, True)
	else:
		should_continue = death_screen(screen, trashes_collected)

	if not should_continue:
		break
	
	if should_continue == "replay":
		should_replay = True

pygame.quit()
sys.exit()
