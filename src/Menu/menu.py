import pygame
from globalFunctions import click

#Initialize menu window
def menu_init(screen:any, screen_i):
  localImage = "src/Menu/Images/Background.png"
  background_image = pygame.image.load(localImage).convert()
  background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
  screen.blit(background_image,[0,0])
  pygame.display.flip()
  # for event in pygame.event.get():
  #   if event.type == pygame.MOUSEMOTION:
  #     (event.pos)

def exit_game(mouse):
  x_init = 563
  width = 729
  y_init = 814
  heigth = 116
  if (click(mouse, x_init, width, y_init, heigth)):
    pygame.quit()
