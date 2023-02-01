import pygame
import random
import math
#screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
#background
background = pygame.image.load('background.png')
#caption and icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load('galaxy.png')
pygame.display.set_icon(icon)

#player
playerimage =pygame.image.load('ufo.png')
playerx = 370
playery = 480
playerx_change = 0
playery_change = 0

#enemy
enemyimage =[]
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
  enemyimage.append(pygame.image.load('alien.png'))
  enemyx.append(random.randint(0,736))
  enemyy.append(random.randint(50,150))
  enemyx_change.append (4)
  enemyy_change.append (40)

#bullet
# ready - you cant see the bullet on the screen
# fire - the bullet is currently moving

bulletimage =pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "ready"


score = 0

def player(x,y):
    screen.blit(playerimage, (x, y))

def enemy(x,y,i):
    screen.blit(enemyimage[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimage, (x +16 , y+10))

def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx-bulletx,2))+( math.pow(enemyy-bullety,2)))
    if distance < 27 :
        return True
    else:
        return False

running = True

while running:
    # red-green-blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                    playerx_change = -5
            if event.key == pygame.K_RIGHT:
                    playerx_change = +5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletx = playerx
                    fire_bullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0



    #if keystroke is pressed check if its right or left
    #bounderes
    playerx += playerx_change
    if playerx <=0:
        playerx = 0
    elif playerx >=736:
        playerx = 736

    for i in range(num_of_enemies):
      enemyx[i] += enemyx_change[i]
      if enemyx[i] <= 0:
        enemyx_change[i] = 4
        enemyy[i] += enemyy_change[i]
      elif enemyx[i] >= 736:
        enemyx_change[i] = -4
        enemyy[i] += enemyy_change[i]

      # collision
      collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
      if collision:
            bullety = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)
      enemy(enemyx[i], enemyy[i],i)

    # bullet movement
    if bullety <= 0 :
        bullety = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change

    player(playerx,playery)

    pygame.display.update()



