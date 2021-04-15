import pygame
import time
import sys
import random
from pygame.constants import *

width = 800
height = 600
fps = 30
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (83, 28, 232)
black = (10, 10, 10)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jylan, TSIS 9')
clock = pygame.time.Clock()


class Food:
    def __init__(self):
        test = False
        while 1:
            self.x = random.randint(1, 79) * 10
            self.y = random.randint(1, 59) * 10
            for bord in food_borders:
                if bord[0] <= self.x <= bord[0] + 60 and bord[1] <= self.y <= bord[1] + 60:
                    test = False
                    break
                else:
                    test = True
            if test:
                break

    def gen(self):
        test = False
        while 1:
            self.x = random.randint(1, 79) * 10
            self.y = random.randint(1, 59) * 10
            for bord in food_borders:
                if bord[0] <= self.x <= bord[0] + 60 and bord[1] <= self.y <= bord[1] + 60:
                    test = False
                    break
                else:
                    test = True
            if test:
                break

    def draw(self):
        pygame.draw.rect(screen, purple, [self.x, self.y, 10, 10])


class Jylan:
    def __init__(self, x, y, color):
        self.size = 1
        self.elements = [[x, y]]
        self.dx = 10
        self.dy = 0
        self.is_add = False
        self.speed = 20
        self.color = color
        self.load_highscore()

    def load_highscore(self):
        with open('highscore.txt', 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def draw(self):
        for elem in self.elements:
            pygame.draw.rect(screen, self.color, [elem[0], elem[1], 10, 10])

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 5 == 0:
            self.speed += 2

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

        if self.elements[0][0] > 800:
            self.elements[0][0] = 0
        if self.elements[0][0] < 0:
            self.elements[0][0] = 800
        if self.elements[0][1] > 600:
            self.elements[0][1] = 0
        if self.elements[0][1] < 0:
            self.elements[0][1] = 600

    def krendel(self):
        x = self.elements[0][0]
        y = self.elements[0][1]
        for i in range(1, self.size):
            if self.elements[i][0] == x and self.elements[i][1] == y:
                time.sleep(2)
                self.game_over()

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx == x and foody == y:
            return True
        return False

    def crash_wall(self, wallx, wally):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if wallx <= x <= wallx + 60 and wally <= y <= wally + 60:
            return True
        return False

    def game_over(self):
        go_font = pygame.font.SysFont('Verdana', 50, True, False)
        lil_font = pygame.font.SysFont('Verdana', 30, True, False)
        go_text = go_font.render('Game Over', True, black)

        if self.size > self.highscore:
            # Написать: Новый рекорд!
            with open('highscore.txt', 'w') as f:
                f.write(str(self.size))

        go_score = lil_font.render('Score: {}'.format(self.size), True, black)
        screen.fill(red)
        screen.blit(go_text, (260, 120))
        screen.blit(go_score, (270, 180))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, green, [self.x, self.y, 70, 70])


jylan = Jylan(50, 300, red)
snake = Jylan(50, 400, blue)
wall_levels = [[180, 50], [180, 500], [550, 50], [550, 500], [365, 265]]
food_borders = [[180, 50], [180, 500], [550, 50], [550, 500], [365, 265]]
food = Food()
walls = []
level = 10
done = False
d = 10

while not done:
    clock.tick(jylan.speed)
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
            if event.key == K_RIGHT:
                if jylan.dx != -d:
                    jylan.dx = d
                    jylan.dy = 0
            if event.key == K_LEFT:
                if jylan.dx != d:
                    jylan.dx = -d
                    jylan.dy = 0
            if event.key == K_UP:
                if jylan.dy != d:
                    jylan.dx = 0
                    jylan.dy = -d
            if event.key == K_DOWN:
                if jylan.dy != -d:
                    jylan.dx = 0
                    jylan.dy = d
            if event.key == K_1:
                jylan.is_add = True

            if event.key == K_d:
                if snake.dx != -d:
                    snake.dx = d
                    snake.dy = 0
            if event.key == K_a:
                if snake.dx != d:
                    snake.dx = -d
                    snake.dy = 0
            if event.key == K_w:
                if snake.dy != d:
                    snake.dx = 0
                    snake.dy = -d
            if event.key == K_s:
                if snake.dy != -d:
                    snake.dx = 0
                    snake.dy = d

    if jylan.eat(food.x, food.y):
        jylan.is_add = True
        food.gen()
    if snake.eat(food.x, food.y):
        snake.is_add = True
        food.gen()

    jylan.move()
    snake.move()
    screen.fill(black)
    jylan.krendel()
    snake.krendel()
    jylan.draw()
    snake.draw()
    food.draw()

    if jylan.size == level:
        if len(wall_levels) != 0:
            level += 10
            if [wall_levels[0][0], wall_levels[0][1]] not in walls:
                walls.append(Wall(wall_levels[0][0], wall_levels[0][1]))
                wall_levels.pop(0)

    if snake.size == level:
        if len(wall_levels) != 0:
            level += 10
            if [wall_levels[0][0], wall_levels[0][1]] not in walls:
                walls.append(Wall(wall_levels[0][0], wall_levels[0][1]))
                wall_levels.pop(0)

    for wall in walls:
        wall.draw()
    for wall in walls:
        if jylan.crash_wall(wall.x, wall.y):
            time.sleep(1)
            jylan.game_over()
        if snake.crash_wall(wall.x, wall.y):
            time.sleep(1)
            snake.game_over()

    pygame.display.flip()
pygame.quit()
