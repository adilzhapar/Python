import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
surf = pygame.Surface((300, 300))
surf.fill((255, 255, 255))
pygame.display.set_caption("Moving of circles")
clock = pygame.time.Clock()

image = pygame.image.load('wb.jpg')

red = (255, 0, 0)
white = (255, 255, 255)
lils = []
x = 60
y = 90
dy = 2
dx = 2


def circles():
    global x, dx, dy, y
    pygame.draw.circle(surf, red, (150, 150), 100)
    pygame.draw.circle(surf, white, (x, 150), 10)
    pygame.draw.circle(surf, white, (150, y), 10)
    x += dx
    y += dy
    if x > 240 or x < 60:
        dx *= -1
    if y > 240 or y < 60:
        dy *= -1


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image, (0, 0))

    circles()

    screen.blit(surf, (250, 150))
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
