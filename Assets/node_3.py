from cube_3 import Cube3

class Node(Cube3):
    def __init__(self, cube = None, movement = None, parent = None, generation = 0):
        Cube3.__init__(self, cube)
        self.movement = movement
        self.generation = generation
        self.parent = parent


    # def copy(self):
    #     return Node(self.cube, 0, self.node, self.generation + 1)
    

    def transformation(self, *transformations):
        transformed_node = Node(self.cube)
        for transformation in transformations:
             transformed_node.cube = getattr(transformed_node, transformation)()
        
        return transformed_node.cube


    
    def reflect_XY(self):
        return [
            self[0][6] + self[0][7] + self[0][8] + self[0][3] + self[0][4] + self[0][5] + self[0][0] + self[0][1] + self[0][2],

            self[1][2] + self[1][1] + self[1][0] + self[1][5] + self[1][4] + self[1][3] + self[1][8] + self[1][7] + self[1][6],
            self[4][2] + self[4][1] + self[4][0] + self[4][5] + self[4][4] + self[4][3] + self[4][8] + self[4][7] + self[4][6],
            self[3][2] + self[3][1] + self[3][0] + self[3][5] + self[3][4] + self[3][3] + self[3][8] + self[3][7] + self[3][6],
            self[2][2] + self[2][1] + self[2][0] + self[2][5] + self[2][4] + self[2][3] + self[2][8] + self[2][7] + self[2][6],

            self[5][6] + self[5][7] + self[5][8] + self[5][3] + self[5][4] + self[5][5] + self[5][0] + self[5][1] + self[5][2]]
    
    def reflect_XZ(self):
        return [
            self[5][6] + self[5][7] + self[5][8] + self[5][3] + self[5][4] + self[5][5] + self[5][0] + self[5][1] + self[5][2],
            
            self[1][6] + self[1][7] + self[1][8] + self[1][3] + self[1][4] + self[1][5] + self[1][0] + self[1][1] + self[1][2],
            self[2][6] + self[2][7] + self[2][8] + self[2][3] + self[2][4] + self[2][5] + self[2][0] + self[2][1] + self[2][2],
            self[3][6] + self[3][7] + self[3][8] + self[3][3] + self[3][4] + self[3][5] + self[3][0] + self[3][1] + self[3][2],
            self[4][6] + self[4][7] + self[4][8] + self[4][3] + self[4][4] + self[4][5] + self[4][0] + self[4][1] + self[4][2],

            self[0][6] + self[0][7] + self[0][8] + self[0][3] + self[0][4] + self[0][5] + self[0][0] + self[0][1] + self[0][2]]

    def reflect_YZ(self):
        return [
            self[0][2] + self[0][1] + self[0][0] + self[0][5] + self[0][4] + self[0][3] + self[0][8] + self[0][7] + self[0][6],

            self[3][2] + self[3][1] + self[3][0] + self[3][5] + self[3][4] + self[3][3] + self[3][8] + self[3][7] + self[3][6],
            self[2][2] + self[2][1] + self[2][0] + self[2][5] + self[2][4] + self[2][3] + self[2][8] + self[2][7] + self[2][6],
            self[1][2] + self[1][1] + self[1][0] + self[1][5] + self[1][4] + self[1][3] + self[1][8] + self[1][7] + self[1][6],
            self[4][2] + self[4][1] + self[4][0] + self[4][5] + self[4][4] + self[4][3] + self[4][8] + self[4][7] + self[4][6],

            self[5][2] + self[5][1] + self[5][0] + self[5][5] + self[5][4] + self[5][3] + self[5][8] + self[5][7] + self[5][6]]

    
    def X_2(self):
        cube = Cube3(self.cube)
        cube.move("X")
        return cube.X()
    
    def Y_2(self):
        cube = Cube3(self.cube)
        cube.move("Y")
        return cube.Y()

    def Z_2(self):
        cube = Cube3(self.cube)
        cube.move("Z")
        return cube.Z()
    
    def Y_2_X(self):
        cube = Cube3(self.cube)
        cube.move("Y", "Y")
        return cube.X()
    
    def reflect_XZ_X_Prime(self):
        cube = Cube3(self.cube)
        cube.cube = cube.reflect_XZ()
        return cube.X_Prime