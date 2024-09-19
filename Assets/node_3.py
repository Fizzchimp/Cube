from cube_3 import Cube_3

class Node(Cube_3):
    def __init__(self, cube = None, movement = None, parent = None, generation = 0):
        Cube_3.__init__(self, cube)
        self.movement = movement
        self.generation = generation
        self.parent = parent