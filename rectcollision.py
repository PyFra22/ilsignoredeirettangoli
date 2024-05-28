import pygame as pyg
import random as rm
import time as tm
import sys as sy

pyg.init()

color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_light = (170,170,170) 
color_dark = (100,100,100)


obstacles = []
for _ in range(60):
    obstacle_rectangle = pyg.Rect(
    rm.randint(25, 575), rm.randint(25, 275), 25, 25)
    obstacles.append(obstacle_rectangle)

total_live = 100
width = 800
height = 400
vel = 2

height_main_rectangle = 22
width_main_rectangle = 22

window = pyg.display.set_mode((width, height))
clock = pyg.time.Clock()
running = True

font_text_tot_life = pyg.font.Font('freesansbold.ttf', 18)
text_life = font_text_tot_life.render("Vita totale: ", False, color_black)
textRect_tot_life = text_life.get_rect()
textRect_tot_life.center = (width/1.2, height/12)
font_text_number_of_life = pyg.font.Font('freesansbold.ttf', 18)

font_quit_button = pyg.font.SysFont("Arial", 24)
text_quit_button = font_quit_button.render("QUIT", True, color_white)
text_quit_rect = text_quit_button.get_rect()
text_quit_rect.center = (width/2, height/2)

font_text_retry = pyg.font.SysFont("Arial", 16)
text_retry = font_text_retry.render("PREMERE R PER UNA NUOVA PARTITA", True, color_white)
text_retry_rect = text_retry.get_rect()
text_retry_rect.center = (width/2, height/1.75)

main_rectangle = pyg.Rect(0, 0, height_main_rectangle, width_main_rectangle)
pyg.draw.rect(window, color_green, main_rectangle)
pyg.mouse.set_visible(False)

def lose_and_win_window(text):
    window.fill("black")
    font_text = pyg.font.Font('freesansbold.ttf', 48)
    text_displayed = font_text.render(text, False, "white")
    textRect = print("Ciao")

def main_rectangle_movements(keys, position, vel):
    if keys[pyg.K_w]:
        position.y -= vel * 1.8
    if keys[pyg.K_a]:
        position.x -= vel * 1.8
    if keys[pyg.K_s]:
        position.y += vel * 1.8
    if keys[pyg.K_d]:
        position.x += vel * 1.8 

winnig_finish_rectangle = pyg.Rect(700, 100, 100, 125)
border_outside_rectangle = pyg.Rect(0, 300 , 800, 125)

while running:
    
    window.fill("white")

    rectangle_color = color_green
    for obstacle in obstacles:
        if main_rectangle.colliderect(obstacle) and total_live != 0:
            total_live -= 1
            rectangle_color = color_red

    text_number_of_life = font_text_number_of_life.render(str(total_live), False, color_black)
    textRect_number_of_life = text_number_of_life.get_rect()
    textRect_number_of_life.center = (width/1.1, height/12)
    
    if total_live < 0:
        total_live = 0
    
    window.blit(text_number_of_life, textRect_number_of_life)           
    window.blit(text_life, textRect_tot_life)

    pyg.draw.rect(window, color_red, winnig_finish_rectangle)
    pyg.draw.rect(window, color_black, border_outside_rectangle)
    if main_rectangle.colliderect(border_outside_rectangle) and total_live != 0:
        total_live -= 1
        rectangle_color = color_red
            

    for obstacle in obstacles:
        pyg.draw.rect(window, color_blue, obstacle)
        
    pyg.draw.rect(window, rectangle_color, main_rectangle)
    main_rectangle_key = pyg.key.get_pressed()
    main_rectangle_movements(main_rectangle_key, main_rectangle, vel)

    if main_rectangle.colliderect(winnig_finish_rectangle) and total_live != 0:
        window.fill("black")
        font_text_lose = pyg.font.Font('freesansbold.ttf', 48)
        text_lose = font_text_lose.render("HAI VINTO", False, "white")
        textRect_lose = text_lose.get_rect()
        textRect_lose.center = (width/2, height/3)
        window.blit(text_lose, textRect_lose)
        pyg.mouse.set_visible(True)
        window.blit(text_quit_button, text_quit_rect)
        window.blit(text_retry, text_retry_rect)    
                 
    if total_live == 0:
        window.fill("black")
        font_text_lose = pyg.font.Font('freesansbold.ttf', 48)
        text_lose = font_text_lose.render("HAI PERSO", False, "white")
        textRect_lose = text_lose.get_rect()
        textRect_lose.center = (width/2, height/3)
        window.blit(text_lose, textRect_lose)
        pyg.mouse.set_visible(True)
        window.blit(text_quit_button, text_quit_rect)
        window.blit(text_retry, text_retry_rect)
        
    retry_button = pyg.key.get_pressed()
    exit_button = pyg.key.get_pressed()
        
    if retry_button[pyg.K_r]:
        total_live = 100
        obstacles = []             
        for _ in range(45):
            obstacle_rectangle = pyg.Rect(rm.randint(25, 575), rm.randint(25, 275), 25, 25)
            obstacles.append(obstacle_rectangle)
        main_rectangle = pyg.Rect(0,0,height_main_rectangle,width_main_rectangle)         
    if exit_button[pyg.K_ESCAPE]:
        running = False
    
    position_of_mouse = pyg.mouse.get_pos()
    
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        if event.type == pyg.MOUSEBUTTONDOWN:
            if width/2 <= position_of_mouse[0] <= width/2+100 and height/2 <= position_of_mouse[1] <= height/2+25: 
                pyg.quit()
        
    pyg.display.flip()
    dt = clock.tick(60)/1000

pyg.quit()
