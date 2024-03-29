import pygame

from Game.MainGame import init_game
from Pause.pause import pauseMenu, pauseScreen
from Menu.menu import menu_init, exit_game

#Initialize pygame
pygame.init()

font = pygame.font.SysFont("arial", 30)

info_screen = pygame.display.Info()
imx = info_screen.current_w
imy = info_screen.current_h
screen_i = [imx, imy],[1440,1024]

window_width = pygame.display.Info().current_w
window_height = pygame.display.Info().current_h
size = (window_width, window_height)
# screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
screen = pygame.display.set_mode((size))

while True:
  #Get events in pygame
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pauseScreen(screen, font, screen_i)
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse = event.pos
      exit_game(mouse, screen_i)
      init_game(screen, mouse, font, screen_i)
      pauseMenu(screen, mouse, font, screen_i)

    menu_init(screen, screen_i)
