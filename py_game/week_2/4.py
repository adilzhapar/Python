import pygame
# surface прозрачный
pygame.init()
screen = pygame.display.set_mode((700, 500))
surf = pygame.Surface((400, 300))
surf.fill((255, 255, 255))
surf.set_alpha(30)
done = False

pygame.draw.rect(screen, (0, 255, 0), (0, 80, 300, 40))
screen.blit(surf, (50, 25))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
