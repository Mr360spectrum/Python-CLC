# Karter Ence
# PyGame Template
# 4/1/2020
import pygame
import random
import os

# Game settings
WIDTH = 360 # Width of game window
HEIGHT = 480 # Height of game window
FPS = 30 # Frames per second

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up asset folders
gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder, "img")
playerIMG = pygame.image.load(os.path.join(imgFolder, "playerImage.png")).convert()

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerIMG
        self.image.set_colorkey(BLACK)
        
        # self.color = GREEN

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        self.speedx = random.randint(-100, 100)
        self.speedy = random.randint(-100, 100)

    def update(self):
        global screenColor

        # self.rect.x += self.speedx # Left or right (pixels per frame)
        # self.rect.y += self.speedy

        # Screen wrap right
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
        # # Screen wrap left
        # if self.rect.right < 0:
        #     self.rect.left = WIDTH
        # if self.rect.top > HEIGHT:
        #     self.rect.bottom = 0
        # if self.rect.bottom < 0:
        #     self.rect.top = HEIGHT
        # if self.rect.top > HEIGHT:
        #     self.rect.bottom = 0

        # # Screen bounce and color change
        # if self.rect.right > WIDTH:
        #     self.speedx *= -1
        #     screenColor = random.choice(colorList)
        #     self.color = random.choice(colorList)
        # if self.rect.left < 0:
        #     self.speedx *= -1
        #     screenColor = random.choice(colorList)
        #     self.color = random.choice(colorList)
        # if self.rect.bottom > HEIGHT:
        #     self.speedy *= -1
        #     screenColor = random.choice(colorList)
        #     self.color = random.choice(colorList)
        # if self.rect.top < 0:
        #     self.speedy *= -1
        #     screenColor = random.choice(colorList)
        #     self.color = random.choice(colorList)

        # self.image.fill(self.color)

#######################################

gameTitle = "A game, I guess."

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
PINK = (255, 0, 127)
GREY = (128, 128, 128)
CORNFLOWERBLUE = (39, 58, 93)
DEEPPURPLE = (105, 34, 191)

colorList = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, PINK, GREY, CORNFLOWERBLUE, DEEPPURPLE]

screenColor = random.choice(colorList)

#######################################

# Creating game objects
pygame.init()
pygame.mixer.init()
pygame.display.set_caption(gameTitle)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()

# Add sprites to groups
all_sprites.add(player)

# Start of game loop
running = True
while running:
    clock.tick(FPS)

    # Process input (events)
#######################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_r:
        #         screen.fill(CORNFLOWERBLUE)
        #     elif event.key == pygame.K_e:
        #         screen.fill(RED)
                

#######################################
    # Update
#######################################
    all_sprites.update()

#######################################
    # Render (draw)
#######################################
    screen.fill(screenColor)
    all_sprites.draw(screen)

    # After drawing everything, flip the display
    # Must be the last call in the draw section
    pygame.display.flip()

#######################################


pygame.quit()
