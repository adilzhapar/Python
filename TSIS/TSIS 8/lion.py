import pygame
import sys
import random
import time
from pygame.constants import *

# Variables
width = 800
height = 600
speed = 25
score = 0
fps = 30

# Colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Initialization
pygame.init()
background = pygame.image.load('back_adil.jpg')
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hungry Lion')
clock = pygame.time.Clock()
pygame.mixer.music.load('sound_adil.mp3')
pygame.mixer.music.play(-1)


class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 0, 255))
        self.image = self.surf
        self.rect = self.surf.get_rect(center=(380, 570))

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 0, 0))
        self.image = self.surf
        self.rect = self.surf.get_rect(center=
                                       (random.randint(20, width-150), random.randint(20, height-20)))

    def move(self):
        global score
        self.rect.move_ip(0, 5)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(20, width-20), 0)


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 255, 0))
        self.image = self.surf
        self.rect = self.surf.get_rect(center=
                                       (random.randint(20, width-20), random.randint(20, height-20)))

    def move(self):
        global score
        self.rect.move_ip(0, -5)
        if self.rect.top <= 0:
            self.rect.bottom = 600
            self.rect.center = (random.randint(20, width-20), 600)


def game_over():
    pygame.mixer.music.stop()
    over = pygame.image.load('go_adil.png')
    screen.blit(over, (0, 0))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()


# Sprites:
p1 = PLayer()
enemy_list = [Enemy() for i in range(20)]
food_list = [Food() for j in range(10)]

enemies_sprite = pygame.sprite.Group()
food_sprite = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)

for i in enemy_list:
    enemies_sprite.add(i)
    all_sprites.add(i)
for i in food_list:
    food_sprite.add(i)
    all_sprites.add(i)


# Main part:
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_1:
                score += 1
    screen.blit(background, (0, 0))

    font = pygame.font.SysFont('Times New Roman', 35)
    scores = font.render(str(score), True, white)
    screen.blit(scores, (10, 10))

    for sp in all_sprites:
        screen.blit(sp.image, sp.rect)
        sp.move()

    for e in enemies_sprite:
        if pygame.sprite.collide_rect(p1, e):
            if score != 0:
                score -= 1
                e.kill()
                m = Enemy()
                enemies_sprite.add(m)
                all_sprites.add(m)
                pygame.display.update()
            else:
                game_over()

    for f in food_sprite:
        if pygame.sprite.collide_rect(p1, f):
            score += 1
            f.kill()
            x = Food()
            food_sprite.add(x)
            all_sprites.add(x)
            pygame.display.update()

    pygame.display.update()
    clock.tick(fps)










