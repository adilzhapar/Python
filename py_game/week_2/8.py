# wav
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
sound = pygame.mixer.Sound('engine.wav')
sound.play()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()
