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

food_x = 10*random.randint(0,80)
food_y = 10*random.randint(0,60)
x = 400
y = 300

mov_x=0
mov_y=0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mov_x = 0
                mov_y = -10
            if event.key == pygame.K_DOWN:
                mov_x = 0
                mov_y = 10
            if event.key == pygame.K_LEFT:
                mov_x = -10
                mov_y = 0
            if event.key == pygame.K_RIGHT:
                mov_x = 10
                mov_y = 0
    x += mov_x
    y += mov_y
    dis.fill(screenColor)
    pygame.draw.rect(dis,snakeColor,[x,y,10,10])
    pygame.draw.rect(dis,foodColor,[food_x,food_y,10,10])
    pygame.display.update()
    clock.tick(30)
        
pygame.quit()
quit()

