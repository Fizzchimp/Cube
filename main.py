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
        nodeQ = Queue(999)
        nodeQ.enqueue(Node(startCube))

        # Queue for the visited node states
        visitedQ = Queue(999)
        

        solved = False
        while not solved:
            # Fetch the current node
            cNode = nodeQ.dequeue()
            cNode.cube.display()
            # Check if the current node is solved
            if cNode.cube.solved():
                solved = True
                
            else:
                nNode1 = Node(Cube(cNode.cube.U()), cNode, "U")
                nNode2 = Node(Cube(cNode.cube.U_Prime()), cNode, "U'")
                
                nNode3 = Node(Cube(cNode.cube.F()), cNode, "F")
                nNode4 = Node(Cube(cNode.cube.F_Prime()), cNode, "F'")

                nNode5 = Node(Cube(cNode.cube.L()), cNode, "L")
                nNode6 = Node(Cube(cNode.cube.L_Prime()), cNode, "L'")
                
                nodeQ.enqueue(nNode1)
        print("DONE")
            
            
              
            
            


world = World()
cube = Cube()
cube.cube = cube.U()
world.solve(cube)