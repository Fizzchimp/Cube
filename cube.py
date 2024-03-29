colours = {"W" : "\33[37m",
           "Y" : "\33[33m",
           "B" : "\33[34m",
           "O" : "\033[93m",
           "G" : "\33[32m",
           "R" : "\33[31m"}

class Cube():
    def __init__(self):
        # Representation of cube as an array
        self.cube = ["ORGW",
                     
                     "GGGG",
                     "RRRR",
                     "BBBB",
                     "OOOO",

                     "YYYY"]
    # Display the cube in net form
    def display(self):
        cube = self.cube
        for face in cube:
            newFace = ""
            for x in face:
                newFace += colours[x] + x
            face = newFace
            print(face)
        print(f"""
   |{cube[0][:2]}|
   |{cube[0][2:4]}|
|{cube[1][:2]}|{cube[2][:2]}|{cube[3][:2]}|{cube[4][:2]}|
|{cube[1][2:4]}|{cube[2][2:4]}|{cube[3][2:4]}|{cube[4][2:4]}|
   |{cube[5][:2]}|
   |{cube[5][2:4]}|\33[47m""")
   
    # Face rotation R
    def move_U(self, prime):
        if not prime:
            self.cube[0] = self.cube[0][2] + self.cube[0][0] + self.cube[0][3] + self.cube[0][1]

            

cube = Cube()
cube.move_U(False)
cube.display()