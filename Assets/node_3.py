from cube_3 import Cube3

class Node(Cube3):
    def __init__(self, cube = None, movement = None, parent = None, generation = 0):
        Cube3.__init__(self, cube)
        self.movement = movement
        self.generation = generation
        self.parent = parent