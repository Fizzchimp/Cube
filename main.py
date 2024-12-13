import pygame as pg
from numpy import pi

from Display.display import Display
from cube_2 import Cube2
from cube_3 import Cube3

from Assets.solve_2 import solve_2
from Assets.solve_3 import solve_3
from Assets.cqueue import Queue
from Thistlethwaite.thistlethwaite import thistle_solve
      
MAX_FPS = 200
ROTATION_SPEED = 125
BG_SPEED = 40

WIDTH = 700
HEIGHT = 700


SHIFT = (1, 2, 3)
MOVE_KEYS = {pg.K_u: "U",
             pg.K_r: "R",
             pg.K_f: "F",
             pg.K_d: "D",
             pg.K_l: "L",
             pg.K_b: "B",
             pg.K_m: "M",
             pg.K_s: "S",
             pg.K_e: "E",
             pg.K_LEFT: "Y",
             pg.K_RIGHT: "Y'",
             pg.K_UP: "X",
             pg.K_DOWN: "X'",
             pg.K_z: "Z"}

EDITING_MOVES = (
    pg.K_LEFT,
    pg.K_RIGHT,
    pg.K_UP,
    pg.K_DOWN,
    pg.K_z)

BUTTON_KEYS = (
    "U", "U'",
    "F", "F'",
    "R", "R'",
    "D", "D'",
    "B", "B'",
    "L", "L'")

EDITING_COLS = {
    pg.K_w: "W",
    pg.K_g: "G",
    pg.K_r: "R",
    pg.K_b: "B",
    pg.K_o: "O",
    pg.K_y: "Y"}



HALF_PI = pi / 2
DOUBLE_PI = pi * 2

BOB_SPEED = 600
BOB_STRENGTH = WIDTH * 0.015

