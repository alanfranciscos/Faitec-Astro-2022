import pygame
# from Game.shotGame import shotGame
from Pause.pause import pauseScreen

def shotGame(screen, font, screen_i):
  cursor =[0,0]
  mouse_ant = [0,0]
  mouse = [0,0]
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
    drawPlanets(screen)
    cursor = drawMouse(screen,mouse, mouse_ant, cursor)
    mouse_ant = mouse
    pygame.display.flip()
    pygame.time.delay(10)

##############################################################################


def drawMouse(screen, mouse, mouse_ant, cursor):
  dif = [mouse[0] - mouse_ant[0], mouse[1] - mouse_ant[1]]
  if(cursor[0]+dif[0] >= 1100):
    cursor = [1100, cursor[1]+dif[1]]
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

def drawPlanets(screen):
  terra_path = "src\Game\ShotGame\Images\ShotGame\Terra.png"
  lua_path = "src\Game\ShotGame\Images\ShotGame\lua.png"
  saturno_path = "src\Game\ShotGame\Images\ShotGame\saturno.png"
  sol_path = "src\Game\ShotGame\Images\ShotGame\sol.png"
  terra =  pygame.image.load(terra_path).convert_alpha()
  screen.blit(terra,[0,0])

  lua =  pygame.image.load(lua_path).convert_alpha()
  screen.blit(lua,[0,0])

  saturno =  pygame.image.load(saturno_path).convert_alpha()
  screen.blit(saturno,[0,0])

  sol =  pygame.image.load(sol_path).convert_alpha()
  screen.blit(sol,[0,0])
