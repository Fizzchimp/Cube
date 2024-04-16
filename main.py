import pygame as pg
from display import Display
from cube import Cube
from cqueue import Queue
from node import Node


class World:
    #def __init__(self):
    #    window = Display(700, 700)
    

    def solve(self, startCube):
        # Cube used for checking each node
        cube = Cube(startCube.cube)
        

        # Queue for the current nodes
        nodeQ = Queue(9999999)
        nodeQ.enqueue(Node(startCube))

        # Queue for the visited node states
        visitedQ = Queue(9999)
        

        solved = False
        while not solved:
            # Fetch the current node
            cNode = nodeQ.dequeue()

            # Check if the current node is solved
            if cNode.cube.solved():
                solved = True
                
            else:
                nodeQ.enqueue(Node(Cube(cNode.cube.U()), cNode, "U"))
                nodeQ.enqueue(Node(Cube(cNode.cube.U_Prime()), cNode, "U'"))
                
                nodeQ.enqueue(Node(Cube(cNode.cube.F()), cNode, "F"))
                nodeQ.enqueue(Node(Cube(cNode.cube.F_Prime()), cNode, "F'"))

                nodeQ.enqueue(Node(Cube(cNode.cube.R()), cNode, "R"))
                nodeQ.enqueue(Node(Cube(cNode.cube.R_Prime()), cNode, "R'"))
                
        print("DONE")
        cNode.cube.display()
        path = []
        while True:
            if cNode.parent != None:
                path.append(cNode.move)
                cNode = cNode.parent
            else:
                break
        print(path)

            
              
            
            


world = World()
cube = Cube()
cube.cube = cube.U()
cube.cube = cube.R()
cube.cube = cube.F()
cube.cube = cube.R_Prime()
cube.cube = cube.U_Prime()
# cube.cube = cube.F()
# cube.cube = cube.R_Prime()

world.solve(cube)