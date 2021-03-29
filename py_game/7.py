#змейка растет
import pygame
pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

black = (0, 0, 0)
yellow = (255, 255, 0)

x = 50
y = 50
dx = 0
dy = 0
recs_x = [x]
recs_y = [y]

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dx = 0
            dy = -3
            recs_x.append(recs_x[0])
            recs_x.append(y+50)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dx = 0
            dy = 3
            recs_x.append(recs_x[0])
            recs_x.append(y-50)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dx = -3
            dy = 0
            recs_x.append(x-20)
            recs_x.append(y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dx = 3
            dy = 0
            recs_x.append(x+20)
            recs_x.append(y)
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     recs_x.append(x+10)
        #     recs_y.append(10)

    screen.fill(black)

    for i, j in zip(range(len(recs_x)), range(len(recs_y))):
        recs_x[i] += dx
        recs_y[j] += dy

    for i, j in zip(range(len(recs_x)), range(len(recs_y))):
        if recs_x[i] > 700:
            recs_x[i] = 0
        if recs_x[i] < 0:
            recs_x[i] = 700
        if recs_y[j] > 500:
            recs_y[j] = 0
        if recs_y[j] < 0:
            recs_y[j] = 500

    for i, j in zip(range(len(recs_x)), range(len(recs_y))):
        pygame.draw.rect(screen, yellow, [recs_x[i], recs_y[j], 50, 50])
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
