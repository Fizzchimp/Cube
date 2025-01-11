try:
    import pygame as pg
    from numpy import pi
    
except:
    import pip
    pip.main(["install", "pygame"])
    pip.main(["install", "numpy"])
    print("MODULES INSTALLED. CLOSE AND RUN PROGRAM AGAIN")
    exit()
    
    

from Display.display import Display
from cube_2 import Cube2
from cube_3 import Cube3

from Assets.solve_2 import solve_2
from Assets.cqueue import Queue
from Thistlethwaite.thistlethwaite import thistle_solve
      
MAX_FPS = 200
ROTATION_SPEED = 12
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
        
        # 2 by 2 cube object
        self.cube_2 = Cube2()
        
        # 3 by 3 cube object
        self.cube_3 = Cube3()

    
        # Sets the current cube to one of the cube objects
        self.cube = getattr(self, f"cube_{self.cube_type}")
        
        # Initiating Pygame
        pg.init()

        # Initiate display module
        self.screen = Display(WIDTH, HEIGHT, BOB_STRENGTH, self.cube_type)

         # Clock to keep track of time and update frames accordingly
        self.clock = pg.time.Clock()

         # Queue of moves to be performed on the current cube
        self.move_queue = Queue(100)
        

        # Points to a facelet on the current cube that is being edited. Set to -1 when not on the editing screen
        self.edit_pointer = -1
        

        # Set when on the solving screen
        self.is_solving = False
           
    # Swaps between 2x2 and 3x3
    def swap_cubes(self):

        if self.cube_type == 2: # If cube type is 2 by 2, set current cube to 3 by 3
            self.cube_type = 3
            self.cube = self.cube_3

        elif self.cube_type == 3: # If cube type is 3 by 3, set current cube to 2 by 2
            self.cube_type = 2
            self.cube = self.cube_2
        
        # Tells the display class to swap cube models
        self.screen.swap_cubes()


    # Organises Pathfinding for each cube
    def solve(self):

        # Solving for 2 by 2 cube
        if self.cube_type == 2:
            solved = True
            solution = []
            
            # Check cube is not already solved
            for face in self.cube.cube:
                if not (face[0] == face[1] == face[2] == face[3]):
                    solved = False
                    break
            
            if not solved:
                # Executes meet in the middle BFS for the 2 by 2 cube
                sNode, eNode = solve_2(self.cube.cube)
            
                # If no path is found, return false to indicate the cube cannot be solved
                if sNode == None:
                    return False
            
                # Adds the move from each node at start tree
                while sNode.parent != None:
                    solution.append(sNode.movement)
                    sNode = sNode.parent

                # Reverse moves to correct order
                solution = solution[::-1]

                # Adds the move from each node at the end tree
                while eNode.parent != None:
                    solution.append(eNode.movement)
                    eNode = eNode.parent

        # Solving for 3 by 3
        elif self.cube_type == 3:
            # Execute thistlethwaite algorithm
            solution = thistle_solve(self.cube)
        

        # If algorithm returns none, cube is not solvable
        if solution == False:
            print("No solution")
        
        # If solution is blank, cube is already in solved state
        elif solution == []:
            print("Already Solved!")

        else:
            print(", ".join(solution))
            # Set the solution attribute to display solution on screen
            self.solution = solution
            self.solution_pointer = 0


        # print("Length:", len(self.solution))

         # Tick the clock to stop the cube jumping as large amount of time may have passed
        self.clock.tick()
        
        # Swap to solving screen
        self.swap_solving()
        
            
    # Swaps between solving and main screens   
    def swap_solving(self):

        # If already on solving screen, switch to main screen
        if self.is_solving:
            # Unhide main screen buttons
            for button in self.screen.main_buttons + self.screen.movement_buttons:
                button.hidden = False
            
            # Hide solving screen buttons
            for button in self.screen.solving_buttons:
                button.hidden = True
                
            # Attribute to tell if cube is solving
            self.is_solving = False
            
            # Reset cube positions to origional positions
            if self.cube_type == 2: self.screen.model.centre = [250, 300]
            if self.cube_type == 3: self.screen.model.centre = [450, 300]
            

        
        # If not on solving screen, switch to solving screen
        elif not self.is_solving:
            # Hide main screen buttons
            for button in self.screen.main_buttons + self.screen.movement_buttons:
                button.hidden = True
                
            # Unhide solving screen buttons (apart from previous move button)
            for button in self.screen.solving_buttons[1:]:
                button.hidden = False
                
            # Attribute to tell if cube is solving
            self.is_solving = True

            # Set cube centre to middle of screen
            self.screen.model.centre = [370, 250]

    

    ### EDITING
    # Swaps between editing and main screens
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
        events = pg.event.get()

        # Update all buttons on screen
        mouse_pos = pg.mouse.get_pos()
        for button in self.screen.main_buttons + self.screen.editing_buttons + self.screen.movement_buttons + self.screen.solving_buttons:
            button.get_state(mouse_pos)


        for event in events:
                if event.type == pg.QUIT: return False
                elif event.type == pg.KEYDOWN: self.keyDown, self.key = True, event.key
                elif event.type == pg.KEYUP: self.keyDown = False

                elif event.type == pg.MOUSEBUTTONDOWN:
                    # Main Buttons
                    if not self.is_editing() and self.is_solving == False:
                        if self.screen.main_buttons[0].state == 2:
                            self.solve()

                        if self.screen.main_buttons[1].state == 2:
                            moves = self.cube.scramble()
                            print(moves)

                        if self.screen.main_buttons[2].state == 2:
                            self.swap_cubes()
                        
                        if self.screen.main_buttons[3].state == 2:
                            self.swap_editing()


                    # Editing Buttons
                    if self.is_editing():
                        if self.screen.editing_buttons[0].state == 2:
                            self.swap_editing()


                        if self.screen.editing_buttons[1].state == 2:
                            if self.cube_type == 2: self.cube.cube = ["----" for i in range(6)]
                            elif self.cube_type == 3: self.cube.cube = ["---------" for i in range(6)]


                    # Solving Buttons
                    if self.is_solving:

                        # Previous move button
                        if self.screen.solving_buttons[0].state == 2:

                            self.screen.solving_buttons[1].hidden = False
                            if self.solution_pointer == 1: self.screen.solving_buttons[0].hidden = True

                            self.solution_pointer -= 1
                            move = self.solution[self.solution_pointer]
                            if len(move) == 1: move += "_Prime"
                            elif len(move) == 7:
                                move = move[0]
                            
                            try: self.move_queue.enqueue(move)
                            except: self.swap_solving()

                        # Next move button
                        if self.screen.solving_buttons[1].state == 2:
                            
                            self.screen.solving_buttons[0].hidden = False
                            if self.solution_pointer == len(self.solution) - 1: self.screen.solving_buttons[1].hidden = True
                            
                            try: self.move_queue.enqueue(self.solution[self.solution_pointer])
                            except: self.swap_solving()
                            self.solution_pointer += 1
                            
                        
                        if self.screen.solving_buttons[2].state == 2:
                            self.screen.solving_buttons[1].hidden = True
                            self.screen.solving_buttons[0].hidden = False
                            for move in self.solution[self.solution_pointer:]:
                                self.move_queue.enqueue(move)
                                self.solution_pointer = len(self.solution)
                        
                        if self.screen.solving_buttons[3].state == 2:
                            self.swap_solving()
                        


                    # Movement Buttons
                    if not self.is_editing() and self.is_solving == False:
                        for i, button in enumerate(self.screen.movement_buttons):
                            if button.state == 2:
                                self.do_move(BUTTON_KEYS[i], False)
        


        if self.keyDown == True:
            if self.key == pg.K_ESCAPE: return False
                                   
            else:
                if not self.is_editing() and not self.is_solving:
                    if not self.screen.model.is_moving() and self.move_queue.is_empty() and self.key in MOVE_KEYS.keys():
                        self.do_move(MOVE_KEYS[self.key], pg.key.get_mods())
                        
                    
                elif self.is_editing():
                    if not self.screen.model.is_moving() and self.key in EDITING_MOVES:
                        self.do_move(MOVE_KEYS[self.key], pg.key.get_mods())

                    # Editing events
                    elif self.key in EDITING_COLS.keys():
                        self.edit_cube_colour(EDITING_COLS[self.key])
                        self.update_edit_pointer()
                        self.key = None

                elif self.is_solving:
                    if not self.screen.model.is_moving() and self.key == pg.K_LEFT and self.solution_pointer > 0:
                        self.screen.solving_buttons[1].hidden = False
                        if self.solution_pointer == 1: self.screen.solving_buttons[0].hidden = True

                        self.solution_pointer -= 1
                        move = self.solution[self.solution_pointer]
                    
                        if len(move) == 1: move += "_Prime"
                        elif len(move) == 7: move = move[0]
                        
                        try: self.move_queue.enqueue(move)
                        except: self.swap_solving()
                        
                    elif not self.screen.model.is_moving() and self.key == pg.K_RIGHT and self.solution_pointer < len(self.solution):
                        self.screen.solving_buttons[0].hidden = False
                        if self.solution_pointer == len(self.solution) - 1: self.screen.solving_buttons[1].hidden = True
                        
                        try: self.move_queue.enqueue(self.solution[self.solution_pointer])
                        except: self.swap_solving()
                        self.solution_pointer += 1


        

                    

    
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
            
            # iter += 1
            # if iter % MAX_FPS == 0:
            #     pg.display.set_caption(str(self.clock.get_fps()))
            
            # Draw the screen
            if self.is_solving: self.screen.draw_screen(self.cube.cube, delta_time, self.edit_pointer, self.solution.copy(), self.solution_pointer)
            else: self.screen.draw_screen(self.cube.cube, delta_time, self.edit_pointer)    
            
            delta_time = self.clock.tick(MAX_FPS)

        pg.quit()

world = World()
world.run()