import pygame as pg
from display import Display
from cube import Cube
from cqueue import Queue
from node import Node
from binsearch import binSearch
from mergesort import mergeSort

class World:
    #def __init__(self):
    #    window = Display(700, 700)
    
    def normalisedSolved(self, cube):
        # Returns a new solved state normalised to be comparable with start node
        colKeys = {"W":"YYYY", "G":"BBBB", "R":"OOOO", "B":"GGGG", "O":"RRRR", "Y":"WWWW"}
        return [
            colKeys[cube[5][2]],
            
            cube[1][2] * 4,
            colKeys[cube[4][3]],
            colKeys[cube[1][2]],
            cube[4][3] * 4,

            cube[5][2] * 4
    ]

    def solve(self, startState):
        # Queue for the current nodes
        sNodeQ = Queue(999999)
        cSNode = Node(startState)

        eNodeQ = Queue(999999)
        cENode = Node(self.normalisedSolved(startState))

        solved = False
        generation = 0
        vENodes = []
        
        while not solved:
 #           print(generation)
            # Start state tree
            vSNodes = []
            nextGen = generation + 1

            while cSNode.generation == generation:
                if binSearch(vENodes, cSNode):
                    solved = True
                    break
                
                # Append current node to visited nodes
                vSNodes.append(cSNode)

                # Enqueue all adjacent nodes
                if cSNode.movement != "U'":  
                    sNodeQ.enqueue(Node(cSNode.U(), cSNode, "U", ))
                if cSNode.movement != "U":   
                    sNodeQ.enqueue(Node(cSNode.U_Prime(), cSNode, "U'", nextGen))

                if cSNode.movement != "R'":  
                    sNodeQ.enqueue(Node(cSNode.R(), cSNode, "R", nextGen))
                if cSNode.movement != "R":   
                    sNodeQ.enqueue(Node(cSNode.R_Prime(), cSNode, "R'", nextGen))
                
                if cSNode.movement != "F'":  
                    sNodeQ.enqueue(Node(cSNode.F(), cSNode, "F", nextGen))
                if cSNode.movement != "F":   
                    sNodeQ.enqueue(Node(cSNode.F_Prime(), cSNode, "F'", nextGen))

                # Fetch the next node
                cSNode = sNodeQ.dequeue()

            # Sort visited nodes
            vSNodes = mergeSort(vSNodes)

            # End state tree
            vENodes = []
            while cENode.generation == generation:

                if binSearch(vSNodes, cENode):
                    solved = True
                    break

                # Append current node to visited nodes
                vENodes.append(cENode)

                # Enqueue all adjacent nodes
                if cENode.movement != "U'":  
                    eNodeQ.enqueue(Node(cENode.U(), cENode, "U", ))
                if cENode.movement != "U":   
                    eNodeQ.enqueue(Node(cENode.U_Prime(), cENode, "U'", nextGen))

                if cENode.movement != "R'":  
                    eNodeQ.enqueue(Node(cENode.R(), cENode, "R", nextGen))
                if cENode.movement != "R":   
                    eNodeQ.enqueue(Node(cENode.R_Prime(), cENode, "R'", nextGen))
                
                if cENode.movement != "F'":  
                    eNodeQ.enqueue(Node(cENode.F(), cENode, "F", nextGen))
                if cENode.movement != "F":   
                    eNodeQ.enqueue(Node(cENode.F_Prime(), cENode, "F'", nextGen))

                # Fetch the next node
                cENode = eNodeQ.dequeue()

            # Sort visited nodes
            vENodes = mergeSort(vENodes)
            #print(vENodes)

            # Increment the node generation counter
            generation += 1



        print("DONE")
        
        path = [cSNode]
        while path[-1].parent != None:
            path.append(path[-1].parent)
        path = path[::-1]

        path.append(cENode)
        while path[-1].parent != None:
            path.append(path[-1].parent)
            
        for x in path:
            print(x.movement)
        

            
              
            
            


world = World()
cube = Cube()
cube.move(["U'"])
#cube.move(["L'", "U", "U", "L", "U", "L'", "U", "L"])
# cube.display()
world.solve(cube.cube)