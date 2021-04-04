#тут крутится текст
import pygame

pygame.init()

RB = (100,  0, 255)
GB = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (100, 200, 100)
blue = (0, 0, 255)
white = (255, 255, 255)

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Drawing")
clock = pygame.time.Clock() #fps


rotation = 1
run = False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
    screen.fill(white)
    
    font = pygame.font.SysFont('Tahoma', 50, True, True)
    text = font.render("rotation", True, black)
    text = pygame.transform.rotate(text, rotation)
    screen.blit(text, (200, 200))
    rotation += 1
    clock.tick(60)
    pygame.display.flip()
pygame.quit()

