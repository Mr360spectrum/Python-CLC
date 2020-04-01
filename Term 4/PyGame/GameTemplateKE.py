# Karter Ence
# PyGame Template
# 4/1/2020
import pygame
import random

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    
    def update(self):
        self.rect.x += 5
        if self.rect.right > WIDTH:
            # self.rect.right = 0
        # if self.rect.top > HEIGHT:
        #     self.rect.bottom = 0

#######################################

# Game settings
WIDTH = 360 # Width of game window
HEIGHT = 480 # Height of game window
FPS = 60 # Frames per second

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

#######################################

# Creating game objects
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    screen.fill(DEEPPURPLE)
    all_sprites.draw(screen)

    # After drawing everything, flip the display
    # Must be the last call in the draw section
    pygame.display.flip()

#######################################


pygame.quit()
