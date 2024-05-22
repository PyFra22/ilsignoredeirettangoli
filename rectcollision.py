import pygame as pyg
import random as rm
import time as tm

pyg.init()

color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_black = (0, 0, 0)

obstacles = []
for _ in range(36):
    obstacle_rectangle = pyg.Rect(
        rm.randint(0, 600), rm.randint(0, 250), 25, 25)
    obstacles.append(obstacle_rectangle)

total_live = 100

width = 800
height = 400

window = pyg.display.set_mode((width, height))
clock = pyg.time.Clock()
running = True

font_text_tot_life = pyg.font.Font('freesansbold.ttf', 18)
text_life = font_text_tot_life.render("Vita totale: ", False, color_black)
textRect_tot_life = text_life.get_rect()
textRect_tot_life.center = (width/1.2, height/12)

font_text_number_of_life = pyg.font.Font('freesansbold.ttf', 18)


main_rectangle = pyg.Rect(0, 0, 30, 30)

pyg.mouse.set_visible(False)

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

    
    for obstacle in obstacles:
        pyg.draw.rect(window, color_blue, obstacle)
        

    position_of_mouse = pyg.mouse.get_pos()
    main_rectangle.center = position_of_mouse

    pyg.draw.rect(window, rectangle_color, main_rectangle)

    if total_live == 0:
        window.fill("black")
        font_text_lose = pyg.font.Font('freesansbold.ttf', 48)
        text_lose = font_text_lose.render("HAI PERSO", False, "white")
        textRect_lose = text_lose.get_rect()
        textRect_lose.center = (width/2, height/3)
        window.blit(text_lose, textRect_lose)
        
        

    exit_pressed = pyg.key.get_pressed()

    if exit_pressed[pyg.K_ESCAPE]:
        running = False

    pyg.display.flip()
    dt = clock.tick(60)/1000

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False



pyg.quit()
