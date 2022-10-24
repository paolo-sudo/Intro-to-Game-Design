# Paolo S.
# CS3-1 | OE5

#submit this file serately using txt sile or py file

import pygame
pygame.init()

win = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My Sprite Game")
pygame.display.update()

#To load the source images/sprite. Outside the loop
walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/R10.png')]
walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/L10.png')]
bg = pygame.image.load('c:/git/Intro-to-Game-Design/OE5/bg3.png') #load background
char = pygame.image.load('c:/git/Intro-to-Game-Design/PT1/images/standing.png') #steady image

#Viking character link https://www.freepik.com/free-vector/game-character-viking-walk-jump-cycle-sequence_29386716.htm#query=game%20character%20sprite&position=25&from_view=keyword
#background link https://cdn.wallpapersafari.com/51/57/uJmAfY.jpg
clock = pygame.time.Clock() #To change the sprite framerate 
FPS = 60

class player(object):
    def __init__(self, x,y,width,height): 
        self.x = 50
        self.y = 340
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

#new class for enemy
class enemy(object):
    walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER0.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/ER9.png')]
    walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL0.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE5/EL9.png')]
    #2nd character link https://www.gameart2d.com/temple-run---free-sprites.html

    def __init__(self, x,y, width, height, end):
        self.x = 400
        self.y = 270
        self.width = 20
        self.height = 40
        self.path = [x, end] #where the enemy starts and finish the path

        self.walkCounter = 0
        self.speed = 5

    def draw(self, win):
        self.move()
        if self.walkCounter + 1 >= 30: #why 33? 11 images to be animated upper bound (3 frames x 11) = 33
            self.walkCounter = 0
        if self.speed > 0: #Moving the enemy to the right - display walk right images
            win.blit(self.walkRight[self.walkCounter//3], (self.x, self.y))
            self.walkCounter += 1
        else: #moving the enemy walk left
            win.blit(self.walkLeft[self.walkCounter//3], (self.x, self.y))
            self.walkCounter += 1

    def move(self):
        if self.speed > 0: #moving right
            if self.x < self.path[1] + self.speed: #if not yet reach the farthest right point
                self.x += self.speed
            else: #Change direction and move back
                self.speed = self.speed * -1
                self.x += self.speed
                self.walkCounter = 0
        else: #Moving left
            if self.x > self.path[0] - self.speed: #if not yet reach the farthest left point
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.x += self.speed
                self.walkCounter = 0

def redrawWindowgame():
    #global walk_counter
    win.blit(bg, (0,0)) #draw the background image at 0,0
    play.draw(win)
    monster.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


play = player(200, 410, 64, 64) #instance of player class (64 pixels dapat ang size ng character na gagawin)
monster = enemy(50,410,50,10,700) #instance of the enemy
#mons = enemy(x,y,width,height,end)
bullets = [] #array that hold the bullet - circle
run = True
#main loop
while run:
    clock.tick(30)

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