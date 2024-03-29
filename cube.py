class Cube():
    def __init__(self):
        # Representation of cube as an array
        self.cube = ["WWWW",
                     
                     "GGGG",
                     "RRRR",
                     "BBBB",
                     "OOOO",

                     "YYYY"]
        
    # Display the cube in net form
    def display(self):
        print(f"""
   |{self.cube[0][:2]}|
   |{self.cube[0][2:4]}|
|{self.cube[1][:2]}|{self.cube[2][:2]}|{self.cube[3][:2]}|{self.cube[4][:2]}|
|{self.cube[1][2:4]}|{self.cube[2][2:4]}|{self.cube[3][2:4]}|{self.cube[4][2:4]}|
   |{self.cube[5][:2]}|
   |{self.cube[5][2:4]}|""")
   
    # Rotation U clockwise
    def U(self):
        self.cube[0] = self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1]

        sub = self.cube[1][:2]
        for i in range(1, 4):
            self.cube[i] = self.cube[i + 1][:2] + self.cube[i][2:4]
        self.cube[4] = sub + self.cube[4][2:4]

    # Rotation U anticlockwise
    def U_Prime(self):
        self.cube[0] = self.cube[0][1] + self.cube[0][3] + self.cube[0][0] + self.cube[0][2]
        
        sub = self.cube[4][:2]
        for i in range(3):
            self.cube[4 - i] = self.cube[3 - i][:2] + self.cube[4 - i][2:4]
        self.cube[1] = sub + self.cube[1][2:4]

    # Rotation D clockwise
    def D(self):
        self.cube[5] = self.cube[5][2] + self.cube[5][0] + self.cube[0][3] + self.cube[0][1]
        

cube = Cube()
cube.U()
cube.U_Prime()
cube.display()