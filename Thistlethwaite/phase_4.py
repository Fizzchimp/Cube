from Assets.node_3 import Node
from Assets.cqueue import Queue
from Assets.binsearch import bin_search
from Assets.mergesort import merge_sort


G_3 = (
    "L_2", "R_2",
    "F_2", "B_2",
    "U_2", "D_2")

### Phase 4
def bfs_sides(start_state):
    cur_start_node = Node(start_state)
    cur_end_node = Node([start_state[i][4] * 9 for i in range(6)])
    
    start_queue = Queue(999999)
    end_queue = Queue(999999)

    visited_start_nodes = []
    visited_end_nodes = []

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

    raise Exception("FINAL BFS NOT SOLVED")



def phase_4(start_node):
    start_node, end_node = bfs_sides(start_node.cube)
    path = []


    if start_node == None:
        raise Exception("No path found")

    else:
        while start_node.parent != None:
            path.append(G_3[start_node.movement])
            start_node = start_node.parent
        path = path[::-1]

        while end_node.parent != None:
            path.append(G_3[end_node.movement])
            end_node = end_node.parent

    return path

