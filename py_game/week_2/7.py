# tokyo drift
# music
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.mixer.music.load('short_tokyo.mp3')
# pygame.mixer.music.queue()
pygame.mixer.music.play(0, 0, 10)  # how much seconds
# pygame.mixer.music.play(-1)  infinite
# pygame.mixer.music.stop()

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

image = pygame.image.load('bmw.png')
back = pygame.image.load('tok.jpg')
x = 100
done = False


while not done:
    screen.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print("Song end")
    if x < 600:
        x += 2
    else:
        x = 0

    screen.blit(image, (x, 270))
    pygame.display.flip()
    pygame.time.delay(15)

pygame.quit()
