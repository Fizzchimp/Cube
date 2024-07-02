import random as rnd

class Cube_2():
    def __init__(self, cube = None):
        # Representation of cube as an array
        self.cube = cube if cube != None else [
            "WWWW",
                        
            "GGGG",
            "RRRR",
            "BBBB",
            "OOOO",

            "YYYY"]
        
    
    def display(self):
        # Display the cube in net form
        print(f"""
   |{self.cube[0][:2]}|
   |{self.cube[0][2:4]}|
|{self.cube[1][:2]}|{self.cube[2][:2]}|{self.cube[3][:2]}|{self.cube[4][:2]}|
|{self.cube[1][2:4]}|{self.cube[2][2:4]}|{self.cube[3][2:4]}|{self.cube[4][2:4]}|
   |{self.cube[5][:2]}|
   |{self.cube[5][2:4]}|""")
   

    def solved(self):
        # Checks if the cube is solved
        for face in self.cube:
            if face[0] == face[1] == face[2] == face[3]:
                continue
            else: return False
        return True


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
        # Returns full clockwise cube rotation about x axis
        return [self.cube[2],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2],
                self.cube[5],
                self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1],
                self.cube[0][::-1],
                
                self.cube[4][::-1]]

    def X_Prime(self):
        # Returns full anticlockwise cube rotation about x axis
        return [self.cube[4][::-1],
                
                self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1],
                self.cube[0],
                self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2],
                self.cube[5][::-1],
                
                self.cube[2]]
    

    def Y(self):
        # Returns full clockwise cube rotation about y axis
        return [self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1],
                
                self.cube[2],
                self.cube[3],
                self.cube[4],
                self.cube[1],
                
                self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2]]
    
    def Y_Prime(self):
        # Returns full anticlockwise cube rotation about y axis
        return [self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2],
                
                self.cube[4],
                self.cube[1],
                self.cube[2],
                self.cube[3],
                
                self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1]]
    

    def Z(self):
        return [self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1],
                
                self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1],
                self.cube[2][2] + self.cube[2][0] + self.cube[2][3] + self.cube[2][1],
                self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1],
                self.cube[4][1] + self.cube[4][3] + self.cube[4][0] + self.cube[4][2],

                self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1]]
    
    def Z_Prime(self):
        return [self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2],
                
                self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2],
                self.cube[2][1] + self.cube[2][3] + self.cube[2][0] + self.cube[2][2],
                self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2],
                self.cube[4][2] + self.cube[4][0] + self.cube[4][3] + self.cube[4][1],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2]]
    

    def move(self, move):
        # Sets the cube structure after given movement
        if move == "U": self.cube = self.U()
        elif move == "U'": self.cube = self.U_Prime()

        elif move == "D": self.cube = self.D()
        elif move == "D'": self.cube = self.D_Prime()

        elif move == "F": self.cube = self.F()
        elif move == "F'": self.cube = self.F_Prime()

        elif move == "B": self.cube = self.B()
        elif move == "B'": self.cube = self.B_Prime()

        elif move == "L": self.cube = self.L()
        elif move == "L'": self.cube = self.L_Prime()

        elif move == "R": self.cube = self.R()
        elif move == "R'": self.cube = self.R_Prime()

        elif move == "X": self.cube = self.X()
        elif move == "X'": self.cube = self.X_Prime()

        elif move == "Y": self.cube = self.Y()
        elif move == "Y'": self.cube = self.Y_Prime()

        elif move == "Z": self.cube = self.Z()
        elif move == "Z'": self.cube = self.Z_Prime()

        else: print("Not a valid movement")

    def scramble(self, num = 20):
        # Scrambles the cube to a random position
        moves = []
        for i in range(num):
            move = rnd.choice(["U", "D", "F", "B", "R", "L"]) + rnd.choice(["'", ""])
            moves.append(move)
            self.move(move)
        return moves