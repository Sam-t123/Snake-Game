import pygame

pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Snake game')
game_over=False
# color (R,G,B)
snakeColor = (255,255,255)  # White
screenColor = (0,0,0)       # Black


x = 400
y = 300

delx=0
dely=0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dely = -10
            if event.key == pygame.K_DOWN:
                dely = 10
            if event.key == pygame.K_LEFT:
                delx = -10
            if event.key == pygame.K_RIGHT:
                delx = 10
    x += delx
    y += dely
    dis.fill(screenColor)
    pygame.draw.rect(dis,snakeColor,[x,y,10,10])
    pygame.display.update()
    clock.tick(30)
        
pygame.quit()
quit()

