import pygame.display
import pygame.draw
import pygame.event
import pygame.time
import pygame.font
import pygame
import random

disWidth = 800
disHeight = 600

pygame.init()
dis=pygame.display.set_mode((disWidth,disHeight))
pygame.display.update()
pygame.display.set_caption('Snake Game')


# color (R,G,B)
snakeColor = (255,255,255)  # White
screenColor = (0,0,0)       # Black
foodColor = (255,0,0)       # Red
textColor = (0,0,255)       # Blue

cellSize = 20
snakeSpeed = 15

clock = pygame.time.Clock()

food_x = 0
food_y = 0

gameOver=False
gameClose = False

def message(msgString,msgColor,location):
    fontStyle = pygame.font.SysFont(None, 50)
    message = fontStyle.render(msgString,True,msgColor)
    dis.blit(message,location)
    pygame.display.update()

def gamePause(): 
    message("Game Paused, Press P to continue",textColor,[100,100])
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_p:
                return
            if event.type == pygame.QUIT:
                global gameOver
                gameOver = True
                return
            
def checkSnakeHead(snakeList,snakeHead):
    for x in snakeList[:-1]:
            if x == snakeHead:
                return True
    return False

def generateFood():
    global food_x
    global food_y
    food_x = cellSize*random.randint(1,(disWidth-cellSize)/cellSize)
    food_y = cellSize*random.randint(1,(disHeight-cellSize)/cellSize)
    pygame.draw.rect(dis,foodColor,[food_x,food_y,cellSize,cellSize])
    pygame.display.update()

def move(snakeList):
        for x,y in snakeList:
            pygame.draw.rect(dis, snakeColor, [x, y, cellSize, cellSize])

def gameloop():
    global gameOver
    global gameClose

    x = disWidth/2
    y = disHeight/2
    mov_x=0
    mov_y=0
    if not gameOver :generateFood()

    snakeList = []
    snakeLength = 1
    while not gameOver:
        while gameClose == True:
            # Display Message
            dis.fill(screenColor)
            message('Game Over! Press R to Restart',textColor,[disWidth/2-300,disHeight/2-50])
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    gameOver = True
                    gameloop()
                if event.type == pygame.KEYUP and event.key == pygame.K_r:
                    gameClose = False
                    gameloop()      
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameOver=True
            if event.type == pygame.KEYUP and event.key == pygame.K_p:
                gamePause()
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    mov_x = 0
                    mov_y = -cellSize
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    mov_x = 0
                    mov_y = cellSize
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    mov_x = -cellSize
                    mov_y = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    mov_x = cellSize
                    mov_y = 0
        x+=mov_x
        y+=mov_y
        x%=800
        y%=600
        dis.fill(screenColor)
        pygame.draw.rect(dis, foodColor, [food_x, food_y, cellSize, cellSize])
        
        
        snakeList.append([x,y])
        if len(snakeList) > snakeLength:
            del snakeList[0]

        
        if checkSnakeHead(snakeList,[x,y]):
            gameClose =True

        move(snakeList)
        pygame.display.update()
    

        # Checks if food eaten
        if x==food_x and y==food_y: 
            generateFood()
            snakeLength += 1
        clock.tick(snakeSpeed)
    pygame.quit()
    quit()


gameloop()