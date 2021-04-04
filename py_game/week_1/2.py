# рисование 
# drawing
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
PI = 3.14
run = False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    screen.fill(white)
    pygame.draw.line(screen, GB, [0, 0], [100, 100], 5)
    #lines:
    for y in range(0, 100, 10):
        pygame.draw.line(screen, green, [0, 15 + y], [100, 115 + y], 2)
    
    #rectangles & ellipse:
    for x in range(0, 200, 60):
        pygame.draw.rect(screen, green, (10+x, 210, 50, 30), 2)
        pygame.draw.ellipse(screen, RB, (10+x, 210, 50, 30), 1)

    #arc:
    pygame.draw.arc(screen, red, [10, 250, 250, 100], 0, PI / 2, 2)
    pygame.draw.arc(screen, blue, [10, 250, 250, 100], PI / 2, PI, 2)
    pygame.draw.arc(screen, green, [10, 250, 250, 100], PI, 3 * PI / 2,  2)
    pygame.draw.arc(screen, black, [10, 250, 250, 100], 3 * PI / 2, 2* PI, 2)

    #text:
    font = pygame.font.Font(None, 50)
    text1 = font.render("Welcome to PyGame", True,  red)
    text2 = font.render("PyGame - my game", True,  red)
    screen.blit(text1, (20, 350))
    screen.blit(text2, (20, 400))

    #text rotating:
    font = pygame.font.SysFont('Tahoma', 30, True, True) #bold, italic
    text = font.render("Programming principles", True, black) #сглаживание, цвет
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (460, 0))
    pygame.display.flip()
pygame.quit()
