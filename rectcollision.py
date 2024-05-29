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


def text_child(text, colortext, coordinatex, coordinatey):
    if colortext == True:
        colortext = color_white
    else:
        colortext = color_black
    text_child_font = pyg.font.SysFont("Arial", 18)
    text_child_render = text_child_font.render(text, True, colortext)
    text_child_rect = text_child_render.get_rect()
    text_child_rect.center = (width/coordinatex, height/coordinatey)
    window.blit(text_child_render, text_child_rect)

main_rectangle = pyg.Rect(0, 0, height_main_rectangle, width_main_rectangle)
pyg.draw.rect(window, color_green, main_rectangle)
pyg.mouse.set_visible(False)

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

def lose_and_win_window(text):
    window.fill("black")
    font_text_parents = pyg.font.Font('freesansbold.ttf', 48)
    text_displayed_parents = font_text_parents.render(text, True, "white")
    text_rect = text_displayed_parents.get_rect()
    text_rect.center = (width/2, height/3)
    pyg.mouse.set_visible(True)
    window.blit(text_displayed_parents, text_rect)


while running:
    
    window.fill("white")

    rectangle_color = color_green
    for obstacle in obstacles:
        if main_rectangle.colliderect(obstacle) and total_live != 0:
            total_live -= 1
            rectangle_color = color_red
  
    if total_live < 0:
        total_live = 0
        
    text_child(text="VITA TOTALE: ", colortext=False, coordinatex=1.2, coordinatey=12)
    text_child(text=str(total_live), colortext=False, coordinatex=1.08, coordinatey=12)


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
        lose_and_win_window(text="HAI VINTO")
        text_child(text="QUIT", colortext=True, coordinatex=2, coordinatey=2)
        text_child(text="PREMERE R PER UNA NUOVA PARTITA", colortext=True, coordinatex=2, coordinatey=1.75)  
                 
    if total_live == 0:
        lose_and_win_window(text="HAI PERSO")
        text_child(text="QUIT", colortext=True, coordinatex=2, coordinatey=2)
        text_child(text="PREMERE R PER UNA NUOVA PARTITA", colortext=True, coordinatex=2, coordinatey=1.75)
        
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
