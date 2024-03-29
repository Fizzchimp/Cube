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
   
    # Face rotation U
    def move_U(self, prime):
        if not prime:
            #U face rotation
            self.cube[0] = self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1]

            # Other faces rotation
            sub = self.cube[1][:2]
            self.cube[1] = self.cube[2][:2] + self.cube[1][2:4]
            self.cube[2] = self.cube[3][:2] + self.cube[2][2:4]
            self.cube[3] = self.cube[4][:2] + self.cube[3][2:4]
            self.cube[4] = sub + self.cube[4][2:4]

            

cube = Cube()
cube.move_U(False)
cube.display()