import pygame
import sys
import random
import time

class Game:
    def __init__(self):
        self.width = 700
        self.height = 460

        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)

        self.fps = pygame.time.Clock()
        self.score = 0 #колличество сьеденного
    
    def init_and_check_errors(self):
        '''Начальная функция для инициализации и
        проверки как запустится игры'''
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print("OK")
    
    def set_surface_and_title(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        
    def event_loop(self, change_to):
        '''Отслеживание нажатий клавиш'''

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to
    
    def refresh_screen(self):
        pygame.display.flip()
        game.fps.tick(20)
    
    def show_score(self, choice=1):
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render("Score: {}".format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        #дефолтный случай, показывать результат на верхнем левом углу
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (360, 120)
        self.screen.blit(s_surf, s_rect)
    
    def game_over(self):
        go_font = pygame.font.SysFont('mpnaco', 72)
        go_surf = go_font.render("Game Over", True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.screen.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

class Snake():
    def __init__(self, snake_color):
        self.snake_head_pos = [100, 50]
        '''тело змеи состоит из трех элементов
        голова змеи, ..., хвост змеи'''
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color

        self.direction = "RIGHT"
        # куда будет меняться направление движения змеи
        # при нажатии соответствующих клавиш
        self.change_to = self.direction
    
    def validate_direction_and_change(self):
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT", 
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to
    
    def change_head_position(self):
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10

    def snake_body_mechanism(self, score, food_pos, width, height):
        self.snake_body.insert(0, list(self.snake_head_pos))
    # если сьел еду
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):
            food_pos = [random.randrange(1, width/10)*10, 
                        random.randrange(1, height/10)*10]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos
    
    def draw_snake(self, screen, surface_color):
        screen.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                screen, self.snake_color, pygame.Rect(
                    pos[0], pos[1], 10, 10))
    
    def check_for_boundaries(self, game_over, width, height):
        """Проверка, что столкунлись с концами экрана или сами с собой
        (змея закольцевалась)"""
        if any((
            self.snake_head_pos[0] > width-10
            or self.snake_head_pos[0] < 0,
            self.snake_head_pos[1] > height-10
            or self.snake_head_pos[1] < 0
                )):
            game_over()
        for block in self.snake_body[1:]:
            # проверка на то, что первый элемент(голова) врезался в
            # любой другой элемент змеи (закольцевались)
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()
        

class Food():
    def __init__(self, food_color, width, height):
        """Инит еды"""
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, width/10)*10,
                         random.randrange(1, height/10)*10]

    def draw_food(self, screen):
        """Отображение еды"""
        pygame.draw.rect(
            screen, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))

game = Game()
snake = Snake(game.red)
food = Food(game.green, game.width, game.height)

game.init_and_check_errors()
game.set_surface_and_title()
    
while True:
    snake.change_to = game.event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(
        game.score, food.food_pos, game.width, game.height)
    snake.draw_snake(game.screen, game.white)

    food.draw_food(game.screen)

    snake.check_for_boundaries(
        game.game_over, game.width, game.height)

    game.show_score()
    game.refresh_screen()