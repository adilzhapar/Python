import pygame
import random
from pygame.constants import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

surf = pygame.surface.Surface((800, 250))
surf.fill((229, 198, 135))

blackboard = pygame.surface.Surface((760, 350))
blackboard.fill((239, 224, 224))

screen.blit(surf, (0, 0))
screen.blit(blackboard, (40, 0))
pygame.display.set_caption("Paint")


colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'purple': (83, 28, 232),
        'black': (0, 0, 0),
        'random': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    }


def line(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), d)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), d)

def rectangle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if x1 < x2 and y1 < y2:
        pygame.draw.rect(screen, color, [x1, y1, width, height], d)
    elif x1 < x2 and y2 < y1:
        pygame.draw.rect(screen, color, [x1, y2, width, height], d)
    elif x2 < x1 and y1 < y2:
        pygame.draw.rect(screen, color, [x2, y1, width, height], d)
    elif x2 < x1 and y2 < y1:
        pygame.draw.rect(screen, color, [x2, y2, width, height], d)


def circle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if x1 < x2 and y1 < y2:
        pygame.draw.ellipse(screen, color, [x1, y1, width, height], d)
    elif x1 < x2 and y2 < y1:
        pygame.draw.ellipse(screen, color, [x1, y2, width, height], d)
    elif x2 < x1 and y1 < y2:
        pygame.draw.ellipse(screen, color, [x2, y1, width, height], d)
    elif x2 < x1 and y2 < y1:
        pygame.draw.ellipse(screen, color, [x2, y2, width, height], d)


def info_text(surf):
    pygame.draw.aaline(surf, colors['black'], (40, 0), (40, 250), 2)
    font = pygame.font.SysFont('Times New Roman', 20, False, False)

    t1 = font.render("Alt + R -- rectangle", True, colors['black'], (229, 198, 135))
    t2 = font.render("Alt + L -- line", True, colors['black'], (229, 198, 135))
    t3 = font.render("Alt + C -- circle", True, colors['black'], (229, 198, 135))
    t4 = font.render("Alt + E -- eraser", True, colors['black'], (229, 198, 135))
    t5 = font.render("Alt + Up -- size-up for eraser", True, colors['black'], (229, 198, 135))
    t6 = font.render("Alt + Down -- size-down for eraser", True, colors['black'], (229, 198, 135))

    t7 = font.render("Ctrl + R -- red", True, colors['black'], (229, 198, 135))
    t8 = font.render("Ctrl + G -- green", True, colors['black'], (229, 198, 135))
    t9 = font.render("Ctrl + B -- blue", True, colors['black'], (229, 198, 135))
    t10 = font.render("Ctrl + P -- purple", True, colors['black'], (229, 198, 135))
    t11 = font.render("Ctrl + Space -- random-color", True, colors['black'], (229, 198, 135))
    t12 = font.render("Up -- size-up", True, colors['black'], (229, 198, 135))
    t13 = font.render("Down -- size-down", True, colors['black'], (229, 198, 135))
    t14 = font.render("Ctrl + S -- for save", True, colors['black'], (229, 198, 135))


    surf.blit(t1, (150, 15))
    surf.blit(t2, (150, 40))
    surf.blit(t3, (150, 65))
    surf.blit(t4, (150, 90))
    surf.blit(t5, (150, 115))
    surf.blit(t6, (150, 140))

    surf.blit(t7, (500, 15))
    surf.blit(t8, (500, 40))
    surf.blit(t9, (500, 65))
    surf.blit(t10, (500, 90))
    surf.blit(t11, (500, 115))

    surf.blit(t12, (500, 150))
    surf.blit(t13, (500, 175))
    surf.blit(t14, (500, 200))


done = False
draw_line = False
erase = False

commands = {
    "lining": True,
    "recting": False,
    "circling": False,
    "erasing": False
}
surf_elements = {
    'line': (255, 0, 0),
    'rec': (10, 10, 10),
    'circ': (10, 10, 10),
    'erase': (10, 10, 10)
}
x, y = 0, 0
last_pos = (0, 0)
d = 2
ed = 20
color = (0, 0, 0)
Pi = 3.14

