from Assets.node_2 import Node
from Assets.cqueue import Queue
from Assets.binsearch import bin_search
from Assets.mergesort import merge_sort

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

    # Current start node
    cSNode = Node(startState, None, "-")
    

    # Queue for current end nodes
    eNodeQ = Queue(99999)

    # Current end node
    cENode = Node(normalisedSolved(startState), None, "-")
    
    # Used to determine when all nodes in one depth have been explored
    generation = 0
    
    # List of visited nodes from the previous generation
    vENodes = []
    vSNodes = []
    
    while generation <= 5:
        ## Start state tree
        vSNodes = []
        nextGen = generation + 1

        while cSNode.generation == generation: # Checks current node is at current depth
            
            # Check visited start states for matching nodes
            check, node = bin_search(vENodes, cSNode)
            if check == True:
                return cSNode, node
            
            # Append current node to visited nodes
            vSNodes.append(cSNode)

            # Enqueue all adjacent nodes
            if cSNode.movement[0] != "U":  
                sNodeQ.enqueue(Node(cSNode.U(), cSNode, "U", nextGen))
                sNodeQ.enqueue(Node(cSNode.U_Prime(), cSNode, "U'", nextGen))
                sNodeQ.enqueue(Node(cSNode.U_2(), cSNode, "U2", nextGen))

            if cSNode.movement[0] != "R":  
                sNodeQ.enqueue(Node(cSNode.R(), cSNode, "R", nextGen))  
                sNodeQ.enqueue(Node(cSNode.R_Prime(), cSNode, "R'", nextGen))
                sNodeQ.enqueue(Node(cSNode.R_2(), cSNode, "R2", nextGen))
            
            if cSNode.movement[0] != "F":  
                sNodeQ.enqueue(Node(cSNode.F(), cSNode, "F", nextGen))  
                sNodeQ.enqueue(Node(cSNode.F_Prime(), cSNode, "F'", nextGen))
                sNodeQ.enqueue(Node(cSNode.F_2(), cSNode, "F2", nextGen))

            # Fetch the next node
            cSNode = sNodeQ.dequeue()

        # Sort visited start nodes
        vSNodes = merge_sort(vSNodes)

        # End state tree
        vENodes = []
        while cENode.generation == generation:
            
            # Check visited end states for matching nodes
            check, node = bin_search(vSNodes, cENode)
            if check == True:
                return node, cENode

            # Append current node to visited nodes
            vENodes.append(cENode)

            # Enqueue all adjacent nodes
            if cENode.movement[0] != "U":
                eNodeQ.enqueue(Node(cENode.U_Prime(), cENode, "U", nextGen)) 
                eNodeQ.enqueue(Node(cENode.U(), cENode, "U'", nextGen))
                eNodeQ.enqueue(Node(cENode.U_2(), cENode, "U2", nextGen))

            if cENode.movement[0] != "R":  
                eNodeQ.enqueue(Node(cENode.R_Prime(), cENode, "R", nextGen)) 
                eNodeQ.enqueue(Node(cENode.R(), cENode, "R'", nextGen))
                eNodeQ.enqueue(Node(cENode.R_2(), cENode, "R2", nextGen))
            
            if cENode.movement[0] != "F":  
                eNodeQ.enqueue(Node(cENode.F_Prime(), cENode, "F", nextGen))
                eNodeQ.enqueue(Node(cENode.F(), cENode, "F'", nextGen))
                eNodeQ.enqueue(Node(cENode.F_2(), cENode, "F2", nextGen))

            # Fetch the next end node
            cENode = eNodeQ.dequeue()
            

        # Sort visited end nodes
        vENodes = merge_sort(vENodes)

        # Increment the node generation counter
        generation += 1
        



    ### Final generation 6 check

    # Start tree
    vSNodes = []
    while True:
        try: # Use try here to detect when queue runs out of nodes
            # Check visited end states for matching nodes
            check, node = bin_search(vENodes, cSNode)
            if check == True:
                return cSNode, node
        
            # Append current node to visited nodes
            vSNodes.append(cSNode)
        
            # Fetch the next node
            cSNode = sNodeQ.dequeue()
            
        except:
            break
        
    # Sort visited nodes
    vSNodes = merge_sort(vSNodes)
    
    # End tree
    while True:
        try: # Use try here to detect when queue runs out of nodes
            # Check visited start states for matching nodes
            check, node = bin_search(vSNodes, cENode)
            if check == True:
                return node, cENode

            # Fetch the next node
            cENode = eNodeQ.dequeue()
            
        except:
            break

    # If no connecting nodes found, return false (unsolvable)
    return None, None