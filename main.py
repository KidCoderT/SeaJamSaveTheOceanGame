import sys
import pygame

pygame.init()

from game import *

screen = pygame.display.set_mode((SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1))
pygame.display.set_caption("Clean the Ocean")
pygame.display.set_icon(pygame.image.load("assets/icon.ico"))

trashes_collected = run_game(screen)
print(trashes_collected)

pygame.quit()
sys.exit()