class World:
    def __init__(self):
        # Tells the program what the current cube is
        self.cube_type = 3
        
        self.cube_2 = Cube2()
        
        # self.cube_3 = Cube3(['OYWYWOOWY', 'GBGGBGGBB', 'YRRYRROOO', 'BGBGGBBBG', 'RRWROWROR', 'WYYOYWYWW']) # No move table in phase 3
        # self.cube_3 = Cube3(['RWYWYRRYW', 'BBBGGBBBG', 'YRRYRROOO', 'GBGGBGGGB', 'RRWOOYOOO', 'YWWOWWYYW']) # No move table in phase 3
        self.cube_3 = Cube3()

    
        # Sets the current cube to one of the cube objects
        self.cube = getattr(self, f"cube_{self.cube_type}")
        
        # Initiating Pygame and display module
        pg.init()
        self.screen = Display(WIDTH, HEIGHT, BOB_STRENGTH, self.cube_type)
        self.clock = pg.time.Clock() # Clock to keep track of time and update frames accordingly
        self.move_queue = Queue(100) # Queue of moves to be performed on the current cube
        

        # Points to a facelet on the current cube that is being edited. Set to -1 when not on the editing screen
        self.edit_pointer = -1
        

        # Set when on the solving screen
        self.is_solving = False
           
    # Swaps between 2x2 and 3x3
    def swap_cubes(self):

        # Changes the cube type, and sets the current cube structure accordingly
        if self.cube_type == 2:
            self.cube_type = 3
            self.cube = self.cube_3

        elif self.cube_type == 3:
            self.cube_type = 2
            self.cube = self.cube_2
        
        # Tells the display class to swap cube models
        self.screen.swap_cubes()


    ### SOLVING
    # Organises Pathfinding for each cube
    def solve(self):

        if self.cube_type == 2:
            # Executes meet in the middle BFS for the 2 by 2 cube
            solved = True
            moves = []
            for face in self.cube.cube:
                if not (face[0] == face[1] == face[2] == face[3]):
                    solved = False
                    break
            
            if not solved:
                sNode, eNode = solve_2(self.cube.cube)
            
                # If no path is found, return false to indicate the cube cannot be solved
                if sNode == None:
                    return False
            
                # Adds the move from each node at the start node chain then reverse it.
                while sNode.parent != None:
                    moves.append(sNode.movement)
                    sNode = sNode.parent
                moves = moves[::-1]

                # Adds the move from each node at the end chain to the move path
                while eNode.parent != None:
                    moves.append(eNode.movement)
                    eNode = eNode.parent

        
        # Executes the thistlethwaite solver for the 3 by 3 cube
        elif self.cube_type == 3:
            moves = thistle_solve(self.cube)
        


        if moves == False:
            print("No solution")
        elif moves == []:
            print("Already Solved!")
        else:
            print(", ".join(moves))
            for move in moves:
                self.move_queue.enqueue(move)


        self.clock.tick() # Tick the clock to stop the cube jumping as large amount of time may have passed
        
        self.swap_solving()
        return
        
    def swap_solving(self):
        if self.is_solving:
            for button in self.screen.main_buttons + self.screen.movement_buttons:
                button.hidden = False
            
            for button in self.screen.solving_buttons:
                button.hidden = True
                
            self.is_solving = False
        

        elif not self.is_solving:
            for button in self.screen.main_buttons + self.screen.movement_buttons:
                button.hidden = True
                
            for button in self.screen.solving_buttons:
                button.hidden = False
                
            self.is_solving = True

    



    ### EDITING
    # Swaps between editing and solving
    def swap_editing(self):
        for face in self.cube.cube:
            if "-" in face:
                print("Not finished editing!")
                return
            
        if self.edit_pointer != -1:
            for button in self.screen.main_buttons + self.screen.movement_buttons:
                button.hidden = False
            if self.cube_type == 3:
                
                for button in self.screen.movement_buttons[12:]:
                    button.hidden = False
            
            self.screen.editing_buttons[0].hidden = True
            self.screen.editing_buttons[1].hidden = True
            self.edit_pointer = -1
            self.screen.model.centre = [200 * self.cube_type - 150, 300]


        else:
            for button in self.screen.main_buttons + self.screen.movement_buttons:
                button.hidden = True
        
            self.screen.editing_buttons[0].hidden = False
            self.screen.editing_buttons[1].hidden = False
            self.screen.model.centre = [450, 250]
            self.edit_pointer = self.cube_type ** 2 * 2

    # Method to check if the program is in editing state
    def is_editing(self):
        if self.edit_pointer == -1:
            return False
        return True
    
    # Updates the edit pointer 
    def update_edit_pointer(self):
        self.edit_pointer += 1

        if self.edit_pointer == self.cube_type ** 2 * 3:
            self.do_move("Y")
            self.edit_pointer = self.cube_type ** 2 * 2

    # Edits the facelet of one colour
    def edit_cube_colour(self, colour):
        editing_face = self.cube[self.edit_pointer // (self.cube_type ** 2)]

        facelet_pointer = self.edit_pointer % (self.cube_type ** 2)

        first_half = editing_face[:facelet_pointer]
        second_half = editing_face[facelet_pointer + 1:]

        self.cube.cube[self.edit_pointer // (self.cube_type ** 2)] = first_half + colour + second_half
    
    


    # Executes a move on both cube data strucure and model
    def do_move(self, move, mod = None):
        if mod in SHIFT and move not in ("X", "X'", "Y", "Y'"): move += "'"
        move = move.replace("_Prime", "'").replace("_2", "2")
        self.cube.move(move)
        
        if move == "U": self.screen.model.u_phase = -HALF_PI
        elif move == "U'": self.screen.model.u_phase = HALF_PI
        elif move == "U2": self.screen.model.u_phase = -pi
            
        elif move == "R": self.screen.model.r_phase = HALF_PI
        elif move == "R'": self.screen.model.r_phase = -HALF_PI
        elif move == "R2": self.screen.model.r_phase = pi
            
        elif move == "F": self.screen.model.f_phase = -HALF_PI
        elif move == "F'": self.screen.model.f_phase = HALF_PI
        elif move == "F2": self.screen.model.f_phase = -pi
            
        elif move == "D": self.screen.model.d_phase = HALF_PI
        elif move == "D'": self.screen.model.d_phase = -HALF_PI
        elif move == "D2": self.screen.model.d_phase = pi
            
        elif move == "L": self.screen.model.l_phase = -HALF_PI
        elif move == "L'": self.screen.model.l_phase = HALF_PI
        elif move == "L2": self.screen.model.l_phase = -pi
            
        elif move == "B": self.screen.model.b_phase = HALF_PI
        elif move == "B'": self.screen.model.b_phase = -HALF_PI
        elif move == "B2": self.screen.model.b_phase = -pi
        
        elif move == "M": self.screen.model.m_phase = -HALF_PI
        elif move == "M'": self.screen.model.m_phase = HALF_PI
        
        elif move == "S": self.screen.model.s_phase = HALF_PI
        elif move == "S'": self.screen.model.s_phase = -HALF_PI
        
        elif move == "E": self.screen.model.e_phase = HALF_PI
        elif move == "E'": self.screen.model.e_phase = -HALF_PI
            
        elif move == "X": self.screen.model.x_phase = HALF_PI
        elif move == "X'": self.screen.model.x_phase = -HALF_PI
            
        elif move == "Y": self.screen.model.y_phase = -HALF_PI
        elif move == "Y'": self.screen.model.y_phase = HALF_PI
            
        elif move == "Z": self.screen.model.z_phase = -HALF_PI
        elif move == "Z'": self.screen.model.z_phase = HALF_PI

    # Handles all program events
    def handle_events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT: return False
                elif event.type == pg.KEYDOWN:
                    if self.key == pg.K_q: self.cube.cube = self.cube.reflect_XZ()
                    self.keyDown, self.key = True, event.key
                elif event.type == pg.KEYUP: self.keyDown = False
      
        
        if self.keyDown == True:
            if self.key == pg.K_ESCAPE: return False
                                   
            else:
                if not self.is_editing():
                    if not self.screen.model.is_moving() and self.move_queue.is_empty() and self.key in MOVE_KEYS.keys():
                        self.do_move(MOVE_KEYS[self.key], pg.key.get_mods())
                    
                elif self.is_editing():
                    if not self.screen.model.is_moving() and self.key in EDITING_MOVES:
                        self.do_move(MOVE_KEYS[self.key], pg.key.get_mods())

                    # Editing events
                    if self.key in EDITING_COLS.keys():
                        self.edit_cube_colour(EDITING_COLS[self.key])
                        self.update_edit_pointer()
                        self.key = None
        


        mouse_pos = pg.mouse.get_pos()
        # Main Buttons
        if self.screen.main_buttons[0].get_state(mouse_pos) == 3:
            self.solve()

        if self.screen.main_buttons[1].get_state(mouse_pos) == 3:
            moves = self.cube.scramble()
            print(moves)

        if self.screen.main_buttons[2].get_state(mouse_pos) == 3:
            self.swap_cubes()

        # Editing Buttons
        if self.edit_pointer != -1:
            if self.screen.main_buttons[3].get_state(mouse_pos) == 3 or self.screen.editing_buttons[0].get_state(mouse_pos) == 3:
                self.swap_editing()

            if self.screen.editing_buttons[1].get_state(mouse_pos) == 3:
                if self.cube_type == 2: self.cube.cube = ["----" for i in range(6)]
                elif self.cube_type == 3: self.cube.cube = ["---------" for i in range(6)]


        # Solving Buttons
        if self.is_solving:
            if self.screen.solving_buttons[0].get_state(mouse_pos) == 3:
                pass
            
            if self.screen.solving_buttons[1].get_state(mouse_pos) == 3:
                pass
            
            if self.screen.solving_buttons[2].get_state(mouse_pos) == 3:
                pass
            
            if self.screen.solving_buttons[3].get_state(mouse_pos) == 3:
                self.swap_solving()
            


        # Movement Buttons
        if self.edit_pointer == -1:
            for i, button in enumerate(self.screen.movement_buttons):
                if button.get_state(mouse_pos) == 3:
                    self.do_move(BUTTON_KEYS[i], False)
                    

    
        return True
    
    # Main program loop
    def run(self):
        iter = 0
        
        # World loop
        self.keyDown = False
        self.key = None

        delta_time = 0

        running = True
        self.clock.tick()
        while running:
            
            # Get and run input events (keys, buttons and others)
            running = self.handle_events()

            # Get moves from the movement queue
            if not self.move_queue.is_empty() and not self.screen.model.is_moving():
                move = self.move_queue.dequeue()
                self.do_move(move, False)
            
                
            # Update aspects of the screen
            self.screen.model.update_phase((delta_time / ROTATION_SPEED) * HALF_PI)
            self.screen.cubeBob = (self.screen.cubeBob + delta_time / BOB_SPEED) % DOUBLE_PI
            
            # self.screen.backgroundPosition[0] = (self.screen.backgroundPosition[0] + delta_time / BG_SPEED) % 90 - 90
            # self.screen.backgroundPosition[1] = (self.screen.backgroundPosition[1] + delta_time / BG_SPEED) % 90 - 90
            
            iter += 1
            if iter % MAX_FPS == 0:
                pg.display.set_caption(str(self.clock.get_fps()))
            
            # Draw the screen
            self.screen.draw_screen(self.cube.cube, delta_time, self.edit_pointer)

            delta_time = self.clock.tick(MAX_FPS)

        pg.quit()

world = World()
world.run()