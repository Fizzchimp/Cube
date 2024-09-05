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

    def U_2(self):
        return [self[0][::-1],
                
                self[3][:3] + self[1][3:],
                self[4][:3] + self[2][3:],
                self[1][:3] + self[3][3:],
                self[2][:3] + self[4][3:],
                
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

    def D_2(self):
        return [self[0],
                
                self[1][:6] + self[3][6:],
                self[2][:6] + self[4][6:],
                self[3][:6] + self[1][6:],
                self[4][:6] + self[2][6:],                
                
                self[5][::-1]]


    

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

    def F_2(self):
        return [self[0][:6] + self[5][:3][::-1],
                
                self[1][:2] + self[3][6] + self[1][3:5] + self[3][3] + self[1][6:8] + self[3][0],
                self[2][::-1],
                self[1][8] + self[3][1:3] + self[1][5] + self[3][4:6] + self[1][2] + self[3][7:],
                self[4],
                
                self[0][6:][::-1] + self[5][3:]]


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

    def B_2(self):
        return [self[5][6:][::-1] + self[0][3:], 
                
                self[3][8] + self[1][1:3] + self[3][5] + self[1][4:6] + self[3][2] + self[1][7:],
                self[2],
                self[3][:2] + self[1][6] + self[3][3:5] + self[1][3] + self[3][6:8] + self[1][0],
                self[4][::-1],
                
                self[5][:6] + self[0][:3][::-1]]




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
    
    def R_2(self):
        return [self[0][:2] + self[5][2] + self[0][3:5] + self[5][5] + self[0][6:8] + self[5][8],
                
                self[1],
                self[2][:2] + self[4][6] + self[2][3:5] + self[4][3] + self[2][6:8] + self[4][0],
                self[3][::-1],
                self[2][8] + self[4][1:3] + self[2][5] + self[4][4:6] + self[2][2] + self[4][7:],
                
                self[5][:2] + self[0][2] + self[5][3:5] + self[0][5] + self[5][6:8] + self[0][8]]
    

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

    def L_2(self):
        return [self[5][0] + self[0][1:3] + self[5][3] + self[0][4:6] + self[5][6] + self[0][7:],
                
                self[1][::-1],
                self[4][8] + self[2][1:3] + self[4][5] + self[2][4:6] + self[4][2] + self[2][7:],
                self[3],
                self[4][:2] + self[2][6] + self[4][3:5] + self[2][3] + self[4][6:8] + self[2][0],

                self[0][0] + self[5][1:3] + self[0][3] + self[5][4:6] + self[0][6] + self[5][7:]]



    def move(self, *moves):
        for move in moves:
            # Executes the moves on the cube
            move = move.replace("'", "_Prime").replace("2", "_2")
            try: self.cube = getattr(self, move)()
            except AttributeError: print(f"'{move}' not a valid movement")


    def scramble(self, num = 20):
        # Scrambles the cube to a random position
        moves = []
        for i in range(num):
            move = rnd.choice(["U", "D", "F", "B", "R", "L"]) + rnd.choice(["", "'", "2"])
            moves.append(move)
            self.move(move)
        return moves
