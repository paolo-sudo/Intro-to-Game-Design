# Paolo S.
# CS3-1 | PT3

#adding
#Video Reference: https://www.youtube.com/watch?v=JLUqOmE9veI
#Music Reference: https://mixkit.co/free-sound-effects/game/ , https://pixabay.com/sound-effects/search/bullet/?theme=musical
#This is only for school purposes

import pygame
pygame.init()

win = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My Sprite Game")
pygame.display.update()

#To load the source images/sprite. Outside the loop
walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/R10.png')]
walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L9.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/L10.png')]
bg = pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/bg3.png') #load background
char = pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/standing.png') #steady image

#Viking character link https://www.freepik.com/free-vector/game-character-viking-walk-jump-cycle-sequence_29386716.htm#query=game%20character%20sprite&position=25&from_view=keyword
#background link https://cdn.wallpapersafari.com/51/57/uJmAfY.jpg
clock = pygame.time.Clock() #To change the sprite framerate 
FPS = 60
score = 0 #new added variable

#Load the source audio
bulletSound = pygame.mixer.Sound('c:/git/Intro-to-Game-Design/OE7/music/bullet.wav')
hitSound = pygame.mixer.Sound('c:/git/Intro-to-Game-Design/OE7/music/hit.wav')

musicBackground = pygame.mixer.music.load('c:/git/Intro-to-Game-Design/OE7/music/music.mp3')
pygame.mixer.music.play(-1) # -1 keeps the song on loop

#PLAYER CLASS
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
        self.health = 9
        self.visible = True

        self.hitObject = (self.x + 20, self.y + 11, 30, 60) #rectangle

    def draw(self,win):
        if self.visible:
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
            pygame.draw.rect(win, (255,0,0), (self.hitObject[0], self.hitObject[1] - 20, 50, 10)) # red
            pygame.draw.rect(win, (0,128,0), (self.hitObject[0], self.hitObject[1] - 20, 55 - (5 * (10 - self.health)), 10)) #green

            self.hitObject = (self.x + 2, self.y + 1, 80, 85) #added code for hit object = rectangle
            #self.x + 10 = is for box x axis adjustment

            #draw the rectangle around the player
            #pygame.draw.rect(win, (255,0,0), self.hitObject, 2)
    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 50
        self.y = 340
        self.walkCount = 0

        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-2', 1, (255,0,0))
        win.blit(text, (450 -(text.get_width()/2), 150))
        if score <= -8:
            self.visible = False
            text = font.render('You Lose!', 1, (0,0,0)) #new code
            win.blit(text, (380,40)) #new code
            pygame.time.delay(500)
            pygame.quit()
            
        pygame.display.update()
        x = 0
        while x < 50:
            pygame.time.delay(1)
            x += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = 301
                    pygame.quit()

#CLASS for handling player projectile for bullet
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

