import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (83, 28, 232)


class Food:
    def __init__(self):
        self.x = random.randrange(1, int(800 / 10)) * 10
        self.y = random.randrange(1, int(600 / 10)) * 10

    def gen(self):
        self.x = random.randint(1, int(800/10)) * 10
        self.y = random.randint(1, int(600/10)) * 10

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))


class Snake:
    def __init__(self, x, y, color):
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 10
        self.dx = 10
        self.dy = 0
        self.is_add = False
        self.speed = 20
        self.color = color

    def draw(self):
        for elem in self.elements:
            pygame.draw.rect(screen, self.color, [elem[0], elem[1], 10, 10])

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 7 == 0:
            self.speed += 2

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

        if self.elements[0][0] > 800:  # that's mine
            self.elements[0][0] = 0
        if self.elements[0][0] < 0:
            self.elements[0][0] = 800
        if self.elements[0][1] > 600:
            self.elements[0][1] = 0
        if self.elements[0][1] < 0:
            self.elements[0][1] = 600

    def krendel(self):  # that's mine
        for elem in self.elements[1:]:
            if elem[0] == self.elements[0][0] and elem[1] == self.elements[0][1]:
                sys.exit()

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx == x and foody == y:
            return True
        return False


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 5
        self.dy = 5

    def draw(self):
        pygame.draw.rect(screen, (100, 100, 100), [self.x, self.y, 400, 20])

    def move(self):
        self.x += self.dx
        self.y += self.dy


snake = Snake(100, 100, red)
food = Food()
running = True

d = 10
fps = 30

while running:
    clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                if snake.dx != -d:
                    snake.dx = d
                    snake.dy = 0
            if event.key == pygame.K_LEFT:
                if snake.dx != d:
                    snake.dx = -d
                    snake.dy = 0
            if event.key == pygame.K_DOWN:
                if snake.dy != -d:
                    snake.dx = 0
                    snake.dy = d
            if event.key == pygame.K_UP:
                if snake.dy != d:
                    snake.dx = 0
                    snake.dy = -d
            if event.key == pygame.K_1:
                snake.is_add = True

            if event.key == pygame.K_d and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d

    if snake.eat(food.x, food.y):
        snake.is_add = True
        food.gen()

    snake.move()
    screen.fill((10, 10, 10))
    snake.krendel()
    snake.draw()
    food.draw()

    pygame.display.flip()
pygame.quit()

