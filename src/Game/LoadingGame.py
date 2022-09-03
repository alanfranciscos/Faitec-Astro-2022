import pygame

from globalFunctions import click

def loading_game(screen: any, screen_i):
  i = 0
  button = False
  while not button:
    image_path = "src\Game\Images\Loading\History.png"
    background_image = pygame.image.load(image_path).convert()
    background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
    screen.blit(background_image,[0,0])
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = event.pos
        button = buttonPlay(mouse)

  while i<4:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    if i == 0:
      image_path = "src\Game\Images\Loading\Loading_3.png"
    elif i == 1:
      image_path = "src\Game\Images\Loading\Loading_2.png"
    elif i == 2:
      image_path = "src\Game\Images\Loading\Loading_1.png"
    else:
      image_path = "src\Game\Images\Loading\Loading_GO.png"
    background_image = pygame.image.load(image_path).convert()
    background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
    screen.blit(background_image,[0,0])
    pygame.display.flip()
    # pygame.time.delay(1000)
    i = i+1
###

def buttonPlay(mouse):
  x_init = 1442
  x_final = 350
  y_init = 812
  y_final = 110
  if (click(mouse, x_init, x_final, y_init, y_final)):
    return True
  else:
    return False
