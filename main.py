import pygame as pg

class Cube():
    def __init__(self):
        self.cube = [[["W", "W"], 
                      ["W", "W"]],

                     [["G", "G"], 
                      ["G", "G"]],

                     [["R", "R"], 
                      ["R", "R"]],

                     [["B", "B"], 
                      ["B", "B"]],

                     [["O", "O"], 
                      ["O", "O"]],

                     [["Y", "Y"], 
                      ["Y", "Y"]]]
        

    def display(self):
    def move_R(self, prime):
        if prime:
            sub1 = self.cube[0][1][1]
            sub2 = self.cube[0][0][1]

            self.cube[0][1][1] = self.cube[4][0][0]
            self.cube[0][1][0] = self.cube[4][0][1]

            self.cube[4][0][0] = self.cube[5][1][1]
            self.cube[4][0][1] = self.cube[5][0][1]

            self.cube[5][1][1] = self.cube[2][1][1]
            self.cube[5][0][0] = self.cube[2][0][0]

            self.cube[2][1][1] = sub1
            self.cube[2][0][1] = sub2

pg.init()
screen = pg.display.set_mode([500, 500])
screen.fill((255, 255, 255))

image = pg.image.load("icon.png")
pg.display.set_icon(image)
pg.display.set_caption("Cube")
pg.display.flip()

cube = Cube()
cube.move_R(True)
print(cube.cube)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): running = False
pg.quit()