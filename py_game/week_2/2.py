# pressed = pygame.key.get_pressed()
# pressed[pygame.K_UP]

import pygame
pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

done = False
is_blue = True
x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_blue = not is_blue
    screen.fill((0, 0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    elif pressed[pygame.K_DOWN]:
        y += 3
    elif pressed[pygame.K_LEFT]:
        x -= 3
    elif pressed[pygame.K_RIGHT]:
        x += 3

    if is_blue:
        color = (0, 125, 255)
    else:
        color = (255, 100, 0)

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
