import pygame
from globalFunctions import click, text

def pauseMenu(screen: any, mouse: any, font, screen_i):
  x_init = 563
  x_final = 729
  y_init = 652
  y_final = 116
  if (click(mouse, x_init, x_final, y_init, y_final)):
    pauseScreen(screen , font, screen_i)

#################################################################

def pauseScreen(screen: any, font: any, screen_i):
  stopWhile = True
  pygame.mouse.set_visible(True)
  while(stopWhile):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          stopWhile = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = event.pos
        tutorialButton(mouse)
        musicButton (mouse)
        stopWhile = returnButton (mouse)
    image_path = "src\Pause\Images\Background.png"
    background_image = pygame.image.load(image_path).convert()
    background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
    screen.blit(background_image,[0,0])

    text(screen,font, "on", [500,500])

    pygame.display.flip()

#################################################################

def tutorialButton(mouse):
  x_init = 595
  x_final = 729
  y_init = 676
  y_final = 116
  if (click(mouse, x_init, x_final, y_init, y_final)):
    print("tutorial")

def musicButton(mouse):
  x_init = 595
  x_final = 729
  y_init = 467
  y_final = 116
  if (click(mouse, x_init, x_final, y_init, y_final)):
    print("music")


def returnButton(mouse):
  x_init = 1533
  x_final = 363
  y_init = 25
  y_final = 126
  if (click(mouse, x_init, x_final, y_init, y_final)):
    return False
  else:
    return True

