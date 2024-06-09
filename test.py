import pygame as pg

pg.init()
screen = pg.display.set_mode([700, 700])
screen.fill((150, 150, 150))

for font in pg.font.get_fonts():
    screen.fill((150, 150, 150))
    text = pg.font.SysFont(font, 50)
    surface = text.render(f"{font}: Solve", False, (0, 0, 0))
    screen.blit(surface, (100, 350))
    pg.display.flip()
    pg.time.wait(2000)