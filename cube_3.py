import random as rnd


class Cube3():
    def __init__(self, cube = None):
        # Representation of cube as an array
        self.cube = cube if cube != None else [
            "WWWWWWWWW", # Top face

            "GGGGGGGGG", # Left face
            "RRRRRRRRR", # Front face
            "BBBBBBBBB", # Right face
            "OOOOOOOOO", # Back face

            "YYYYYYYYY"] # Bottom face
        

    def display(self):
        # Display the cube in net form
        print(f"""
    |{self[0][:3]}|
    |{self[0][3:6]}|
    |{self[0][6:]}|
|{self[1][:3]}|{self[2][:3]}|{self[3][:3]}|{self[4][:3]}|
|{self[1][3:6]}|{self[2][3:6]}|{self[3][3:6]}|{self[4][3:6]}|
|{self[1][6:]}|{self[2][6:]}|{self[3][6:]}|{self[4][6:]}|
    |{self[5][:3]}|
    |{self[5][3:6]}|
    |{self[5][6:]}|""")
        
    # Allows object to be indexed and return attribute structure
    def __getitem__(self, index):
        return self.cube[index]
    


    # Returns full 90 degree clockwise cube rotation about x axis
    def X(self):
        return [self[2],
                
                self[1][2] + self[1][5] + self[1][8] + self[1][1] + self[1][4] + self[1][7] + self[1][0] + self[1][3] + self[1][6],
                self[5],
                self[3][6] + self[3][3] + self[3][0] + self[3][7] + self[3][4] + self[3][1] + self[3][8] + self[3][5] + self[3][2],
                self[0][::-1],
                
                self[4][::-1]]
    
    # Returns full 90 degree anticlockwise cube rotation about x axis
    def X_Prime(self):
        return [self[4][::-1],
                
                self[1][6] + self[1][3] + self[1][0] + self[1][7] + self[1][4] + self[1][1] + self[1][8] + self[1][5] + self[1][2],
                self[0],
                self[3][2] + self[3][5] + self[3][8] + self[3][1] + self[3][4] + self[3][7] + self[3][0] + self[3][3] + self[3][6],
                self[5][::-1],
                
                self[2]]

    

    # Returns full 90 degree clockwise cube rotation about y axis
    def Y(self):
        return [self[0][6] + self[0][3] + self[0][0] + self[0][7] + self[0][4] + self[0][1] + self[0][8] + self[0][5] + self[0][2],
                
                self[2],
                self[3],
                self[4],
                self[1],
                
                self[5][2] + self[5][5] + self[5][8] + self[5][1] + self[5][4] + self[5][7] + self[5][0] + self[5][3] + self[5][6]]
    
    # Returns full 90 degree anticlockwise cube rotation about y axis
    def Y_Prime(self): 
        return [self[0][2] + self[0][5] + self[0][8] + self[0][1] + self[0][4] + self[0][7] + self[0][0] + self[0][3] + self[0][6],
                
                self[4],
                self[1],
                self[2],
                self[3],
                
                self[5][6] + self[5][3] + self[5][0] + self[5][7] + self[5][4] + self[5][1] + self[5][8] + self[5][5] + self[5][2]]



    # Returns full 90 degree clockwise cube rotation about z axis
    def Z(self):
        return [self[1][6] + self[1][3] + self[1][0] + self[1][7] + self[1][4] + self[1][1] + self[1][8] + self[1][5] + self[1][2],
                
                self[5][6] + self[5][3] + self[5][0] + self[5][7] + self[5][4] + self[5][1] + self[5][8] + self[5][5] + self[5][2],
                self[2][6] + self[2][3] + self[2][0] + self[2][7] + self[2][4] + self[2][1] + self[2][8] + self[2][5] + self[2][2],
                self[0][6] + self[0][3] + self[0][0] + self[0][7] + self[0][4] + self[0][1] + self[0][8] + self[0][5] + self[0][2],
                self[4][2] + self[4][5] + self[4][8] + self[4][1] + self[4][4] + self[4][7] + self[4][0] + self[4][3] + self[4][6],
                
                self[3][6] + self[3][3] + self[3][0] + self[3][7] + self[3][4] + self[3][1] + self[3][8] + self[3][5] + self[3][2]]
    
    # Returns full 90 degree anticlockwise cube rotation about z axis
    def Z_Prime(self):
        return [self[3][2] + self[3][5] + self[3][8] + self[3][1] + self[3][4] + self[3][7] + self[3][0] + self[3][3] + self[3][6],
                
                self[0][2] + self[0][5] + self[0][8] + self[0][1] + self[0][4] + self[0][7] + self[0][0] + self[0][3] + self[0][6],
                self[2][2] + self[2][5] + self[2][8] + self[2][1] + self[2][4] + self[2][7] + self[2][0] + self[2][3] + self[2][6],
                self[5][2] + self[5][5] + self[5][8] + self[5][1] + self[5][4] + self[5][7] + self[5][0] + self[5][3] + self[5][6],
                self[4][6] + self[4][3] + self[4][0] + self[4][7] + self[4][4] + self[4][1] + self[4][8] + self[4][5] + self[4][2],
                              
                self[1][2] + self[1][5] + self[1][8] + self[1][1] + self[1][4] + self[1][7] + self[1][0] + self[1][3] + self[1][6],]
    


    # Returns rotation U clockwise
    def U(self):
        return [self[0][6] + self[0][3] + self[0][0] + self[0][7] + self[0][4] + self[0][1] + self[0][8] + self[0][5] + self[0][2],
                
                self[2][:3] + self[1][3:],
                self[3][:3] + self[2][3:],
                self[4][:3] + self[3][3:],
                self[1][:3] + self[4][3:],
                
                self[5]]
    
    # Return rotation U anticlockwise
    def U_Prime(self):
        return [self[0][2] + self[0][5] + self[0][8] + self[0][1] + self[0][4] + self[0][7] + self[0][0] + self[0][3] + self[0][6],
                
                self[4][:3] + self[1][3:],
                self[1][:3] + self[2][3:],
                self[2][:3] + self[3][3:],
                self[3][:3] + self[4][3:],
                
                self[5]]

    # Return 180 degree rotation U
    def U_2(self):
        return [self[0][::-1],
                
                self[3][:3] + self[1][3:],
                self[4][:3] + self[2][3:],
                self[1][:3] + self[3][3:],
                self[2][:3] + self[4][3:],
                
                self[5]]



    # Returns rotation E clockwise
    def E(self):
        return [self[0],
                self[1][:3] + self[4][3:6] + self[1][6:],
                self[2][:3] + self[1][3:6] + self[2][6:],
                self[3][:3] + self[2][3:6] + self[3][6:],
                self[4][:3] + self[3][3:6] + self[4][6:],
                
                self[5]]
    
    # Returns rotation E anticlockwise
    def E_Prime(self):
        return [self[0],
                
                self[1][:3] + self[2][3:6] + self[1][6:],
                self[2][:3] + self[3][3:6] + self[2][6:],
                self[3][:3] + self[4][3:6] + self[3][6:],
                self[4][:3] + self[1][3:6] + self[4][6:],
                
                self[5]]



    # Returns rotation D clockwise
    def D(self):
        return [self[0],
                
                self[1][:6] + self[4][6:],
                self[2][:6] + self[1][6:],
                self[3][:6] + self[2][6:],
                self[4][:6] + self[3][6:],
                
                self[5][6] + self[5][3] + self[5][0] + self[5][7] + self[5][4] + self[5][1] + self[5][8] + self[5][5] + self[5][2]]
    
    # Returns rotation D anticlockwise
    def D_Prime(self):
        return [self[0],
                
                self[1][:6] + self[2][6:],
                self[2][:6] + self[3][6:],
                self[3][:6] + self[4][6:],
                self[4][:6] + self[1][6:],
                    
                self[5][2] + self[5][5] + self[5][8] + self[5][1] + self[5][4] + self[5][7] + self[5][0] + self[5][3] + self[5][6]]

    # Return 180 degree rotation D
    def D_2(self):
        return [self[0],
                
                self[1][:6] + self[3][6:],
                self[2][:6] + self[4][6:],
                self[3][:6] + self[1][6:],
                self[4][:6] + self[2][6:],                
                
                self[5][::-1]]


    
    # Returns rotation F clockwise
    def F(self):
        return [self[0][:6] + self[1][8] + self[1][5] + self[1][2],
                
                self[1][:2] + self[5][0] + self[1][3:5] + self[5][1] + self[1][6:8] + self[5][2],
                self[2][6] + self[2][3] + self[2][0] + self[2][7] + self[2][4] + self[2][1] + self[2][8] + self[2][5] + self[2][2],
                self[0][6] + self[3][1:3] + self[0][7] + self[3][4:6] + self[0][8] + self[3][7:],
                self[4],
                                
                self[3][6] + self[3][3] + self[3][0] + self[5][3:]]
    
    # Returns rotation E anticlockwise
    def F_Prime(self):
        return [self[0][:6] + self[3][0] + self[3][3] + self[3][6],
                
                self[1][:2] + self[0][8] + self[1][3:5] + self[0][7] + self[1][6:8] + self[0][6],
                self[2][2] + self[2][5] + self[2][8] + self[2][1] + self[2][4] + self[2][7] + self[2][0] + self[2][3] + self[2][6],
                self[5][2] + self[3][1:3] + self[5][1] + self[3][4:6] + self[5][0] + self[3][7:],
                self[4],
                
                self[1][2] + self[1][5] + self[1][8] + self[5][3:]]

    # Return 180 degree rotation F
    def F_2(self):
        return [self[0][:6] + self[5][:3][::-1],
                
                self[1][:2] + self[3][6] + self[1][3:5] + self[3][3] + self[1][6:8] + self[3][0],
                self[2][::-1],
                self[1][8] + self[3][1:3] + self[1][5] + self[3][4:6] + self[1][2] + self[3][7:],
                self[4],
                
                self[0][6:][::-1] + self[5][3:]]




    # Returns rotation S clockwise
    def S(self):
        return [self[0][:3] + self[3][1] + self[3][4] + self[3][7] + self[0][6:],
                
                self[1][0] + self[0][5] + self[1][2:4] + self[0][4] + self[1][5:7] + self[0][3] + self[1][8],
                self[2],
                self[3][0] + self[5][5] + self[3][2:4] + self[5][4] + self[3][5:7] + self[5][3] + self[3][8],
                self[4],
                
                self[5][:3] + self[1][1] + self[1][4] + self[1][7] + self[5][6:]]   

    # Returns rotation S anticlockwise
    def S_Prime(self):
        return [self[0][:3] + self[1][7] + self[1][4] + self[1][1] + self[0][6:],
                
                self[1][0] + self[5][3] + self[1][2:4] + self[5][4] + self[1][5:7] + self[5][5] + self[1][8],
                self[2],
                self[3][0] + self[0][3] + self[3][2:4] + self[0][4] + self[3][5:7] + self[0][5] + self[3][8],
                self[4],
                
                self[5][:3] + self[3][7] + self[3][4] + self[3][1] + self[5][6:]]
                


    # Returns rotation B clockwise
    def B(self):
        return [self[3][2] + self[3][5] + self[3][8] + self[0][3:],
                
                self[0][2] + self[1][1:3] + self[0][1] + self[1][4:6] + self[0][0] + self[1][7:],
                self[2],
                self[3][:2] + self[5][8] + self[3][3:5] + self[5][7] + self[3][6:8] + self[5][6],
                self[4][6] + self[4][3] + self[4][0] + self[4][7] + self[4][4] + self[4][1] + self[4][8] + self[4][5] + self[4][2],
                
                self[5][:6] + self[1][0] + self[1][3] + self[1][6]]

    # Returns rotation B anticlockwise
    def B_Prime(self):
        return [self[1][6] + self[1][3] + self[1][0] + self[0][3:],
                
                self[5][6] + self[1][1:3] + self[5][7] + self[1][4:6] + self[5][8] + self[1][7:],
                self[2],
                self[3][:2] + self[0][0] + self[3][3:5] + self[0][1] + self[3][6:8] + self[0][2],
                self[4][2] + self[4][5] + self[4][8] + self[4][1] + self[4][4] + self[4][7] + self[4][0] + self[4][3] + self[4][6],
                
                self[5][:6] + self[3][8] + self[3][5] + self[3][2]]

    # Return 180 degree rotation B
    def B_2(self):
        return [self[5][6:][::-1] + self[0][3:], 
                
                self[3][8] + self[1][1:3] + self[3][5] + self[1][4:6] + self[3][2] + self[1][7:],
                self[2],
                self[3][:2] + self[1][6] + self[3][3:5] + self[1][3] + self[3][6:8] + self[1][0],
                self[4][::-1],
                
                self[5][:6] + self[0][:3][::-1]]



    # Returns rotation R clockwise
    def R(self):
        return [self[0][:2] + self[2][2] + self[0][3:5] + self[2][5] + self[0][6:8] + self[2][8],
                
                self[1],
                self[2][:2] + self[5][2] + self[2][3:5] + self[5][5] + self[2][6:8] + self[5][8],
                self[3][6] + self[3][3] + self[3][0] + self[3][7] + self[3][4] + self[3][1] + self[3][8] + self[3][5] + self[3][2],
                self[0][8] + self[4][1:3] + self[0][5] + self[4][4:6] + self[0][2] + self[4][7:],
                
                self[5][:2] + self[4][6] + self[5][3:5] + self[4][3] + self[5][6:8] + self[4][0]]

    # Returns rotation R anticlockwise
    def R_Prime(self):
        return [self[0][:2] + self[4][6] + self[0][3:5] + self[4][3] + self[0][6:8] + self[4][0],
                
                self[1],
                self[2][:2] + self[0][2] + self[2][3:5] + self[0][5] + self[2][6:8] + self[0][8],
                self[3][2] + self[3][5] + self[3][8] + self[3][1] + self[3][4] + self[3][7] + self[3][0] + self[3][3] + self[3][6],
                self[5][8] + self[4][1:3] + self[5][5] + self[4][4:6] + self[5][2] + self[4][7:],
                
                self[5][:2] + self[2][2] + self[5][3:5] + self[2][5] + self[5][6:8] + self[2][8]]
    
    # Return 180 degree rotation R
    def R_2(self):
        return [self[0][:2] + self[5][2] + self[0][3:5] + self[5][5] + self[0][6:8] + self[5][8],
                
                self[1],
                self[2][:2] + self[4][6] + self[2][3:5] + self[4][3] + self[2][6:8] + self[4][0],
                self[3][::-1],
                self[2][8] + self[4][1:3] + self[2][5] + self[4][4:6] + self[2][2] + self[4][7:],
                
                self[5][:2] + self[0][2] + self[5][3:5] + self[0][5] + self[5][6:8] + self[0][8]]
    


    # Returns rotation M clockwise
    def M(self):
        return [self[0][0] + self[4][7] + self[0][2:4] + self[4][4] + self[0][5:7] + self[4][1] + self[0][8],
                
                self[1],
                self[2][0] + self[0][1] + self[2][2:4] + self[0][4] + self[2][5:7] + self[0][7] + self[2][8],
                self[3],
                self[4][0] + self[5][7] + self[4][2:4] + self[5][4] + self[4][5:7] + self[5][1] + self[4][8],
   
                self[5][0] + self[2][1] + self[5][2:4] + self[2][4] + self[5][5:7] + self[2][7] + self[5][8]]
    
    # Returns rotation M anticlockwise
    def M_Prime(self):
        return [self[0][0] + self[2][1] + self[0][2:4] + self[2][4] + self[0][5:7] + self[2][7] + self[0][8],
                
                self[1],
                self[2][0] + self[5][1] + self[2][2:4] + self[5][4] + self[2][5:7] + self[5][7] + self[2][8],
                self[3],
                self[4][0] + self[0][7] + self[4][2:4] + self[0][4] + self[4][5:7] + self[0][1] + self[4][8],
                
                self[5][0] + self[4][7] + self[5][2:4] + self[4][4] + self[5][5:7] + self[4][1] + self[5][8]]
    



    # Returns rotation L clockwise
    def L(self):
        return [self[4][8] + self[0][1:3] + self[4][5] + self[0][4:6] + self[4][2] + self[0][7:],
                
                self[1][6] + self[1][3] + self[1][0] + self[1][7] + self[1][4] + self[1][1] + self[1][8] + self[1][5] + self[1][2],
                self[0][0] + self[2][1:3] + self[0][3]+ self[2][4:6] + self[0][6] + self[2][7:],
                self[3],
                self[4][:2] + self[5][6] + self[4][3:5] + self[5][3] + self[4][6:8] + self[5][0],

                self[2][0] + self[5][1:3] + self[2][3] + self[5][4:6] + self[2][6] + self[5][7:]]

    # Returns rotation L anticlockwise
    def L_Prime(self):
        return [self[2][0] + self[0][1:3] + self[2][3] + self[0][4:6] + self[2][6] + self[0][7:],
                
                self[1][2] + self[1][5] + self[1][8] + self[1][1] + self[1][4] + self[1][7] + self[1][0] + self[1][3] + self[1][6],
                self[5][0] + self[2][1:3] + self[5][3]+ self[2][4:6] + self[5][6] + self[2][7:],
                self[3],
                self[4][:2] + self[0][6] + self[4][3:5] + self[0][3] + self[4][6:8] + self[0][0],

                self[4][8] + self[5][1:3] + self[4][5] + self[5][4:6] + self[4][2] + self[5][7:]]

    # Return 180 degree rotation L
    def L_2(self):
        return [self[5][0] + self[0][1:3] + self[5][3] + self[0][4:6] + self[5][6] + self[0][7:],
                
                self[1][::-1],
                self[4][8] + self[2][1:3] + self[4][5] + self[2][4:6] + self[4][2] + self[2][7:],
                self[3],
                self[4][:2] + self[2][6] + self[4][3:5] + self[2][3] + self[4][6:8] + self[2][0],

                self[0][0] + self[5][1:3] + self[0][3] + self[5][4:6] + self[0][6] + self[5][7:]]


    
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
            move = rnd.choice(["U", "D", "F", "B", "R", "L"]) + rnd.choice(["", "'", "2"])
            moves.append(move)
            self.move(move)
            
        return moves

