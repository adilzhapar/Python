import pygame

keys = filter(lambda x: 'K_' in x, dir(pygame))

for key in keys:
    print(key)
