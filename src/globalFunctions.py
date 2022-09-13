import pygame


def click(mouse, x_init, widht, y_init, height):
    x_final = x_init + widht
    y_final = y_init + height
    return (xValue(x_init)) <= mouse[0] <= (xValue(x_final)) and (
        yValue(y_init)) <= mouse[1] <= (yValue(y_final))


def text(screen, font, text, position):
    text = font.render(text, True, (250, 250, 250))
    screen.blit(text, (xValue(position[0]), yValue(position[1])))


## RegraDeTres:
def xValue(value):
    info_screen = pygame.display.Info()
    return (info_screen.current_w * value) / 1920


def yValue(value):
    info_screen = pygame.display.Info()
    return (info_screen.current_h * value) / 1080


## time
def verifyHandleTime(anterior, atual):
    igual = False
    if (anterior != atual):
        igual = True
    return igual


def drawMouseCursor(screen, mouse):
    image_path = "src/Images/Cursor.png"
    selectImage = pygame.image.load(image_path).convert_alpha()
    selectImage = pygame.transform.scale(selectImage,
                                         (xValue(100), yValue(100)))
    mouse = [int(xValue(mouse[0])-xValue(20)), int(yValue(mouse[1])-yValue(20))]
    screen.blit(selectImage, mouse)
