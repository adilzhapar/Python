import pygame
import random

width = 800
height = 650
fps = 30

#Colors: (R, G, B)
black = (0, 0, 0)
red = (255, 0, 0)
green = (100, 200, 100)
blue = (0, 0, 255)
white = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

    def update(self):
        self.rect.x += 5
        self.rect.y += 4
        if self.rect.left > width and self.rect.bottom > height:
            self.rect.right = 0
            self.rect.top = 0
        

#Create game and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Square")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Cycle
running = True
while running:
    #keep velocity:
    clock.tick(fps)
    #entering process(events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()

    #rendering:
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
