from Assets.node_3 import Node
from Assets.cqueue import Queue
from Assets.binsearch import binSearch
from Assets.mergesort import mergeSort


def normalisedSolved(state):
    return [
        state[0][4] * 9,
        state[1][4] * 9,
        state[2][4] * 9,
        state[3][4] * 9,
        state[4][4] * 9,
        state[5][4] * 9
    ]


def solve_3(startState):
    # Queue for the current nodes
    sNodeQ = Queue(99999)
    cSNode = Node(startState)
    
    eNodeQ = Queue(99999)
    cENode = Node(normalisedSolved(startState))

    generation = 0
    # List of visited nodes from the previous generation
    vENodes = []
    vSNodes = []

    while generation <= 6:
        # Start state tree
        vSNodes = []
        nextGen = generation + 1

        while cSNode.generation == generation:
            
            check, node = binSearch(vENodes, cSNode)
            if check == True:
                return cSNode, node
            
            # Append current node to visited nodes
            vSNodes.append(cSNode)

            # Enqueue all adjacent nodes
            if cSNode.movement != "M'": sNodeQ.enqueue(Node(cSNode.M(), cSNode, "M", nextGen))
            if cSNode.movement != "M": sNodeQ.enqueue(Node(cSNode.M_Prime(), cSNode, "M'", nextGen))

            if cSNode.movement != "U'":  
                sNodeQ.enqueue(Node(cSNode.U(), cSNode, "U", nextGen))
            if cSNode.movement != "U":   
                sNodeQ.enqueue(Node(cSNode.U_Prime(), cSNode, "U'", nextGen))

            if cSNode.movement != "E'":  
                sNodeQ.enqueue(Node(cSNode.E(), cSNode, "E", nextGen))
            if cSNode.movement != "E":   
                sNodeQ.enqueue(Node(cSNode.E_Prime(), cSNode, "E'", nextGen))
            
            if cSNode.movement != "D'":
                sNodeQ.enqueue(Node(cSNode.D(), cSNode, "D", nextGen))
            if cSNode.movement != "D":
                sNodeQ.enqueue(Node(cSNode.D_Prime(), cSNode, "D'", nextGen))


            if cSNode.movement != "R'":  
                sNodeQ.enqueue(Node(cSNode.R(), cSNode, "R", nextGen))
            if cSNode.movement != "R":   
                sNodeQ.enqueue(Node(cSNode.R_Prime(), cSNode, "R'", nextGen))

            if cSNode.movement != "L'":  
                sNodeQ.enqueue(Node(cSNode.L(), cSNode, "L", nextGen))
            if cSNode.movement != "L":   
                sNodeQ.enqueue(Node(cSNode.L_Prime(), cSNode, "L'", nextGen))
            

            if cSNode.movement != "F'":  
                sNodeQ.enqueue(Node(cSNode.F(), cSNode, "F", nextGen))
            if cSNode.movement != "F":   
                sNodeQ.enqueue(Node(cSNode.F_Prime(), cSNode, "F'", nextGen))
                               
            if cSNode.movement != "S'": 
                sNodeQ.enqueue(Node(cSNode.S(), cSNode, "S", nextGen))
            if cSNode.movement != "S":   
                sNodeQ.enqueue(Node(cSNode.S_Prime(), cSNode, "S'", nextGen))

            if cSNode.movement != "B'":  
                sNodeQ.enqueue(Node(cSNode.B(), cSNode, "B", nextGen))
            if cSNode.movement != "B":   
                sNodeQ.enqueue(Node(cSNode.B_Prime(), cSNode, "B'", nextGen))

            # Fetch the next node
            cSNode = sNodeQ.dequeue()
            
        # Sort visited nodes
        vSNodes = mergeSort(vSNodes)

        # End state tree
        vENodes = []
        while cENode.generation == generation:

            check, node = binSearch(vSNodes, cENode)
            if check == True:
                return node, cENode

            # Append current node to visited nodes
            vENodes.append(cENode)

            # Enqueue all adjacent nodes

            if cENode.movement != "M'":
                eNodeQ.enqueue(Node(cENode.M_Prime(), cENode, "M", nextGen))
            if cENode.movement != "M":   
                eNodeQ.enqueue(Node(cENode.M(), cENode, "M'", nextGen))


            if cENode.movement != "U'":
                eNodeQ.enqueue(Node(cENode.U_Prime(), cENode, "U", nextGen))
            if cENode.movement != "U":   
                eNodeQ.enqueue(Node(cENode.U(), cENode, "U'", nextGen))

            if cENode.movement != "E'":
                eNodeQ.enqueue(Node(cENode.E_Prime(), cENode, "E", nextGen))
            if cENode.movement != "E":   
                eNodeQ.enqueue(Node(cENode.E(), cENode, "E'", nextGen))

            if cENode.movement != "D'":
                eNodeQ.enqueue(Node(cENode.D_Prime(), cENode, "D", nextGen))
            if cENode.movement != "D":   
                eNodeQ.enqueue(Node(cENode.D(), cENode, "D'", nextGen))


            if cENode.movement != "R'":  
                eNodeQ.enqueue(Node(cENode.R_Prime(), cENode, "R", nextGen))
            if cENode.movement != "R":   
                eNodeQ.enqueue(Node(cENode.R(), cENode, "R'", nextGen))
        

            if cENode.movement != "L'":
                eNodeQ.enqueue(Node(cENode.L_Prime(), cENode, "L", nextGen))
            if cENode.movement != "L":   
                eNodeQ.enqueue(Node(cENode.L(), cENode, "L'", nextGen))
            

            if cENode.movement != "F'":  
                eNodeQ.enqueue(Node(cENode.F_Prime(), cENode, "F", nextGen))
            if cENode.movement != "F":   
                eNodeQ.enqueue(Node(cENode.F(), cENode, "F'", nextGen))

            if cENode.movement != "S'":
                eNodeQ.enqueue(Node(cENode.S_Prime(), cENode, "S", nextGen))
            if cENode.movement != "S":   
                eNodeQ.enqueue(Node(cENode.S(), cENode, "S'", nextGen))

            if cENode.movement != "B'":
                eNodeQ.enqueue(Node(cENode.B_Prime(), cENode, "B", nextGen))
            if cENode.movement != "B":   
                eNodeQ.enqueue(Node(cENode.B(), cENode, "B'", nextGen))

            # Fetch the next node
            cENode = eNodeQ.dequeue()
            

        # Sort visited nodes
        vENodes = mergeSort(vENodes)

        # Increment the node generation counter
        generation += 1

    return None, None