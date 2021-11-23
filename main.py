import sys
import pygame
import tkinter as tk
from tkinter import ttk

from pygame.transform import scale

pygame.init()

from game import *
from death_screen import show_death_screen

screen = pygame.display.set_mode((SCREEN_WIDTH * 1.1, SCREEN_HEIGHT * 1.1))
pygame.display.set_caption("Clean the Ocean")
pygame.display.set_icon(pygame.image.load("assets/icon.ico"))

while True:
	trashes_collected = run_game(screen)
	should_continue = show_death_screen(screen, trashes_collected)
	
	if not should_continue:
		break

pygame.quit()
sys.exit()
