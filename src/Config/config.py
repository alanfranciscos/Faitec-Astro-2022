import pygame
from globalFunctions import click, drawMouseCursor, xValue, yValue


def pauseMenu(screen: any, mouse: any, screen_i, config):
    x_init = 654
    x_final = 600
    y_init = 496
    y_final = 150
    if (click(mouse, x_init, x_final, y_init, y_final)):
        pauseScreen(screen, screen_i, config)


#################################################################


def pauseScreen(screen: any, screen_i, config):
    print(config)
    stopWhile = True
    pygame.mouse.set_visible(False)
    mouse = pygame.mouse.get_pos()
    while (stopWhile):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stopWhile = False
            if event.type == pygame.MOUSEMOTION:
                mouse = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = event.pos
                tutorialButton(mouse, config)
                musicButton(mouse, config)
                difficultButton(mouse, config)
                stopWhile = returnButton(mouse)
        image_path = "src\Config\Images\Background.png"
        background_image = pygame.image.load(image_path).convert()
        background_image = pygame.transform.scale(
            background_image, (screen_i[0][0], screen_i[0][1]))
        screen.blit(background_image, [0, 0])
        drawConfiguarion(screen, config)
        drawMouseCursor(screen, mouse)
        pygame.display.flip()


#################################################################


def tutorialButton(mouse, configuration):
    x_init = 594
    x_final = 100
    y_init = 540
    y_final = 100
    if (click(mouse, x_init, x_final, y_init, y_final)):
        configuration[1] = not configuration[1]


def musicButton(mouse, configuration):
    x_init = 594
    x_final = 100
    y_init = 356
    y_final = 100
    if (click(mouse, x_init, x_final, y_init, y_final)):
        configuration[0] = not configuration[0]


def difficultButton(mouse, configuration):
    x_init = 758
    x_final = 100
    y_init = 701
    y_final = 100
    if (click(mouse, x_init, x_final, y_init, y_final)):
        configuration[2] = 0
    x_init = 999
    if (click(mouse, x_init, x_final, y_init, y_final)):
        configuration[2] = 1
    x_init = 1255
    if (click(mouse, x_init, x_final, y_init, y_final)):
        configuration[2] = 2


def returnButton(mouse):
    x_init = 78
    x_final = 150
    y_init = 75
    y_final = 150
    return not click(mouse, x_init, x_final, y_init, y_final)


def drawSelectTrue(screen, position):
    image_path = "src\Config\Images\Select.png"
    selectImage = pygame.image.load(image_path).convert_alpha()
    selectImage = pygame.transform.scale(selectImage,
                                         (xValue(100), yValue(100)))
    position = [xValue(position[0]), yValue(position[1])]
    screen.blit(selectImage, position)


def drawConfiguarion(screen, config):
    if (config[0] == True):
        musicCoordinates = [594, 356]
        drawSelectTrue(screen, musicCoordinates)

    if (config[1] == True):
        tutorialCoordinates = [594, 540]
        drawSelectTrue(screen, tutorialCoordinates)

    if (config[2] == 0):
        dificuldadeCoordinate = [758, 701]
        drawSelectTrue(screen, dificuldadeCoordinate)
    elif (config[2] == 1):
        dificuldadeCoordinate = [999, 701]
        drawSelectTrue(screen, dificuldadeCoordinate)
    elif (config[2] == 2):
        dificuldadeCoordinate = [1255, 701]
        drawSelectTrue(screen, dificuldadeCoordinate)
