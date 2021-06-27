import pygame.display
import pygame.draw
import pygame.event
import pygame.time
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
foodColor=(255,0,0)         # Red

cellSize = 20
snakeSpeed = 15

clock = pygame.time.Clock()

food_x = cellSize*random.randint(0,disWidth/cellSize)
food_y = cellSize*random.randint(0,disHeight/cellSize)
def move(x,y,mov_x,mov_y):
        mov_x/=cellSize
        mov_y/=cellSize
        for i in range(cellSize):
            x+=mov_x
            y+=mov_y
            dis.fill(screenColor)
            pygame.draw.rect(dis,foodColor,[food_x,food_y,cellSize,cellSize])
            pygame.draw.rect(dis,snakeColor,[x,y,cellSize,cellSize])
            pygame.display.update()
            clock.tick(10*snakeSpeed)

def gameloop():    
    game_over=False
    x = disWidth/2
    y = disHeight/2

    mov_x=0
    mov_y=0


    

    while not game_over:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: # Pause
                    mov_x = 0
                    mov_y = 0
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

        move(x,y,mov_x,mov_y)
        x+=mov_x
        y+=mov_y
        x%=800
        y%=600
        if x==food_x and y==food_y: print('Tasty') 
            
    pygame.quit()
    quit()


gameloop()