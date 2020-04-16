# Karter Ence
# Shmup
# 4/16/2020
import pygame
import random
import os

# Game settings
WIDTH = 480 # Width of game window
HEIGHT = 600 # Height of game window
FPS = 60 # Frames per second

# Create the game window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up asset folders
# gameFolder = os.path.dirname(__file__)
# imgFolder = os.path.join(gameFolder, "img")
# playerIMG = pygame.image.load(os.path.join(imgFolder, "playerImage.png")).convert()

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Create the image
        pygame.sprite.Sprite.__init__(self)
        # self.image = playerIMG
        # self.image.set_colorkey(BLACK)
        
        self.color = GREEN
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)

        # Create a hitbox
        self.rect = self.image.get_rect()
        self.rect.centerx = int(WIDTH / 2)
        self.rect.bottom = int(HEIGHT - (HEIGHT * 0.05))
        #Get the speed at which the image moves
        self.speedx = 0

    def update(self):
        # Player movement
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx

        # Binding sprite to screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.color = RED
        self.image.fill(self.color)
        #TODO: Enemy image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)
    
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

#######################################

gameTitle = "Space Shooter"

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
mobs = pygame.sprite.Group()

player = Player()
for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

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

#######################################
    # Update
#######################################

    all_sprites.update()

#######################################
   # Render (draw)
#######################################

    screen.fill(BLACK)
    all_sprites.draw(screen)

    # After drawing everything, flip the display
    # Must be the last call in the draw section
    pygame.display.flip()

#######################################


pygame.quit()
