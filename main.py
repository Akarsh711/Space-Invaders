# Spacd Invader
import pygame
import random
import math
pygame.init()

# create the screen
# Width, Height
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


score = 0
# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
def player(x, y):
    # To Draw on surface
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY =random.randint(50, 150)
enemyX_change = 3
enemyY_change = 40
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY =480
bulletX_change = 0.3
bulletY_change = 10
bullet_state = 'ready'
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


# Collison
def isCollison(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY,2))
    if distance < 64:
        return True
    else:
        return False
# Game loop
running = True
while running:
    # Background
    # RGB 
    screen.fill((255, 0, 0))
    screen.blit(background, (0,0))

    # playerX+=0.1
    # Event for close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 3
                print("Left arrow is pressed")
        
            if event.key == pygame.K_RIGHT:
                playerX_change += 3
                print("Right arrow is pressed")

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("KeyStroke has been released")
    
    playerX += playerX_change
    # so that player can't go out of screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    enemyX += enemyX_change 
    if enemyX <= 0:
        enemyX_change = 3
        enemyY +=enemyY_change
    elif enemyX >= 736:
        enemyX_change = 3
        enemyY +=enemyY_change
        enemyX_change = -3

    # Bullet Movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -=bulletY_change


    # Collision
    collision = isCollison(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score+=1
        enemyX = random.randint(0, 800)
        enemyY =random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
