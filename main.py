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
        
        solved = False
        
        # Queue for the current nodes
        nodeQ = Queue(999)
        nodeQ.enqueue(Node(startCube))

        # Queue for the visited node states
        visitedQ = Queue(999)
        
        while not solved:
            # Fetch the current node
            node = nodeQ.dequeue()
            
            # Check if the current node is solved
            if node.cube.solved():
                solved = True
                
            else:
                nNode1 = Node(node.cube, node, "U")
                nNode1.cube.U()
                nNode1.cube.display
                
            
            
              
            
            


world = World()
world.solve(Cube(["WWWW",
                     
                  "GGGG",
                  "RBRR",
                  "BBBB",
                  "OOOO",

                  "YYYY"]))