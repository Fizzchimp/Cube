import random as rnd


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
        return [self[2],
                
                self[1][2] + self[1][5] + self[1][8] + self[1][1] + self[1][4] + self[1][7] + self[1][0] + self[1][3] + self[1][6],
                self[5],
                self[3][6] + self[3][3] + self[3][0] + self[3][7] + self[3][4] + self[3][1] + self[3][8] + self[3][5] + self[3][2],
                self[0][::-1],
                
                self[4][::-1]]
    
    def X_Prime(self):
        return [self[4][::-1],
                
                self[1][6] + self[1][3] + self[1][0] + self[1][7] + self[1][4] + self[1][1] + self[1][8] + self[1][5] + self[1][2],
                self[0],
                self[3][2] + self[3][5] + self[3][8] + self[3][1] + self[3][4] + self[3][7] + self[3][0] + self[3][3] + self[3][6],
                self[5][::-1],
                
                self[2]]

    
    def Y(self):
        return [self[0][6] + self[0][3] + self[0][0] + self[0][7] + self[0][4] + self[0][1] + self[0][8] + self[0][5] + self[0][2],
                
                self[2],
                self[3],
                self[4],
                self[1],
                
                self[5][2] + self[5][5] + self[5][8] + self[5][1] + self[5][4] + self[5][7] + self[5][0] + self[5][3] + self[5][6]]
    
    def Y_Prime(self): 
        return [self[0][2] + self[0][5] + self[0][8] + self[0][1] + self[0][4] + self[0][7] + self[0][0] + self[0][3] + self[0][6],
                
                self[4],
                self[1],
                self[2],
                self[3],
                
                self[5][6] + self[5][3] + self[5][0] + self[5][7] + self[5][4] + self[5][1] + self[5][8] + self[5][5] + self[5][2]]


    def Z(self):
        return [self[1][6] + self[1][3] + self[1][0] + self[1][7] + self[1][4] + self[1][1] + self[1][8] + self[1][5] + self[1][2],
                
                self[5][6] + self[5][3] + self[5][0] + self[5][7] + self[5][4] + self[5][1] + self[5][8] + self[5][5] + self[5][2],
                self[2][6] + self[2][3] + self[2][0] + self[2][7] + self[2][4] + self[2][1] + self[2][8] + self[2][5] + self[2][2],
                self[0][6] + self[0][3] + self[0][0] + self[0][7] + self[0][4] + self[0][1] + self[0][8] + self[0][5] + self[0][2],
                self[4][2] + self[4][5] + self[4][8] + self[4][1] + self[4][4] + self[4][7] + self[4][0] + self[4][3] + self[4][6],
                
                self[3][6] + self[3][3] + self[3][0] + self[3][7] + self[3][4] + self[3][1] + self[3][8] + self[3][5] + self[3][2]]
    
    def Z_Prime(self):
        return [self[3][2] + self[3][5] + self[3][8] + self[3][1] + self[3][4] + self[3][7] + self[3][0] + self[3][3] + self[3][6],
                
                self[0][2] + self[0][5] + self[0][8] + self[0][1] + self[0][4] + self[0][7] + self[0][0] + self[0][3] + self[0][6],
                self[2][2] + self[2][5] + self[2][8] + self[2][1] + self[2][4] + self[2][7] + self[2][0] + self[2][3] + self[2][6],
                self[5][2] + self[5][5] + self[5][8] + self[5][1] + self[5][4] + self[5][7] + self[5][0] + self[5][3] + self[5][6],
                self[4][6] + self[4][3] + self[4][0] + self[4][7] + self[4][4] + self[4][1] + self[4][8] + self[4][5] + self[4][2],
                              
                self[1][2] + self[1][5] + self[1][8] + self[1][1] + self[1][4] + self[1][7] + self[1][0] + self[1][3] + self[1][6],]
    

    def U(self):
        return [self[0][6] + self[0][3] + self[0][0] + self[0][7] + self[0][4] + self[0][1] + self[0][8] + self[0][5] + self[0][2],
                
                self[2][:3] + self[1][3:],
                self[3][:3] + self[2][3:],
                self[4][:3] + self[3][3:],
                self[1][:3] + self[4][3:],
                
                self[5]]
                
    def U_Prime(self):
        return [self[0][2] + self[0][5] + self[0][8] + self[0][1] + self[0][4] + self[0][7] + self[0][0] + self[0][3] + self[0][6],
                
                self[4][:3] + self[1][3:],
                self[1][:3] + self[2][3:],
                self[2][:3] + self[3][3:],
                self[3][:3] + self[4][3:],
                
                self[5]]


    def E(self):
        return [self[0],
                self[1][:3] + self[4][3:6] + self[1][6:],
                self[2][:3] + self[1][3:6] + self[2][6:],
                self[3][:3] + self[2][3:6] + self[3][6:],
                self[4][:3] + self[3][3:6] + self[4][6:],
                
                self[5]]
    
    def E_Prime(self):
        return [self[0],
                
                self[1][:3] + self[2][3:6] + self[1][6:],
                self[2][:3] + self[3][3:6] + self[2][6:],
                self[3][:3] + self[4][3:6] + self[3][6:],
                self[4][:3] + self[1][3:6] + self[4][6:],
                
                self[5]]


    def D(self):
        return [self[0],
                
                self[1][:6] + self[4][6:],
                self[2][:6] + self[1][6:],
                self[3][:6] + self[2][6:],
                self[4][:6] + self[3][6:],
                
                self[5][6] + self[5][3] + self[5][0] + self[5][7] + self[5][4] + self[5][1] + self[5][8] + self[5][5] + self[5][2]]
    
    def D_Prime(self):
        return [self[0],
                
                self[1][:6] + self[2][6:],
                self[2][:6] + self[3][6:],
                self[3][:6] + self[4][6:],
                self[4][:6] + self[1][6:],
                    
                self[5][2] + self[5][5] + self[5][8] + self[5][1] + self[5][4] + self[5][7] + self[5][0] + self[5][3] + self[5][6]]


    def F(self):
        return [self[0][:6] + self[1][8] + self[1][5] + self[1][2],
                
                self[1][:2] + self[5][0] + self[1][3:5] + self[5][1] + self[1][6:8] + self[5][2],
                self[2][6] + self[2][3] + self[2][0] + self[2][7] + self[2][4] + self[2][1] + self[2][8] + self[2][5] + self[2][2],
                self[0][6] + self[3][1:3] + self[0][7] + self[3][4:6] + self[0][8] + self[3][7:],
                self[4],
                                
                self[3][6] + self[3][3] + self[3][0] + self[5][3:]]
    
    def F_Prime(self):
        return [self[0][:6] + self[3][0] + self[3][3] + self[3][6],
                
                self[1][:2] + self[0][8] + self[1][3:5] + self[0][7] + self[1][6:8] + self[0][6],
                self[2][2] + self[2][5] + self[2][8] + self[2][1] + self[2][4] + self[2][7] + self[2][0] + self[2][3] + self[2][6],
                self[5][2] + self[3][1:3] + self[5][1] + self[3][4:6] + self[5][0] + self[3][7:],
                self[4],
                
                self[1][2] + self[1][5] + self[1][8] + self[5][3:]]


    def S(self):
        return [self[0][:3] + self[3][1] + self[3][4] + self[3][7] + self[0][6:],
                
                self[1][0] + self[0][5] + self[1][2:4] + self[0][4] + self[1][5:7] + self[0][3] + self[1][8],
                self[2],
                self[3][0] + self[5][5] + self[3][2:4] + self[5][4] + self[3][5:7] + self[5][3] + self[3][8],
                self[4],
                
                self[5][:3] + self[1][1] + self[1][4] + self[1][7] + self[5][6:]]   

    def S_Prime(self):
        return [self[0][:3] + self[1][7] + self[1][4] + self[1][1] + self[0][6:],
                
                self[1][0] + self[5][3] + self[1][2:4] + self[5][4] + self[1][5:7] + self[5][5] + self[1][8],
                self[2],
                self[3][0] + self[0][3] + self[3][2:4] + self[0][4] + self[3][5:7] + self[0][5] + self[3][8],
                self[4],
                
                self[5][:3] + self[3][7] + self[3][4] + self[3][1] + self[5][6:]]
                

    def B(self):
        return [self[3][2] + self[3][5] + self[3][8] + self[0][3:],
                
                self[0][2] + self[1][1:3] + self[0][1] + self[1][4:6] + self[0][0] + self[1][7:],
                self[2],
                self[3][:2] + self[5][8] + self[3][3:5] + self[5][7] + self[3][6:8] + self[5][6],
                self[4][6] + self[4][3] + self[4][0] + self[4][7] + self[4][4] + self[4][1] + self[4][8] + self[4][5] + self[4][2],
                
                self[5][:6] + self[1][0] + self[1][3] + self[1][6]]

    def B_Prime(self):
        return [self[1][6] + self[1][3] + self[1][0] + self[0][3:],
                
                self[5][6] + self[1][1:3] + self[5][7] + self[1][4:6] + self[5][8] + self[1][7:],
                self[2],
                self[3][:2] + self[0][0] + self[3][3:5] + self[0][1] + self[3][6:8] + self[0][2],
                self[4][2] + self[4][5] + self[4][8] + self[4][1] + self[4][4] + self[4][7] + self[4][0] + self[4][3] + self[4][6],
                
                self[5][:6] + self[3][8] + self[3][5] + self[3][2]]


    def R(self):
        return [self[0][:2] + self[2][2] + self[0][3:5] + self[2][5] + self[0][6:8] + self[2][8],
                
                self[1],
                self[2][:2] + self[5][2] + self[2][3:5] + self[5][5] + self[2][6:8] + self[5][8],
                self[3][6] + self[3][3] + self[3][0] + self[3][7] + self[3][4] + self[3][1] + self[3][8] + self[3][5] + self[3][2],
                self[0][8] + self[4][1:3] + self[0][5] + self[4][4:6] + self[0][2] + self[4][7:],
                
                self[5][:2] + self[4][6] + self[5][3:5] + self[4][3] + self[5][6:8] + self[4][0]]

    def R_Prime(self):
        return [self[0][:2] + self[4][6] + self[0][3:5] + self[4][3] + self[0][6:8] + self[4][0],
                
                self[1],
                self[2][:2] + self[0][2] + self[2][3:5] + self[0][5] + self[2][6:8] + self[0][8],
                self[3][2] + self[3][5] + self[3][8] + self[3][1] + self[3][4] + self[3][7] + self[3][0] + self[3][3] + self[3][6],
                self[5][8] + self[4][1:3] + self[5][5] + self[4][4:6] + self[5][2] + self[4][7:],
                
                self[5][:2] + self[2][2] + self[5][3:5] + self[2][5] + self[5][6:8] + self[2][8]]
    

    def M(self):
        return [self[0][0] + self[4][7] + self[0][2:4] + self[4][4] + self[0][5:7] + self[4][1] + self[0][8],
                
                self[1],
                self[2][0] + self[0][1] + self[2][2:4] + self[0][4] + self[2][5:7] + self[0][7] + self[2][8],
                self[3],
                self[4][0] + self[5][7] + self[4][2:4] + self[5][4] + self[4][5:7] + self[5][1] + self[4][8],
   
                self[5][0] + self[2][1] + self[5][2:4] + self[2][4] + self[5][5:7] + self[2][7] + self[5][8]]
    
    def M_Prime(self):
        return [self[0][0] + self[2][1] + self[0][2:4] + self[2][4] + self[0][5:7] + self[2][7] + self[0][8],
                
                self[1],
                self[2][0] + self[5][1] + self[2][2:4] + self[5][4] + self[2][5:7] + self[5][7] + self[2][8],
                self[3],
                self[4][0] + self[0][7] + self[4][2:4] + self[0][4] + self[4][5:7] + self[0][1] + self[4][8],
                
                self[5][0] + self[4][7] + self[5][2:4] + self[4][4] + self[5][5:7] + self[4][1] + self[5][8]]


    def L(self):
        return [self[4][8] + self[0][1:3] + self[4][5] + self[0][4:6] + self[4][2] + self[0][7:],
                
                self[1][6] + self[1][3] + self[1][0] + self[1][7] + self[1][4] + self[1][1] + self[1][8] + self[1][5] + self[1][2],
                self[0][0] + self[2][1:3] + self[0][3]+ self[2][4:6] + self[0][6] + self[2][7:],
                self[3],
                self[4][:2] + self[5][6] + self[4][3:5] + self[5][3] + self[4][6:8] + self[5][0],

                self[2][0] + self[5][1:3] + self[2][3] + self[5][4:6] + self[2][6] + self[5][7:]]

    def L_Prime(self):
        return [self[2][0] + self[0][1:3] + self[2][3] + self[0][4:6] + self[2][6] + self[0][7:],
                
                self[1][2] + self[1][5] + self[1][8] + self[1][1] + self[1][4] + self[1][7] + self[1][0] + self[1][3] + self[1][6],
                self[5][0] + self[2][1:3] + self[5][3]+ self[2][4:6] + self[5][6] + self[2][7:],
                self[3],
                self[4][:2] + self[0][6] + self[4][3:5] + self[0][3] + self[4][6:8] + self[0][0],

                self[4][8] + self[5][1:3] + self[4][5] + self[5][4:6] + self[4][2] + self[5][7:]]



    def move(self, move):
        # Executes the moves on the cube
        if move == "X": self.cube = self.X()
        elif move == "X'": self.cube = self.X_Prime()
        
        elif move == "Y": self.cube = self.Y()
        elif move == "Y'": self.cube = self.Y_Prime()
            
        elif move == "Z": self.cube = self.Z()
        elif move == "Z'": self.cube = self.Z_Prime()
       
        elif move == "U": self.cube = self.U()
        elif move == "U'": self.cube = self.U_Prime()
        
        elif move == "E": self.cube = self.E()
        elif move == "E'": self.cube = self.E_Prime()
        
        elif move == "D": self.cube = self.D()
        elif move == "D'": self.cube = self.D_Prime()
        
        elif move == "F": self.cube = self.F()
        elif move == "F'": self.cube = self.F_Prime()
        
        elif move == "S": self.cube = self.S()
        elif move == "S'": self.cube = self.S_Prime()

        elif move == "B": self.cube = self.B()
        elif move == "B'": self.cube = self.B_Prime()

        elif move == "R": self.cube = self.R()
        elif move == "R'": self.cube = self.R_Prime()

        elif move == "M": self.cube = self.M()
        elif move == "M'": self.cube = self.M_Prime()

        elif move == "L": self.cube = self.L()
        elif move == "L'": self.cube = self.L_Prime()


        else: print("Not a valid movement")

    def scramble(self, num = 20):
        # Scrambles the cube to a random position
        moves = []
        for i in range(num):
            move = rnd.choice(["U", "E", "D", "F", "S", "B", "R", "M", "L"]) + rnd.choice(["'", ""])
            moves.append(move)
            # self.move(move)
        return moves  