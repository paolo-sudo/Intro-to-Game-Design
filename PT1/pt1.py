# Paolo S.
# CS3-1 | PT1

import pygame
pygame.init()

win = pygame.display.set_mode((900, 400))
pygame.display.set_caption("My Sprite Game")
pygame.display.update()

#To load the source images/sprite. Outside the loop
walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R10.png')]
#load image = pygame.image.load('File location and name ex r1.png')
walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L10.png')] 
#same with walkRight
jumpRight = [pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/J1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/J2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/J3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/J4.png'), pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/J5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/J6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/J7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/J8.png')]
bg = pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/bg.png') #load background
char = pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/standing.png') #steady image ata

# Viking Character - https://www.freepik.com/free-vector/game-character-viking-walk-jump-cycle-sequence_29386716.htm#query=game%20character%20sprite&position=25&from_view=keyword - Image by upklyak on Freepik
# Background - https://www.freepik.com/free-vector/game-character-viking-walk-jump-cycle-sequence_29386716.htm#query=game%20character%20sprite&position=25&from_view=keyword - Image by upklyak on Freepik

x = 50
y = 300
width = 40
height = 60
speed = 5

clock = pygame.time.Clock() #To change the sprite framerate 

#Variables to keep track the way the sprite is facing
left = False
right = False
walk_counter = 0 #character animation

isJump = False
jumpCount = 10

def redrawWindowgame():
    global walk_counter
    win.blit(bg, (0,0)) #draw the background image at 0,0

    if walk_counter + 1 >= 27:
        walk_counter = 0
    if left:
        win.blit(walkLeft[walk_counter//3], (x,y))
        walk_counter += 1
    elif right:
        win.blit(walkRight[walk_counter//3], (x,y))
        walk_counter += 1
    elif isJump:
        win.blit(jumpRight[walk_counter//3], (x,y))
        walk_counter += 1
    else:
        win.blit(char, (x,y))
        walk_counter = 0

    pygame.display.update()

#clock = pygame.time.Clock() #To change the sprite framerate 

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = False
        right = True
    elif keys[pygame.K_RIGHT] and x < 850 - speed - width:
        x += speed
        left = True
        right = False
    else: #if the character is not moving left/right set to false and reset the animation counter
        #left = False
        #right = False
        standing = True
        walk_counter = 0

    #for jumping
    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
            left = False
            right = False
            walk_counter = 0   
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    redrawWindowgame()

pygame.quit()
