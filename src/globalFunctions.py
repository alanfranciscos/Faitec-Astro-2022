import pygame

def click(mouse, x_init, widht, y_init, height):
  x_final = x_init + widht
  y_final = y_init + height
  return (xValue(x_init))<= mouse[0] <= (xValue(x_final)) and (yValue(y_init)) <= mouse[1] <=(yValue(y_final))

def text(screen, font, text, position):
  text = font.render(text, True ,(250,250,250))
  screen.blit(text, (position[0], position[1]))

## RegraDeTres:
def xValue(value):
  info_screen = pygame.display.Info()
  return (info_screen.current_w*value)/1920

def yValue(value):
  info_screen = pygame.display.Info()
  return (info_screen.current_h*value)/1080
