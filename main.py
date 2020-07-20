import pygame
import config
import math
pygame.init()

# SCREEN
screen = pygame.display.set_mode((config.SCREEN_SIZE))
pygame.display.set_caption("HANGMAN GAME")

# LOADING IMGS
images = [pygame.image.load("imgs/hangman" + str(x) + ".png") for x in range(0, 5)]
print(images)


# SETTING LETTERS POS
letters = []    # X, Y
firstX = round((config.WIDTH - (config.RADIUS * 2 + config.GAP) * 13) / 2)
firtsY = 400
A = 65
for i in range(26):
    X = firstX + config.GAP * 2 + ((config.RADIUS * 2 + config.GAP) * (i % 13))
    Y = firtsY + ((i  // 13) * (config.GAP + config.RADIUS * 2))
    letters.append([X, Y, chr(A + i)])
print(len(letters))

def draw():
    screen.fill((255, 255, 255))
    # LETTERS
    for letter in letters:
        x, y, s = letter
        pygame.draw.circle(screen, (0, 0, 0), (x, y), config.RADIUS, 3)
        l = config.LETTERS_FONT.render(s, 1, (0, 0, 0))
        screen.blit(l, (x - l.get_width()/2, y - l.get_height() / 2))
    screen.blit(images[0], (0, 0))
    pygame.display.update()

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

    draw()

