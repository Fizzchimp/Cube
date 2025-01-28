from Assets.node_3 import Node
from Assets.stack import Stack
from Thistlethwaite.transformations import *
from Thistlethwaite.Tables.table import Table

# Return the state of a node after applied move
def get_node_move(parent, move_num, move_set):
    try: return getattr(parent, move_set[move_num])()
    except IndexError: raise Exception("Invalid Move!")
    

# Phase 2 Moveset
PHASE_2_MOVES = (
    "L", "L_Prime", "L_2",
    "R", "R_Prime", "R_2", 
    "F", "F_Prime", "F_2",
    "B", "B_Prime", "B_2", 
    "U_2", "D_2")

# List of indexes for each corner peice
CORNERS = (
    ((1, 0), (4, 2), (0, 0)),
    ((1, 2), (0, 6), (2, 0)),
    ((1, 6), (5, 6), (4, 8)),
    ((1, 8), (2, 6), (5, 0)),
    
    ((3, 0), (2, 2), (0, 8)),
    ((3, 2), (0, 2), (4, 0)),
    ((3, 6), (5, 2), (2, 8)),
    ((3, 8), (4, 6), (5, 8)))

# Checks if the given node is already in G_2
def check_state(node):
    # Get the group to compare all facelets to
    target_group = (node[1][4], node[3][4])
    # Check each facelet. If all are in correct group, cube already in G_2
    for face in (node[1], node[3]):
        for facelet in face:
            if facelet not in target_group: return False
    return True


# Check the state of the UD slice
def UD_side_check(node):
    # Gets the target group
    group_c = (node[0][4], node[5][4])
    # If all UD slice peices in the correct place, returns True
    if node[1][3] in group_c and node[1][5] in group_c and node[3][3] in group_c and node[3][5] in group_c: return True
    return False

# IDDFS to get required sides in the UD slice
def get_UD_slice_iddfs(start_node):

    # Checks if UD slice is already fixed
    if UD_side_check(start_node): return start_node

    # Maximum depth is 6
    for i in range(5):
        # Create stack and push first node
        node_stack = Stack(i + 1)
        node_stack.push(Node(start_node.L(), 0, start_node))

        exhausted = False
        # If at all possible nodes explored, exhasuted will be set to true
        while not exhausted:

            # Branch down to required depth
            if not node_stack.is_full():
                parent = node_stack.peek()
                # Add first movement node
                node_stack.push(Node(parent.L(), 0, parent))

            else:
                # Retreive the youngest node
                current_node = node_stack.pop()
                current_movement = current_node.movement
                parent = current_node.parent

                # Check if the current node is correct
                if UD_side_check(current_node): return current_node
                
                # If not the final node, push node with next movement
                if current_movement <= 10:
                    node_stack.push(Node(get_node_move(parent, current_movement + 1, PHASE_2_MOVES), current_movement + 1, parent))

                # If current branch exhausted remove node and change upper branch
                else:
                    # Indicates if at the top of stack
                    top = True
                    for j in range(i):
                        # Get parent of current node
                        parent = node_stack.pop()
                        # Check if parent is the final node
                        if parent.movement <= 12:
                            top = False
                            break
                    if top: # If at the top of the stack, current depth must be exhausted
                        exhausted = True
                    else: # Change the last node on the stack to be the next movement
                        node_stack.push(Node(get_node_move(parent.parent, parent.movement + 1, PHASE_2_MOVES), parent.movement + 1, parent.parent))
    
    # If no node is found at maximum depth raise an exception
    raise Exception("UD slice not solvable - Phase 2")



# Calculates key based on twist of corners
def get_corners(node):
    # Declare key string
    state = ""
    # Declare target group
    target_colours = (node[1][4], node[3][4])
    
    # Check the twist of each corner
    for corner in CORNERS:
        # Check each facelet of the corner until facelet in target group is found
        for i in range(3):
            if node[corner[i][0]][corner[i][1]] in target_colours:
                state += str(i)
                break

    return state
        

# List of transformations used to find moves in table
TRANSFORMATION_LIST = (
    ("reflect_XY", REF_XY),
    ("reflect_XZ", REF_XZ),
    ("reflect_YZ", REF_YZ),
    ("X_2", ROT_X_2),
    ("Y_2", ROT_Y_2),
    ("Z_2", ROT_Z_2))

# Declare move table used
move_table = Table("Thistlethwaite/Tables/phase_2.txt")

def phase_2(G_1_node):
    # Checks the node is not already in G_2
    if check_state(G_1_node): return [], G_1_node

    # Find set of moves to get correct pieces into UD slice
    node = get_UD_slice_iddfs(Node(G_1_node))
    
    # Create path using returned node
    if node.movement != None:
        parent = node.parent
        path = [PHASE_2_MOVES[node.movement]]
        
        # Append each nodes move in reverse order
        while parent.parent != None:
            path.append(PHASE_2_MOVES[parent.movement])
            parent = parent.parent

        # Reverse order of moves to correct them
        path = path[::-1]

    else: path = []



    ## Use the move table to find moves
    # Attempt with no transformations
    corners = get_corners(node.cube) # Calculate key
    moves = move_table.search_table(corners)
    if moves != None: # If match is found, perform moves on node and add to path
        for move in moves:
            path.append(move)
            node.move(move)
        return path, node
    
    # Attempt with one transformation
    for transformation, moveset in TRANSFORMATION_LIST:
        corners = get_corners(node.transformation(transformation)) # Calculate key from transformed node
        moves = move_table.search_table(corners)
        if moves != None: # If a match is found, transform and perform moves on node and add to path
            for move in moves:
                if move in moveset.keys(): move = moveset[move]
                path.append(move)
                node.move(move)
            return path, node
        
    # Attempt with two transformations
    for transformation_1, moveset_1 in TRANSFORMATION_LIST:
        for transformation_2, moveset_2 in TRANSFORMATION_LIST:
            corners = get_corners(node.transformation(transformation_1, transformation_2)) # Calculate key from transformed node
            moves = move_table.search_table(corners)
            if moves != None: # If a match is found, transform and perform moves on node and add to path
                for move in moves:
                    if move in moveset_2.keys(): move = moveset_2[move]
                    if move in moveset_1.keys(): move = moveset_1[move]
                    path.append(move)
                    node.move(move)
                return path, node
    
    # If no match is found, node is unsolvable
    raise Exception("No moves found - Phase 2")
