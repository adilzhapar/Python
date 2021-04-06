import pygame, sys
import random, time
from pygame.constants import *

pygame.init()

fps = 60
clock = pygame.time.Clock()

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

width = 400
height = 600
speed = random.randint(1, 5)
score = 0
coins_sum = 0

font = pygame.font.SysFont('Verdana', 60)
lil_font = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game Over', True, black)

background = pygame.image.load('AnimatedStreet.png')

screen = pygame.display.set_mode((400, 600))
screen.fill(white)
pygame.display.set_caption('Race')
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center=
                                       (random.randint(40, width-40), 0))

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width-40), 0)


class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.png')
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(160, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(center=((random.randint(50, width-50), 0)))

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)


p1 = PLayer()
e1 = Enemy()
c1 = Coins()

enemies = pygame.sprite.Group()
enemies.add(e1)
coins = pygame.sprite.Group()
coins.add(c1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
all_sprites.add(c1)

# inc_speed = pygame.USEREVENT + 1
# pygame.time.set_timer(inc_speed, 1000)

while 1:
    for event in pygame.event.get():
        # if event.type == inc_speed:
        #     speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    speed = random.randint(1, 10)
    game_score = lil_font.render('Score: ' + str(score), True, black)
    game_coin = lil_font.render('Coins: ' + str(coins_sum), True, black)
    screen.blit(background, (0, 0))
    scores = lil_font.render(str(score), True, black)
    coin_text = lil_font.render(str(coins_sum), True, black)
    screen.blit(scores, (10, 10))
    screen.blit(coin_text, (370, 10))

    for sp in all_sprites:
        screen.blit(sp.image, sp.rect)
        sp.move()

    if pygame.sprite.spritecollideany(p1, coins):
        pygame.mixer.Sound('coin.wav').play()
        coins_sum += 1
        pygame.display.update()
        for sp in coins:
            sp.kill()
            c = Coins()
            coins.add(c)
            all_sprites.add(c)


    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        screen.fill(red)
        screen.blit(game_over, (30, 250))
        screen.blit(game_score, (30, 320))
        screen.blit(game_coin, (30, 350))

        pygame.display.update()
        for sp in all_sprites:
            sp.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    clock.tick(fps)
