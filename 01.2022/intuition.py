import pygame
import random
width = 600
heigth = 600
fps = 30

#Colors: (R, G, B)
black = (0, 0, 0)
red = (255, 0, 0)
green = (100, 200, 100)
blue = (0, 0, 255)
white = (255, 255, 255)

pygame.init()
pygame.mixer.init() #sound
screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("First Page")
clock = pygame.time.Clock()

#Cycle of game
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(black)
    pygame.display.flip()
    #refreshing
    #rendering

pygame.quit()
