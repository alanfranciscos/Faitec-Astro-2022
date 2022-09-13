import pygame

from Game.MainGame import init_game
from Config.config import pauseMenu, pauseScreen
from Menu.menu import menu_init, exit_game

#Initialize pygame
pygame.init()

font = pygame.font.SysFont("arial", 30)

info_screen = pygame.display.Info()
imx = info_screen.current_w
imy = info_screen.current_h
screen_i = [imx, imy], [1920, 1080]

window_width = pygame.display.Info().current_w
window_height = pygame.display.Info().current_h
size = (window_width, window_height)
screen = pygame.display.set_mode((size))

### configuration variables
music = True
tutorial = True
difficult = 0
config = [music, tutorial, difficult]

mouse = pygame.mouse.get_pos()
pygame.mouse.set_visible(False)
while True:

    #Get events in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pauseScreen(screen, screen_i)
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.pos
            exit_game(mouse)
            init_game(screen, mouse, font, screen_i, config)
            pauseMenu(screen, mouse, screen_i, config)

        menu_init(screen, screen_i, mouse)
