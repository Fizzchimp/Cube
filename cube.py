class Cube():
    def __init__(self, cube = ["WWWW",
                     
                               "GGGG",
                               "RRRR",
                               "BBBB",
                               "OOOO",

                               "YYYY"]):
        # Representation of cube as an array
        self.cube = cube
        
    
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

    def move(self, algorithm):
        for move in algorithm:
            match move:
                case "U": cube.cube = cube.U()
                case "U'": cube.cube = cube.U_Prime()

                case "D": cube.cube = cube.D()
                case "D'": cube.cube = cube.D_Prime()

                case "F": cube.cube = cube.F()
                case "F'": cube.cube = cube.F_Prime()

                case "B": cube.cube = cube.B()
                case "B'": cube.cube = cube.B_Prime()

                case "L": cube.cube = cube.L()
                case "L'": cube.cube = cube.L_Prime()

                case "R": cube.cube = cube.R()
                case "R'": cube.cube = cube.R_Prime()

                case _: print("Not a valid movement")
