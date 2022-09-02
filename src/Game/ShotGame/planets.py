import pygame
import random

from globalFunctions import xValue, yValue

def drawPlanets(screen, PlanetsCoordinates):
  terra_path = "src\Game\ShotGame\Images\ShotGame\Terra.png"
  lua_path = "src\Game\ShotGame\Images\ShotGame\lua.png"
  saturno_path = "src\Game\ShotGame\Images\ShotGame\saturno.png"
  sol_path = "src\Game\ShotGame\Images\ShotGame\sol.png"
  terra =  pygame.image.load(terra_path).convert_alpha()
  screen.blit(terra,PlanetsCoordinates.terraCoordinates)

  lua =  pygame.image.load(lua_path).convert_alpha()
  screen.blit(lua, PlanetsCoordinates.luaCoordinates)

  saturno =  pygame.image.load(saturno_path).convert_alpha()
  screen.blit(saturno, PlanetsCoordinates.saturnoCoordinates)

  sol =  pygame.image.load(sol_path).convert_alpha()
  screen.blit(sol, PlanetsCoordinates.solCoordinates)

def calcShowPlanets(PlanetsCoordinates):
  screen =[int(xValue(1505)),int(yValue(1080))]
  PlanetsCoordinates.terraCoordinates = randomPlanets(screen)


def compareLocalPlanets(random, space):
  igual = True
  atualXRandomEqual =  space[0][0] > random[0] and space[0][1] < random[0]
  atualyRandomEqual =  space[1][0] > random[1] and space[1][1] < random[1]
  igual = not atualXRandomEqual and not atualyRandomEqual
  return igual
\
def compareAndDrawPlanets(width,height,space, igual):
  while(igual):
    atualRandom = randomPlanets(width, height)
    igual = compareLocalPlanets(atualRandom, space)


def getSpacePlanet(planet):
  return [[planet[0]-int(xValue(50)), planet[0] + int(xValue(50))],
          [planet[1]-int(yValue(50)), planet[1] + int(yValue(50))]]

def randomPlanets(screen):
  return [random.randint(0, screen[0]-int(xValue(100))), random.randint(0, screen[1]-int(yValue(100)))]


def rangeRandomPlanets(planet):
  return planet[0][0]
