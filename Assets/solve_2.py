from Assets.node_2 import Node
from Assets.cqueue import Queue
from Assets.binsearch import binSearch
from Assets.mergesort import mergeSort

COL_KEYS = {"W":"YYYY", "G":"BBBB", "R":"OOOO", "B":"GGGG", "O":"RRRR", "Y":"WWWW"}


def normalisedSolved(cube):
        # Returns a new solved state normalised to be comparable with start node
        return [
            COL_KEYS[cube[5][2]],
            
            cube[1][2] * 4,
            COL_KEYS[cube[4][3]],
            COL_KEYS[cube[1][2]],
            cube[4][3] * 4,

            cube[5][2] * 4
    ]

def solve_2(startState):
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
            if cSNode.movement != "U'":  
                sNodeQ.enqueue(Node(cSNode.U(), cSNode, "U", nextGen))
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

            check, node = binSearch(vSNodes, cENode)
            if check == True:
                return node, cENode

            # Append current node to visited nodes
            vENodes.append(cENode)

            # Enqueue all adjacent nodes
            if cENode.movement != "U'":
                eNodeQ.enqueue(Node(cENode.U_Prime(), cENode, "U", nextGen))
            if cENode.movement != "U":   
                eNodeQ.enqueue(Node(cENode.U(), cENode, "U'", nextGen))

            if cENode.movement != "R'":  
                eNodeQ.enqueue(Node(cENode.R_Prime(), cENode, "R", nextGen))
            if cENode.movement != "R":   
                eNodeQ.enqueue(Node(cENode.R(), cENode, "R'", nextGen))
            
            if cENode.movement != "F'":  
                eNodeQ.enqueue(Node(cENode.F_Prime(), cENode, "F", nextGen))
            if cENode.movement != "F":   
                eNodeQ.enqueue(Node(cENode.F(), cENode, "F'", nextGen))

            # Fetch the next node
            cENode = eNodeQ.dequeue()
            

        # Sort visited nodes
        vENodes = mergeSort(vENodes)

        # Increment the node generation counter
        generation += 1
        



    ### Final generation 7 check

    # Start tree
    vSNodes = []
    while True:
        try:
            check, node = binSearch(vENodes, cSNode)
            if check == True:
                return cSNode, node
        
            # Append current node to visited nodes
            vSNodes.append(cSNode)
        
            # Fetch the next node
            cSNode = sNodeQ.dequeue()
            
        except:
            break
        
    # Sort visited nodes
    vSNodes = mergeSort(vSNodes)
    
    # End tree
    vENodes = []
    while True:
        try:
            check, node = binSearch(vSNodes, cENode)
            if check == True:
                return node, cENode

            # Fetch the next node
            cENode = eNodeQ.dequeue()
            
        except:
            break
    return None, None