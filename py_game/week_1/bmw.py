import pygame
pygame.init()
wight, height, fps = 700, 500, 60

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

screen = pygame.display.set_mode((wight, height))
pygame.display.set_caption("BMW")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.circle(screen, black, (350, 250), 120)
    pygame.draw.circle(screen, white, (350, 250), 80)

    font = pygame.font.SysFont('Tahoma', 40, True, False)
    text = font.render("B", True, white)
    text = pygame.transform.rotate(text, 45)
    text2 = font.render("M", True, white)
    text3 = font.render("W", True, white)
    text3 = pygame.transform.rotate(text3, 315)

    screen.blit(text, (255, 150))
    screen.blit(text2, (330, 125))
    screen.blit(text3, (390, 150))
    pygame.draw.line(screen, black, [349, 170], [349, 330], 3)
    pygame.draw.line(screen, black, [270, 249], [450, 249], 3)
    pygame.display.flip()
pygame.quit()