import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learning pygame")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)

    for i in range(0, WIDTH, 15):
        if i == 720:
            pygame.draw.aaline(screen, RED, (i, 0), (i, HEIGHT), 1)
        else: pygame.draw.aaline(screen, BLACK, (i, 0), (i, HEIGHT), 1)
    
    for i in range(0, HEIGHT, 15):
        pygame.draw.aaline(screen, BLACK, (0, i), (WIDTH, i), 1)


    

    pygame.display.flip()
pygame.quit()