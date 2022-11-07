# Paolo S.
# CS3-1 | OE6

#submit this file serately using txt sile or py file

import pygame
pygame.init()

win = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My Sprite Game")
pygame.display.update()

#To load the source images/sprite. Outside the loop
walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/R10.png')]
walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/L10.png')]
bg = pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/bg3.png') #load background
char = pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/standing.png') #steady image

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

        self.hitObject = (self.x + 20, self.y + 11, 30, 60) #rectangle

    def draw(self,win):
        if self.walk_counter + 1 >= 27:
            self.walk_counter = 0
        
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walk_counter//3], (self.x, self.y))
                self.walk_counter += 1
            elif self.right:
                win.blit(walkRight[self.walk_counter//3], (self.x, self.y))
                self.walk_counter += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitObject = (self.x + 2, self.y + 1, 80, 85) #added code for hit object = rectangle
        #self.x + 10 = is for box x axis adjustment

        #draw the rectangle around the player
        pygame.draw.rect(win, (255,0,0), self.hitObject, 2)
        
        #if self.left:
        #    win.blit(walkLeft[self.walk_counter//3], (self.x, self.y))
        #    self.walk_counter += 1
        #elif self.right:
        #    win.blit(walkRight[self.walk_counter//3], (self.x, self.y))
        #    self.walk_counter += 1
        #else:
        #    win.blit(char, (self.x,self.y))
        #    self.walk_counter = 0

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
    walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER0.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/ER9.png')]
    walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL0.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/OE6/images/EL9.png')]
    #2nd character link https://www.gameart2d.com/temple-run---free-sprites.html

    def __init__(self, x,y, width, height, end):
        self.x = 400
        self.y = 270
        self.width = 20
        self.height = 40
        self.path = [x, end] #where the enemy starts and finish the path
        self.hitObject = (self.x + 17, self.y + 2, 31, 57) #enemy hit object

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
        self.hitObject = (self.x + 35, self.y + 50, 80, 110)

        #draw rectangle arount the monster/enemy
        pygame.draw.rect(win, (255,0,0), self.hitObject, 2)

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

    #new function to display when the enemy is hit by the bullet
    def hit(self):
        print("hit!")

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
shootLoop = 0
bullets = [] #array that hold the bullet - circle
run = True
#main loop
while run:
    clock.tick(30)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #to add the projectile class in main loop = player with gun
    for bullet in bullets:
        if bullet.y - bullet.radius < monster.hitObject[1] + monster.hitObject[3] and bullet.y + bullet.radius > monster.hitObject[1]: #to check x coordinate
            if bullet.x + bullet.radius > monster.hitObject[0] and bullet.x - bullet.radius < monster.hitObject[0] + monster.hitObject[2]: # to check y coordinate
                monster.hit() # hit function call
                bullets.pop(bullets.index(bullet)) # use/remove bullet from bullet list

        if bullet.x < 900 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0: #Shoot bullets
        if play.left:
            facing = 1
        else:
            facing = -1

        if len(bullets) < 8:
            bullets.append(projectile(round(play.x + play.width // 2), round(play.y + play.height // 2), 5, (255,255,255), facing))
            shootLoop = 1 # newly added

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