class Cube_3():
    def __init__(self, cube = None):
        self.cube = cube if cube != None else [
            "WWWWWWWWW",

            "GGGGGGGGG",
            "RRRRRRRRR",
            "BBBBBBBBB",
            "OOOOOOOOO",

            "YYYYYYYYY"]
        
    def display(self):
        # DIsplay the cube in net form
        print(f"""
    |{self.cube[0][:3]}|
    |{self.cube[0][3:6]}|
    |{self.cube[0][6:]}|
|{self.cube[1][:3]}|{self.cube[2][:3]}|{self.cube[3][:3]}|{self.cube[4][:3]}|
|{self.cube[1][3:6]}|{self.cube[2][3:6]}|{self.cube[3][3:6]}|{self.cube[4][3:6]}|
|{self.cube[1][6:]}|{self.cube[2][6:]}|{self.cube[3][6:]}|{self.cube[4][6:]}|
    |{self.cube[5][:3]}|
    |{self.cube[5][3:6]}|
    |{self.cube[5][6:]}|""")
        
    def __getitem__(self, index):
        return self.cube[index]
    
    def X(self):
        # Returns rotation around X axis clockwise
        return [self[2],
                
                self[1][2] + self[1][5] + self[1][8] + self[1][1] + self[1][4] + self[1][7] + self[1][0] + self[1][3] + self[1][6],
                self[5],
                self[3][6] + self[3][3] + self[3][0] + self[3][7] + self[3][4] + self[3][1] + self[3][8] + self[3][5] + self[3][2],
                self[0][::-1],
                
                self[4][::-1]]
    
    def X_Prime(self):
        # Returns rotation around X axis anticlockwise
        return [self[4][::-1],
                
                self[1][6] + self[1][3] + self[1][0] + self[1][7] + self[1][4] + self[1][1] + self[1][8] + self[1][5] + self[1][2],
                self[0],
                self[3][2] + self[3][5] + self[3][8] + self[3][1] + self[3][4] + self[3][7] + self[3][0] + self[3][3] + self[3][6],
                self[5][::-1],
                
                self[2]]

    
    def Y(self):
        # Return rotation around Y axis clockwise
        return [self[0][6] + self[0][3] + self[0][0] + self[0][7] + self[0][4] + self[0][1] + self[0][8] + self[0][5] + self[0][2],
                
                self[2],
                self[3],
                self[4],
                self[1],
                
                self[5][2] + self[5][5] + self[5][8] + self[5][1] + self[5][4] + self[5][7] + self[5][0] + self[5][3] + self[5][6]]
    
    def Y_Prime(self):
        # Return rotation around Y axis anticlockwise
        return [self[0][2] + self[0][5] + self[0][8] + self[0][1] + self[0][4] + self[0][7] + self[0][0] + self[0][3] + self[0][6],
                
                self[4],
                self[1],
                self[2],
                self[3],
                
                self[5][6] + self[5][3] + self[5][0] + self[5][7] + self[5][4] + self[5][1] + self[5][8] + self[5][5] + self[5][2]]


    def Z(self):
        # Return rotation around Z axis clockwise
# cube = Cube_3()
cube = Cube_3(["OWROWOBRB",
               
               "BBRWRGGBW",
               "YYYYBGRYR",
               "OWBRORYGG",
               "WBWBGROGO", 

               "GOGYYOYWW"])

cube.cube = cube.Y_Prime()

cube.display()