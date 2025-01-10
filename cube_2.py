import random as rnd

class Cube2():
    def __init__(self, cube = None):
        # Representation of cube as an array
        self.cube = cube if cube != None else [
            "WWWW", # Top face
                        
            "GGGG", # Right face
            "RRRR", # Front face
            "BBBB", # Left face
            "OOOO", # Back face

            "YYYY"] # Bottom face
        
    
    def display(self):
        # Display the cube in net form
        print(f"""
   |{self.cube[0][:2]}|
   |{self.cube[0][2:4]}|
|{self.cube[1][:2]}|{self.cube[2][:2]}|{self.cube[3][:2]}|{self.cube[4][:2]}|
|{self.cube[1][2:4]}|{self.cube[2][2:4]}|{self.cube[3][2:4]}|{self.cube[4][2:4]}|
   |{self.cube[5][:2]}|
   |{self.cube[5][2:4]}|""")
   
    # Allows object to be indexed and return attribute structure
    def __getitem__(self, index):
        return self.cube[index]
        

    def U(self):
        # Returns rotation U clockwise
        return [self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1],
                
                self.cube[2][:2] + self.cube[1][2:4],
                self.cube[3][:2] + self.cube[2][2:4],
                self.cube[4][:2] + self.cube[3][2:4],
                self.cube[1][:2] + self.cube[4][2:4],
                
                self.cube[5]]

    def U_Prime(self):
        # Return rotation U anticlockwise
        return [self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2],
                
                self.cube[4][:2] + self.cube[1][2:4],
                self.cube[1][:2] + self.cube[2][2:4],
                self.cube[2][:2] + self.cube[3][2:4],
                self.cube[3][:2] + self.cube[4][2:4],
                
                self.cube[5]]


    def D(self):
        # Returns rotation D clockwise
        return [self.cube[0],
                
                self.cube[1][:2] + self.cube[4][2:4],
                self.cube[2][:2] + self.cube[1][2:4],
                self.cube[3][:2] + self.cube[2][2:4],
                self.cube[4][:2] + self.cube[3][2:4],
                
                self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1]]

    def D_Prime(self):
        # Returns rotation D anticlockwise
        return [self.cube[0],
                
                self.cube[1][:2] + self.cube[2][2:4],
                self.cube[2][:2] + self.cube[3][2:4],
                self.cube[3][:2] + self.cube[4][2:4],
                self.cube[4][:2] + self.cube[1][2:4],

                self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2]]


    def F(self):
        # Returns rotation F clockwise
        return [self.cube[0][:2] + self.cube[1][3] + self.cube[1][1],
                
                self.cube[1][0] + self.cube[5][0] + self.cube[1][2] + self.cube[5][1],
                self.cube[2][2] + self.cube[2][0] + self.cube[2][3] + self.cube[2][1],
                self.cube[0][2] + self.cube[3][1] + self.cube[0][3] + self.cube[3][3],
                self.cube[4],
                
                self.cube[3][2] + self.cube[3][0] + self.cube[5][2:4]]
    
    def F_Prime(self):
        # Returns rotation F anticlockwise
        return [self.cube[0][:2] + self.cube[3][0] + self.cube[3][2],
                
                self.cube[1][0] + self.cube[0][3] + self.cube[1][2] + self.cube[0][2],
                self.cube[2][1] + self.cube[2][3] + self.cube[2][0] + self.cube[2][2],
                self.cube[5][1] + self.cube[3][1] + self.cube[5][0] + self.cube[3][3],
                self.cube[4],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[5][2:4]]


    def B(self):
        # Returns rotation B clockwise
        return [self.cube[3][1] + self.cube[3][3] + self.cube[0][2:4],
                
                self.cube[0][1] + self.cube[1][1] + self.cube[0][0] + self.cube[1][3],
                self.cube[2],
                self.cube[3][0] + self.cube[5][3] + self.cube[3][2] + self.cube[5][2],
                self.cube[4][2] + self.cube[4][0] + self.cube[4][3] + self.cube[4][1],

                self.cube[5][:2] + self.cube[1][0] + self.cube[1][2]]
    
    def B_Prime(self):
        # Returns rotation B anticlockwise
        return [self.cube[1][2] + self.cube[1][0] + self.cube[0][2:4],
                
                self.cube[5][2] + self.cube[1][1] + self.cube[5][3] + self.cube[1][3],
                self.cube[2],
                self.cube[3][0] + self.cube[0][0] + self.cube[3][2] + self.cube[0][1],
                self.cube[4][1] + self.cube[4][3] + self.cube[4][0] + self.cube[4][2],

                self.cube[5][:2] + self.cube[3][3] + self.cube[3][1]]


    def L(self):
        # Returns rotation L clockwise
        return [self.cube[4][3] + self.cube[0][1] + self.cube[4][1] + self.cube[0][3],
                
                self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1],
                self.cube[0][0] + self.cube[2][1] + self.cube[0][2] + self.cube[2][3],
                self.cube[3],
                self.cube[4][0] + self.cube[5][2] + self.cube[4][2] + self.cube[5][0],

                self.cube[2][0] + self.cube[5][1] + self.cube[2][2] + self.cube[5][3]]

    def L_Prime(self):
        # Returns rotation L anticlockwise
        return [self.cube[2][0] + self.cube[0][1] + self.cube[2][2] + self.cube[0][3],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2],
                self.cube[5][0] + self.cube[2][1] + self.cube[5][2] + self.cube[2][3],
                self.cube[3],
                self.cube[4][0] + self.cube[0][2] + self.cube[4][2] + self.cube[0][0],
                
                self.cube[4][3] + self.cube[5][1] + self.cube[4][1] + self.cube[5][3]]
        

    def R(self):
        # Returns rotation R clockwise
        return [self.cube[0][0] + self.cube[2][1] + self.cube[0][2] + self.cube[2][3],

                self.cube[1],
                self.cube[2][0] + self.cube[5][1] + self.cube[2][2] + self.cube[5][3],
                self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1],
                self.cube[0][3] + self.cube[4][1] + self.cube[0][1] + self.cube[4][3],

                self.cube[5][0] + self.cube[4][2] + self.cube[5][2] + self.cube[4][0]]
        
    def R_Prime(self):
        # Returns rotation R anticlockwise
        return [self.cube[0][0] + self.cube[4][2] + self.cube[0][2] + self.cube[4][0],
                
                self.cube[1],
                self.cube[2][0] + self.cube[0][1] + self.cube[2][2] + self.cube[0][3],
                self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2],
                self.cube[5][3] + self.cube[4][1] + self.cube[5][1] + self.cube[4][3],

                self.cube[5][0] + self.cube[2][1] + self.cube[5][2] + self.cube[2][3]]


    def X(self):
        # Returns full 90 degree clockwise cube rotation about x axis
        return [self.cube[2],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2],
                self.cube[5],
                self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1],
                self.cube[0][::-1],
                
                self.cube[4][::-1]]

    def X_Prime(self):
        # Returns full 90 degree anticlockwise cube rotation about x axis
        return [self.cube[4][::-1],
                
                self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1],
                self.cube[0],
                self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2],
                self.cube[5][::-1],
                
                self.cube[2]]
    

    def Y(self):
        # Returns full 90 degree clockwise cube rotation about y axis
        return [self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1],
                
                self.cube[2],
                self.cube[3],
                self.cube[4],
                self.cube[1],
                
                self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2]]
    
    def Y_Prime(self):
        # Returns full 90 degree anticlockwise cube rotation about y axis
        return [self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2],
                
                self.cube[4],
                self.cube[1],
                self.cube[2],
                self.cube[3],
                
                self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1]]
    

    def Z(self):
        # Returns full 90 degree clockwise cube rotation about z axis
        return [self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1],
                
                self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1],
                self.cube[2][2] + self.cube[2][0] + self.cube[2][3] + self.cube[2][1],
                self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1],
                self.cube[4][1] + self.cube[4][3] + self.cube[4][0] + self.cube[4][2],

                self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1]]
    
    def Z_Prime(self):
        # Returns full 90 degree anticlockwise cube rotation about z axis
        return [self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2],
                
                self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2],
                self.cube[2][1] + self.cube[2][3] + self.cube[2][0] + self.cube[2][2],
                self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2],
                self.cube[4][2] + self.cube[4][0] + self.cube[4][3] + self.cube[4][1],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2]]
    
    
    def move(self, *moves):
        # Executes given moves on the cube
        for move in moves:
            try: self.cube = getattr(self, move)()
            except AttributeError: # If move not an attribute, try translating
                move = move.replace("'", "_Prime").replace("2", "_2")
                try: self.cube = getattr(self, move)() # If still not an attribute, entered move is not valid
                except AttributeError: print(f"'{move}' not a valid movement")

        else: print("Not a valid movement")

    def scramble(self, num = 20):
        # Scrambles the cube to a random position
        moves = []
        for i in range(num):
            move = rnd.choice(["U", "D", "F", "B", "R", "L"]) + rnd.choice(["'", ""])
            moves.append(move)
            self.move(move)
        return moves