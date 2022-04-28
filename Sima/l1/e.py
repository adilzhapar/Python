import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD")
clock = pygame.time.Clock()
pygame.mixer.music.load('Ric Flair Scrip.mp3')
pygame.mixer.music.play(-1)
background = pygame.image.load("back.png")


running = True
x = WIDTH // 2
y = HEIGHT // 2
color = RED
dx = 2
dy = 2

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))

    font = pygame.font.SysFont('Verdana', 58, True, True) # Bold, Italic
    text = font.render("DVD", True, BLACK) # True - сглаживание

    pygame.draw.ellipse(screen, color, (x, y, 180, 70))
    screen.blit(text, (x + 22, y - 3))

    x += dx
    y += dy

    if x >= WIDTH - 180 or x <= 0:
        dx *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if y >= HEIGHT - 70 or y <= 0:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        dy *= -1    

    

    pygame.display.flip()
pygame.quit()