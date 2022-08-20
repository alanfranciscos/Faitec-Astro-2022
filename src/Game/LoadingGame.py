import pygame

window_width = 1440
window_height = 1024

def loading_game(screen: any, screen_i):
  i = 0
  while i<4:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    if i == 0:
      image_path = "src\Game\Images\Loading\Loading_3.png"
    elif i == 1:
      image_path = "src\Game\Images\Loading\Loading_2.png"
    elif i == 2:
      image_path = "src\Game\Images\Loading\Loading_1.png"
    else:
      image_path = "src\Game\Images\Loading\Loading_GO.png"
      background_image = pygame.image.load(image_path).convert()
      background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
      screen.blit(background_image,[0,0])
      pygame.display.flip()
      pygame.time.delay(10)
      i = i+1
###
