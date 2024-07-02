from cube_2 import Cube_2

class Node(Cube_2):
    def __init__(self, cube = None, parent = None, movement = None, generation = 0):
        Cube_2.__init__(self, cube)
        self.parent = parent
        self.movement = movement
        self.generation = generation
