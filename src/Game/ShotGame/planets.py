import random
import pygame

from globalFunctions import xValue, yValue

def drawPlanets(screen, allCoordinates):
  terra_path = "src\Game\ShotGame\Images\ShotGame\Terra.png"
  lua_path = "src\Game\ShotGame\Images\ShotGame\lua.png"
  saturno_path = "src\Game\ShotGame\Images\ShotGame\saturno.png"
  sol_path = "src\Game\ShotGame\Images\ShotGame\sol.png"
  terra =  pygame.image.load(terra_path).convert_alpha()
  screen.blit(terra,allCoordinates[0])

  lua =  pygame.image.load(lua_path).convert_alpha()
  screen.blit(lua, allCoordinates[1])

  saturno =  pygame.image.load(saturno_path).convert_alpha()
  screen.blit(saturno, allCoordinates[2])

  sol =  pygame.image.load(sol_path).convert_alpha()
  screen.blit(sol, allCoordinates[3])



def calcShowPlanets(allCoordinates):
  screen =[int(xValue(1505)),int(yValue(1080))]
  all = [[-500,-500],[-500,-500],[-500,-500],[-500,-500]]
  i = 0
  while (i <= 3):
    VerifyLocation(all, screen, i)
    i = i+1
  allCoordinates[0] = all[0]
  allCoordinates[1] = all[1]
  allCoordinates[2] = all[2]
  allCoordinates[3] = all[3]


def VerifyLocation(all, screen, i):
    igual = True
    while(igual):
      if(i == 0):
        atual = randomPlanets(screen)
        all[i] = atual
        igual = False

      if(i == 1):
        atual = randomPlanets(screen)
        all[i] = atual
        spaceTerra = getSpacePlanet(all[0])
        igual = compareLocalPlanets(atual,spaceTerra)
      if(i == 2):
        atual = randomPlanets(screen)
        all[i] = atual
        spaceTerra = getSpacePlanet(all[0])
        spaceLua = getSpacePlanet(all[1])
        igual = compareLocalPlanets(atual,spaceTerra)
        if(igual == False):
          igual = compareLocalPlanets(atual,spaceLua)
      if(i == 3):
        atual = randomPlanets(screen)
        all[i] = atual
        spaceTerra = getSpacePlanet(all[0])
        spaceLua = getSpacePlanet(all[1])
        spaceSat = getSpacePlanet(all[2])
        igual = compareLocalPlanets(atual,spaceTerra)
        if(igual == False):
          igual = compareLocalPlanets(atual,spaceLua)
          if(igual == False):
            igual = compareLocalPlanets(atual,spaceSat)

def compareLocalPlanets(random, space):
  atual = getSpacePlanet(random)

  atualXRandomEqual = atual[0][1] >= space[0][0] or atual[0][0] <= space[0][1]
  atualyRandomEqual =  atual[1][0] <= space[1][1] and atual[1][1] >= space[1][0]
  igual = atualXRandomEqual and atualyRandomEqual
  return igual

def getSpacePlanet(planet):
  value = [[planet[0], planet[0] + (100)],
          [planet[1], planet[1] + ((100))]]
  return value

def randomPlanets(screen):
  return [random.randint(0, screen[0]-int(xValue(100))), random.randint(0, screen[1]-int(yValue(100)))]


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

def clickInPlanets(allCoordinates, mouse):
  i = 0
  clique = False
  while( i <= 3):
    atual = getSpacePlanet(allCoordinates[i])
    atualXRandomEqual = mouse[0] >= atual[0][0] and mouse[0] <= atual[0][1]
    atualyRandomEqual =  mouse[1] >= atual[1][0] and mouse[1] <= atual[1][1]
    print(atualXRandomEqual,atualyRandomEqual )
    print(mouse,atual )
    if(not clique):
      clique = atualXRandomEqual and atualyRandomEqual
    i=i+1
  print("-------------------------")
  return clique
