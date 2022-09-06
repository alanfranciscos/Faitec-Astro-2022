import pygame
from Game.ShotGame.planets import calcShowPlanets, clickInPlanets, drawMouse, drawPlanets, getPlanetClickmouse
from Game.SideBar.sidebar import setQuestion, showQuestion
# from Game.shotGame import shotGame
from Pause.pause import pauseScreen
from globalFunctions import text


def shotGame(screen, font, screen_i):
  cursor =[0,0]
  mouse_ant = [0,0]
  mouse = [0,0]

  terraCoordinates = [-500,-500]
  luaCoordinates = [-500,-500]
  saturnoCoordinates = [-500,-500]
  solCoordinates = [-500,-500]
  allCoordinates =  [terraCoordinates, luaCoordinates, saturnoCoordinates, solCoordinates]

  pontuacao = 0
  correta = 0
  response = 0

  calcShowPlanets(allCoordinates)

  x = [0,0]
  res =[0,0,0,0]
  difficult = 0
  correta = setQuestion(x ,res, difficult)

  pontuacao = 0

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
        if(clickInPlanets(allCoordinates, cursor)):
          response = getPlanetClickmouse(allCoordinates, cursor)
          pontuacao = pontuacao + verifyResponse(correta, response)
          correta = setQuestion(x ,res, difficult)
          calcShowPlanets(allCoordinates)
          # question(x, screen)

    showResponse(screen,pontuacao)
    drawPlanets(screen, allCoordinates)
    showQuestion(x, res,  screen)
    cursor = drawMouse(screen,mouse, mouse_ant, cursor, screen_i)
    mouse_ant = mouse
    pygame.display.flip()
    # pygame.time.delay(100)

##############################################################################


def insertBackground(screen, screen_i):
  image_path = "src\Game\ShotGame\Images\ShotGame\Background.png"
  background_image = pygame.image.load(image_path).convert()
  background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
  screen.blit(background_image,[0,0])

def verifyResponse(correta, response):
  print(correta)
  print(response)
  print("---")
  if(correta == response):
    print("1")
    return 1
  else:
    print("0")
    return 0

def showResponse(screen, pontuacao):
  font = pygame.font.SysFont("arial", 60)
  pontuacaoPosition = [1740,12]
  text(screen, font, str(pontuacao), pontuacaoPosition)
