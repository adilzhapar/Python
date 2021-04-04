#тут квадратик бьется об стенку и меняет цвет при нажатии на пробел
import pygame
import random
pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
green = (100, 200, 100)
blue = (0, 0, 255)
white = (255, 255, 255)
colors = [black, red, green, blue]
color = white

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Recctangle moves")
clock = pygame.time.Clock()
fps = 60

rect_x = 50
rect_y = 50
x_change = 2
y_change = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.fill(white)
    clock.tick(fps)
    
    rect_x += x_change
    rect_y += y_change

    if rect_x > 650 or rect_x < 0:
        x_change *= -1
        
    if rect_y > 450 or rect_y < 0:
        y_change *= -1
        

    pygame.draw.rect(screen, color, (rect_x, rect_y, 50, 50))
    pygame.draw.rect(screen, red, (rect_x+10, rect_y+10, 30, 30))
    pygame.display.flip()

pygame.quit()