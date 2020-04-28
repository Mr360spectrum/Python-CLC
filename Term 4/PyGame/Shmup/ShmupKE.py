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
        # self.color = GREEN
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(GREEN)
        self.image = pygame.transform.scale(playerIMG, (50, 38))
        self.image.set_colorkey(BLACK)
        # Create a hitbox
        self.rect = self.image.get_rect()
        self.radius = 18
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
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top + 1)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((30, 30))
        # self.color = RED
        # self.image.fill(self.color)
        self.imageOriginal = random.choice(mobImages)
        self.imageOriginal.set_colorkey(BLACK)
        self.image = self.imageOriginal.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0 # Rotation
        self.rotSpeed = random.randrange(-8, 8)
        self.lastUpdate = pygame.time.get_ticks() 
        self.points = random.randrange(50, 100)
    
    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)
            self.speedx = random.randrange(-3, 3)
        
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > 50:
            self.last_update = now
            self.rot = (self.rot + self.rotSpeed) % 360
            newImage = pygame.transform.rotate(self.imageOriginal, self.rot)
            oldCenter = self.rect.center
            self.image = newImage
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((10, 20))
        # self.image.fill(YELLOW)
        self.image = pygame.transform.scale(laserIMG, (13, 54))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10
    
    def update(self):
        self.rect.y += self.speed_y
        # Kill the bullet if it goes off the screen
        if self.rect.bottom < 0:
            self.kill()

def drawText(surf, text, x, y, font, size, alias, color):
    font = pygame.font.Font(font, size)
    textSurface = font.render(text, alias, color)
    textRect = textSurface.get_rect()
    textRect.midtop = (x, y)
    surf.blit(textSurface, textRect)

#######################################

gameTitle = "Space Shooter"

FONT_NAME = pygame.font.match_font("arial")

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

# Set up asset folders
gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder, "img")

# Load all game graphics
background = pygame.image.load(os.path.join(imgFolder, "starfield.png")).convert()
backgroundRect = background.get_rect()

playerIMG = pygame.image.load(os.path.join(imgFolder, "playerShip.png")).convert()
# mobIMG = pygame.image.load(os.path.join(imgFolder, "meteor.png")).convert()
laserIMG = pygame.image.load(os.path.join(imgFolder, "laser.png")).convert()

mobImages = []
mobList = ["meteorBrown_big1.png", "meteorBrown_med1.png", 
           "meteorBrown_med3.png", "meteorBrown_small1.png", "meteorBrown_small2.png",
           "meteorBrown_tiny1.png"]

for img in mobList:
    mobImages.append(pygame.image.load(os.path.join(imgFolder, img)).convert())

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()

for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

score = 0

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

#######################################
    # Update
#######################################

    all_sprites.update()

    # Detect collision between player and mobs
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        running = False

    # Detect collision between bullets and mobs
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    # If mob is destroyed, create a new one
    for hit in hits: # Remove/change if level system desired
        score += hit.points - hit.radius
        print(score)
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

#######################################
   # Render (draw)
#######################################

    screen.fill(BLACK)
    screen.blit(background, backgroundRect)
    all_sprites.draw(screen)

    drawText(screen, str(score), WIDTH/2, 10, FONT_NAME, 35, True, GREEN)
    drawText(screen, "Lives", WIDTH-40, 10, FONT_NAME, 25, True, RED)

    # After drawing everything, flip the display
    # Must be the last call in the draw section
    pygame.display.flip()

#######################################


pygame.quit()
