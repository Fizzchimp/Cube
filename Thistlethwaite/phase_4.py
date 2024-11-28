from Assets.node_3 import Node
from Assets.stack import Stack
from Assets.cqueue import Queue
from Assets.binsearch import binSearch
from Assets.mergesort import merge_sort
from Thistlethwaite.transformations import *


G_3 = (
    "L_2", "R_2",
    "F_2", "B_2",
    "U_2", "D_2")

### Phase 4
## Fix corners
def corners_iddfs(start_node):
    possible_nodes = []
    if check_corners(start_node): possible_nodes.append(start_node)
    
    for i in range(4):
        node_stack = Stack(i + 1)
        node_stack.push(Node(start_node.L_2(), 0, start_node))
        
        exhausted = False
        while not exhausted:
            # Branch down to required depth
            if not node_stack.is_full():
                parent = node_stack.peek()
                node_stack.push(Node(parent.L_2(), 0, parent))
                
            else:
                # Retrieve youngest node
                current_node = node_stack.pop()
                current_movement = current_node.movement
                
                parent = current_node.parent
                
                # Check if the current node is correct
                if check_corners(current_node):
                    possible_nodes.append(current_node)
                
                # Push next movement
                if current_movement < 5:
                    node_stack.push(Node(getattr(parent, G_3[current_movement + 1])(), current_movement + 1, parent))
                    
                # If current branch exhausted remove node and change upper branch
                else:
                    top = True
                    for j in range(i):
                        node = node_stack.pop()
                        if node.movement < 5:
                            top = False
                            break
                    if top: exhausted = True
                    else: node_stack.push(Node(getattr(node.parent, G_3[node.movement + 1])(), node.movement + 1, node.parent))
                        
    if possible_nodes != []: return possible_nodes
    raise Exception("Corner search exhausted!")
                        
# Check if all the corners are home
def check_corners(node):
    for face in node.cube:
        if not (face[4] == face[0] == face[2] == face[6] == face[8]):
            return False
    return True


def phase_4_side_key(state):
    key = ""
    for face in state:
        for side in (1, 3, 5, 7):
            if face[side] == face[4]: key += "-"
            else: key += "X"
        key += "|"
    return key[:-1]

def read_table_4(state):
    key = phase_4_side_key(state)
    if key == "----|----|----|----|----|----": return []
    with open("Thistlethwaite/Tables/phase_4.txt", "r") as table:
        table = table.readlines()
    
    for line in table:
        if line[:29] == key:
            moves = line[32:].strip("\n").split(" ")
            return moves


PHASE_4_TRANSFORMATIONS = [
    ("reflect_XY", REF_XY),
    ("reflect_XZ", REF_XZ),
    ("reflect_YZ", REF_YZ),
    ("X", ROT_X_PRIME),
    ("X_Prime", ROT_X),
    ("X_2", ROT_X_2),
    ("Y", ROT_Y_PRIME),
    ("Y_Prime", ROT_Y),
    ("Y_2", ROT_Y_2),
    ("Z", ROT_Z_PRIME),
    ("Z_Prime", ROT_Z),
    ("Z_2", ROT_Z_2)]

