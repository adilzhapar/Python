import pygame
pygame.init()
# image
screen = pygame.display.set_mode((600, 400))

'''
_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        _path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(path)
        _image_library[path] = image
    return image
screen.blit(get_image('.png'), (x, y))
'''

image = pygame.image.load('bmw.png')
x = 100
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if x < 600:
        x += 2
    else:
        x = 0

    screen.fill((255, 255, 255))
    screen.blit(image, (x, 100))
    pygame.display.flip()
    pygame.time.delay(15)

pygame.quit()
