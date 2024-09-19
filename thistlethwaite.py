from cube_3 import Cube_3
from Assets.node_3 import Node
from Assets.stack import Stack
import time


# Moveset to get from G0 -> G1
G_0 = ("U", "U_Prime", "D", "D_Prime",
       "L", "L_Prime", "R", "R_Prime",
       "F", "F_Prime", "B", "B_Prime")


# Moveset to get from G1 -> G2
G_1 = ("L", "L_Prime", "L_2",
       "R", "R_Prime", "R_2", 
       "F", "F_Prime", "F_2",
       "B", "B_Prime", "B_2", 
       "U_2", "D_2")

NO_MOVES = [i for i in range(14)]

CORNERS = (((1, 0), (4, 2), (0, 0)),
           ((1, 2), (0, 6), (2, 0)),
           ((1, 6), (5, 6), (4, 8)),
           ((1, 8), (2, 6), (5, 0)),
           
           ((3, 0), (2, 2), (0, 8)),
           ((3, 2), (0, 2), (4, 0)),
           ((3, 6), (5, 2), (2, 8)),
           ((3, 8), (4, 6), (5, 8)))


# Return the state of a node after applied move
def get_node_move(parent, move_num, move_set):
    try: return getattr(parent, move_set[move_num])()
    except IndexError: raise Exception("Invalid Move!")


### Phase 1
def side_check(cube):
    # Flip all side peices to be "good" (can be returned home without the use of an odd number of quater turns of U or D)    
    facePattern1 = (3, 7, 5, 1)
    facePattern2 = (3, 1, 5, 7)
    groups = ((cube[2][4], cube[4][4]), (cube[1][4], cube[3][4]))

    for i in range(4):
        side_peices = ((cube[i + 1][1], cube[0][facePattern1[i]]),
                       (cube[i + 1][3], cube[(i + 3) % 4 + 1][5]),
                       (cube[i + 1][7], cube[5][facePattern2[i]]))

        # Decision tree for 'Good' and 'Bad' Peices
        for peice in side_peices:
            if peice[0] in groups[(i) % 2]: return False
            elif peice[1] in groups[(i + 1) % 2]: return False
    return True

def solve_sides(start_node):
    # IDDFS to get to G1
    if side_check(start_node): return start_node

    for i in range(7):
        node_stack = Stack(i + 1)
        node_stack.push(Node(start_node.U(), 0, start_node))

        exhausted = False
        while not exhausted:

            # Branch down to required depth
            if not node_stack.is_full():
                parent = node_stack.peek()
                node_stack.push(Node(parent.U(), 0, parent))

            else:
                # Retreive the youngest node
                current_node = node_stack.pop()
                current_movement = current_node.movement

                parent = current_node.parent

                # Check if the current node is correct
                if side_check(current_node):
                    node_stack.push(current_node)
                    return current_node
                
            
                # Push D movement (Last move can only be U or D)
                if current_movement == 0:
                    node_stack.push(Node(parent.D(), 2, parent))

                # If current branch exhausted remove node and change upper branch
                else:
                    top = True
                    for j in range(i):
                        parent = node_stack.pop()
                        if parent.movement <= 10:
                            top = False
                            break
                    if top:
                        exhausted = True
                    else:
                        node_stack.push(Node(get_node_move(parent.parent, parent.movement + 1, G_0), parent.movement + 1, parent.parent))

def phase_1(start_state):
    start_time = time.time()

    node = solve_sides(Node(start_state))
    if node == None: return "Cannot Solve!"
    end_state = node.cube

    print(f"Phase 1 finished in {time.time() - start_time}s")

    path = []
    while node.parent != None:
        move = G_0[node.movement]
        path.append(move)
        node = node.parent

    return path[::-1], end_state
    
    

### Phase 2
def UD_side_check(cube):
    group_c = (cube[0][4], cube[5][4])
    if cube[1][3] in group_c and cube[1][5] in group_c and cube[3][3] in group_c and cube[3][5] in group_c: return True
    return False

