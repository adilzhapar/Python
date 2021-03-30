import pygame
from math import sin, cos, radians, pi

pygame.init()
wn = pygame.display.set_mode((800, 600))

r = 100
a1 = 100
b1 = 200
a2 = 300
b2 = 200
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # for i in range(1, 181):
    #     pygame.draw.line(wn, (255, 255, 255), [int(r * cos(radians(i)) + a1), int(r * sin(radians(i)) + b1)], [int(r * cos(radians(i)) + a1), int(r * sin(radians(i)) + b1)], 2)
    # for i in range(180, 361):
    #     pygame.draw.line(wn, (255, 255, 255), [int(r * cos(radians(i)) + a2), int(r * sin(radians(i)) + b2)], [int(r * cos(radians(i)) + a2), int(r * sin(radians(i)) + b2)], 2)
    for x in range(100, 700):
        cos_y1 = 240 * cos((x-100) / 150 * pi)
        cos_y2 = 240 * cos((x-99) / 150 * pi)
        pygame.draw.aalines(wn, (0, 0, 255), False, [(x, 300 + cos_y1), ((x+1), 300 + cos_y2)])
    pygame.display.update()
pygame.quit()