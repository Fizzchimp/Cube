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
        nodeQ = Queue(999999)
        nodeQ.enqueue(Node(startCube))

        # Queue for the visited node states
        #visitedQ = Queue(9999)

        iter = 0
        solved = False
        while not solved:
            # Fetch the current node
            cNode = nodeQ.dequeue()

            # Check if the current node is solved
            if cNode.cube.solved():
                solved = True
                
            else:  
                # Enqueueing all nodes adjacent to cNode
                if cNode.move != "U'":  
                    nodeQ.enqueue(Node(Cube(cNode.cube.U()), cNode, "U"))
                if cNode.move != "U":   
                    nodeQ.enqueue(Node(Cube(cNode.cube.U_Prime()), cNode, "U'"))
                
                if cNode.move != "F'":  
                    nodeQ.enqueue(Node(Cube(cNode.cube.F()), cNode, "F"))
                if cNode.move != "F":   
                    nodeQ.enqueue(Node(Cube(cNode.cube.F_Prime()), cNode, "F'"))

                if cNode.move != "R'":  
                    nodeQ.enqueue(Node(Cube(cNode.cube.R()), cNode, "R"))
                if cNode.move != "R":   
                    nodeQ.enqueue(Node(Cube(cNode.cube.R_Prime()), cNode, "R'"))
                
        print("DONE", iter)

        cNode.cube.display()
        path = []
        while True:
            if cNode.parent != None:
                path.append(cNode.move)
                cNode = cNode.parent
            else:
                break
        print(", ".join(path[::-1]))

            
              
            
            


world = World()
cube = Cube()
for i in range(5):
    cube.scramble()
    cube.display()

#world.solve(cube)