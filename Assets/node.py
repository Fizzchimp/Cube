from cube import Cube

class Node(Cube):
    def __init__(self, cube = None, parent = None, movement = None, generation = 0):
        Cube.__init__(self, cube)
        self.parent = parent
        self.movement = movement
        self.generation = generation
