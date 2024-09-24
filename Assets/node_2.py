from cube_2 import Cube2

class Node(Cube2):
    def __init__(self, cube = None, parent = None, movement = None, generation = 0):
        Cube2.__init__(self, cube)
        self.parent = parent
        self.movement = movement
        self.generation = generation
