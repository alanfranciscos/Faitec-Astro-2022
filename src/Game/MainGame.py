from Game.LoadingGame import loading_game
from Game.ShotGame.shotGame import shotGame
from globalFunctions import click

def init_game(screen, mouse, font, screen_i):
  x_init = 563
  x_final = 729
  y_init = 487
  y_final = 116
  if (click(mouse, x_init, x_final, y_init, y_final)):
    loading_game(screen, screen_i)
    shotGame(screen, font, screen_i)
