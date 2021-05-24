import pygame
import time
import sys
import random
import json
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
background = pygame.image.load('back1.png')
pygame.display.set_caption('Jylan, TSIS 9')
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()


class Food:
    def __init__(self):
        test = False
        self.image = pygame.image.load('redstone.png')
        self.surf = pygame.Surface((10, 10))
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
        screen.blit(self.image, (self.x, self.y))


class Jylan:
    def __init__(self, x, y, color):
        self.size = 1
        self.elements = [[x, y]]
        self.dx = 0
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
            self.speed += 1

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
                pygame.mixer.music.stop()
                pygame.mixer.Sound('lose.wav').play()
                time.sleep(2)
                return True

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx == x and foody == y:
            pygame.mixer.Sound('my-man.wav').play()
            return True
        return False

    def crash_wall(self, wallx, wally):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if wallx <= x <= wallx + 60 and wally <= y <= wally + 60:
            pygame.mixer.music.stop()
            pygame.mixer.Sound('lose.wav').play()
            time.sleep(2)
            return True
        return False


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rock = pygame.image.load('wall.png')

    def draw(self):
        # pygame.draw.rect(screen, green, [self.x, self.y, 70, 70])
        screen.blit(self.rock, (self.x, self.y))


def first_win():
    pygame.mixer.Sound('win.wav').play()
    font = pygame.font.SysFont('Verdana', 50, True, True)
    screen.blit(background, (0, 0))
    winner_text = font.render('Player 1 wins!', True, (52, 193, 209))
    screen.blit(winner_text, (200, 200))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def second_win():
    pygame.mixer.Sound('win.wav').play()
    font = pygame.font.SysFont('Verdana', 50, True, True)
    screen.blit(background, (0, 0))
    winner_text = font.render('Player 2 wins!', True, (246, 196, 31))
    screen.blit(winner_text, (200, 200))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def new_record(x):
    pygame.mixer.Sound('my-man.wav').play()
    font = pygame.font.SysFont('Verdana', 50, True, True)
    screen.blit(background, (0, 0))
    winner_text = font.render('New Record: {}!!!'.format(x), True, purple)
    screen.blit(winner_text, (150, 200))
    pygame.display.flip()
    time.sleep(3)


def show_score(first, second, high):
    font = pygame.font.SysFont("Verdana", 15, True, False)
    t1 = font.render('First player: {}'.format(first), True, purple)
    t2 = font.render('Second player: {}'.format(second), True, purple)
    t3 = font.render('High score: {}'.format(high), True, purple)

    screen.blit(t1, (20, 20))
    screen.blit(t2, (20, 40))
    screen.blit(t3, (20, 60))


def save_game():
    x = {
        "jylan": jylan.elements,
        "jylan_dx": jylan.dx,
        "jylan_dy": jylan.dy,
        "snake_dx": snake.dx,
        "snake_dy": snake.dy,
        "snake": snake.elements,
        "food_x": food.x,
        "food_y": food.y,
        "walls_num": len(walls),
        "size_1": jylan.size,
        "size_2": snake.size,
        "speed_1": jylan.speed,
        "speed_2": snake.speed
    }
    y = json.dumps(x)
    with open('save.json', 'w') as f:
        f.write(y)


jylan = Jylan(50, 300, (52, 193, 209))
snake = Jylan(50, 400, (246, 196, 31))
wall_levels = [[180, 50], [180, 500], [550, 50], [550, 500], [365, 265]]
food_borders = [[180, 50], [180, 500], [550, 50], [550, 500], [365, 265]]
food = Food()
walls = []
num_of_walls = 0
level = 10
done = False
d = 10

with open('save.json', 'r') as f:
    try:
        reader = f.read()
        my_json = json.loads(reader)
        jylan.elements = my_json['jylan']
        snake.elements = my_json['snake']
        jylan.dx = my_json['jylan_dx']
        jylan.dy = my_json['jylan_dy']
        snake.dx = my_json['snake_dx']
        snake.dy = my_json['snake_dy']
        food.x = my_json['food_x']
        food.y = my_json['food_y']
        num_of_walls = my_json['walls_num']
        jylan.size = my_json['size_1']
        snake.size = my_json['size_2']
        jylan.speed = my_json['speed_1']
        snake.speed = my_json['speed_2']
    except:
        pass

while not done:
    if jylan.speed >= snake.speed:
        clock.tick(jylan.speed)
    else:
        clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            save_game()
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
            if event.key == K_2:
                snake.is_add = True

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
        jylan.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        food.gen()
    if snake.eat(food.x, food.y):
        snake.is_add = True
        snake.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        food.gen()

    jylan.move()
    snake.move()
    screen.blit(background, (0, 0))
    show_score(jylan.size, snake.size, jylan.highscore)

    jylan.draw()
    snake.draw()
    food.draw()

    if jylan.krendel():
        with open('save.json', 'w') as f:
            f.write('')
        time.sleep(1)
        if jylan.size > jylan.highscore:
            with open('highscore.txt', 'w') as f:
                f.write(str(jylan.size))
            new_record(jylan.size)
        second_win()
    if snake.krendel():
        with open('save.json', 'w') as f:
            f.write('')
        time.sleep(1)
        if snake.size > snake.highscore:
            with open('highscore.txt', 'w') as f:
                f.write(str(snake.size))
            new_record(snake.size)
        first_win()

    while num_of_walls != 0:
        if [wall_levels[0][0], wall_levels[0][1]] not in walls:
            walls.append(Wall(wall_levels[0][0], wall_levels[0][1]))
            wall_levels.pop(0)
        num_of_walls -= 1

    if jylan.size == level or snake.size == level:
        if len(wall_levels) != 0:
            level += 10
            if [wall_levels[0][0], wall_levels[0][1]] not in walls:
                walls.append(Wall(wall_levels[0][0], wall_levels[0][1]))
                wall_levels.pop(0)

    for wall in walls:
        wall.draw()

    for wall in walls:
        if jylan.crash_wall(wall.x, wall.y):
            with open('save.json', 'w') as f:
                f.write('')
            time.sleep(1)
            if jylan.size > jylan.highscore:
                with open('highscore.txt', 'w') as f:
                    f.write(str(jylan.size))
                new_record(jylan.size)
            second_win()

        if snake.crash_wall(wall.x, wall.y):
            with open('save.json', 'w') as f:
                f.write('')
            time.sleep(1)
            if snake.size > snake.highscore:
                with open('highscore.txt', 'w') as f:
                    f.write(str(snake.size))
                new_record(snake.size)
            first_win()

    pygame.display.flip()
pygame.quit()