def get_UD_slice(start_node):
    # To get UD slice correct
    for i in range(5):
        print("Depth:", i)
        node_stack = Stack(i + 1)
        node_stack.push(Node(start_node.L(), 0, start_node))

        exhausted = False
        while not exhausted:

            # Branch down to required depth
            if not node_stack.is_full():
                parent = node_stack.peek()
                node_stack.push(Node(parent.L(), 0, parent))

            else:
                # Retreive the youngest node
                current_node = node_stack.pop()
                current_movement = current_node.movement

                parent = current_node.parent

                # Check if the current node is correct
                if UD_side_check(current_node):
                    return current_node
                
            
                if current_movement <= 10:
                    node_stack.push(Node(get_node_move(parent, current_movement + 1, G_1), current_movement + 1, parent))

                # If current branch exhausted remove node and change upper branch
                else:
                    top = True
                    for j in range(i):
                        parent = node_stack.pop()
                        if parent.movement <= 12:
                            top = False
                            break
                    if top:
                        exhausted = True
                    else:
                        node_stack.push(Node(get_node_move(parent.parent, parent.movement + 1, G_1), parent.movement + 1, parent.parent))

def get_corners(node):
    state = ""
    target_colours = (node[1][4], node[3][4])
    
    for corner in CORNERS:
        for i in range(3):
            if node[corner[i][0]][corner[i][1]] in target_colours:
                state += str(i)
                break

    return state

# All the transformations for the corners
def reflection_XY(corners):
    return corners[1] + corners[0] + corners[3] + corners[2] + corners[5] + corners[4] + corners[7] + corners[6]

def reflection_XZ(corners):
    return corners[2] + corners[3] + corners[0] + corners[1] + corners[6] + corners[7] + corners[4] + corners[5]

def reflection_YZ(corners):
    return corners[5] + corners[4] + corners[7] + corners[6] + corners[1] + corners[0] + corners[3] + corners[2]
REF_YZ = (4, 3, 5, 1, 0, 2, 7, 6, 8, 10, 9, 11, 12, 13)

def rotation_X(corners):
    return corners[3] + corners[2] + corners[1] + corners[0] + corners[7] + corners[6] + corners[5] + corners[4]
ROT_X = (0, 1, 2, 3, 4, 5, 9, 10, 11, 6, 7, 8, 13, 12)

def rotation_Y(corners):
    return corners[4:] + corners[:4]
ROT_Y = (3, 4, 5, 0, 1, 2, 9, 10, 11, 6, 7, 8, 12, 13)

def rotation_Z(corners):
    return corners[::-1]
ROT_Z = (3, 4, 5, 0, 1, 2, 6, 7, 8, 9, 10, 11, 13, 12)

def get_table_moves(corners):
    with open("Tables/phase_2.txt") as table:
        for line in table.readlines():
            if line[:8] == corners:
                return line[11:].split(" ")
        
def phase_2(start_state):
    node = get_UD_slice(Node(start_state))
    if node == None: return "Cannot Solve!"
    end_state = node.cube

    path = []
    while node.parent != None:
        move = G_1[node.movement]
        path.append(move)
        node = node.parent
    path = path[::-1]


    corners = get_corners(end_state)

    # Attempt with no transformations
    moves = get_table_moves(corners)
    if moves != None:
        print("No transformation")
        for move in moves:
            path.append(G_1[int(move)])
        return path

    # Attempt with transformations
    for transformation, moveset in ((reflection_XY, NO_MOVES), (reflection_XZ, NO_MOVES), (reflection_YZ, REF_YZ), (rotation_X, ROT_X), (rotation_Y, ROT_Y), (rotation_Z, ROT_Z)):
        moves = get_table_moves(transformation(corners))
        if moves != None:
            print(transformation)
            for move in moves:
                path.append(G_1[moveset[int(move)]])
            return path

    else: print("NOT FOUND")
    return path
        

    

# Function to organise solving the cube
def thistle_solve(start_state):
    # Phase 1
    phase_1_moves, next_state = phase_1(start_state)
    
    # Phase 2
    phase_2_moves = phase_2(next_state)

    return phase_1_moves + phase_2_moves