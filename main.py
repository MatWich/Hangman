import pygame
import config
pygame.init()

screen = pygame.display.set_mode((config.SCREEN_SIZE))



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


    pygame.display.update()
