# Try and import pygame and numpy modules
try:
    import pygame as pg
    from numpy import pi

# If not installed, install then restart program
except:
    import pip
    pip.main(["install", "pygame"])
    pip.main(["install", "numpy"])
    print("MODULES INSTALLED. CLOSE AND RUN PROGRAM AGAIN")
    exit()
    
    
# Import used modules
from Display.display import Display
from cube_2 import Cube2
from cube_3 import Cube3

from Assets.solve_2 import solve_2
from Assets.cqueue import Queue
from Thistlethwaite.thistlethwaite import thistle_solve

# Maximum number of frames claculated per second
MAX_FPS = 100

# Time taken to complete one cube rotation in milliseconds
ROTATION_SPEED = 150


# Dimensions of the screen
WIDTH = 700
HEIGHT = 700

# Modifier values for shift key
SHIFT = (1, 2, 3)

# Keyboard inputs and corresponding moves
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
             pg.K_RIGHT: "Y_Prime",
             pg.K_UP: "X",
             pg.K_DOWN: "X_Prime",
             pg.K_z: "Z"}

# Keyboard inputs used in editing screen
EDITING_MOVES = (
    pg.K_LEFT,
    pg.K_RIGHT,
    pg.K_UP,
    pg.K_DOWN,
    pg.K_z)


# Values corresponding to movement buttons on main screen
BUTTON_KEYS = (
    "U", "U_Prime",
    "F", "F_Prime",
    "R", "R_Prime",
    "D", "D_Prime",
    "B", "B_Prime",
    "L", "L_Prime")


# Keyboard inputs and corresponding facelet colours used in editing screen
EDITING_COLS = {
    pg.K_w: "W",
    pg.K_g: "G",
    pg.K_r: "R",
    pg.K_b: "B",
    pg.K_o: "O",
    pg.K_y: "Y"}


# Constant used to rotate model
HALF_PI = pi / 2

