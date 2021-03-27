# управляй шариком
import pygame

pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
green = (100, 200, 100)
blue = (0, 0, 255)
white = (255, 255, 255)
colors = [black, red, green, blue]
color = white

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Circle moves")
clock = pygame.time.Clock()
fps = 120

x = 100
y = 100
dx = 0
dy = 0
speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dx = 0
            dy = 1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dx = 0
            dy = -1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dx = 1 * speed
            dy = 0 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dx = -1 * speed
            dy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed += 1
            dx *= speed
            dy *= speed
    screen.fill(black)
    x += dx
    y += dy
        
    if x > 700:
        x = 0
    if x < 0:
        x = 700
    if y > 500:
        y = 0
    if y < 0:
        y = 500

    pygame.draw.ellipse(screen, white, [x, y, 50, 50])

    
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()