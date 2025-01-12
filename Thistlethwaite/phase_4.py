from Assets.node_3 import Node
from Assets.cqueue import Queue
from Assets.binsearch import bin_search
from Assets.mergesort import merge_sort


G_3 = (
    "L_2", "R_2",
    "F_2", "B_2",
    "U_2", "D_2")

### Phase 4
# Meet in the middle BFS to find path
def bfs_sides(start_state):
    # Create starting nodes for start and end trees
    cur_start_node = Node(start_state)
    cur_end_node = Node([start_state[i][4] * 9 for i in range(6)])
    
    # Create two queues start and end trees
    start_queue = Queue(999999)
    end_queue = Queue(999999)

    # List of visited spaces for both trees
    visited_start_nodes = []
    visited_end_nodes = []

    # Indicates what generation (depth) the search is at
    generation = 0

    # Limits the search to a certain depth
    while generation <= 7:
        next_gen = generation + 1

        # Searches through the current generation of start nodes
        visited_start_nodes = []
        while cur_start_node.generation == generation:
            
            # If the node is found in the visited end nodes, return both the current node and the found node
            check, node = bin_search(visited_end_nodes, cur_start_node)
            if check == True:
                return cur_start_node, node
            
            # If the node is not found, add it to the visited start nodes list
            visited_start_nodes.append(cur_start_node)
            

            # Enqueue all adjacent nodes to start queue
            for i in range(6):
                if cur_start_node.movement != i:
                    start_queue.enqueue(Node(getattr(cur_start_node, G_3[i])(), i, cur_start_node, next_gen))


            # Fetch the next node
            cur_start_node = start_queue.dequeue()
        
        # Sort visited nodes
        visited_start_nodes = merge_sort(visited_start_nodes)



        # Searches through the current generation of end nodes
        visited_end_nodes = []
        while cur_end_node.generation == generation:

            # If the node is found in the visited start nodes, return both the current node and the found node
            check, node = bin_search(visited_start_nodes, cur_end_node)
            if check == True:
                return node, cur_end_node
            
            # If the node is not found, add it to the visited end nodes list
            visited_end_nodes.append(cur_end_node)


            # Enqueue all adjacent nodes to end queue
            for i in range(6):
                if cur_end_node.movement != i:
                    end_queue.enqueue(Node(getattr(cur_end_node, G_3[i])(), i, cur_end_node, next_gen))

            # Fetch the next node
            cur_end_node = end_queue.dequeue()



        # Sort visited nodes
        visited_end_nodes = merge_sort(visited_end_nodes)

        
        # Increment the generation counter
        generation += 1

    # If no path is found, node is deemed unsolvable
    raise Exception("Final BFS not solved - Phase 4")



def phase_4(start_node):
    # Test if already solved
    solved = True
    for face in start_node.cube:
        if not (face[0] == face[1] == face[2] == face[3] == face[4] == face[5] == face[6] == face[7] == face[8]):
            solved = False
    if solved: return []

    # Get the two meeting nodes
    start_node, end_node = bfs_sides(start_node.cube)
    path = []

    # Add moves from the start tree to list of moves
    while start_node.parent != None:
        path.append(G_3[start_node.movement])
        start_node = start_node.parent
        
    # Reverse moves to correct order
    path = path[::-1]

    # Add moves from end tree to list of moves
    while end_node.parent != None:
        path.append(G_3[end_node.movement])
        end_node = end_node.parent


    return path
