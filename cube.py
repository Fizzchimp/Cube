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
        # Rotation D clockwise
        self.cube[5] = self.cube[5][2] + self.cube[5][0] + self.cube[5][3] + self.cube[5][1]

        sub = self.cube[4][2:4]
        for i in range(3):
            self.cube[4 - i] = self.cube[4 - i][:2] + self.cube[3 - i][2:4]
        self.cube[1] = self.cube[1][:2] + sub

    def D_Prime(self):
        # Rotation D anticlockwise
        self.cube[5] = self.cube[5][1] + self.cube[5][3] + self.cube[5][0] + self.cube[5][2]

        sub = self.cube[1][2:4]
        for i in range(1, 4):
            self.cube[i] = self.cube[i][:2] + self.cube[i + 1][2:4]
        self.cube[4] = self.cube[4][:2] + sub


    def F(self):
        # Returns rotation F clockwise
        return [self.cube[0][:2] + self.cube[1][1] + self.cube[1][3],
                
                self.cube[1][0] + self.cube[5][0] + self.cube[1][2] + self.cube[5][1],
                self.cube[2][2] + self.cube[2][0] + self.cube[2][3] + self.cube[2][1],
                self.cube[0][2] + self.cube[3][1] + self.cube[0][3] + self.cube[3][3],
                self.cube[4],
                
                self.cube[3][0] + self.cube[3][2] + self.cube[5][2:4]]
    
    def F_Prime(self):
        # Returns rotation F anticlockwise
        return [self.cube[0][:2] + self.cube[3][0] + self.cube[3][2],
                
                self.cube[1][0] + self.cube[0][2] + self.cube[1][2] + self.cube[0][3],
                self.cube[2][1] + self.cube[2][3] + self.cube[2][0] + self.cube[2][2],
                self.cube[5][1] + self.cube[3][1] + self.cube[5][0] + self.cube[3][3],
                self.cube[4],
                
                self.cube[1][1] + self.cube[1][3] + self.cube[5][2:4]]

    def B(self):
        # Rotation B clockwise
        self.cube[4] = self.cube[4][2] + self.cube[4][0] + self.cube[4][3] + self.cube[4][1]

        sub = self.cube[0][:2]
        self.cube[0] = self.cube[3][1] + self.cube[3][3] + self.cube[0][2:4]
        self.cube[3] = self.cube[3][0] + self.cube[5][3] + self.cube[3][2] + self.cube[5][2]
        self.cube[5] = self.cube[5][:2] + self.cube[1][0] + self.cube[1][2]
        self.cube[1] = sub[1] + self.cube[1][1] + sub[0] + self.cube[1][3]
    
    def B_Prime(self):
        # Rotatio B anticlockwise
        self.cube[4] = self.cube[4][1] + self.cube[4][3] + self.cube[4][0] + self.cube[4][2]
        
        sub = self.cube[0][:2]
        self.cube[0] = self.cube[1][2] + self.cube[1][0] + self.cube[0][2:4]
        self.cube[1] = self.cube[5][2] + self.cube[1][1] + self.cube[5][3] + self.cube[1][3]
        self.cube[5] = self.cube[5][:2] + self.cube[3][1] + self.cube[3][3]
        self.cube[3] = self.cube[3][0] + sub[0] + self.cube[3][2] + sub[1]


    def L(self):
        # Rotation L clockwise
        self.cube[1] = self.cube[1][2] + self.cube[1][0] + self.cube[1][3] + self.cube[1][1]

        sub = self.cube[0][0] + self.cube[0][2]
        self.cube[0] = self.cube[4][3] + self.cube[0][1] + self.cube[4][1] + self.cube[0][3]
        self.cube[4] = self.cube[4][0] + self.cube[5][2] + self.cube[4][2] + self.cube[5][0]
        self.cube[5] = self.cube[2][0] + self.cube[5][1] + self.cube[2][2] + self.cube[5][3]
        self.cube[2] = sub[0] + self.cube[2][1] + sub[1] + self.cube[2][3]

    def L_Prime(self):
        # Rotation L anticlockwise
        self.cube[1] = self.cube[1][1] + self.cube[1][3] + self.cube[1][0] + self.cube[1][2]

        sub = self.cube[0][0] + self.cube[0][2]
        self.cube[0] = self.cube[2][0] + self.cube[0][1] + self.cube[2][2] + self.cube[0][3]
        self.cube[2] = self.cube[5][0] + self.cube[2][1] + self.cube[5][2] + self.cube[2][3]
        self.cube[5] = self.cube[4][3] + self.cube[5][1] + self.cube[4][1] + self.cube[5][3]
        self.cube[4] = self.cube[4][0] + sub[1] + self.cube[4][2] + sub[0]
        

    def R(self):
        # Rotation R clockwise
        self.cube[3] = self.cube[3][2] + self.cube[3][0] + self.cube[3][3] + self.cube[3][1]

        sub = self.cube[0][1] + self.cube[0][3]
        self.cube[0] = self.cube[0][0] + self.cube[2][1] + self.cube[0][2] + self.cube[2][3]
        self.cube[2] = self.cube[2][0] + self.cube[5][1] + self.cube[2][2] + self.cube[5][3]
        self.cube[5] = self.cube[5][0] + self.cube[4][2] + self.cube[5][2] + self.cube[4][0]
        self.cube[4] = sub[1] + self.cube[4][1] + sub[0] + self.cube[4][3]

    def R_Prime(self):

        # Rotation R anticlockwise
        self.cube[3] = self.cube[3][1] + self.cube[3][3] + self.cube[3][0] + self.cube[3][2]

        sub = self.cube[0][1] + self.cube[0][3]
        self.cube[0] = self.cube[0][0] + self.cube[4][2] + self.cube[0][2] + self.cube[4][0]
        self.cube[4] = self.cube[5][3] + self.cube[4][1] + self.cube[5][1] + self.cube[4][3]
        self.cube[5] = self.cube[5][0] + self.cube[2][1] + self.cube[5][2] + self.cube[2][3]
        self.cube[2] = self.cube[2][0] + sub[0] + self.cube[2][2] + sub[1]
       

cube = Cube()
cube.cube = cube.F_Prime()
cube.display()