from random import randint
import pygame
pygame.init()
# двухэтажный Surface

screen = pygame.display.set_mode((400, 400))

flour_1 = pygame.Surface((400, 200))
flour_1.fill((0, 255, 0))

xb = 0
yb = 100

flour_2 = pygame.Surface((100, 100))
flour_2.fill((255, 0, 0))

x = 0
y = 50

flour_1.blit(flour_2, (x, y))
screen.blit(flour_1, (xb, yb))

pygame.display.update()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            yb = randint(0, 200)

    if x < 400:
        x += 2
    else:
        x = 0
    screen.fill((0, 0, 0))
    flour_1.fill((0, 255, 0))
    flour_1.blit(flour_2, (x, y))
    screen.blit(flour_1, (xb, yb))
    pygame.display.flip()

    pygame.time.delay(30)
pygame.quit()