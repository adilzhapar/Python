import pygame, sys

#variables:
height = 500
width = 700
fps = 60
yellow = (255, 255, 0)
blue = (9, 91, 255)
purple = (83, 28, 232)
black = (0, 0, 0)


class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 350
        self.y = 400
        self.dx = 5
        self.dy = 5
        self.r = 30
        self.image = pygame.Surface((self.r, self.r))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < height:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)


player = Pacman()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


def main():
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pacman')
    clock = pygame.time.Clock()
    while 1:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        for sp in all_sprites:
            screen.blit(sp.image, sp.rect)
            sp.move()

        pygame.display.update()


pygame.quit()
main()


