# Paolo S.
# CS3-1 | OE4

#Optimizing the code to OOP and adding projectile - gun with a bullet
#use the arrow key as jump and spacebar for shooting bullet
#also submit this file serately using txt sile or py file

import pygame
pygame.init()

win = pygame.display.set_mode((900, 400))
pygame.display.set_caption("My Sprite Game")
pygame.display.update()

#To load the source images/sprite. Outside the loop
walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R10.png')]
walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L10.png')]
bg = pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/bg.png') #load background
char = pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/standing.png') #steady image

clock = pygame.time.Clock() #To change the sprite framerate 

class player(object):
    def __init__(self, x,y,width,height): 
        self.x = 50
        self.y = 300
        self.width = 40
        self.height = 60
        self.speed = 5

        #Variables to keep track the way the sprite is facing
        self.left = False
        self.right = False
        self.walk_counter = 0 #character animation

        self.isJump = False
        self.jumpCount = 10
        self.standing = True

    def draw(self,win):
        if self.walk_counter + 1 >= 27:
            self.walk_counter = 0
        if self.left:
            win.blit(walkLeft[self.walk_counter//3], (self.x, self.y))
            self.walk_counter += 1
        elif self.right:
            win.blit(walkRight[self.walk_counter//3], (self.x, self.y))
            self.walk_counter += 1
        else:
            win.blit(char, (self.x,self.y))
            self.walk_counter = 0

#new class for handling player projectile for bullet
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing #speed or velocity

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

def redrawWindowgame():
    #global walk_counter
    win.blit(bg, (0,0)) #draw the background image at 0,0
    play.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


play = player(200, 410, 64, 64) #instance of player class (64 pixels dapat ang size ng character na gagawin)
bullets = []
run = True
#main loop
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #to add the projectile class in main loop = player with gun
    for bullet in bullets:
        if bullet.x < 900 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]: #Shoot bullets
        if play.left:
            facing = 1
        else:
            facing = -1

        if len(bullets) < 16:
            bullets.append(projectile(round(play.x + play.width // 2), round(play.y + play.height // 2), 5, (255,255,255), facing))

    if keys[pygame.K_LEFT] and play.x > play.speed:
        play.x -= play.speed
        play.left = False
        play.right = True
        #play.left = True
        #play.right = False
        play.standing = False

    elif keys[pygame.K_RIGHT] and play.x < 850 - play.speed - play.width:
        play.x += play.speed
        play.left = True
        play.right = False
        #play.left = False
        #play.right = True
        play.standing = False #added object in the class

    else: #if the character is not moving left/right set to false and reset the animation counter
        #play.left = False
        #play.right = False
        play.standing = True #remove 2 Lines
        play.walk_counter = 0

    if not(play.isJump):
        if keys[pygame.K_UP]:
            play.isJump = True
            play.left = False
            play.right = False
            play.walk_counter = 0
    else:
        if play.jumpCount >= -10:
            neg = 1
            if play.jumpCount < 0:
                neg = -1
            #play.y -= (play.jumpCount * abs(play.jumpCount)) * 0.5
            play.y -= (play.jumpCount ** 2) * 0.5 * neg
            play.jumpCount -= 1
        else:
            play.jumpCount = 10
            play.isJump = False
    redrawWindowgame()

pygame.quit()
