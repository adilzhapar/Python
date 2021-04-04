#появление шариков
import pygame as pp
import random
pp.init()
screen = pp.display.set_mode((700, 500))
clock = pp.time.Clock()

running = True
x = random.randint(50, 650)
y = random.randint(50, 450)
dx = 1
dy = 1
circles_x = [x]
circles_y = [y]

black = (0, 0, 0)
white = (255, 255, 255)


while running:
    for event in pp.event.get():
        if event.type == pp.QUIT:
            running = False
        if event.type == pp.KEYDOWN and event.key == pp.K_DOWN:
            dy = 1
            dx = 0
        if event.type == pp.KEYDOWN and event.key == pp.K_UP:
            dy = -1
            dx = 0
        if event.type == pp.KEYDOWN and event.key == pp.K_RIGHT:
            dy = 0
            dx = 1
        if event.type == pp.KEYDOWN and event.key == pp.K_LEFT:
            dy = 0
            dx = -1
        if event.type == pp.KEYDOWN and event.key == pp.K_SPACE:
            circles_x.append(random.randint(0, 255))
            circles_y.append(random.randint(0, 255))
    screen.fill(black)

    for i, j in zip(range(len(circles_x)), range(len(circles_y))):
        circles_x[i] += dx
        circles_y[j] += dy

    for i, j in zip(circles_x, circles_y):
        if i > 670 or i < 0:
            dx *= -1
        if j > 470 or j < 0:
            dy *= -1

    for i, j in zip(range(len(circles_x)), range(len(circles_y))):
        pp.draw.circle(screen, white, (circles_x[i], circles_y[j]), 30)
    clock.tick(60)
    pp.display.update()
pp.quit()
