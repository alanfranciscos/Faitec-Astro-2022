import pygame
import datetime
from Game.ShotGame.planets import calcShowPlanets, clickInPlanets, drawMouse, drawPlanets, getPlanetClickmouse
from Game.SideBar.sidebar import setQuestion, showQuestion, showResponse, showTime
# from Game.shotGame import shotGame
from Config.config import pauseScreen
from globalFunctions import verifyHandleTime


def shotGame(screen, font, screen_i, config):
    cursor = [0, 0]
    mouse_ant = [0, 0]
    mouse = [0, 0]

    terraCoordinates = [-500, -500]
    luaCoordinates = [-500, -500]
    saturnoCoordinates = [-500, -500]
    solCoordinates = [-500, -500]
    allCoordinates = [
        terraCoordinates, luaCoordinates, saturnoCoordinates, solCoordinates
    ]

    pontuacao = 0
    correta = 0
    response = 0

    calcShowPlanets(allCoordinates)

    x = [0, 0]
    res = [0, 0, 0, 0]
    difficult = 0
    correta = setQuestion(x, res, difficult)

    pontuacao = 0

    pygame.mouse.set_visible(False)

    timer = datetime.datetime.now()
    timeAnt = timer.second
    timeAtual = timer.second
    difficultTime = 0

    time = 60

    lose = False

    while not lose:

        timer = datetime.datetime.now()
        timeAtual = timer.second
        timeEqual = verifyHandleTime(timeAnt, timeAtual)
        if (timeEqual):
            time = time - 1
        timeAnt = timeAtual
        if (time < 0):
            break

        insertBackground(screen, screen_i)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pauseScreen(screen, screen_i, config)
                    pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEMOTION:
                mouse = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (clickInPlanets(allCoordinates, cursor)):
                    response = getPlanetClickmouse(allCoordinates, cursor)
                    pontuacao = pontuacao + verifyResponse(correta, response)

                    difficultTime = setDificult(pontuacao)
                    if (verifyResponse(correta, response) == 1):
                        time = setTimedifficult(difficultTime)
                    else:
                        time = -1
                        break

                    correta = setQuestion(x, res, difficult)
                    calcShowPlanets(allCoordinates)
        showTime(screen, time)
        showResponse(screen, pontuacao)
        drawPlanets(screen, allCoordinates)
        showQuestion(x, res, screen)
        cursor = drawMouse(screen, mouse, mouse_ant, cursor, screen_i)
        mouse_ant = mouse
        pygame.display.flip()


##############################################################################


def insertBackground(screen, screen_i):
    image_path = "src\Game\ShotGame\Images\ShotGame\Background.png"
    background_image = pygame.image.load(image_path).convert()
    background_image = pygame.transform.scale(background_image,
                                              (screen_i[0][0], screen_i[0][1]))
    screen.blit(background_image, [0, 0])


def verifyResponse(correta, response):
    if (correta == response):
        return 1
    else:
        return 0


def setTimedifficult(difficult):
    time = 60
    if (difficult == 0):
        time = 60
    if (difficult == 1):
        time = 50
    if (difficult == 2):
        time = 40
    if (difficult == 3):
        time = 30
    if (difficult == 4):
        time = 20
    return time


def setDificult(pontuacao):
    dificuldade = 0
    if (pontuacao < 5):
        dificuldade = 0
    if (pontuacao >= 5):
        dificuldade = 1
    if (pontuacao >= 10):
        dificuldade = 2
    if (pontuacao >= 15):
        dificuldade = 3
    if (pontuacao > 20):
        dificuldade = 4
    return dificuldade