# Constant used to animate cube bobbing
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
        self.cube_3 = Cube3(['BYGRWRROB', 'YBGBGWWGR', 'YWORROWGO', 'WYOGBBYYG', 'YBROOWWGO', 'BRBYYOGWR'])

    
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
           
        self.time_clock = pg.time.Clock()
        self.times = []
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



    ### SOLVING
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
                self.time_clock.tick()
                sNode, eNode = solve_2(self.cube.cube)
                time_taken = self.time_clock.tick()
                self.times.append(time_taken)
                print("Average time:", round(sum(self.times) / len(self.times), 2), "| Maximum time:", max(self.times))

            
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
            try:
                solution = thistle_solve(self.cube)
            except:
                solution = False

        # If algorithm returns none, cube is not solvable
        if solution == False:
            print("No solution!")
            return
        
        # If solution is blank, cube is already in solved state
        elif solution == []:
            print("Already Solved!")
            return

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
            
            # Reset cube position to origional position
            self.screen.model.centre = [200 * self.cube_type - 150, 300]
            

        
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

    # Undo the last move on the solving screen
    def prev_move(self):
        # Unhide next move button
        self.screen.solving_buttons[1].hidden = False

        # If last move in solution, hide next move button
        if self.solution_pointer == 1: self.screen.solving_buttons[0].hidden = True

        # Decrease current move pointer by 1
        self.solution_pointer -= 1

        # Get and reverse move (undo previous move)
        move = self.solution[self.solution_pointer]
        if len(move) == 1: move += "_Prime"
        elif len(move.replace("'", "_Prime")) == 7: move = move[0]
        
        # Add reversed move to move queue
        try: self.move_queue.enqueue(move)
        except: self.swap_solving()

    # Execute next move on solving screen
    def next_move(self):
        # Unhide previous move button
        self.screen.solving_buttons[0].hidden = False

        # If at first move in solution, hide hide previous move button
        if self.solution_pointer == len(self.solution) - 1: self.screen.solving_buttons[1].hidden = True
        
        # Add move to move queue
        self.move_queue.enqueue(self.solution[self.solution_pointer])

        # Increase current move pointer by 1
        self.solution_pointer += 1

    # Execute all remaining moves in solution
    def all_moves(self):
        # Hide next move button (at end of solution)
        self.screen.solving_buttons[1].hidden = True

        # Unhide previous move button
        self.screen.solving_buttons[0].hidden = False

        # Enqueue all moves from current move onwards to move queue
        for move in self.solution[self.solution_pointer:]:
            self.move_queue.enqueue(move)

            # Set current move pointer to end of solution
            self.solution_pointer = len(self.solution)



    ### EDITING
    # Swaps between editing and main screens
    def swap_editing(self):
        # Check there are no blank facelets on the cube
        for face in self.cube.cube:
            if "-" in face:
                # If any blank facelet, stay on editing screen
                print("Not finished editing!")
                return
            
        # If on editing screen
        if self.is_editing():
            # Unhide main screen buttons
            for button in self.screen.main_buttons + self.screen.movement_buttons:
                button.hidden = False
            
            # Hide editing screen buttons
            self.screen.editing_buttons[0].hidden = True
            self.screen.editing_buttons[1].hidden = True

            # Set the edit pointer to -1 to indicate not editing
            self.edit_pointer = -1

            # Reset cube position to origional position
            self.screen.model.centre = [200 * self.cube_type - 150, 300]

        # If on main screen
        else:
            # Hide all main screen buttons
            for button in self.screen.main_buttons + self.screen.movement_buttons:
                button.hidden = True
        
            # Unhide editing screen buttons
            self.screen.editing_buttons[0].hidden = False
            self.screen.editing_buttons[1].hidden = False

            # Set new cube position on screen
            self.screen.model.centre = [450, 250]

            # Set the edit pointer to the top left of the front face
            self.edit_pointer = self.cube_type ** 2 * 2

    # Method to check if the program is in editing state
    def is_editing(self):
        # When edit pointer is set to -1, program is not in editing state
        if self.edit_pointer == -1:
            return False
        return True

    # Updates the edit pointer 
    def update_edit_pointer(self):
        # Increment the edit pointer
        self.edit_pointer += 1

        # If edit pointer now points to facelet not on front face,
        if self.edit_pointer == self.cube_type ** 2 * 3:
            self.do_move("Y") # Rotate cube to next face
            self.edit_pointer = self.cube_type ** 2 * 2 # Set edit pointer to top left of front face

    # Edits the facelet of one colour
    def edit_cube_colour(self, colour):
        # Determine which face is being edited
        editing_face = self.cube[self.edit_pointer // (self.cube_type ** 2)]

        # Points at facelet being edited
        facelet_pointer = self.edit_pointer % (self.cube_type ** 2)

        first_half = editing_face[:facelet_pointer] # Get face string from start to facelet being edited
        second_half = editing_face[facelet_pointer + 1:] # Get face string from facelet being edited to end

        # Set the face on the cube to the first half plus the new facelet plus the second half
        self.cube.cube[self.edit_pointer // (self.cube_type ** 2)] = first_half + colour + second_half
    
    

    # Executes a move on both cube data strucure and model
    def do_move(self, move, mod = None):
        # Translate move into program notation
        move = move.replace("'", "_Prime").replace("_2", "-").replace("2", "_2").replace("-", "_2")

        # Apply shift modifier to move
        if mod in SHIFT and len(move) == 1 and move not in ("X", "Y"): move += "_Prime"
        
        # Execute move on cube object
        self.cube.move(move)
        
        # Get the angle of rotation for the model
        if move[0] in ("U", "F", "L", "M", "Y", "Z"):
            if len(move) == 1: rot_angle = -HALF_PI
            elif len(move) == 3: rot_angle = -pi
            elif len(move) == 7: rot_angle = HALF_PI

        elif move[0] in ("R", "D", "B", "S", "E", "X"):
            if len(move) == 1: rot_angle = HALF_PI
            elif len(move) == 3: rot_angle = pi
            elif len(move) == 7: rot_angle = -HALF_PI

        # Set the corresponding phase attribute to model
        setattr(self.screen.model, move[0].lower() + "_phase", rot_angle)

    # Handles all program events
    def handle_events(self):
        # Get all events in the pygame event queue
        events = pg.event.get()

        # Get the current mouse position
        mouse_pos = pg.mouse.get_pos()

        # Update the state of all buttons on screen
        for button in self.screen.main_buttons + self.screen.editing_buttons + self.screen.movement_buttons + self.screen.solving_buttons:
            button.get_state(mouse_pos)

        # Check each event
        for event in events:
                if event.type == pg.QUIT: return False # Exit program
                elif event.type == pg.KEYDOWN: self.key_down, self.key = True, event.key # Keyboard pressed
                elif event.type == pg.KEYUP: self.key_down = False # Keyboard released

                # Mouse click (check buttons)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    ## Main Buttons
                    if not self.is_editing() and self.is_solving == False:

                        # Solve button
                        if self.screen.main_buttons[0].state == 2:
                            self.solve()

                        # Scramble button
                        if self.screen.main_buttons[1].state == 2:
                            moves = self.cube.scramble()
                            print(moves)

                        # Swap cube button
                        if self.screen.main_buttons[2].state == 2:
                            self.swap_cubes()
                        
                        # Editing screen button
                        if self.screen.main_buttons[3].state == 2:
                            self.swap_editing()


                    ## Editing Buttons
                    if self.is_editing():
                        # Done button (back to main screen)
                        if self.screen.editing_buttons[0].state == 2:
                            self.swap_editing()

                        # Clear cube button
                        if self.screen.editing_buttons[1].state == 2:
                            self.cube.cube = ["-" * (self.cube_type ** 2) for i in range(6)]


                    # Solving Buttons
                    if self.is_solving:

                        # Previous move button
                        if self.screen.solving_buttons[0].state == 2 and not self.screen.model.is_moving():
                            # Undo previous move in solution
                            self.prev_move()


                        # Next move button
                        if self.screen.solving_buttons[1].state == 2 and not self.screen.model.is_moving():
                            # Execute next move in solution
                            self.next_move()
                            
                        
                        # All moves button
                        if self.screen.solving_buttons[2].state == 2:
                            # Execute all remaining moves in solution
                            self.all_moves()
                        
                        
                        # Cancel button
                        if self.screen.solving_buttons[3].state == 2 and self.move_queue.is_empty():
                            # Return to main screen
                            self.swap_solving()
                        


                    # Movement Buttons
                    if not self.is_editing() and self.is_solving == False:
                        # Check all move buttons
                        for i, button in enumerate(self.screen.movement_buttons):
                            if button.state == 2:
                                # Perform corresponding move to cube object and model
                                self.do_move(BUTTON_KEYS[i], False)
        

        # Keyboard pressed
        if self.key_down == True:
            # Exit the program
            if self.key == pg.K_ESCAPE: return False
                                   
            else:
                # Move the cube with movement keys
                if not self.is_editing() and not self.is_solving:
                    # Check the cube is not already moving and there are no moves in the queue
                    if not self.screen.model.is_moving() and self.move_queue.is_empty() and self.key in MOVE_KEYS.keys():
                        # Execute move on cube object and model
                        self.do_move(MOVE_KEYS[self.key], pg.key.get_mods())
                        
                # Editing screen keys
                elif self.is_editing():
                    # Rotate whole cube
                    if not self.screen.model.is_moving() and self.key in EDITING_MOVES:
                        # Perform move on cube object and model
                        self.do_move(MOVE_KEYS[self.key], pg.key.get_mods())

                    # Change the colour of the selected facelet
                    elif self.key in EDITING_COLS.keys():
                        # Get the selected colour
                        self.edit_cube_colour(EDITING_COLS[self.key])
                        
                        # Change the colour of the facelet
                        self.update_edit_pointer()
                        
                        # Reset key attribute
                        self.key = None

                # Solving screen keys
                elif self.is_solving and not self.screen.model.is_moving():

                    # Previous move key
                    if self.key == pg.K_LEFT and self.solution_pointer > 0:
                        # Undo previous move in solution
                        self.prev_move()
                        
                    elif self.key == pg.K_RIGHT and self.solution_pointer < len(self.solution):
                        # Execute next move in solution
                        self.next_move()

                    elif self.key == pg.K_RETURN:
                        # Execute all remaining moves in solution
                        self.all_moves()

        # Return true to indicate program still running
        return True
    
    # Main program loop
    def run(self):
        
        # Indicates if a key is being pressed
        self.key_down = False
        # Indicates what key is being pressed
        self.key = None

        # Indicates when to exit program
        running = True

        # Tick the clock to start timing
        self.clock.tick()

        # Time passed between frames
        delta_time = 0

        # Main loop
        while running:

            # Get and run input events (keys, buttons and others)
            running = self.handle_events()

            # Execute moves from the movement queue
            if not self.move_queue.is_empty() and not self.screen.model.is_moving():
                move = self.move_queue.dequeue()
                self.do_move(move, False)
                    

            # Update phase attributes of current model
            self.screen.model.update_phase((delta_time / ROTATION_SPEED) * HALF_PI)

            # Update the position of the cube model
            self.screen.cubeBob = (self.screen.cubeBob + delta_time / BOB_SPEED) % DOUBLE_PI
            

            # Draw the screen
            if self.is_solving: self.screen.draw_screen(self.cube.cube, delta_time, self.edit_pointer, self.solution.copy(), self.solution_pointer)
            else: self.screen.draw_screen(self.cube.cube, delta_time, self.edit_pointer)    
            
            # Get time taken to process frame
            delta_time = self.clock.tick(MAX_FPS)

        # When loop ends, exit the program
        pg.quit()


world = World()
world.swap_cubes()
for i in range(1000):
    world.cube.scramble()
    world.solve()
world.run()
