import pygame as pg
from pygame import gfxdraw
from Display.model_2 import Model2
from Display.model_3 import Model3
from numpy import sin, cos, sqrt, arctan2
import numpy as np

colour_keys = {
    "W": (245, 245, 245),
    "Y": (255, 255, 50),
    "G": (50, 205, 50),
    "R": (220, 40, 60),
    "B": (80, 80, 205),
    "O": (255, 140, 0),
    "-": (150, 150, 150)}


BG_IMAGE_SIZE = 90
CUBE_MOVE_COEFFICIENT = 0.02

def depth(face):
    return face[-2]

class Display():
    def __init__(self, width, height, bobStrength, cube_type):

        # Setup the window
        self.screen = pg.display.set_mode([width, height])
        image = pg.image.load("Display/Textures/01_icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")
    
        # Background
        image = pg.transform.scale(pg.image.load("Display/Textures/Background.png"), (BG_IMAGE_SIZE, BG_IMAGE_SIZE)).convert()
        dims = (BG_IMAGE_SIZE * (width // BG_IMAGE_SIZE + 2), BG_IMAGE_SIZE * (height // BG_IMAGE_SIZE + 2))

        # self.background = pg.Surface(dims)
        # for i in range(dims[0] // BG_IMAGE_SIZE):
        #     for j in range(dims[1] // BG_IMAGE_SIZE):
        #         self.background.blit(image, (i * BG_IMAGE_SIZE, j * BG_IMAGE_SIZE))
        # self.backgroundPosition = [-BG_IMAGE_SIZE, -BG_IMAGE_SIZE]

        ### Cube

        self.cube_target = 450

        # Dimensions for the cube
        self.length = width / 5 if width <= height else height / 5

        self.cubeBob = 0
        self.bobStrength = bobStrength

        self.edit_phase = 0
        
        ### 2 by 2
        self.model_2 = Model2([250, 300])
        
        ### 3 by 2
        self.model_3 = Model3([450, 300])
       
        self.cube_type = cube_type
        if cube_type == 2: self.model = self.model_2
        elif cube_type == 3: self.model = self.model_3
        
        # Buttons
        fontSize = 47
        self.main_buttons = [
            Button((200, 600), 1 ,"SOLVE", 35),
            Button((400, 600), 1 ,"SCRAMBLE", 35),
            Button((350, 40), 1 ,"SWAP", 35),
            Button((600, 600), 1 ,"EDIT", 35)]

        self.editing_buttons = [
            Button((550, 550), 1 ,"DONE", 35, True),
            Button((550, 630), 1 ,"CLEAR", 35, True)]
        
        self.solving_buttons = [
            Button((200, 600), 0, "<-", 60, False),
            Button((300, 600), 0, "->", 60, False),
            Button((450, 600), 0, ">>", 60, False)]
        
        self.movement_buttons = [
            Button((45, 30), 0, "U", fontSize),
            Button((125, 30), 0, "U'", fontSize),
            Button((45, 80), 0, "F", fontSize),
            Button((125, 80), 0, "F'", fontSize),
            Button((45, 130), 0, "R", fontSize),
            Button((125, 130), 0, "R'", fontSize),
                         
            Button((45, 190), 0, "D", fontSize),
            Button((125, 190), 0, "D'", fontSize),
            Button((45, 240), 0, "B", fontSize),
            Button((125, 240), 0, "B'", fontSize),
            Button((45, 290), 0, "L", fontSize),
            Button((125, 290), 0, "L'", fontSize)]

    # Swaps between 2x2 and 3x3 cubes 
    def swap_cubes(self):
        if self.cube_type == 2:
            self.cube_type = 3
            self.model = self.model_3
            
            # Changes button positions
            for button in self.movement_buttons:
                button.set_position((button.centre[0] - 530, button.centre[1]))

            self.cube_target = 450
        
        elif self.cube_type == 3:
            self.cube_type = 2
            self.model = self.model_2

            # Changes button positions
            for button in self.movement_buttons:
                button.set_position((button.centre[0] + 530, button.centre[1]))

            self.cube_target = 250

    
    def update_cube_centre(self, delta_time):
        self.cube_centre[0] = np.round(self.cube_centre[0] + (self.cube_target - self.cube_centre[0]) * CUBE_MOVE_COEFFICIENT * delta_time, 2)



    # Draws an antialiased line with given thickness
    def draw_line(self, colour, p1, p2, width):
        centre = ((p1[0] + p2[0]) / 2,
                  (p1[1] + p2[1]) / 2)
        
        length = sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        
        angle = arctan2(p2[0] - p1[0], p2[1] - p1[1])
        cosAngle = cos(angle)
        sinAngle = sin(angle)

        sinHaldWidth = (width / 2) * sinAngle
        cosHalfWidth = (width / 2) * cosAngle

        sinHalfLength = (length / 2) * sinAngle
        cosHalfLength = (length / 2) * cosAngle
        
        UL = (centre[0] + sinHalfLength - cosHalfWidth,
              centre[1] + cosHalfLength + sinHaldWidth)
        UR = (centre[0] - sinHalfLength - cosHalfWidth,
              centre[1] - cosHalfLength + sinHaldWidth)
        BL = (centre[0] + sinHalfLength + cosHalfWidth,
              centre[1] + cosHalfLength - sinHaldWidth)
        BR = (centre[0] - sinHalfLength + cosHalfWidth,
              centre[1] - cosHalfLength - sinHaldWidth)
        
        pg.gfxdraw.aapolygon(self.screen, (UL, UR, BR, BL), colour)
        pg.gfxdraw.filled_polygon(self.screen, (UL, UR, BR, BL), colour)

    # Draws the current cube
    def draw_cube(self, cube, centre_offset = 0, edit_pointer = -1):
        x, y, = self.model.centre[0], self.model.centre[1] + centre_offset

        # Get a list of faces to be drawn and assign colours
        model_points = self.model.get_points()
        draw_list = []
        for i, face in enumerate(model_points):
            for j, facelet in enumerate(face):
                if facelet[2][-1] <= 0:
                    draw_list.append(((
                            (facelet[0][0] * self.length + x, facelet[1][0] * self.length + y),
                            (facelet[0][1] * self.length + x, facelet[1][1] * self.length + y),
                            (facelet[0][2] * self.length + x, facelet[1][2] * self.length + y),
                            (facelet[0][3] * self.length + x, facelet[1][3] * self.length + y)),
                        sum(facelet[2]) / 4,    
                        colour_keys[cube[i][j]]))
            

        # Draw the faces
        for face in sorted(draw_list, key = depth, reverse = True):
            gfxdraw.filled_polygon(self.screen, face[0], face[-1])

            for i in range(4):
                self.draw_line((50, 50, 50), face[0][i], face[0][(i + 1) % 4], 8)
                pg.draw.circle(self.screen, (50, 50, 50), face[0][i], 4)

        # Draw polygon for editing the cube
        if edit_pointer != -1:
            facelet = model_points[edit_pointer // (self.cube_type ** 2)][edit_pointer % (self.cube_type ** 2)]

            edit_points = []
            for i in range(4):
                edit_points.append((facelet[0][i] * self.length + x, facelet[1][i] * self.length + y))

            gfxdraw.filled_polygon(self.screen, edit_points, (0, 0, 0, 100 + 40 * sin(self.edit_phase)))

    # Draws the cube in net form
    def draw_net(self, start_pos, cube):
        face_width = 66
        facelet_width = face_width // self.cube_type
        difference = facelet_width + 2
        
        # Draw face U
        for i, facelet in enumerate(cube[0]):
            draw_x = start_pos[0] + difference * (i % self.cube_type) + (difference * self.cube_type + 2)
            draw_y = start_pos[1] + difference * (i // self.cube_type)
            pg.draw.rect(self.screen, colour_keys[facelet], pg.Rect(draw_x, draw_y, facelet_width, facelet_width))
        

        # Draw faces L, F, R and B
        for j, face in enumerate(cube[1:5]):
            for i, facelet in enumerate(face):
                draw_x = start_pos[0] + difference * (i % self.cube_type) + j * (difference * self.cube_type + 2)
                draw_y = start_pos[1] + difference * (i // self.cube_type + self.cube_type) + 2
                pg.draw.rect(self.screen, colour_keys[facelet], pg.Rect(draw_x, draw_y, facelet_width, facelet_width))
        
        # Draw D face
        for i, facelet in enumerate(cube[5]):
            draw_x = start_pos[0] + difference * (i % self.cube_type) + (difference * self.cube_type + 2)
            draw_y = start_pos[1] + difference * (i // self.cube_type + self.cube_type * 2) + 4
            pg.draw.rect(self.screen, colour_keys[facelet], pg.Rect(draw_x, draw_y, facelet_width, facelet_width))

        ## Draw outlines
        #for i in range(2):
        #    # Draw long horizontal lines
        #    pos_1 = (start_pos[0] - 3, start_pos[1] + facelet_width * self.cube_type + 6)
        #    pos_2 = (start_pos[0] + face_width * 4 + 6, start_pos[1] + facelet_width * self.cube_type + 6)
        #    self.draw_line((50, 50, 50), pos_1, pos_2, 4)

    # Organises drawing all elements on screen
    def draw_screen(self, cube, delta_time, edit_pointer = -1):
        # Draw the background of the screen
        self.screen.fill((255, 255, 255))
        # self.screen.blit(self.background, (self.backgroundPosition))
        
        # Draw the cube onto the screen
        if edit_pointer != -1:
            self.edit_phase += delta_time * 0.005
            self.draw_net((50, 460), cube)

        self.draw_cube(cube, self.bobStrength * sin(self.cubeBob), edit_pointer)

        for button in self.main_buttons + self.solving_buttons + self.movement_buttons:
            if not button.hidden:
                image = button.get_image()
                self.screen.blit(image, button.draw_point)
            
        
        pg.display.flip()
    
    
class Button():
    def __init__(self, centre, size, text, fontSize, hidden = False):
        # Tag stating the current state of the button
        self.state = 0

        # Set the size of the button
        self.size = size

        # Tag to decide if the button is shown on screen
        self.hidden = hidden

        if size == 0:
            # Images for the different button states
            self.image_up = pg.image.load("Display/Textures/Button_Up.png").convert_alpha()
            self.image_hov = pg.image.load("Display/Textures/Button_Hov.png").convert_alpha()
            self.image_down = pg.image.load("Display/Textures/Button_Down.png").convert_alpha()
        
            # Surface for text on the button
            font = pg.font.SysFont("Jhomuria", fontSize)
            textSurface = font.render(text, True, (0, 0, 0)).convert_alpha()
            dims = textSurface.get_size()
            textPoint = (39 - dims[0] / 2, 22 - dims[1] / 2)

            # Rendering the text on each button image
            self.image_up.blit(textSurface, textPoint)
            self.image_hov.blit(textSurface, textPoint)
            self.image_down.blit(textSurface, (textPoint[0], textPoint[1] + 4))
        
        elif size == 1:
            # Images for the different button states
            self.image_up = pg.image.load("Display/Textures/L_Button_Up.png").convert_alpha()
            self.image_hov = pg.image.load("Display/Textures/L_Button_Hov.png").convert_alpha()
            self.image_down = pg.image.load("Display/Textures/L_Button_Down.png").convert_alpha()
        
            # Surface for text on the button
            font = pg.font.SysFont("Jhomuria", fontSize)
            textSurface = font.render(text, True, (0, 0, 0)).convert_alpha()
            dims = textSurface.get_size()
            textPoint = (79 - dims[0] / 2, 26 - dims[1] / 2)
        
            # Rendering the text on each button image
            self.image_up.blit(textSurface, textPoint)
            self.image_hov.blit(textSurface, textPoint)
            self.image_down.blit(textSurface, (textPoint[0], textPoint[1] + 4))

        self.set_position(centre)

    def set_position(self, centre):
        # Sets the centre point of the button
        self.centre = centre


        if self.size == 0:
            # Point where button is drawn
            self.draw_point = (centre[0] - 39, centre[1] - 20)

            # Hitbox for detecting mouse
            self.hitbox = ((centre[0] - 35, centre[1] - 20), (centre[0] + 35, centre[1] + 20))

        elif self.size == 1:
            # Point where button is drawn
            self.draw_point = (centre[0] - 79, centre[1] - 25)

            # Hitbox for detecting mouse
            self.hitbox = ((centre[0] - 75, centre[1] - 25), (centre[0] + 75, centre[1] + 25))


    def get_image(self):
        if self.state == 2: return self.image_down
        elif self.state == 1: return self.image_hov
        else: return self.image_up
        
    def get_state(self, mousePos):
        if self.hidden: return 0
        if self.hitbox[0][0] < mousePos[0] < self.hitbox[1][0] and self.hitbox[0][1] < mousePos[1] < self.hitbox[1][1]:
            if pg.mouse.get_pressed()[0]:
                self.state = 2
                return 2
            self.state = 1
            return 1
        self.state = 0
        return 0