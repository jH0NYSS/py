import pygame
import random
import sys
import time
from pygame.locals import *
from pynput.keyboard import Key, Controller

pygame.init()
keyboard = Controller()

# funções
def on_grid_random():
    x = random.randint(10, 590)
    y = random.randint(10, 590)
    return (x // 10 * 10, y // 10 * 10)

def collision(c1, c2):
    return (c1[0]) == c2[0] and (c1[1] == c2[1]) 

def collision_case():
    snake.append((0, 0))
    global pontos
    pontos += 1

    

# definindo as variaveis
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
WHITE = (255, 255, 255)
pontos = 0
velocidade = 15
game = 0
sair = 0
max_score = 0
pause = False
menu_upgrade = False
life = 2
vex = 0



# text config
pygame.display.set_caption('Show Text')
font = pygame.font.Font(None, 32)
font_pause = pygame.font.Font(None, 70)
font_menu = pygame.font.Font(None, 30)
font_max_score = pygame.font.Font(None, 25)

# tela config
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

# border config
border_pos = [(600, 600)]
border_pos_negative = [(0, 0)]

# snake config
snake = [(300, 300), (601, 0), (601, 0), (601, 0), (601, 0), (601, 0)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

# apples config
apple_pos = on_grid_random()
apple_pos1 = on_grid_random()
apple_pos2 = on_grid_random()
apple = pygame.Surface((10, 10))
apple1 = pygame.Surface((10, 10))
apple2 = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple1.fill((255, 0, 0))
apple2.fill((255, 0, 0))

heart_pos = on_grid_random()
heart = pygame.Surface((10,10))
heart.fill((0, 255, 0))

speed_item_pos = on_grid_random()
speed = pygame.Surface((10,10))
speed.fill((57,176,222))

my_direction = RIGHT

clock = pygame.time.Clock()

while (sair == 0): # tela inicial

    clock.tick(30) # define a velocidade de ticks por segundo
    screen.fill((0, 0, 0))
    text_start = font.render('PRESS "SPACE" TO START', True, WHITE)
    text_max_score = font_max_score.render(f'MAXIMUM SCORE:{max_score}', True, WHITE)
    screen.blit(text_start, (156, 215))
    screen.blit(text_max_score, (10, 10))
    
    for event in pygame.event.get(): # comandos do teclado
        if event.type == QUIT:
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                game += 1
            if event.key == K_ESCAPE:
                sys.exit()   



    pygame.display.update()

    while (game == 1): # jogo rodando

        # atualizando variaveis
        x_snake, y_snake = snake[0]
        x_border_pos, y_border_pos = border_pos[0]
        x_border_pos_negative, y_border_pos_negative = border_pos_negative[0]

        if velocidade > 15:
            time.sleep(0.03)
            velocidade -= 0.05
        else:
            time.sleep(0.05)
            velocidade = 15
        
        for event in pygame.event.get(): # comandos do teclado
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN or event.key == K_w and my_direction != DOWN:
                    my_direction = UP
                if event.key == K_DOWN and my_direction != UP or event.key == K_s and my_direction != UP:
                    my_direction = DOWN
                if event.key == K_LEFT and my_direction != RIGHT or event.key == K_a and my_direction != RIGHT:
                    my_direction = LEFT
                if event.key == K_RIGHT and my_direction != LEFT or event.key == K_d and my_direction != LEFT:
                    my_direction = RIGHT
                if event.key == K_p:
                    pause = True
                if event.key == K_TAB:
                    menu_upgrade = True
                if event.key == K_ESCAPE:
                         sys.exit()


        if collision(snake[0], apple_pos):
             apple_pos = on_grid_random()
             collision_case()
         
        if collision(snake[0], apple_pos1):
             apple_pos1 = on_grid_random()
             collision_case()

        if collision(snake[0], apple_pos2):
            apple_pos2 = on_grid_random()
            collision_case()

        if collision(snake[0], heart_pos):
            heart_pos = on_grid_random()

        if collision(snake[0], speed_item_pos):
            velocidade += 10



        if life <= 0:
            sys.exit()

        for i in range(len(snake) - 1, 0, -1):
             snake[i] = (snake[i - 1][0], snake[i - 1][1])
        if my_direction == UP:
             snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction == DOWN:
             snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction == RIGHT:
             snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction == LEFT:
             snake[0] = (snake[0][0] - 10, snake[0][1])
        for segment in snake[1:]:
             if collision(snake[0], segment):
                 print('A cobra bateu nela mesma!')
                 life -= 1

        if not (x_border_pos_negative <= x_snake <= x_border_pos and y_border_pos_negative <= y_snake <= y_border_pos):
             print('A cobra bateu na borda!')
             sys.exit()

        screen.fill((0, 0, 0)) #deixar antes de todos screen.blit
        screen.blit(apple, apple_pos) # screen.blit define o lugar da tela
        screen.blit(apple1, apple_pos1)
        screen.blit(apple2, apple_pos2)
        screen.blit(heart, heart_pos)
        screen.blit(speed, speed_item_pos)
        text_score = font.render(f'SCORE: {pontos}', True, WHITE)
        text_life = font.render(f'LIFE: {life}', True, WHITE)
        screen.blit(text_score, (10, 10))
        screen.blit(text_life, (510, 10))
        for pos in snake:
            screen.blit(snake_skin, pos)

        pygame.display.update()

        while (pause == True): #jogo pausado

            clock.tick(40)

            for event in pygame.event.get(): # comandos do teclado
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_p:
                        pause = False


            screen.fill((0, 0, 0)) 
            text_pause = font_pause.render('PAUSED', True, WHITE)
            text_menu = font_menu.render('PRESS "P" FOR PLAY:', True, WHITE)
            text_menu_quit = font_menu.render('PRESS "ESQ" FOR QUIT:', True, WHITE)
            screen.blit(text_pause, (10, 10))       
            screen.blit(text_menu, (200, 200))
            screen.blit(text_menu_quit, (187, 240)) 


            # menu "press P for play"    


            pygame.display.update()
        
        while (menu_upgrade == True):
             
            clock.tick(40)

            for event in pygame.event.get(): # comandos do teclado
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_TAB:
                        menu_upgrade = False

            screen.fill((0, 0, 0)) 
            text_pause = font_pause.render('UPGRADE', True, WHITE)
            text_menu = font_menu.render('PRESS "P" FOR PLAY:', True, WHITE)
            text_menu_quit = font_menu.render('PRESS "ESQ" FOR QUIT:', True, WHITE)
            screen.blit(text_pause, (10, 10))       
            screen.blit(text_menu, (200, 200))
            screen.blit(text_menu_quit, (187, 240))    


            pygame.display.update()
            
             

