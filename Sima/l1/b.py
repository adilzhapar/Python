import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learning pygame")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, [250, 250, 100, 100], 2) # where to draw?, which color?, [x, y, width, height], border-radius
    pygame.draw.circle(screen, GREEN, [300, 100], 25)

    for i in range(10, 100, 10):
        pygame.draw.aaline(screen, BLUE, [10, i], [50, i], 2)

    

    pygame.display.flip()
pygame.quit()