import pygame
from pygame.locals import *

# funções
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision_with_apple(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def collision_with_border(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2 [1]) 


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

border_pos = [(600, 600)]
border_pos_negative = [(0, 0)]


snake = [(300, 300), (601, 0), (601, 0), (601, 0)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))


apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = RIGHT

clock = pygame.time.Clock()

while True:
    
    x_snake, y_snake = snake[0]
    x_border_pos, y_border_pos = border_pos[0]
    x_border_pos_negative, y_border_pos_negative = border_pos_negative[0]

    clock.tick(10)

    x_snake, y_snake = snake[0]
    x_border_pos, y_border_pos = border_pos[0]
    x_border_pos_negative, y_border_pos_negative = border_pos_negative[0]

    for event in pygame.event.get():
        if event.type == QUIT:
            break
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN or event.key == K_w and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP or event.key == K_s and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT or event.key == K_a and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT or event.key == K_d and my_direction != LEFT:
                my_direction = RIGHT

    if collision_with_apple(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))



    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])



    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    for segment in snake[1:]:
        if collision_with_border(snake[0], segment):
            print("A cobra colidiu consigo mesma!")
            break
    
    if not (x_border_pos_negative <= x_snake <= x_border_pos and y_border_pos_negative <= y_snake <= y_border_pos):
        print('A cobra bateu na borda!')
        break

    pygame.display.update()     