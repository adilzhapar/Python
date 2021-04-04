'''
pip install virtualenv
python3 -m venv name_env
source path-to-env/bin/activate
pip install pygame
'''
import pygame

size = width, height = (400, 300)
screen = pygame.display.set_mode(size)

screen.fill((0, 0, 0)) #color

pygame.draw.rect(screen, (255, 0, 0), (20, 30, 100, 100), 2) #where_to_draw, color, size, wigth_of_frame

running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #click the quit button
            running = True
    pygame.display.flip()

pygame.quit()

    