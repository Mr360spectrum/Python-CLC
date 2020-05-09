# Karter Ence
# Shmup
# 4/16/2020
import pygame
import random
import os
import sys

# Game settings
WIDTH = 480 # Width of game window
HEIGHT = 600 # Height of game window
FPS = 60 # Frames per second

# Create the game window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = True
score = 0

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
        self.shield = 100
        self.fuel = 100
        self.shootDelay = 500
        self.lastShot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hideTimer = pygame.time.get_ticks()
        self.power = 1
        self.powerTime = pygame.time.get_ticks()

    def update(self):
        # Player movement
        if self.hidden and pygame.time.get_ticks() - self.hideTimer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = int(HEIGHT -(HEIGHT * 0.05))
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx

        # Binding sprite to screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
        if self.power >= 2 and pygame.time.get_ticks() - self.powerTime > POWER_TIME:
            self.power -= 1
            self.powerTime = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.lastShot > self.shootDelay:
            self.lastShot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top + 1)
                all_sprites.add(bullet)
                bullets.add(bullet)
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
            shootSound.play()

    def getHit(self, mob):
        self.shield -= mob.radius
    
    def hide(self):
        # Hide the player temporarily
        self.hidden = True
        self.hideTimer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def powerUp(self):
        self.power += 1
        self.powerTime = pygame.time.get_ticks()

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

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosionAnim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.frameRate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.frameRate:
            self.lastUpdate = now
            self.frame += 1
            if self.frame == len(explosionAnim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosionAnim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["shield", "gun"])
        self.image = powerUpIMG[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy  = random.randrange(2, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

def drawText(surf, text, x, y, font, size, alias, color):
    font = pygame.font.Font(font, size)
    textSurface = font.render(text, alias, color)
    textRect = textSurface.get_rect()
    textRect.midtop = (x, y)
    surf.blit(textSurface, textRect)

def newMob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def drawShieldBar(surf, x, y, pct, color):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, color, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def drawLives(surf, x, y, lives, img):
    for i in range(lives):
        imgRect = img.get_rect()
        imgRect.x = x + 30 * i
        imgRect.y = y
        surf.blit(img, imgRect)

def openScoreFile(mode):
    """Opens the high score file and returns it."""
    try:
        file = open("scores.txt", mode)
        return file
    except IOError as e:
        drawText(screen, "No high scores found.", WIDTH/2, HEIGHT * 3 /4, FONT_NAME, 20, True, WHITE)

def getNextLine(file):
    """Returns the next line in the file.
    
    The cursor will remain where it is when the function is finished."""
    line = file.readline()
    line = line.strip("\n")
    return line

def getHighScores():
    """Displays the high scores listed in scores.txt."""
    file = openScoreFile("r") # Open the file in "read-only" mode
    highScores = []
    # Append each line to highScores
    for i in range(3):
        highScore = getNextLine(file)
        highScore = highScore.rstrip()
        highScores.append(int(highScore))
    # Sorts highScores in descending order
    highScores.sort(reverse = True)
    i = 0
    for score in highScores:
        drawText(screen, str(score), WIDTH/2, HEIGHT*3/4.1 + (i*30), FONT_NAME, 20, True, PINK)
        i += 1
    file.close()
    
def addNewHighScore(newScore):
    """Add a new high score to scores.txt if it is greater than any of the three preexisting values."""
    file = openScoreFile("r+") # Open the file in "read and write" mode
    lines = file.readlines() # Gets all lines in the file as a list
    file.seek(0, 0) # Move the cursor to the beginning to the file
    scoreList = []
    # For each line, clear whitespace and newline characters, convert the value to an integer, and add it to scoreList
    for i in range(len(lines)):
        line = file.readline()
        line = line.rstrip()
        line = int(line)
        scoreList.append(line)
    # Add the new score to scoreList
    scoreList.append(newScore)
    scoreList.sort()
    # If scoreList has more than 3 items in it, remove the first item (which is the lowest value after the list is sorted)
    if len(scoreList) == 4:
        scoreList.pop(0)
    elif len(scoreList) > 4:
        print("What?? That wasn't supposed to happen. :/")
    if scoreList:
        # Clear everything in the file
        file.seek(0, 0)
        file.truncate()
        # Add each high score to the file
        for score in scoreList:
            file.writelines(str(score) + "\n")
    else:
        file.writelines(str(newScore))
    file.close()

def show_go_screen():
    
    screen.blit(background, backgroundRect)
    drawText(screen, gameTitle, WIDTH/2, HEIGHT/4, FONT_NAME, 64, True, WHITE)
    drawText(screen, "Use the arrow keys to move and space to fire.", WIDTH/2, HEIGHT/2, FONT_NAME, 22, True, WHITE)
    drawText(screen, "Press a key to begin", WIDTH/2, HEIGHT* 3 / 5, FONT_NAME, 18, True, WHITE)
    drawText(screen, "High Scores:", WIDTH/2, HEIGHT * 3 / 4.5, FONT_NAME, 20, True, WHITE)
    getHighScores()
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

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

POWER_TIME = 10000

#######################################

# Creating game objects
pygame.init()
pygame.mixer.init()
pygame.display.set_caption(gameTitle)
clock = pygame.time.Clock()

# Set up asset folders
gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder, "img")
sndFolder = os.path.join(gameFolder, "snd")

# Load all game graphics
background = pygame.image.load(os.path.join(imgFolder, "starfield.png")).convert()
backgroundRect = background.get_rect()

# Load all game sounds
shootSound = pygame.mixer.Sound(os.path.join(sndFolder, "Laser_Shoot5.wav"))
powerSound = pygame.mixer.Sound(os.path.join(sndFolder, "Powerup5.wav"))
explSounds = []
for snd in ["Explosion7.wav", "Explosion8.wav"]:
    explSounds.append(pygame.mixer.Sound(os.path.join(sndFolder, snd)))
hurtSound = pygame.mixer.Sound(os.path.join(sndFolder, "Hit_Hurt29.wav"))
# Music
pygame.mixer.music.load(os.path.join(sndFolder, "TimeMachine.ogg"))
pygame.mixer.music.set_volume(0.3)

playerIMG = pygame.image.load(os.path.join(imgFolder, "playerShip.png")).convert()
playerMiniIMG = pygame.transform.scale(playerIMG, (25, 19))
playerMiniIMG.set_colorkey(BLACK)
laserIMG = pygame.image.load(os.path.join(imgFolder, "laser.png")).convert()

mobImages = []
mobList = ["meteorBrown_big1.png", "meteorBrown_med1.png", 
        "meteorBrown_med3.png", "meteorBrown_small1.png", "meteorBrown_small2.png",
        "meteorBrown_tiny1.png"]

explosionAnim = {}
explosionAnim['lg'] = []
explosionAnim['sm'] = []
explosionAnim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join(imgFolder, filename)).convert()
    img.set_colorkey(BLACK)
    imgLG = pygame.transform.scale(img, (75, 75))
    explosionAnim['lg'].append(imgLG)
    imgSM = pygame.transform.scale(img, (32, 32))
    explosionAnim['sm'].append(imgSM)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join(imgFolder, filename)).convert()
    img.set_colorkey(BLACK)
    explosionAnim['player'].append(img)

