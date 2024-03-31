import pygame as pg
from display import Display
from cube import Cube


screen = Display()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): running = False


    screen.draw_cube()
pg.quit()