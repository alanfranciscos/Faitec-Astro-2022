import pygame
from Game.LoadingGame import loading_game
from Game.ShotGame.shotGame import shotGame
from globalFunctions import click

def init_game(screen, mouse, font, screen_i):
  x_init = 430
  x_final = 985
  y_init = 514
  y_final = 617
  if (click(mouse, screen_i, x_init, x_final, y_init, y_final)):
    loading_game(screen, screen_i)
    shotGame(screen, mouse, font, screen_i)