while not done:
    get_pressed = pygame.key.get_pressed()
    alt_press = get_pressed[K_LALT] or get_pressed[K_RALT]
    ctrl_press = get_pressed[K_LCTRL] or get_pressed[K_RCTRL]
    pos = pygame.mouse.get_pos()

    font = pygame.font.SysFont('Verdana', 17, False, False)

    pygame.draw.circle(surf, color, (20, 30), 15)
    pygame.draw.rect(surf, surf_elements['rec'], [5, 60, 30, 30], 1)
    pygame.draw.circle(surf, surf_elements['circ'], [20, 120], 15, 1)
    pygame.draw.arc(surf, surf_elements['line'], [6, 151, 15, 15], Pi, 2 * Pi, 1)
    pygame.draw.arc(surf, surf_elements['line'], [20, 154, 15, 15], 0, Pi, 1)
    pygame.draw.aalines(surf, surf_elements['erase'], True, [[10, 190], [15, 205], [25, 205], [30, 190], [20, 180]])
    size_text = font.render(str(d), True, colors['black'], (229, 198, 135))

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if alt_press and event.key == K_r:
                for i in surf_elements:
                    if i == 'rec':
                        surf_elements[i] = colors['red']
                    else:
                        surf_elements[i] = (10, 10, 10)
                for i in commands:
                    if i == 'recting':
                        commands[i] = True
                    else:
                        commands[i] = False
            if alt_press and event.key == K_l:
                for i in surf_elements:
                    if i == 'line':
                        surf_elements[i] = colors['red']
                    else:
                        surf_elements[i] = (10, 10, 10)
                for i in commands:
                    if i == 'lining':
                        commands[i] = True
                    else:
                        commands[i] = False
            if alt_press and event.key == K_c:
                for i in surf_elements:
                    if i == 'circ':
                        surf_elements[i] = colors['red']
                    else:
                        surf_elements[i] = (10, 10, 10)
                for i in commands:
                    if i == 'circling':
                        commands[i] = True
                    else:
                        commands[i] = False
            if alt_press and event.key == K_e:
                for i in surf_elements:
                    if i == 'erase':
                        surf_elements[i] = colors['red']
                    else:
                        surf_elements[i] = (10, 10, 10)
                for i in commands:
                    if i == 'erasing':
                        commands[i] = True
                    else:
                        commands[i] = False
            if event.key == K_UP:
                if d < 9:
                    d += 1
            if event.key == K_DOWN:
                if d > 1:
                    d -= 1
            if alt_press and event.key == K_UP:
                if ed < 50:
                    ed += 5
            if alt_press and event.key == K_DOWN:
                if ed > 20:
                    ed -= 5
            if ctrl_press and event.key == K_s:
                pygame.image.save(blackboard, 'screenshot.jpg')
            if alt_press and event.key == K_SPACE:
                pygame.image.save(surf, 'screenshot.jpg')
            if ctrl_press and event.key == K_r:
                color = colors['red']
            if ctrl_press and event.key == K_g:
                color = colors['green']
            if ctrl_press and event.key == K_b:
                color = colors['blue']
            if ctrl_press and event.key == K_p:
                color = colors['purple']
            if ctrl_press and event.key == K_SPACE:
                colors['random'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                color = colors['random']

        if commands['recting']:
            if event.type == MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == MOUSEBUTTONUP:
                rectangle(blackboard, last_pos, pos, d, color)

        if commands['lining']:
            if event.type == MOUSEBUTTONDOWN:
                last_pos = pos
                pygame.draw.circle(blackboard, color, pos, d)
                draw_line = True
            if event.type == MOUSEBUTTONUP:
                draw_line = False
            if event.type == MOUSEMOTION:
                if draw_line:
                    line(blackboard, last_pos, pos, d, color)
                last_pos = pos

        if commands['circling']:
            if event.type == MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == MOUSEBUTTONUP:
                circle(blackboard, last_pos, pos, d, color)

        if commands['erasing']:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pos
                pygame.draw.rect(blackboard, (239, 224, 224), [x, y, ed, ed])
                erase = True
            if event.type == pygame.MOUSEMOTION:
                if erase:
                    pygame.draw.rect(blackboard, (239, 224, 224), [pos[0], pos[1], ed, ed])
            if event.type == pygame.MOUSEBUTTONUP:
                erase = False

    info_text(surf)
    surf.blit(size_text, (15, 215))
    screen.blit(surf, (0, 350))
    screen.blit(blackboard, (0, 0))
    pygame.display.flip()

pygame.quit()
