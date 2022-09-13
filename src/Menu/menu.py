import pygame
from globalFunctions import click, drawMouseCursor


#Initialize menu window
def menu_init(screen: any, screen_i, mouse):
    localImage = "src/Menu/Images/Background.png"
    background_image = pygame.image.load(localImage).convert()
    background_image = pygame.transform.scale(background_image,
                                              (screen_i[0][0], screen_i[0][1]))
    screen.blit(background_image, [0, 0])

    drawMouseCursor(screen, mouse)

    pygame.display.flip()


def exit_game(mouse):
    x_init = 810
    width = 294
    y_init = 860
    heigth = 150
    if (click(mouse, x_init, width, y_init, heigth)):
        pygame.quit()
