import pygame as pg
from display import Display
from cube import Cube
from cqueue import Queue
from node import Node


class World:
    #def __init__(self):
    #    window = Display(700, 700)
    

    def solve(self, startCube):
        nodeX = Node(startCube)
        nodeX.cube.display()
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
            node = nodeQ.dequeue()
            
            # Check if the current node is solved
            if node.cube.solved():
                solved = True
                
            else:
                nNode1 = Node(Cube(node.cube.U()), node, "U")
                print(nNode1.cube)
                nNode1.cube.display()
        print("DONE")
            
            
              
            
            


world = World()
world.solve(Cube(["WWYY",
                     
                  "GGGG",
                  "RRRR",
                  "BBBB",
                  "OOOO",

                  "YYYY"]))