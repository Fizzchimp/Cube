from cube_3 import Cube3

class Node(Cube3):
    def __init__(self, cube = None, movement = None, parent = None, generation = 0):
        # Inherit all Cube_3 attributes
        Cube3.__init__(self, cube)

        # Indicates what move this node is a result of
        self.movement = movement

        # Used in pathfinding to search only up to a maximum depth
        self.generation = generation

        # Used in pathfinding to indicate the relationship of nodes
        self.parent = parent

    
    # Returns cube attribute with transformations applied to it
    def transformation(self, *transformations):
        # Create copy of new node to perform transformaions on
        transformed_node = Node(self.cube)

        # Execute transformations
        for transformation in transformations:
             transformed_node.cube = getattr(transformed_node, transformation)()
        
        return transformed_node.cube


    # Returns reflection in XY plane
    def reflect_XY(self):
        return [
            self[0][6] + self[0][7] + self[0][8] + self[0][3] + self[0][4] + self[0][5] + self[0][0] + self[0][1] + self[0][2],

            self[1][2] + self[1][1] + self[1][0] + self[1][5] + self[1][4] + self[1][3] + self[1][8] + self[1][7] + self[1][6],
            self[4][2] + self[4][1] + self[4][0] + self[4][5] + self[4][4] + self[4][3] + self[4][8] + self[4][7] + self[4][6],
            self[3][2] + self[3][1] + self[3][0] + self[3][5] + self[3][4] + self[3][3] + self[3][8] + self[3][7] + self[3][6],
            self[2][2] + self[2][1] + self[2][0] + self[2][5] + self[2][4] + self[2][3] + self[2][8] + self[2][7] + self[2][6],

            self[5][6] + self[5][7] + self[5][8] + self[5][3] + self[5][4] + self[5][5] + self[5][0] + self[5][1] + self[5][2]]
    
    # Returns reflection in XZ plane
    def reflect_XZ(self):
        return [
            self[5][6] + self[5][7] + self[5][8] + self[5][3] + self[5][4] + self[5][5] + self[5][0] + self[5][1] + self[5][2],
            
            self[1][6] + self[1][7] + self[1][8] + self[1][3] + self[1][4] + self[1][5] + self[1][0] + self[1][1] + self[1][2],
            self[2][6] + self[2][7] + self[2][8] + self[2][3] + self[2][4] + self[2][5] + self[2][0] + self[2][1] + self[2][2],
            self[3][6] + self[3][7] + self[3][8] + self[3][3] + self[3][4] + self[3][5] + self[3][0] + self[3][1] + self[3][2],
            self[4][6] + self[4][7] + self[4][8] + self[4][3] + self[4][4] + self[4][5] + self[4][0] + self[4][1] + self[4][2],

            self[0][6] + self[0][7] + self[0][8] + self[0][3] + self[0][4] + self[0][5] + self[0][0] + self[0][1] + self[0][2]]

    # Returns reflection in YZ plane
    def reflect_YZ(self):
        return [
            self[0][2] + self[0][1] + self[0][0] + self[0][5] + self[0][4] + self[0][3] + self[0][8] + self[0][7] + self[0][6],

            self[3][2] + self[3][1] + self[3][0] + self[3][5] + self[3][4] + self[3][3] + self[3][8] + self[3][7] + self[3][6],
            self[2][2] + self[2][1] + self[2][0] + self[2][5] + self[2][4] + self[2][3] + self[2][8] + self[2][7] + self[2][6],
            self[1][2] + self[1][1] + self[1][0] + self[1][5] + self[1][4] + self[1][3] + self[1][8] + self[1][7] + self[1][6],
            self[4][2] + self[4][1] + self[4][0] + self[4][5] + self[4][4] + self[4][3] + self[4][8] + self[4][7] + self[4][6],

            self[5][2] + self[5][1] + self[5][0] + self[5][5] + self[5][4] + self[5][3] + self[5][8] + self[5][7] + self[5][6]]

    # Returns 180 degree rotation about x axis
    def X_2(self):
        cube = Cube3(self.cube)
        cube.move("X")
        return cube.X()
    
    # Returns 180 degree rotation about y axis
    def Y_2(self):
        cube = Cube3(self.cube)
        cube.move("Y")
        return cube.Y()

    # Returns 180 degree rotation about z axis
    def Z_2(self):
        cube = Cube3(self.cube)
        cube.move("Z")
        return cube.Z()
    