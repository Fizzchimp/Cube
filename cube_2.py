import random as rnd

class Cube2():
    def __init__(self, cube = None):
        # Representation of cube as an array
        self.cube = cube if cube != None else [
            "WWWW", # Top face
                        
            "GGGG", # Left face
            "RRRR", # Front face
            "BBBB", # Right face
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
        


    # Returns rotation U clockwise
    def U(self):
        return [self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1],
                
                self.cube[2][:2] + self.cube[1][2:4],
                self.cube[3][:2] + self.cube[2][2:4],
                self.cube[4][:2] + self.cube[3][2:4],
                self.cube[1][:2] + self.cube[4][2:4],
                
                self.cube[5]]
    
    # Return rotation U anticlockwise
    def U_Prime(self):
        return [self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2],
                
                self.cube[4][:2] + self.cube[1][2:4],
                self.cube[1][:2] + self.cube[2][2:4],
                self.cube[2][:2] + self.cube[3][2:4],
                self.cube[3][:2] + self.cube[4][2:4],
                
                self.cube[5]]



    # Returns rotation D clockwise
    def D(self):
        return [self.cube[0],
                
                self.cube[1][:2] + self.cube[4][2:4],
                self.cube[2][:2] + self.cube[1][2:4],
                self.cube[3][:2] + self.cube[2][2:4],
                self.cube[4][:2] + self.cube[3][2:4],
                
                self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1]]

    # Returns rotation D anticlockwise
    def D_Prime(self):
        return [self.cube[0],
                
                self.cube[1][:2] + self.cube[2][2:4],
                self.cube[2][:2] + self.cube[3][2:4],
                self.cube[3][:2] + self.cube[4][2:4],
                self.cube[4][:2] + self.cube[1][2:4],

                self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2]]



    # Returns rotation F clockwise
    def F(self):
        return [self.cube[0][:2] + self.cube[1][3] + self.cube[1][1],
                
                self.cube[1][0] + self.cube[5][0] + self.cube[1][2] + self.cube[5][1],
                self.cube[2][2] + self.cube[2][0] + self.cube[2][3] + self.cube[2][1],
                self.cube[0][2] + self.cube[3][1] + self.cube[0][3] + self.cube[3][3],
                self.cube[4],
                
                self.cube[3][2] + self.cube[3][0] + self.cube[5][2:4]]
    
    # Returns rotation F anticlockwise
    def F_Prime(self):
        return [self.cube[0][:2] + self.cube[3][0] + self.cube[3][2],
                
                self.cube[1][0] + self.cube[0][3] + self.cube[1][2] + self.cube[0][2],
                self.cube[2][1] + self.cube[2][3] + self.cube[2][0] + self.cube[2][2],
                self.cube[5][1] + self.cube[3][1] + self.cube[5][0] + self.cube[3][3],
                self.cube[4],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[5][2:4]]



    # Returns rotation B clockwise
    def B(self):
        return [self.cube[3][1] + self.cube[3][3] + self.cube[0][2:4],
                
                self.cube[0][1] + self.cube[1][1] + self.cube[0][0] + self.cube[1][3],
                self.cube[2],
                self.cube[3][0] + self.cube[5][3] + self.cube[3][2] + self.cube[5][2],
                self.cube[4][2] + self.cube[4][0] + self.cube[4][3] + self.cube[4][1],

                self.cube[5][:2] + self.cube[1][0] + self.cube[1][2]]
    
    # Returns rotation B anticlockwise
    def B_Prime(self):
        return [self.cube[1][2] + self.cube[1][0] + self.cube[0][2:4],
                
                self.cube[5][2] + self.cube[1][1] + self.cube[5][3] + self.cube[1][3],
                self.cube[2],
                self.cube[3][0] + self.cube[0][0] + self.cube[3][2] + self.cube[0][1],
                self.cube[4][1] + self.cube[4][3] + self.cube[4][0] + self.cube[4][2],

                self.cube[5][:2] + self.cube[3][3] + self.cube[3][1]]



    # Returns rotation L clockwise
    def L(self):
        return [self.cube[4][3] + self.cube[0][1] + self.cube[4][1] + self.cube[0][3],
                
                self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1],
                self.cube[0][0] + self.cube[2][1] + self.cube[0][2] + self.cube[2][3],
                self.cube[3],
                self.cube[4][0] + self.cube[5][2] + self.cube[4][2] + self.cube[5][0],

                self.cube[2][0] + self.cube[5][1] + self.cube[2][2] + self.cube[5][3]]

    # Returns rotation L anticlockwise
    def L_Prime(self):
        return [self.cube[2][0] + self.cube[0][1] + self.cube[2][2] + self.cube[0][3],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2],
                self.cube[5][0] + self.cube[2][1] + self.cube[5][2] + self.cube[2][3],
                self.cube[3],
                self.cube[4][0] + self.cube[0][2] + self.cube[4][2] + self.cube[0][0],
                
                self.cube[4][3] + self.cube[5][1] + self.cube[4][1] + self.cube[5][3]]
        


    # Returns rotation R clockwise
    def R(self):
        return [self.cube[0][0] + self.cube[2][1] + self.cube[0][2] + self.cube[2][3],

                self.cube[1],
                self.cube[2][0] + self.cube[5][1] + self.cube[2][2] + self.cube[5][3],
                self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1],
                self.cube[0][3] + self.cube[4][1] + self.cube[0][1] + self.cube[4][3],

                self.cube[5][0] + self.cube[4][2] + self.cube[5][2] + self.cube[4][0]]
    
    # Returns rotation R anticlockwise
    def R_Prime(self):
        return [self.cube[0][0] + self.cube[4][2] + self.cube[0][2] + self.cube[4][0],
                
                self.cube[1],
                self.cube[2][0] + self.cube[0][1] + self.cube[2][2] + self.cube[0][3],
                self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2],
                self.cube[5][3] + self.cube[4][1] + self.cube[5][1] + self.cube[4][3],

                self.cube[5][0] + self.cube[2][1] + self.cube[5][2] + self.cube[2][3]]



    # Returns full 90 degree clockwise cube rotation about x axis
    def X(self):
        return [self.cube[2],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2],
                self.cube[5],
                self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1],
                self.cube[0][::-1],
                
                self.cube[4][::-1]]

    # Returns full 90 degree anticlockwise cube rotation about x axis
    def X_Prime(self):
        return [self.cube[4][::-1],
                
                self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1],
                self.cube[0],
                self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2],
                self.cube[5][::-1],
                
                self.cube[2]]
    


    # Returns full 90 degree clockwise cube rotation about y axis
    def Y(self):
        return [self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1],
                
                self.cube[2],
                self.cube[3],
                self.cube[4],
                self.cube[1],
                
                self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2]]
    
    # Returns full 90 degree anticlockwise cube rotation about y axis
    def Y_Prime(self):
        return [self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2],
                
                self.cube[4],
                self.cube[1],
                self.cube[2],
                self.cube[3],
                
                self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1]]
    


    # Returns full 90 degree clockwise cube rotation about z axis
    def Z(self):
        return [self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1],
                
                self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1],
                self.cube[2][2] + self.cube[2][0] + self.cube[2][3] + self.cube[2][1],
                self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1],
                self.cube[4][1] + self.cube[4][3] + self.cube[4][0] + self.cube[4][2],

                self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1]]
    
    # Returns full 90 degree anticlockwise cube rotation about z axis
    def Z_Prime(self):
        return [self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2],
                
                self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2],
                self.cube[2][1] + self.cube[2][3] + self.cube[2][0] + self.cube[2][2],
                self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2],
                self.cube[4][2] + self.cube[4][0] + self.cube[4][3] + self.cube[4][1],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2]]
    


    # Executes given moves on the cube
    def move(self, *moves):  
        for move in moves:
            try: self.cube = getattr(self, move)()
            # If move not an attribute, try translating
            except AttributeError: 
                move = move.replace("'", "_Prime").replace("2", "_2")
                try: self.cube = getattr(self, move)()
                # If still not an attribute, entered move is not valid
                except AttributeError: print(f"'{move}' not a valid movement")



    # Scrambles the cube to a random position
    def scramble(self, num = 20):
        # List of moves to be returned
        moves = []
        
        # Generate random moves and execute them on the cube
        for i in range(num):
            move = rnd.choice(["U", "D", "F", "B", "R", "L"]) + rnd.choice(["'", ""])
            moves.append(move)
            self.move(move)
            
        return moves