def try_transformations(cube):
    
    # Try with no transformation
    #print("Trying no transformation")
    side_moves = read_table_4(cube)
    if side_moves != None:
        print("NO TRANSFORMATIONS")
        return side_moves
    
    # Try with one transformation
    #print("Trying 1 transformation")
    for transformation, moveset in PHASE_4_TRANSFORMATIONS:
        side_moves = read_table_4(getattr(cube, transformation)())
        if side_moves != None:
            for i, move in enumerate(side_moves):
                if move in moveset.keys(): side_moves[i] = moveset[move]
                
            print(transformation)
            return side_moves
    
    # Try with two transformations
    #print("Trying 2 transformations")
    for transformation_1, moveset_1 in PHASE_4_TRANSFORMATIONS:
            for transformation_2, moveset_2 in PHASE_4_TRANSFORMATIONS:
                side_moves = read_table_4(getattr(Node(getattr(cube, transformation_1)()), transformation_2)())
                if side_moves != None:
                    for i, move in enumerate(side_moves):
                        
                        if move in moveset_2.keys(): transformed_1 = moveset_2[move]
                        else: transformed_1 = move
                        
                        if transformed_1 in moveset_1.keys(): transformed_2 = moveset_1[transformed_1]
                        else: transformed_2 = transformed_1
                        
                        side_moves[i] = transformed_2
                    print(transformation_1, transformation_2)

                    return side_moves
    

    # Try with three transformations
    #print("Trying 3 transformations")
    for transformation_1, moveset_1 in PHASE_4_TRANSFORMATIONS:
        for transformation_2, moveset_2 in PHASE_4_TRANSFORMATIONS:
            for transformation_3, moveset_3 in PHASE_4_TRANSFORMATIONS:
                side_moves = read_table_4(getattr(Node(getattr(Node(getattr(cube, transformation_1)()), transformation_2)()), transformation_3)())
                if side_moves != None:
                    for i, move in enumerate(side_moves):
                        
                        if move in moveset_3.keys(): transformed_1 = moveset_3[move]
                        else: transformed_1 = move
                        
                        if transformed_1 in moveset_2.keys(): transformed_2 = moveset_2[transformed_1]
                        else: transformed_2 = transformed_1
                        
                        if transformed_2 in moveset_1.keys(): transformed_3 = moveset_1[transformed_2]
                        else: transformed_3 = transformed_2
                        
                        side_moves[i] = transformed_3
                    print(transformation_1, transformation_2, transformation_3)

                    
                    raise Exception("THREE TRANSFORMATIONS")
                    return side_moves

    # Try with four transformations
    #print("Trying 4 transformations")
    #for transformation_1, moveset_1 in PHASE_4_TRANSFORMATIONS:
    #   for transformation_2, moveset_2 in PHASE_4_TRANSFORMATIONS:
    #       for transformation_3, moveset_3 in PHASE_4_TRANSFORMATIONS:
    #           for transformation_4, moveset_4 in PHASE_4_TRANSFORMATIONS:
    #               side_moves = read_table_4(getattr(Node(getattr(Node(getattr(Node(getattr(cube, transformation_1)()), transformation_2)()), transformation_3)()), transformation_4)())
    #               if side_moves != None:
    #                   for i, move in enumerate(side_moves):
    #                       
    #                       if move in moveset_4.keys(): transformed_1 = moveset_4[move]
    #                       else: transformed_1 = move
    #               
    #                       if transformed_1 in moveset_3.keys(): transformed_2 = moveset_3[transformed_1]
    #                       else: transformed_2 = transformed_1
    #                       
    #                       if transformed_2 in moveset_2.keys(): transformed_3 = moveset_2[transformed_2]
    #                       else: transformed_3 = transformed_2
    #                       
    #                       if transformed_3 in moveset_1.keys(): transformed_4 = moveset_1[transformed_3]
    #                       else: transformed_4 = transformed_2
    #                      
    #                       side_moves[i] = transformed_4
    #                      
    #                   print(transformation_1, transformation_2, transformation_3, transformation_4)
    #                   return side_moves
    raise Exception("No phase 4 table moves found")   



def bfs_sides(start_state):
    cur_start_node = Node(start_state)
    cur_end_node = Node([start_state[i][4] * 9 for i in range(6)])

    start_queue = Queue(9999999)
    end_queue = Queue(9999999)

    visited_start_nodes = []
    visited_end_nodes = []

    generation = 0

    # Limits the search to a certain depth
    while generation <= 8:
        print(generation)
        next_gen = generation + 1


        # Searches through the current generation of start nodes
        visited_start_nodes = []
        while cur_start_node.generation == generation:
            
            # If the node is found in the visited end nodes, return both the current node and the found node
            check, node = binSearch(visited_end_nodes, cur_start_node)
            if check == True:
                print("FOUND")
                return cur_start_node, node, generation
            
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
            check, node = binSearch(visited_start_nodes, cur_end_node)
            if check == True:
                return node, cur_end_node, generation
            
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
    start_node, end_node, generation = bfs_sides(start_node.cube)
    path = []


    if start_node == None:
        print("No path found")

    else:
        while start_node.parent != None:
            path.append(G_3[start_node.movement])
            start_node = start_node.parent
        path = path[::-1]

        while end_node.parent != None:
            path.append(G_3[end_node.movement])
            end_node = end_node.parent

    return path, generation


    # corner_moves = []
    # ## Get moves to fix the corners
    # returned_nodes = corners_iddfs(Node(start_node.cube))

    # for node in returned_nodes:

    #     parent = node.parent
    #     if parent != None:
    #         corner_moves.append(G_3[node.movement])
    #         while parent.movement != None:
    #             corner_moves.append(G_3[parent.movement])
    #             parent = parent.parent


    #     start_node, end_node = bfs_sides(node.cube)
    #     path = []


    #     if start_node == None:
    #         print("No path found")

    #     else:
    #         while start_node.parent != None:
    #             path.append(G_3[start_node.movement])
    #             start_node = start_node.parent
    #         path = path[::-1]

    #         while end_node.parent != None:
    #             path.append(G_3[end_node.movement])
    #             end_node = end_node.parent

    #     return corner_moves + path

    #     # try:
    #     #     corner_moves = []
    
    #     #     parent = corner_node.parent
    #     #     if parent != None:
    #     #         corner_moves.append(G_3[corner_node.movement])
    #     #         while parent.movement != None:
    #     #             corner_moves.append(G_3[parent.movement])
    #     #             parent = parent.parent
    
        
    #     #     corner_moves = corner_moves[::-1]
    
    #     #     side_moves = try_transformations(corner_node)

    #     #     return corner_moves + side_moves
        
    #     # except: pass
    raise Exception("No moves found for phase 4")

