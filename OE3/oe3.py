# Paolo S.
# CS3-1 | OE3

import pygame
pygame.init()

game_win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

#variables for coordinates
#x & y: top left corner, x + w: top right corner, x,y + h: bottom left
pygame
#set the row, col
# BOX1 RED
x = 400
y = 400
width = 40
height = 40
speed = 20

# BOX2 YELLOW
x2 = 50
y2 = 400
width2 = 40
height2 = 40
speed2 = 20

#variables to set jump movement 
#RED BOX
isJump = False
jumpCount = 10

#YELLOW
jump = False
jCount = 10

run = True

while run:
    pygame.time.delay(100) #delay the game movement in ms
    
    for event in pygame.event.get(): #loop through a list of any key or mouse event
        if event.type == pygame.QUIT:
            run = False #END THE GAME LOOP

    keys = pygame.key.get_pressed() #list of key to use

#Red Box     
    #to check which key is pressed
    if keys[pygame.K_LEFT] and x > speed: #There is no movement
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - speed - width: #Stop right corner less than the screen width
        x += speed
    
    if not(isJump): #check the user not jumping
        if keys[pygame.K_UP] and y > speed: #same principle apply for the y coordinates
            y -= speed
        if keys[pygame.K_DOWN] and y < 500 - height - speed:
            y += speed

        if keys[pygame.K_SLASH]:
            isJump = True
    else:
        #user is jumping
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
  
#Yellow Box  
    if keys[pygame.K_a] and x2 > speed:
        x2 -= speed
    if keys[pygame.K_d] and x2 < 500 - speed - width:
        x2 += speed
    
    if not(jump):
        if keys[pygame.K_w] and y2 > speed:
            y2 -= speed
        if keys[pygame.K_s] and y2 < 500 - height - speed:
            y2 += speed
        
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        #User is jumping
        if jCount >= -10:
            y2 -= (jCount * abs(jCount)) * 0.5
            jCount -= 1
        else:
            jCount = 10
            jump = False
            
    game_win.fill((0,0,0)) #fill with black
    box1 = pygame.draw.rect(game_win, (255,0,0), (x,y,width,height)) #window surface color and rectangle
    pygame.display.update() #enable to update the screen to the object/rect
         
    box2 = pygame.draw.rect(game_win, (255,255,0), (x2,y2,width2,height2)) #window surface color and rectangle
    pygame.display.update() #enable to update the screen to the object/rect  
    
    pygame.time.delay(100) #delay the game movement in ms  
    
pygame.quit()