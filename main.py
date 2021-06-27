import pygame.display
import pygame.draw
import pygame.event
import pygame.time
import pygame
import random

pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Snake game')
game_over=False
# color (R,G,B)
snakeColor = (255,255,255)  # White
screenColor = (0,0,0)       # Black
foodColor=(255,0,0)         # Red

cellSize = 10
snakeSpeed = 15

food_x = 10*random.randint(0,80)
food_y = 10*random.randint(0,60)
x = 400
y = 300

mov_x=0
mov_y=0
clock = pygame.time.Clock()


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

while not game_over:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            game_over=True
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
    # x += mov_x
    # y += mov_y
    
    move(x,y,mov_x,mov_y)
    x+=mov_x
    y+=mov_y
    x%=800
    y%=600
    # dis.fill(screenColor)
    # pygame.draw.rect(dis,snakeColor,[x,y,10,10])
    # pygame.draw.rect(dis,foodColor,[food_x,food_y,10,10])
    # pygame.display.update()
    # clock.tick(snakeSpeed)
        
pygame.quit()
quit()

