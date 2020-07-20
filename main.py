import pygame
import config
import math
pygame.init()

screen = pygame.display.set_mode((config.SCREEN_SIZE))

images = [pygame.image.load("imgs/hangman" + str(x) + ".png") for x in range(0, 5)]
print(images)

# SETTING LETTERS POS
letters = []    # X, Y
firstX = round((config.WIDTH - (config.RADIUS * 2 + config.GAP) * 13) / 2)
firtsY = 400
for i in range(26):
    X = firstX + config.GAP * 2 + ((config.RADIUS * 2 + config.GAP) * (i % 13))
    Y = firtsY + ((i  // 13) * (config.GAP + config.RADIUS * 2))
    letters.append([X, Y])
print(len(letters))



clock = pygame.time.Clock()


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


    pygame.display.update()
