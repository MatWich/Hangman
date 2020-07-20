import pygame
import config
pygame.init()

screen = pygame.display.set_mode((config.SCREEN_SIZE))

images = [pygame.image.load("imgs/hangman" + str(x) + ".png") for x in range(0, 5)]
print(images)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


    pygame.display.update()
