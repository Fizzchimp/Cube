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
    start_queue = Queue(99999)

    # Current start node
    cur_start_node = Node(startState, None, "-")
    

    # Queue for current end nodes
    end_queue = Queue(99999)

    # Current end node
    cur_end_node = Node(normalisedSolved(startState), None, "-")
    
    # Used to determine when all nodes in one depth have been explored
    generation = 0
    
    # List of visited nodes from the previous generation
    visited_start = []    
    visited_end = []
    
    while generation <= 5:
        ## Start state tree
        visited_start = []
        next_gen = generation + 1

        while cur_start_node.generation == generation: # Checks current node is at current depth
            
            # Check visited start states for matching nodes
            check, node = bin_search(visited_end, cur_start_node)
            if check == True:
                return cur_start_node, node
            
            # Append current node to visited nodes
            visited_start.append(cur_start_node)

            # Enqueue all adjacent nodes
            if cur_start_node.movement[0] != "U":  
                start_queue.enqueue(Node(cur_start_node.U(), cur_start_node, "U", next_gen))
                start_queue.enqueue(Node(cur_start_node.U_Prime(), cur_start_node, "U'", next_gen))
                start_queue.enqueue(Node(cur_start_node.U_2(), cur_start_node, "U2", next_gen))

            if cur_start_node.movement[0] != "R":  
                start_queue.enqueue(Node(cur_start_node.R(), cur_start_node, "R", next_gen))  
                start_queue.enqueue(Node(cur_start_node.R_Prime(), cur_start_node, "R'", next_gen))
                start_queue.enqueue(Node(cur_start_node.R_2(), cur_start_node, "R2", next_gen))
            
            if cur_start_node.movement[0] != "F":  
                start_queue.enqueue(Node(cur_start_node.F(), cur_start_node, "F", next_gen))  
                start_queue.enqueue(Node(cur_start_node.F_Prime(), cur_start_node, "F'", next_gen))
                start_queue.enqueue(Node(cur_start_node.F_2(), cur_start_node, "F2", next_gen))

            # Fetch the next node
            cur_start_node = start_queue.dequeue()

        # Sort visited start nodes
        visited_start = merge_sort(visited_start)

        # End state tree
        visited_end = []
        while cur_end_node.generation == generation:
            
            # Check visited end states for matching nodes
            check, node = bin_search(visited_start, cur_end_node)
            if check == True:
                return node, cur_end_node

            # Append current node to visited nodes
            visited_end.append(cur_end_node)

            # Enqueue all adjacent nodes
            if cur_end_node.movement[0] != "U":
                end_queue.enqueue(Node(cur_end_node.U_Prime(), cur_end_node, "U", next_gen)) 
                end_queue.enqueue(Node(cur_end_node.U(), cur_end_node, "U'", next_gen))
                end_queue.enqueue(Node(cur_end_node.U_2(), cur_end_node, "U2", next_gen))

            if cur_end_node.movement[0] != "R":  
                end_queue.enqueue(Node(cur_end_node.R_Prime(), cur_end_node, "R", next_gen)) 
                end_queue.enqueue(Node(cur_end_node.R(), cur_end_node, "R'", next_gen))
                end_queue.enqueue(Node(cur_end_node.R_2(), cur_end_node, "R2", next_gen))
            
            if cur_end_node.movement[0] != "F":  
                end_queue.enqueue(Node(cur_end_node.F_Prime(), cur_end_node, "F", next_gen))
                end_queue.enqueue(Node(cur_end_node.F(), cur_end_node, "F'", next_gen))
                end_queue.enqueue(Node(cur_end_node.F_2(), cur_end_node, "F2", next_gen))

            # Fetch the next end node
            cur_end_node = end_queue.dequeue()
            

        # Sort visited end nodes
        visited_end = merge_sort(visited_end)

        # Increment the node generation counter
        generation += 1
        



    ### Final generation 6 check

    # Start tree
    visited_start = []
    while True:
        try: # Use try here to detect when queue runs out of nodes
            # Check visited end states for matching nodes
            check, node = bin_search(visited_end, cur_start_node)
            if check == True:
                return cur_start_node, node
        
            # Append current node to visited nodes
            visited_start.append(cur_start_node)
        
            # Fetch the next node
            cur_start_node = start_queue.dequeue()
            
        except:
            break
        
    # Sort visited nodes
    visited_start = merge_sort(visited_start)
    
    # End tree
    while True:
        try: # Use try here to detect when queue runs out of nodes
            # Check visited start states for matching nodes
            check, node = bin_search(visited_start, cur_end_node)
            if check == True:
                return node, cur_end_node

            # Fetch the next node
            cur_end_node = end_queue.dequeue()
            
        except:
            break

    # If no connecting nodes found, return false (unsolvable)
    return None, None