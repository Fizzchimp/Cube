from Assets.node_3 import Node
from Assets.cqueue import Queue
from Assets.binsearch import binSearch
from Assets.mergesort import mergeSort


MOVES = ("U", "U2", "U'",
         "D", "D2", "D'",
         "R", "R2", "R'",
         "L", "L2", "L'",
         "F", "F2", "F'",
         "B", "B2", "B'")


def normalisedSolved(state):
    return [
        state[0][4] * 9,
        state[1][4] * 9,
        state[2][4] * 9,
        state[3][4] * 9,
        state[4][4] * 9,
        state[5][4] * 9
    ]

def enqueue_nodes(queue, parent, next_generation):
    previous_move = parent.movement
    
    if previous_move // 3 != 0:
        queue.enqueue(Node(parent.U(), parent, 0, next_generation))
        queue.enqueue(Node(parent.U_2(), parent, 1, next_generation))
        queue.enqueue(Node(parent.U_Prime(), parent, 2, next_generation))
        
    if previous_move // 3 != 1:
        queue.enqueue(Node(parent.D(), parent, 3, next_generation))
        queue.enqueue(Node(parent.D_2(), parent, 4, next_generation))
        queue.enqueue(Node(parent.D_Prime(), parent, 5, next_generation))
        
    if previous_move // 3 != 2:
        queue.enqueue(Node(parent.R(), parent, 6, next_generation))
        queue.enqueue(Node(parent.R_2(), parent, 7, next_generation))
        queue.enqueue(Node(parent.R_Prime(), parent, 8, next_generation))
        
    if previous_move // 3 != 3:
        queue.enqueue(Node(parent.L(), parent, 9, next_generation))
        queue.enqueue(Node(parent.L_2(), parent, 10, next_generation))
        queue.enqueue(Node(parent.L_Prime(), parent, 11, next_generation))
        
    if previous_move // 3 != 4:
        queue.enqueue(Node(parent.F(), parent, 12, next_generation))
        queue.enqueue(Node(parent.F_2(), parent, 13, next_generation))
        queue.enqueue(Node(parent.F_Prime(), parent, 14, next_generation))
        
    if previous_move // 3 != 5:
        queue.enqueue(Node(parent.B(), parent, 15, next_generation))
        queue.enqueue(Node(parent.B_2(), parent, 16, next_generation))
        queue.enqueue(Node(parent.B_Prime(), parent, 17, next_generation))
        

    

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

        while cSNode.generation == generation:
            
            check, node = binSearch(vENodes, cSNode)
            if check:
                print(cSNode)
                return cSNode, node
            
            # Append current node to visited nodes
            vSNodes.append(cSNode)

            # Enqueue all adjacent nodes
            enqueue_nodes(sNodeQ, cSNode, generation + 1)

            # Fetch the next node
            cSNode = sNodeQ.dequeue()
            
        # Sort visited nodes
        vSNodes = mergeSort(vSNodes)

        # End state tree
        vENodes = []
        while cENode.generation == generation:

            check, node = binSearch(vSNodes, cENode)
            if check:
                return node, cENode

            # Append current node to visited nodes
            vENodes.append(cENode)

            # Enqueue all adjacent nodes

            # Fetch the next node
            cENode = eNodeQ.dequeue()
            

        # Sort visited nodes
        vENodes = mergeSort(vENodes)

        # Increment the node generation counter
        generation += 1

    return None, None

