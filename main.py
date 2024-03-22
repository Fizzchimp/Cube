import pygame

class Cube():
    def __init__(self):
        self.cube1 = [["WW", "WW"],
                      ["OO", "OO"],
                      ["BB", "BB"],
                      ["RR", "RR"],
                      ["GG", "GG"],
                      ["YY", "YY"]]
pygame.init()
screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()