# zombie mob game
import itertools, sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *

def calc_velocity(direction, vel=1.0):
    velocity = Point(0,0)
    if direction == 0: #north
        velocity.y = -vel
    elif direction == 2: #east
        velocity.x = vel
    elif direction == 4: #south
        velocity.y = vel
    elif direction == 6: #west
        velocity.x = -vel
    return velocity

def reverse_direction(sprite):
    if sprite.direction ==0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

#THINGS ARE GOING DOWN NOW
pygame,init()
screen = pygame,display.set_mode((1280,720))
pygame.display.set_caption("Collision Demo")
font = pygame.font.Font(None, 36)
timer = pygame.time.Clock()

#creatin' sprite groups
player_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
health_group = pygame.sprite.Group()

#make the player sprite
player = MySprite()
play.load("farmer walk.png", 96, 96, 8)
player.position = 80, 80
player.direction = 4
player_group.add(player)

#create zombie sprite
zombie_image = pygame.image.load("zombie walk.png").convert_alpha()
for n in range(0, 10):
    zombie = MySprite()
    zombie.load("zombie walk.png", 96, 96, 8)
    zombie.position = random.randint(0,700), random.randit(0,500)
    zombie.direction = random.randit(0,3) * 2
    zombie_group.add(zombie)

#creat health sprite
health = MySprite()
health.load("health.png", 32, 32, 1)
health.position = 400,300
health_group.add(health)

game_over = False
player_moving = False
player_health = 100

#repeating loop mah bro
while true:
    timer.tick(30)
    ticks = pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == OUT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    elif keys[K_UP] or keys[K_w]:
        player.direction = 0
        player_moving = True
    elif keys[K_RIGHT] or keys[K_d]:
        player.direction = 2
        player_moving = True
    elif keys[K_DOWN] or keys[K_s]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT] or keys[K_a]:
        player.direction = 6
        player_moving = True
    else:
        player_moving = False

#things that shouldn't happen when game ends
if not game_over:
    #set animation frames based on player's direction
    player.first_frame = player.direction * player.columns
    player.last_frame = player.first_frame + player.columns-1
    if player.frame < player.first_frame:
        player.frame = player.first_frame

    if not player_moving:
        #stop animation when the player is not pressing a key
        player.frame = player.first_frame = player.last_frame
    else:
        #move player in that direction
        player.velocity = calc_velocity(player.direction, 1.5)
        player.velocity.x *= 1.5
        player.velocity.y *= 1.5

#update the player sprite homie
player_group.update(ticks, 50)

#manually move the player nerd
if player_moving:
    player.X += player.velocity.x
    player.Y += player.velocity.y
    if player.X < 0: player.X = 0
    elif player.X > 700: player.X = 700
    if player.Y < 0: player.Y = 0
    elif player.Y > 500: player.Y = 500

#update zombie sprite
zombie_group.update(ticks, 50)

#manually iterate through all the zombies
for z in zombie_group:
    #set the sombies animation range
    z.first_frame = z.direction * z.columns
    z.last_frame = z.first_frame * z.columns-1
    if z.frame < z.first_frame:
        z.frame = z.first_frame
        z.velocity = calc_velocity(z.direction)

#keep the zombie on the screen
z.X += z.velocity.x
z.Y += z.velocity.y
if z.X < 0 or z.X > 700 or z.Y < 0 or z.Y > 500:
    reverse_direction(z)


#check for collision with zombies
attacker = None
attacker = pygame.sprite.spritecollideany(player, zombie_group)
if attacker != None:
    #we got hit, do precise check
    if pygame.sprite.collide_rect_ratio(0,5)(player,attacker):
        player_health -= 10
        if attacker.X < player.X:
            attacker.X -= 10
        elif attacker.X > player.X:
            attacker.X += 10

    else:
        attacker = None

#update the health drop
health_group.update(ticks, 50)

#check for collision
if pygame.sprite.collide_rect_ratio(0,5)(player,health):
    player_health += 30

