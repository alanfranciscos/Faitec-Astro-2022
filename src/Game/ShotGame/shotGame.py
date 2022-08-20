import pygame
# from Game.shotGame import shotGame
from Pause.pause import pauseScreen

def shotGame(screen, mouse, font, screen_i):
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pauseScreen(screen, font, screen_i)

    image_path = "src\Game\ShotGame\Images\ShotGame\Background.png"
    background_image = pygame.image.load(image_path).convert()
    background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
    screen.blit(background_image,[0,0])
    pygame.display.flip()
    pygame.time.delay(10)
##############################################################################
