from cube_2 import Cube2

class Node(Cube2):
    def __init__(self, cube = None, parent = None, movement = None, generation = 0):
        # Inherit all Cube_2 attributes
        Cube2.__init__(self, cube)

        # Used in pathfinding to indicate the relationship of nodes
        self.parent = parent

        # Indicates what move this node is a result of
        self.movement = movement

        # Used in pathfinding to search only up to a maximum depth
        self.generation = generation