for img in mobList:
    mobImages.append(pygame.image.load(os.path.join(imgFolder, img)).convert())

powerUpIMG = {}
powerUpIMG["shield"] = pygame.image.load(os.path.join(imgFolder, "shield_gold.png")).convert()
powerUpIMG["gun"] = pygame.image.load(os.path.join(imgFolder, "bolt_gold.png")).convert()

# Start of game loop
running = True
while running:
    if game_over:

        addNewHighScore(score)
        score = 0
        show_go_screen()
        game_over = False

        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerUps = pygame.sprite.Group()

        player = Player()

        for i in range(10):
            newMob()

        # Add sprites to groups
        all_sprites.add(player)

        pygame.mixer.music.play(loops=-1)

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

    # Detect collision between player and mobs
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 1.25
        hurtSound.play()
        newMob()
        if player.shield <= 0:
            deathExpl = Explosion(player.rect.center, "player")
            all_sprites.add(deathExpl)
            player.hide()
            player.lives -= 1
            player.shield = 100

    if (player.lives == 0) and not deathExpl.alive():
        game_over = True

    # Detect collision between bullets and mobs
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    # If mob is destroyed, create a new one
    for hit in hits: # Remove/change if level system desired
        score += hit.points - hit.radius
        random.choice(explSounds).play()
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)
        newMob()
        if random.random() > 0.98:
            powerUp = PowerUp(hit.rect.center)
            all_sprites.add(powerUp)
            powerUps.add(powerUp)

    hits = pygame.sprite.spritecollide(player, powerUps, True)
    for hit in hits:
        if hit.type == "shield":
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == "gun":
            player.powerUp()
        powerSound.play()

#######################################
   # Render (draw)
#######################################

    screen.fill(BLACK)
    screen.blit(background, backgroundRect)
    
    all_sprites.draw(screen)
    drawText(screen, str(score), WIDTH/2, 10, FONT_NAME, 35, True, WHITE)
    drawShieldBar(screen, 5, 5, player.shield, GREEN)
    drawShieldBar(screen, 5, 20, player.fuel, BLUE)
    drawLives(screen, WIDTH-100, 20, player.lives, playerMiniIMG)

    # After drawing everything, flip the display
    # Must be the last call in the draw section
    pygame.display.flip()

#######################################


pygame.quit()
