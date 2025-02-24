import pygame as pg
from pygame import gfxdraw
from Display.model_2 import Model2
from Display.model_3 import Model3
from numpy import sin, cos, sqrt, arctan2

# Keys used to interpret cube object into colours on the screen
colour_keys = {
    "W": (245, 245, 245),
    "Y": (255, 255, 50),
    "G": (50, 205, 50),
    "R": (220, 40, 60),
    "B": (80, 80, 205),
    "O": (255, 140, 0),
    "-": (150, 150, 150)}


# Key used to sort faces back to front
def depth(face):
    return face[-2]


# Controls how the screen is drawn
class Display():
    def __init__(self, width, height, bob_strength, cube_type):

        # Font used for moves in solving screen
        self.MOVE_FONT = pg.font.SysFont("", 80)


        # Setup the window
        self.screen = pg.display.set_mode([width, height])
        
        # Icon at top left corner of window
        pg.display.set_icon(pg.image.load("Display/Textures/icon.png"))

        # Caption at top left corner of window
        pg.display.set_caption("Cube")
    
        ### Cube
        # Dimensions for the cube
        self.length = width / 5 if width <= height else height / 5


        # Attributes to create little cube bobbing animation on screen
        self.cube_bob = 0 # Determines current displacement of cube
        self.bob_strength = bob_strength # Determines maximum displacement of cube


        # Determines the transparency of the editing facelet cover to create animation when editing
        self.edit_phase = 0
        
        # Model for 2 by 2 cube
        self.model_2 = Model2([250, 300])
        
        # Model for 3 by 3 cube
        self.model_3 = Model3([450, 300])
       
        # Used to determine the cube currently on screen
        self.cube_type = cube_type
        
        # Determine the current model being used
        if cube_type == 2: self.model = self.model_2
        elif cube_type == 3: self.model = self.model_3
        
        ### Buttons
        self.main_buttons = [ # Buttons at edges of screen
            Button((150, 625), 1 ,"SOLVE", 35), # Initiates solving
            Button((350, 625), 1 ,"SCRAMBLE", 35), # Scrambles the cube
            Button((350, 40), 1 ,"SWAP", 35), # Swaps between 2 by 2 and 3 by 3
            Button((550, 625), 1 ,"EDIT", 35)] # Goes to editing screen

        self.editing_buttons = [ # Buttons that appear on editing screen
            Button((550, 550), 1 ,"DONE", 35, True), # Returns to main screen with new cube
            Button((550, 630), 1 ,"CLEAR", 35, True)] # Clears all cube faces
        
        self.solving_buttons = [ # Buttons that appear on solving screen
            Button((150, 650), 0, "<-", 60, True), # Do next move
            Button((240, 650), 0, "->", 60, True), # Undo previous move
            Button((365, 650), 0, ">>", 60, True), # Do all moves left in solving sequence
            Button((550, 650), 1, "CANCEL", 35, True)] # Returns to the main screen
        
        self.movement_buttons = [ # Buttons that appear on main screen. Perform moves on current cube
            Button((45, 30), 0, "U", 47),
            Button((125, 30), 0, "U'", 47),
            Button((45, 80), 0, "F", 47),
            Button((125, 80), 0, "F'", 47),
            Button((45, 130), 0, "R", 47),
            Button((125, 130), 0, "R'", 47),
                         
            Button((45, 190), 0, "D", 47),
            Button((125, 190), 0, "D'", 47),
            Button((45, 240), 0, "B", 47),
            Button((125, 240), 0, "B'", 47),
            Button((45, 290), 0, "L", 47),
            Button((125, 290), 0, "L'", 47)]

    # Swaps between 2x2 and 3x3 cubes 
    def swap_cubes(self):
        if self.cube_type == 2: # If current cube is 2 by 2, swap to 3 by 3
            self.cube_type = 3
            self.model = self.model_3
            
            # Changes button positions
            for button in self.movement_buttons:
                button.set_position((button.centre[0] - 530, button.centre[1]))

        
        elif self.cube_type == 3: # If current cube is 3 by 3, swap to 2 by 2
            self.cube_type = 2
            self.model = self.model_2

            # Changes button positions
            for button in self.movement_buttons:
                button.set_position((button.centre[0] + 530, button.centre[1]))



    # Draws an antialiased line with given thickness (used in drawing the cube)
    def draw_line(self, colour, p1, p2, width):
        centre = ((p1[0] + p2[0]) / 2,
                  (p1[1] + p2[1]) / 2)
        
        # Get length of line
        length = sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        
        # Constants used in calcupper_leftating line corners
        angle = arctan2(p2[0] - p1[0], p2[1] - p1[1])
        cos_angle = cos(angle)
        sin_angle = sin(angle)

        sin_half_width = (width / 2) * sin_angle
        cos_half_width = (width / 2) * cos_angle

        sin_half_length = (length / 2) * sin_angle
        cos_half_length = (length / 2) * cos_angle
        
        # Positions of all 4 corners of the line
        upper_left =   (centre[0] + sin_half_length - cos_half_width,
                        centre[1] + cos_half_length + sin_half_width)
        upper_right =  (centre[0] - sin_half_length - cos_half_width,
                        centre[1] - cos_half_length + sin_half_width)
        bottom_left =  (centre[0] + sin_half_length + cos_half_width,
                        centre[1] + cos_half_length - sin_half_width)
        bottom_right = (centre[0] - sin_half_length + cos_half_width,
                        centre[1] - cos_half_length - sin_half_width)
        
        # Draw antialiased outline
        pg.gfxdraw.aapolygon(self.screen, (upper_left, upper_right, bottom_right, bottom_left), colour)
        # Fill the outline
        pg.gfxdraw.filled_polygon(self.screen, (upper_left, upper_right, bottom_right, bottom_left), colour)

    # Draws the current cube
    def draw_cube(self, cube, centre_offset = 0, edit_pointer = -1):
        # Centre coordinates of the drawn cube
        x, y, = self.model.centre[0], self.model.centre[1] + centre_offset

        # Get a list of faces to be drawn and assign colours
        model_points = self.model.get_points()
        draw_list = []
        for i, face in enumerate(model_points):
            for j, facelet in enumerate(face):
                if facelet[2][-1] <= 0: # If centre z vale < 0, facelet cant be seen and therefore doesnt need to be drawn
                    draw_list.append((( # 4 corners of drawn facelet
                            (facelet[0][0] * self.length + x, facelet[1][0] * self.length + y),
                            (facelet[0][1] * self.length + x, facelet[1][1] * self.length + y),
                            (facelet[0][2] * self.length + x, facelet[1][2] * self.length + y),
                            (facelet[0][3] * self.length + x, facelet[1][3] * self.length + y)),
                        sum(facelet[2]) / 4, # Depth value of centre of facelet
                        colour_keys[cube[i][j]])) # Colour of facelet
            

        # Draw the faces
        for face in sorted(draw_list, key = depth, reverse = True): # Sorts the faces back to front so front faces drawn on top
            gfxdraw.filled_polygon(self.screen, face[0], face[-1])

            # Draw antialiased outline around each facelet
            for i in range(4):
                self.draw_line((50, 50, 50), face[0][i], face[0][(i + 1) % 4], 8)
                pg.draw.circle(self.screen, (50, 50, 50), face[0][i], 4) # Rounds edges of outline off

        # Draw transparent editing indicator
        if edit_pointer != -1: # Check program is in editing state
            # Determine which facelet is being edited
            facelet = model_points[edit_pointer // (self.cube_type ** 2)][edit_pointer % (self.cube_type ** 2)]

            # Find points of facelet being edited
            edit_points = []
            for i in range(4):
                edit_points.append((facelet[0][i] * self.length + x, facelet[1][i] * self.length + y))

            # Draw a transparent cover over facelet being edited
            gfxdraw.filled_polygon(self.screen, edit_points, (0, 0, 0, 100 + 40 * sin(self.edit_phase)))

    # Draws the cube in net form (used in editing screen)
    def draw_net(self, start_pos, cube):
        # Determines width of drawn face
        face_width = 66

        # Detemines width of drawn facelet
        facelet_width = face_width // self.cube_type

        # Determines the gap between drawn facelets
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


    # Draws move sequence on solving screen
    def draw_moves(self, move_list, pointer):
        # Translate all move string (eg "U_Prime" -> "U'" and "D_2" -> "D2")
        for i, move in enumerate(move_list):
            if len(move) == 3: move_list[i] = move[0] + "2"
            elif len(move) == 7: move_list[i] = move[0] + "'"
            
        # Draw all previous moves
        for i, move in enumerate(move_list[:pointer][::-1]):
            if i > 2: break # Stops drawing moves off screen
            text_surface = self.MOVE_FONT.render(move, True, (120, 120, 120)).convert_alpha()
            self.screen.blit(text_surface, (210 - 100 * i, 530))

        # Draw current_move
        if pointer < len(move_list):
            text_surface = self.MOVE_FONT.render(move_list[pointer], True, (0, 0, 0)).convert_alpha()
            self.screen.blit(text_surface, (310, 530))
        
        # Draw next moves
        for i, move in enumerate(move_list[pointer + 1:]):
            if i > 2: break # Stops drawing moves off screen
            text_surface = self.MOVE_FONT.render(move, True, (120, 120, 120)).convert_alpha()
            self.screen.blit(text_surface, (410 + 100 * i, 530))



    # Organises drawing all elements on screen
    def draw_screen(self, cube, delta_time, edit_pointer = -1, solution = None, solution_pointer = None):
        # Clear the screen
        self.screen.fill((255, 255, 255))
        
        # Editing screen drawings
        if edit_pointer != -1:
            self.edit_phase += delta_time * 0.005 # Update edit phase for editing animation
            self.draw_net((50, 460), cube)# Draw cube in net form

        # Draw the cube onto the screen
        self.draw_cube(cube, self.bob_strength * sin(self.cube_bob), edit_pointer)

        # Draw all buttons on screen
        for button in self.main_buttons + self.editing_buttons + self.solving_buttons + self.movement_buttons:
            if not button.hidden: # Only draws buttons on current screen
                image = button.get_image()
                self.screen.blit(image, button.draw_point)
               
        # If on solving screen, draw move sequence
        if solution != None: self.draw_moves(solution, solution_pointer)
            
        # Update the display
        pg.display.flip()
    
class Button():
    def __init__(self, centre, size, text, fontSize, hidden = False):
        # Tag stating the current state of the button
        self.state = 0

        # Set the size of the button
        self.size = size

        # Tag to decide if the button is shown on current screen
        self.hidden = hidden


        # Small button properties
        if size == 0:
            # Images for the different button states
            self.image_up = pg.image.load("Display/Textures/Button_Up.png").convert_alpha()
            self.image_hov = pg.image.load("Display/Textures/Button_Hov.png").convert_alpha()
            self.image_down = pg.image.load("Display/Textures/Button_Down.png").convert_alpha()
        
            # Surface for text on the button
            font = pg.font.SysFont("", fontSize)
            textSurface = font.render(text, True, (0, 0, 0)).convert_alpha()
            dims = textSurface.get_size()
            textPoint = (39 - dims[0] / 2, 22 - dims[1] / 2)

            # Rendering the text on each button image
            self.image_up.blit(textSurface, textPoint)
            self.image_hov.blit(textSurface, textPoint)
            self.image_down.blit(textSurface, (textPoint[0], textPoint[1] + 4))
        

        # Large button properties
        elif size == 1: 
            # Images for the different button states
            self.image_up = pg.image.load("Display/Textures/L_Button_Up.png").convert_alpha()
            self.image_hov = pg.image.load("Display/Textures/L_Button_Hov.png").convert_alpha()
            self.image_down = pg.image.load("Display/Textures/L_Button_Down.png").convert_alpha()
        
            # Surface for text on the button
            font = pg.font.SysFont("", fontSize)
            textSurface = font.render(text, True, (0, 0, 0)).convert_alpha()
            dims = textSurface.get_size()
            textPoint = (79 - dims[0] / 2, 26 - dims[1] / 2)
        
            # Rendering the text on each button image
            self.image_up.blit(textSurface, textPoint)
            self.image_hov.blit(textSurface, textPoint)
            self.image_down.blit(textSurface, (textPoint[0], textPoint[1] + 4))


        # Set the position of the button
        self.set_position(centre)

    def set_position(self, centre):
        # Sets the centre point of the button
        self.centre = centre

        # Small button
        if self.size == 0:
            # Point where button is drawn
            self.draw_point = (centre[0] - 39, centre[1] - 20)

            # Hitbox for detecting mouse
            self.hitbox = ((centre[0] - 35, centre[1] - 20), (centre[0] + 35, centre[1] + 20))

        # Large button
        elif self.size == 1:
            # Point where button is drawn
            self.draw_point = (centre[0] - 79, centre[1] - 25)

            # Hitbox for detecting mouse
            self.hitbox = ((centre[0] - 75, centre[1] - 25), (centre[0] + 75, centre[1] + 25))


    # Get the current button image to be drawn on screen
    def get_image(self):
        if self.state == 2: return self.image_down
        elif self.state == 1: return self.image_hov
        else: return self.image_up
        
    # Determines the current state of the button
    def get_state(self, mousePos):
        # If not on current screen, state is 0
        if self.hidden:
            self.state = 0
            return 0
        
        # Determines if current mouse position is within button hitbox
        if self.hitbox[0][0] < mousePos[0] < self.hitbox[1][0] and self.hitbox[0][1] < mousePos[1] < self.hitbox[1][1]:
            if pg.mouse.get_pressed()[0]: # If mouse is pressed
                self.state = 2
                return 2
            self.state = 1
            return 1
        self.state = 0
        return 0
    