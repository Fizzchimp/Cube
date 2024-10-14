import threading
import pygame as pg
from numpy import pi

from Display.display import Display
from cube_2 import Cube2
from cube_3 import Cube3

from Assets.solve_2 import solve_2
from Assets.solve_3 import solve_3
from Assets.cqueue import Queue
from thistlethwaite import thistle_solve

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
    "L", "L'",
    "E", "E'",
    "S", "S'",
    "M", "M'")

EDITING_COLS = {
    pg.K_w: "W",
    pg.K_g: "G",
    pg.K_r: "R",
    pg.K_b: "B",
    pg.K_o: "O",
    pg.K_y: "Y"}



HALF_PI = pi / 2
DOUBLE_PI = pi * 2

BOB_SPEED = 500
BOB_STRENGTH = WIDTH * 0.02

class World:
    def __init__(self):
        # Creating Cube object
        self.cube_type = 3
        self.cube_2 = Cube2(["BROO", "RGGB", "WBWR", "YWYB", "GWYO", "OGYR"])
        # self.cube_3 = Cube3(["WOWGWBWRW", "GWGOGRGYG", "RWRGRBRYR", "BWBRBOBYB", "OWOBOGOYO", "YRYGYBYOY"])
        self.cube_3 = Cube3(["WRWYRRROR", "GBBGGGBGB", "WYWRYWYYO", "GBBBBBGGG", "OWOOWYRWY", "RRYOOWOOY"])
        #self.cube_3 = Cube3(["GWBWWWGWB", "OGROGRGGG", "WRWGRBRRR", "RBORBOBBB", "WOWBOGOOO", "YYYYYYYYY"])
        # self.cube_3 = Cube3()
        # L' U2 R' U2 D2 R2 D2 L' F2 L D2 L'

        #self.cube_3.move("F", "L", "R'", "D2", "B2", "U")
        #self.cube_3.move("F2", "D2", "L", "R'", "F", "R2", "F", "B2", "R", "B'", "R2", "B", "R", "B")
        self.cube = getattr(self, f"cube_{self.cube_type}")
        
        # Initiating Pygame and display module
        pg.init()
        self.screen = Display(WIDTH, HEIGHT, BOB_STRENGTH, self.cube_type)
        self.clock = pg.time.Clock()
        self.move_queue = Queue(100)
        
        
        self.edit_pointer = -1
           
    # Organises Pathfinding for each cube
    def find_path(self, cube):
        if self.cube_type == 2:
            sNode, eNode = solve_2(cube)
            path = []
            
            if sNode == None:
                return False
            
            while sNode.parent != None:
                path.append(sNode.movement)
                sNode = sNode.parent
            path = path[::-1]

            while eNode.parent != None:
                path.append(eNode.movement)
                eNode = eNode.parent

            return path
        
        elif self.cube_type == 3:
            moves = thistle_solve(cube)
            return moves
    
    # Swap between 2 by 2 and 3 by 3
    def swap_cubes(self):
        if self.cube_type == 2:
            self.cube_type = 3
            self.cube = self.cube_3
            self.screen.cube_type = 3
            self.screen.model = self.screen.model_3
            if self.edit_pointer != -1:
                for button in self.screen.movement_buttons[12:]:
                    button.hidden = False
            
        elif self.cube_type == 3:
            self.cube_type = 2
            self.cube = self.cube_2
            self.screen.cube_type = 2
            self.screen.model = self.screen.model_2
            if self.edit_pointer != -1:
                for button in self.screen.movement_buttons[12:]:
                    button.hidden = True
    
    
    # Swaps between editing and solving
    def swap_editing(self):
        for face in self.cube.cube:
            if "-" in face:
                print("Not finished editing!")
                return
            
        if self.edit_pointer != -1:
            for button in self.screen.buttons + self.screen.movement_buttons[:12]:
                button.hidden = False
            if self.cube_type == 3:
                
                for button in self.screen.movement_buttons[12:]:
                    button.hidden = False
            
            self.screen.buttons[4].hidden = True
            self.screen.buttons[5].hidden = True
            self.edit_pointer = -1


        else:
            for button in self.screen.buttons + self.screen.movement_buttons:
                button.hidden = True
        
            self.screen.buttons[4].hidden = False
            self.screen.buttons[5].hidden = False
            self.edit_pointer = 0

    # Method to check if the program is in editing state
    def is_editing(self):
        if self.edit_pointer == -1:
            return False
        return True
    
    # Updates the edit pointer 
    def update_edit_pointer(self):
        self.edit_pointer += 1

        if (self.cube_type == 2 and self.edit_pointer >= 4) or self.edit_pointer == 9:
            self.do_move("Y")
            self.edit_pointer = 0


    # Executes a move on both cube data strucure and model
    def do_move(self, move, mod = None):
        if mod in SHIFT and move not in ("X", "X'", "Y", "Y'"): move += "'"
        move = move.replace("_Prime", "'").replace("_2", "2")
        self.cube.move(move)
        
        if move == "U": self.screen.model.uPhase = -HALF_PI
        elif move == "U'": self.screen.model.uPhase = HALF_PI
        elif move == "U2": self.screen.model.uPhase = -pi
            
        elif move == "R": self.screen.model.rPhase = HALF_PI
        elif move == "R'": self.screen.model.rPhase = -HALF_PI
        elif move == "R2": self.screen.model.rPhase = pi
            
        elif move == "F": self.screen.model.fPhase = -HALF_PI
        elif move == "F'": self.screen.model.fPhase = HALF_PI
        elif move == "F2": self.screen.model.fPhase = -pi
            
        elif move == "D": self.screen.model.dPhase = HALF_PI
        elif move == "D'": self.screen.model.dPhase = -HALF_PI
        elif move == "D2": self.screen.model.dPhase = pi
            
        elif move == "L": self.screen.model.lPhase = -HALF_PI
        elif move == "L'": self.screen.model.lPhase = HALF_PI
        elif move == "L2": self.screen.model.lPhase = -pi
            
        elif move == "B": self.screen.model.bPhase = HALF_PI
        elif move == "B'": self.screen.model.bPhase = -HALF_PI
        elif move == "B2": self.screen.model.bPhase = -pi
        
        elif move == "M": self.screen.model.mPhase = -HALF_PI
        elif move == "M'": self.screen.model.mPhase = HALF_PI
        
        elif move == "S": self.screen.model.sPhase = HALF_PI
        elif move == "S'": self.screen.model.sPhase = -HALF_PI
        
        elif move == "E": self.screen.model.ePhase = HALF_PI
        elif move == "E'": self.screen.model.ePhase = -HALF_PI
            
        elif move == "X": self.screen.model.xPhase = HALF_PI
        elif move == "X'": self.screen.model.xPhase = -HALF_PI
            
        elif move == "Y": self.screen.model.yPhase = -HALF_PI
        elif move == "Y'": self.screen.model.yPhase = HALF_PI
            
        elif move == "Z": self.screen.model.zPhase = -HALF_PI
        elif move == "Z'": self.screen.model.zPhase = HALF_PI

    # Handles all program events
    def handle_events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT: return False
                elif event.type == pg.KEYDOWN:
                    self.keyDown, self.key = True, event.key
                elif event.type == pg.KEYUP: self.keyDown = False
      
        
        if self.keyDown == True:
            if self.key == pg.K_ESCAPE: return False
                                   
            else:
                if not self.is_editing():
                    if not self.screen.model.isMoving() and self.key in MOVE_KEYS.keys():
                        self.do_move(MOVE_KEYS[self.key], pg.key.get_mods())
                    
                elif self.is_editing():
                    if not self.screen.model.isMoving() and self.key in EDITING_MOVES:
                        self.do_move(MOVE_KEYS[self.key], pg.key.get_mods())

                    if self.key in EDITING_COLS.keys():
                        self.cube.cube[2] = self.cube[2][:self.edit_pointer] + EDITING_COLS[self.key] + self.cube[2][self.edit_pointer + 1:]
                        self.update_edit_pointer()
                        self.key = None
                
        


        # Get any buttons that are pressed
        pressed = None
        mousePos = pg.mouse.get_pos()
        for i, button in enumerate(self.screen.buttons + self.screen.movement_buttons):
            if not button.hidden and button.get_state(mousePos) == 2:
                pressed = i
                
        if pressed != None and self.move_queue.is_empty() and not self.screen.model.isMoving():
            if not self.buttonDown:
                
                # Solve Button
                if pressed == 0:
                    solution = self.find_path(self.cube.cube)
                    if solution == False:
                        print("No solution")
                    elif solution == []:
                        print("Already Solved!")
                    else:
                        print(", ".join(solution))
                        for move in solution:
                            self.move_queue.enqueue(move)
                    self.clock.tick()
                    
                # Scramble Button
                elif pressed == 1:
                    moves = self.cube.scramble()
                    print(moves)
                    
                elif pressed == 2:
                    self.swap_cubes()
                
                elif pressed == 3 or pressed == 4:
                    self.swap_editing()
                    
                elif pressed == 5:
                    if self.cube_type == 2: self.cube.cube = ["----" for i in range(6)]
                    elif self.cube_type == 3: self.cube.cube = ["---------" for i in range(6)]
                    

                # Movement Buttons
                elif 0 <= pressed - len(self.screen.buttons) <= 17:
                    self.do_move(BUTTON_KEYS[pressed - len(self.screen.buttons)], False)
                    
                    
            self.buttonDown = True


        elif pressed == None:
            self.buttonDown = False
    
        return True
    
    
    def run(self):
        iter = 0
        
        # World loop
        self.keyDown = False
        self.key = None
        self.buttonDown = False

        delta_time = 0

        running = True
        self.clock.tick()
        while running:
            
            # Get and run input events (keys, buttons and others)
            running = self.handle_events()

            # Get moves from the movement queue
            if not self.move_queue.is_empty() and not self.screen.model.isMoving():
                move = self.move_queue.dequeue()
                self.do_move(move, False)
            
                
            # Update aspects of the screen
            
            self.screen.model.phaseUpdate((delta_time / ROTATION_SPEED) * HALF_PI)
            self.screen.cubeBob = (self.screen.cubeBob + delta_time / BOB_SPEED) % DOUBLE_PI
            
            self.screen.backgroundPosition[0] = (self.screen.backgroundPosition[0] + delta_time / BG_SPEED) % 90 - 90
            self.screen.backgroundPosition[1] = (self.screen.backgroundPosition[1] + delta_time / BG_SPEED) % 90 - 90
            
            iter += 1
            if iter % MAX_FPS == 0:
                pg.display.set_caption(str(self.clock.get_fps()))
            
            # Draw the screen
            self.screen.drawScreen(self.cube.cube, delta_time, self.edit_pointer)

            delta_time = self.clock.tick(MAX_FPS)
            

        pg.quit()

world = World()
world.run()