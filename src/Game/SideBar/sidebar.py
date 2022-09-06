import random
import pygame

from globalFunctions import text

def setQuestion(x , res, difficult):
  resposta = 0
  if(difficult ==0 ):
    x[0] = random.randint(0, 10)
    x[1] = random.randint(0, 10)
    correta = random.randint(0, 3)
    resposta = x[0]+x[1]
    i = 0
    while(i<=3):
      if(i == correta):
        res[i] = resposta
      else:
        igual = True
        while(igual):
          resAtual =  random.randint(resposta-5, resposta+5)
          if(resAtual == resposta):
            igual = True
          else:
            igual = False
            res[i] = resAtual
      i = i+1
    return correta

def showQuestion(x, res, screen):
  font = pygame.font.SysFont("arial", 60)
  position = [1609, 364]
  question = str(x[0]) + "+" + str(x[1])
  text(screen, font, question, position)

  solPosition = [1682,519]
  saturnoPosition = [1682, 657]
  luaPosition = [1682,795]
  terraPosition = [1682,933]

  text(screen, font, str(res[0]), solPosition)
  text(screen, font, str(res[1]), saturnoPosition)
  text(screen, font, str(res[2]), luaPosition)
  text(screen, font, str(res[3]), terraPosition)

def getAnswer(x, difficult):
  if(difficult == 0):
    return x[0]+x[1]

