

import random
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800,600))


clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
light_green= (0,200,0)
gray = (119,118,100)

car_image = pygame.image.load('/home/sonia/Music/sonia/scripts/car-clipart-sprite-sheet-14.jpg')
car_image = pygame.transform.scale(car_image,(100,100))
backg_round1 = pygame.image.load('/home/sonia/Music/sonia/scripts/background1.jpg')
grass = pygame.image.load('/home/sonia/Music/sonia/scripts/download12.jpg')



def Message(size,mess,x_poss,y_poss):
    font = pygame.font.SysFont(None,size)
    render = font.render(mess,True,white)
    screen.blit(render,(x_poss,y_poss))


Message(100,"START",150,100)
clock.tick(2)

def car(x,y):
    screen.blit(car_image,(x,y))
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    if 0 < x < 90 or 700 < x + 100:
        Message(100,"GAME OVER",200,100)
        pygame.display.update()
        clock.tick(0.17)
        Game_intro()

def enemy_car(x_r,y_r):
    screen.blit(car_image,(x_r,y_r))


def button(x_button,y_button,mess_b):
    pygame.draw.rect(screen,green,[x_button,y_button,100,30])
    Message(50,mess_b,x_button,y_button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(mouse)
    # print(click)
    if x_button < mouse[0] < x_button + 100 and  y_button < mouse[1] < y_button + 30:
        pygame.draw.rect(screen,light_green,[x_button,y_button,100,30])
        Message(50,mess_b,x_button,y_button)
        if click == (1,0,0) and mess_b == "PLAY":
            Game_loop()
        elif click == (1,0,0) and  mess_b == "QUIT":
            pygame.quit()
            quit()

def car_crash(x,x_r,y,y_r):
    if x_r < x < x_r + 85 and  y_r < y < y_r + 85  or x_r < x + 85 < x_r + 85 and y_r < y < y_r + 85:
        Message(50,"CRASHED",200,200)
        pygame.display.update()
        time.sleep(1)
        Game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def score(count):
    Message(50,"SCORE : " +str(count),600,10)

def Game_intro():
    intro = False
    while intro == False:
        screen.blit(backg_round1,(0,0))
        button(100,300,"PLAY")
        button(600,300,"QUIT")
        for event in pygame.event.get():   # given event 
            if event.type == pygame.QUIT:   # if event ==  quit button the quit screen
               #intro = False or 
                pygame.quit()
                quit()
        pygame.display.update()

def Game_loop():
    x = 300
    x_r = random.randrange(100,600)
    y = 400
    y_r = 0
    count = 0
    x_change = 0
    # y_change = 0
    game_over = False
    while game_over == False:
     for event in pygame.event.get():   # given event 
        if event.type == pygame.QUIT:   # if event ==  quit button the quit screen
                game_over = True
           #basic movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change += 10 
                count += 1
            elif event.key == pygame.K_RIGHT:
                x_change -= 10
                count += 1
            # elif event.key == pygame.K_UP:
            #   y_change += 10
            # else:
            #  y_change+= 10
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
               x_change = 0 

     screen.fill(gray)
     car(x,y)
     score(count)
     enemy_car(x_r,y_r)
     y_r += 10
     if y_r == 600:
        x_r = random.randrange(100,600)
        y_r = 0
     car_crash(x,x_r,y,y_r)
     x = x - x_change
    #y = y - y_change 
     clock.tick(50)
     pygame.display.update()
      
Game_intro()
pygame.quit()
quit()
