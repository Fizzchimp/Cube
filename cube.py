class Cube():
    def __init__(self):
        # Representation of cube as an array
        self.__cube = ["WWWW",
                     
                        "GGGG",
                        "RRRR",
                        "BBBB",
                        "OOOO",

                        "YYYY"]
        
    def display(self):
    # Display the cube in net form
        print(f"""
   |{self.__cube[0][:2]}|
   |{self.__cube[0][2:4]}|
|{self.__cube[1][:2]}|{self.__cube[2][:2]}|{self.__cube[3][:2]}|{self.__cube[4][:2]}|
|{self.__cube[1][2:4]}|{self.__cube[2][2:4]}|{self.__cube[3][2:4]}|{self.__cube[4][2:4]}|
   |{self.__cube[5][:2]}|
   |{self.__cube[5][2:4]}|""")
   

    def solved(self):
        # Checks if the cube is solved
        for face in self.__cube:
            if face[0] == face[1] == face[2] == face[3]:
                continue
            else: return False
        return True


    def U(self):
        # Rotation U clockwise
        self.__cube[0] = self.__cube[0][2] + self.__cube[0][0] + self.__cube[0][3] + self.__cube[0][1]

        sub = self.__cube[1][:2]
        for i in range(1, 4):
            self.__cube[i] = self.__cube[i + 1][:2] + self.__cube[i][2:4]
        self.__cube[4] = sub + self.__cube[4][2:4]

    def U_Prime(self):
        # Rotation U anticlockwise
        self.__cube[0] = self.__cube[0][1] + self.__cube[0][3] + self.__cube[0][0] + self.__cube[0][2]
        
        sub = self.__cube[4][:2]
        for i in range(3):
            self.__cube[4 - i] = self.__cube[3 - i][:2] + self.__cube[4 - i][2:4]
        self.__cube[1] = sub + self.__cube[1][2:4]


    def D(self):
        # Rotation D clockwise
        self.__cube[5] = self.__cube[5][2] + self.__cube[5][0] + self.__cube[5][3] + self.__cube[5][1]

        sub = self.__cube[4][2:4]
        for i in range(3):
            self.__cube[4 - i] = self.__cube[4 - i][:2] + self.__cube[3 - i][2:4]
        self.__cube[1] = self.__cube[1][:2] + sub

    def D_Prime(self):
        # Rotation D anticlockwise
        self.__cube[5] = self.__cube[5][1] + self.__cube[5][3] + self.__cube[5][0] + self.__cube[5][2]

        sub = self.__cube[1][2:4]
        for i in range(1, 4):
            self.__cube[i] = self.__cube[i][:2] + self.__cube[i + 1][2:4]
        self.__cube[4] = self.__cube[4][:2] + sub


    def F(self):
        # Rotation F clockwise
        self.__cube[2] = self.__cube[2][2] + self.__cube[2][0] + self.__cube[2][3] + self.__cube[2][1]
    
        sub = self.__cube[0][2:4]
        self.__cube[0] = self.__cube[0][:2] + self.__cube[1][1] + self.__cube[1][3]
        self.__cube[1] = self.__cube[1][0] + self.__cube[5][0] + self.__cube[1][2] + self.__cube[5][1]
        self.__cube[5] = self.__cube[3][0] + self.__cube[3][2] + self.__cube[5][2:4]
        self.__cube[3] = sub[0] + self.__cube[3][1] + sub[1] + self.__cube[3][3]
    
    def F_Prime(self):
        # Rotation F anticlockwise
        self.__cube[2] = self.__cube[2][1] + self.__cube[2][3] + self.__cube[2][0] + self.__cube[2][2]

        sub = self.__cube[0][2:4]
        self.__cube[0] = self.__cube[0][:2] + self.__cube[3][0] + self.__cube[3][2]
        self.__cube[3] = self.__cube[5][1] + self.__cube[3][1] + self.__cube[5][0] + self.__cube[3][3]
        self.__cube[5] = self.__cube[1][1] + self.__cube[1][3] + self.__cube[5][2:4]
        self.__cube[1] = self.__cube[1][0] + sub[1] + self.__cube[1][2] + sub[0]


    def B(self):
        # Rotation B clockwise
        self.__cube[4] = self.__cube[4][2] + self.__cube[4][0] + self.__cube[4][3] + self.__cube[4][1]

        sub = self.__cube[0][:2]
        self.__cube[0] = self.__cube[3][1] + self.__cube[3][3] + self.__cube[0][2:4]
        self.__cube[3] = self.__cube[3][0] + self.__cube[5][3] + self.__cube[3][2] + self.__cube[5][2]
        self.__cube[5] = self.__cube[5][:2] + self.__cube[1][0] + self.__cube[1][2]
        self.__cube[1] = sub[1] + self.__cube[1][1] + sub[0] + self.__cube[1][3]
    
    def B_Prime(self):
        # Rotatio B anticlockwise
        self.__cube[4] = self.__cube[4][1] + self.__cube[4][3] + self.__cube[4][0] + self.__cube[4][2]
        
        sub = self.__cube[0][:2]
        self.__cube[0] = self.__cube[1][2] + self.__cube[1][0] + self.__cube[0][2:4]
        self.__cube[1] = self.__cube[5][2] + self.__cube[1][1] + self.__cube[5][3] + self.__cube[1][3]
        self.__cube[5] = self.__cube[5][:2] + self.__cube[3][1] + self.__cube[3][3]
        self.__cube[3] = self.__cube[3][0] + sub[0] + self.__cube[3][2] + sub[1]


    def L(self):
        # Rotation L clockwise
        self.__cube[1] = self.__cube[1][2] + self.__cube[1][0] + self.__cube[1][3] + self.__cube[1][1]

        sub = self.__cube[0][0] + self.__cube[0][2]
        self.__cube[0] = self.__cube[4][3] + self.__cube[0][1] + self.__cube[4][1] + self.__cube[0][3]
        self.__cube[4] = self.__cube[4][0] + self.__cube[5][2] + self.__cube[4][2] + self.__cube[5][0]
        self.__cube[5] = self.__cube[2][0] + self.__cube[5][1] + self.__cube[2][2] + self.__cube[5][3]
        self.__cube[2] = sub[0] + self.__cube[2][1] + sub[1] + self.__cube[2][3]

    def L_Prime(self):
        # Rotation L anticlockwise
        self.__cube[1] = self.__cube[1][1] + self.__cube[1][3] + self.__cube[1][0] + self.__cube[1][2]

        sub = self.__cube[0][0] + self.__cube[0][2]
        self.__cube[0] = self.__cube[2][0] + self.__cube[0][1] + self.__cube[2][2] + self.__cube[0][3]
        self.__cube[2] = self.__cube[5][0] + self.__cube[2][1] + self.__cube[5][2] + self.__cube[2][3]
        self.__cube[5] = self.__cube[4][3] + self.__cube[5][1] + self.__cube[4][1] + self.__cube[5][3]
        self.__cube[4] = self.__cube[4][0] + sub[1] + self.__cube[4][2] + sub[0]
        

    def R(self):
        # Rotation R clockwise
        self.__cube[3] = self.__cube[3][2] + self.__cube[3][0] + self.__cube[3][3] + self.__cube[3][1]

        sub = self.__cube[0][1] + self.__cube[0][3]
        self.__cube[0] = self.__cube[0][0] + self.__cube[2][1] + self.__cube[0][2] + self.__cube[2][3]
        self.__cube[2] = self.__cube[2][0] + self.__cube[5][1] + self.__cube[2][2] + self.__cube[5][3]
        self.__cube[5] = self.__cube[5][0] + self.__cube[4][2] + self.__cube[5][2] + self.__cube[4][0]
        self.__cube[4] = sub[1] + self.__cube[4][1] + sub[0] + self.__cube[4][3]

    def R_Prime(self):

        # Rotation R anticlockwise
        self.__cube[3] = self.__cube[3][1] + self.__cube[3][3] + self.__cube[3][0] + self.__cube[3][2]

        sub = self.__cube[0][1] + self.__cube[0][3]
        self.__cube[0] = self.__cube[0][0] + self.__cube[4][2] + self.__cube[0][2] + self.__cube[4][0]
        self.__cube[4] = self.__cube[5][3] + self.__cube[4][1] + self.__cube[5][1] + self.__cube[4][3]
        self.__cube[5] = self.__cube[5][0] + self.__cube[2][1] + self.__cube[5][2] + self.__cube[2][3]
        self.__cube[2] = self.__cube[2][0] + sub[0] + self.__cube[2][2] + sub[1]

cube = Cube()
cube.display()