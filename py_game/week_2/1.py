import random
import pygame
# рандомные шары в рандомном направлении
black = (0, 0, 0)
white = (255, 255, 255)

width = 700
height = 500


class Ball:
    b_size = 25

    def get_random_change(self):
        change = random.randint(-2, 3)
        while change == 0:
            change = random.randint(-2, 3)
        return change

    def __init__(self):
        self.x = random.randint(self.b_size, width - self.b_size)
        self.y = random.randint(self.b_size, height - self.b_size)
        self.change_x = self.get_random_change()
        self.change_y = self.get_random_change()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x > width - self.b_size or self.x < self.b_size:
            self.change_x *= -1
        if self.y > height - self.b_size or self.y < self.b_size:
            self.change_y *= -1


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Something with  ball")
    done = False
    clock = pygame.time.Clock()
    b_list = []
    ball = Ball()
    b_list.append(ball)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    b_list.append(Ball())

        for ball in b_list:
            ball.move()
        screen.fill(black)
        for ball in b_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.b_size)

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()


main()
