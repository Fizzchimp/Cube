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
   
    # Face rotation R
    def move_R(self, prime):
        if prime:
            sub1 = self.cube[0][1][1]
            sub2 = self.cube[0][0][1]

            self.cube[0][1][1] = self.cube[4][0][0]
            self.cube[0][1][0] = self.cube[4][0][1]

            self.cube[4][0][0] = self.cube[5][1][1]
            self.cube[4][0][1] = self.cube[5][0][1]

            self.cube[5][1][1] = self.cube[2][1][1]
            self.cube[5][0][0] = self.cube[2][0][0]

            self.cube[2][1][1] = sub1
            self.cube[2][0][1] = sub2

cube = Cube()
cube.display()