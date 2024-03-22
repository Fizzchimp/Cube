import pygame as pg

class Cube():
    def __init__(self):
        self.cube1 = [["WW", "WW"],
                      ["OO", "OO"],
                      ["BB", "BB"],
                      ["RR", "RR"],
                      ["GG", "GG"],
                      ["YY", "YY"]]
pg.init()
screen = pg.display.set_mode([500, 500])
screen.fill((255, 255, 255))
pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): running = False
pg.quit()