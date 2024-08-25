from cube_3 import Cube_3

class Node(Cube_3):
    def __init__(self, cube = None, parent = None, movement = None, generation = 0):
        Cube_3.__init__(self, cube)
        self.parent = parent
        self.movement = movement
        self.generation = generation