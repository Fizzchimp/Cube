import random as rnd

class Cube():
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
    
    
    def move(self, algorithm):
        for move in algorithm:
            match move:
                case "U": self.cube = self.U()
                case "U'": self.cube = self.U_Prime()

                case "D": self.cube = self.D()
                case "D'": self.cube = self.D_Prime()

                case "F": self.cube = self.F()
                case "F'": self.cube = self.F_Prime()

                case "B": self.cube = self.B()
                case "B'": self.cube = self.B_Prime()

                case "L": self.cube = self.L()
                case "L'": self.cube = self.L_Prime()

                case "R": self.cube = self.R()
                case "R'": self.cube = self.R_Prime()

                case "X": self.cube = self.X()
                case "X'": self.cube = self.X_Prime()

                case "Y": self.cube = self.Y()
                case "Y'": self.cube = self.Y_Prime()

                case _: print("Not a valid movement")

    def scramble(self, num = 11):
        moves = []
        for i in range(num):
            moves.append(rnd.choice(["U", "D", "F", "B", "R", "L"]) + rnd.choice(["'", ""]))
        self.move(moves)
        print(", ".join(moves))
