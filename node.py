from cube import Cube

class Node(Cube):
    def __init__(self, cube = None, parent = None, movement = None, generation = 0):
        Cube.__init__(self, cube)
        self.parent = parent
        self.movement = movement
        self.generation = generation

    # def clone(self):
    #     return Node(self.cube, self.parent, self.movement, self.generation)
