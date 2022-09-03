import pygame
from Game.ShotGame.planets import calcShowPlanets, drawPlanets
# from Game.shotGame import shotGame
from Pause.pause import pauseScreen


def shotGame(screen, font, screen_i):
  cursor =[0,0]
  mouse_ant = [0,0]
  mouse = [0,0]

  terraCoordinates = [-500,-500]
  luaCoordinates = [-500,-500]
  saturnoCoordinates = [-500,-500]
  solCoordinates = [-500,-500]
  allCoordinates =  [terraCoordinates, luaCoordinates, saturnoCoordinates, solCoordinates]

  calcShowPlanets(allCoordinates)

  pygame.mouse.set_visible(False)
  while True:
    insertBackground(screen, screen_i)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pauseScreen(screen, font, screen_i)
          pygame.mouse.set_visible(False)
      if event.type == pygame.MOUSEMOTION:
        mouse = event.pos
      if event.type == pygame.MOUSEBUTTONDOWN:
        calcShowPlanets(allCoordinates)

    drawPlanets(screen, allCoordinates)
    cursor = drawMouse(screen,mouse, mouse_ant, cursor, screen_i)
    mouse_ant = mouse
    pygame.display.flip()
    # pygame.time.delay(100)

##############################################################################


def drawMouse(screen, mouse, mouse_ant, cursor, screen_i):
  dif = [mouse[0] - mouse_ant[0], mouse[1] - mouse_ant[1]]
  tamanho = 1508
  width = (screen_i[0][0]*tamanho)/screen_i[1][0]
  if(cursor[0]+dif[0] >= (width)):
    cursor = [width, cursor[1]+dif[1]]
  elif (cursor[0]+dif[0] <=0):
     cursor = [0, cursor[1]+dif[1]]
  else:
    cursor = [cursor[0]+dif[0], cursor[1]+dif[1]]
  color = (255 , 0, 0)
  pygame.draw.circle(screen, color, cursor , 10, 10)
  return cursor

def insertBackground(screen, screen_i):
  image_path = "src\Game\ShotGame\Images\ShotGame\Background.png"
  background_image = pygame.image.load(image_path).convert()
  background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
  screen.blit(background_image,[0,0])
