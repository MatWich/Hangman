import pygame
import config
import math
import secrets
pygame.init()

# SCREEN
screen = pygame.display.set_mode((config.SCREEN_SIZE))
pygame.display.set_caption("HANGMAN GAME")

# LOADING IMGS
images = [pygame.image.load("imgs/hangman" + str(x) + ".png") for x in range(0, 5)]
print(images)

# GAME VARIABLES
hangmanStatus = 4
words = ["HANGMAN", "INVADERS", "PYTHON", "PYGAME", "PYQT5"]
choice = secrets.choice(words)
index = words.index(choice)
word = words[index]
print(word)

guessed = []

# SETTING LETTERS POS
letters = []    # X, Y
firstX = round((config.WIDTH - (config.RADIUS * 2 + config.GAP) * 13) / 2)
firtsY = 400
A = 65
for i in range(26):
    X = firstX + config.GAP * 2 + ((config.RADIUS * 2 + config.GAP) * (i % 13))
    Y = firtsY + ((i  // 13) * (config.GAP + config.RADIUS * 2))
    letters.append([X, Y, chr(A + i), True])
print(len(letters))

def draw():
    screen.fill((255, 255, 255))
    # DRAW WORD
    displayWord = ""
    for letter in word:
        if letter in guessed:
            displayWord += letter + " "
        else:
            displayWord += "_ "
    DisplayedWord = config.LETTERS_FONT.render(displayWord, 1, (0, 0, 0))
    screen.blit(DisplayedWord, (400, 200))

    # LETTERS
    for letter in letters:
        x, y, s, visible = letter
        if visible == True:
            pygame.draw.circle(screen, (0, 0, 0), (x, y), config.RADIUS, 3)
            l = config.LETTERS_FONT.render(s, 1, (0, 0, 0))
            screen.blit(l, (x - l.get_width()/2, y - l.get_height() / 2))
    screen.blit(images[hangmanStatus], (0, 0))
    pygame.display.update()

clock = pygame.time.Clock()
run = True
while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, l, visible = letter
                if visible == True:
                    dis = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                    if dis < config.RADIUS:
                        letter[3] = False
                        guessed.append(l)
                        if l not in word:
                            hangmanStatus -= 1
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won == True:
        print("You win")
        break

    if hangmanStatus == -1:
        print("you lost")
        break

    draw()