#ENEMY CLASS
class enemy(object):
    walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER0.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER9.png')]
    walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL0.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL9.png')]
    dead = pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL0.png')
    #2nd character link https://www.gameart2d.com/temple-run---free-sprites.html

    def __init__(self, x,y, width, height, end):
        self.x = 1500
        self.y = 270
        self.width = 20
        self.height = 40
        self.path = [x, end] #where the enemy starts and finish the path
        self.hitObject = (self.x + 17, self.y + 2, 31, 57) #enemy hit object
        self.health = 9
        self.visible = True

        self.walkCounter = 0
        self.speed = 5

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCounter + 1 >= 30: #why 33? 11 images to be animated upper bound (3 frames x 11) = 33
                self.walkCounter = 0
            if self.speed > 0: #Moving the enemy to the right - display walk right images
                win.blit(self.walkRight[self.walkCounter//3], (self.x, self.y))
                self.walkCounter += 1
            else: #moving the enemy walk left
                win.blit(self.walkLeft[self.walkCounter//3], (self.x, self.y))
                self.walkCounter += 1
            pygame.draw.rect(win, (255,0,0), (self.hitObject[0], self.hitObject[1] - 20, 50, 10)) #red
            pygame.draw.rect(win, (0,128,0), (self.hitObject[0], self.hitObject[1] - 20, 55 - (5 * (10 - self.health)), 10)) #green

            self.hitObject = (self.x + 35, self.y + 50, 80, 110)

            #draw rectangle arount the monster/enemy
            #pygame.draw.rect(win, (255,0,0), self.hitObject, 2)

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
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit!") 
        

#SECOND ENEMY CLASS
class enemy2(object):
    walkRight = [pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER0.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/ER9.png')]
    walkLeft = [pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL0.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL1.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL2.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL3.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL4.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL5.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL6.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL7.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL8.png'),pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL9.png')]
    dead = pygame.image.load('c:/git/Intro-to-Game-Design/PT2/images/EL0.png')
    #2nd character link https://www.gameart2d.com/temple-run---free-sprites.html

    def __init__(self, x,y, width, height, end):
        self.x = 1000 #40 0
        self.y = 270
        self.width = 20
        self.height = 40
        self.path = [x, end] #where the enemy starts and finish the path
        self.hitObject = (self.x + 17, self.y + 2, 31, 57) #enemy hit object
        self.health = 9
        self.visible = True

        self.walkCounter = 0
        self.speed = 5

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCounter + 1 >= 30: #why 33? 11 images to be animated upper bound (3 frames x 11) = 33
                self.walkCounter = 0
            if self.speed > 0: #Moving the enemy to the right - display walk right images
                win.blit(self.walkRight[self.walkCounter//3], (self.x, self.y))
                self.walkCounter += 1
            else: #moving the enemy walk left
                win.blit(self.walkLeft[self.walkCounter//3], (self.x, self.y))
                self.walkCounter += 1
            pygame.draw.rect(win, (255,0,0), (self.hitObject[0], self.hitObject[1] - 20, 50, 10)) #red
            pygame.draw.rect(win, (0,128,0), (self.hitObject[0], self.hitObject[1] - 20, 55 - (5 * (10 - self.health)), 10)) #green

            self.hitObject = (self.x + 35, self.y + 50, 80, 110)

            #draw rectangle arount the monster/enemy
            #pygame.draw.rect(win, (255,0,0), self.hitObject, 2)

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
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit!") 

def redrawWindowgame():
    #global walk_counter
    win.blit(bg, (0,0)) #draw the background image at 0,0
    text = font.render('Score: ' + str(score), 1, (0,0,0)) #new code
    win.blit(text, (380,10)) #new code
    if score >= 20:
        text = font.render('You Won!', 1, (0,0,0)) #new code
        win.blit(text, (380,40)) #new code
    #if score <= -1:
        #text = font.render('You Lose!', 1, (0,0,0)) #new code
        #win.blit(text, (380,40)) #new code
        
    play.draw(win)
    monster.draw(win)
    monster2.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


play = player(200, 410, 64, 64) #instance of player class (64 pixels dapat ang size ng character na gagawin)
monster = enemy(50,410,50,10,900) #instance of the enemy
monster2 = enemy2(50,410,50,10,900) #instance of the enemy
#mons = enemy(x,y,width,height,end)
shootLoop = 0
bullets = [] #array that hold the bullet - circle
run = True
font = pygame.font.SysFont('comicsans',20, True)

#MAIN LOOP
while run:
    clock.tick(30)

    if monster.visible == True:
        if play.hitObject[1] < monster.hitObject[1] + monster.hitObject[3] and play.hitObject[1] + play.hitObject[3] > monster.hitObject[1]: #to check x coordinate
            if play.hitObject[0] + play.hitObject[2] > monster.hitObject[0] and play.hitObject[0] < monster.hitObject[0] + monster.hitObject[2]: # to check y coordinate
                hitSound.play()
                play.hit() # hit function call
                score -= 2 #new code

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
                score += 1 #new code
    
                bullets.pop(bullets.index(bullet)) # use/remove bullet from bullet list
    
        if bullet.x < 900 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))
    
    for bullet in bullets:
        if bullet.y - bullet.radius < monster2.hitObject[1] + monster2.hitObject[3] and bullet.y + bullet.radius > monster2.hitObject[1]: #to check x coordinate
            if bullet.x + bullet.radius > monster2.hitObject[0] and bullet.x - bullet.radius < monster2.hitObject[0] + monster2.hitObject[2]: # to check y coordinate
                monster2.hit() # hit function call
                score += 1 #new code
    
                bullets.pop(bullets.index(bullet)) # use/remove bullet from bullet list
    
        if bullet.x < 900 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0: #Shoot bullets
        bulletSound.play()
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
        play.standing = False

    elif keys[pygame.K_RIGHT] and play.x < 850 - play.speed - play.width:
        play.x += play.speed
        play.left = True
        play.right = False
        play.standing = False #added object in the class

    else: #if the character is not moving left/right set to false and reset the animation counter
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
            play.y -= (play.jumpCount ** 2) * 0.5 * neg
            play.jumpCount -= 1
        else:
            play.jumpCount = 10
            play.isJump = False
    redrawWindowgame()

pygame.quit()