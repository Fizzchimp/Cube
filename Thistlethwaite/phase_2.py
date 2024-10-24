from Assets.node_3 import Node
from Assets.stack import Stack


# Return the state of a node after applied move
def get_node_move(parent, move_num, move_set):
    try: return getattr(parent, move_set[move_num])()
    except IndexError: raise Exception("Invalid Move!")
    

# Phase 2 Moveset
G_1 = (
    "L", "L_Prime", "L_2",
    "R", "R_Prime", "R_2", 
    "F", "F_Prime", "F_2",
    "B", "B_Prime", "B_2", 
    "U_2", "D_2")

CORNERS = (
    ((1, 0), (4, 2), (0, 0)),
    ((1, 2), (0, 6), (2, 0)),
    ((1, 6), (5, 6), (4, 8)),
    ((1, 8), (2, 6), (5, 0)),
    
    ((3, 0), (2, 2), (0, 8)),
    ((3, 2), (0, 2), (4, 0)),
    ((3, 6), (5, 2), (2, 8)),
    ((3, 8), (4, 6), (5, 8)))

### Phase 2
def UD_side_check(cube):
    group_c = (cube[0][4], cube[5][4])
    if cube[1][3] in group_c and cube[1][5] in group_c and cube[3][3] in group_c and cube[3][5] in group_c: return True
    return False

def get_UD_slice_iddfs(start_node):
    # To get UD slice correct
    for i in range(5):
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

# All the transformations for the corner
def reflection_XY(corners):
    return (corners[1] + corners[0] + corners[3] + corners[2] + corners[5] + corners[4] + corners[7] + corners[6]).replace("1", "x").replace("2", "1").replace("x", "2")
REF_XY_P2 = (1, 0, 2, 4, 3, 5, 10, 9, 11, 7, 6, 8, 12, 13)

def reflection_XZ(corners):
    return (corners[2] + corners[3] + corners[0] + corners[1] + corners[6] + corners[7] + corners[4] + corners[5]).replace("1", "x").replace("2", "1").replace("x", "2")
REF_XZ_P2 = (1, 0, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 13, 12)

def reflection_YZ(corners):
    return (corners[5] + corners[4] + corners[7] + corners[6] + corners[1] + corners[0] + corners[3] + corners[2]).replace("1", "x").replace("2", "1").replace("x", "2")
REF_YZ_P2 = (4, 3, 5, 1, 0, 2, 7, 6, 8, 10, 9, 11, 12, 13)

def rotation_X(corners):
    return corners[3] + corners[2] + corners[1] + corners[0] + corners[7] + corners[6] + corners[5] + corners[4]
ROT_X_P2 = (0, 1, 2, 3, 4, 5, 9, 10, 11, 6, 7, 8, 13, 12)

def rotation_Y(corners):
    return corners[4:] + corners[:4]
ROT_Y_P2 = (3, 4, 5, 0, 1, 2, 9, 10, 11, 6, 7, 8, 12, 13)

def rotation_Z(corners):
    return corners[::-1]
ROT_Z_P2 = (3, 4, 5, 0, 1, 2, 6, 7, 8, 9, 10, 11, 13, 12)

TRANSFORMATION_LIST = (
    (reflection_XY, REF_XY_P2),
    (reflection_XZ, REF_XZ_P2),
    (reflection_YZ, REF_YZ_P2),
    (rotation_X, ROT_X_P2),
    (rotation_Y, ROT_Y_P2),
    (rotation_Z, ROT_Z_P2))

def get_table_2_moves(corners):
    with open("Thistlethwaite/Tables/phase_2.txt") as table:
        for line in table.readlines():
            if line[:8] == corners:
                return line[11:].split(" ")
        
def phase_2(G_1_state):
    node = get_UD_slice_iddfs(Node(G_1_state))
    if node == None: return "Cannot Solve!"
    G_1_state = node.cube

    path = []
    while node.parent != None:
        move = G_1[node.movement]
        path.append(move)
        node = node.parent
    path = path[::-1]


    corners = get_corners(G_1_state)
    node = Node(G_1_state)

    # Attempt with no transformations
    moves = get_table_2_moves(corners)
    if moves != None:
        for move in moves:
            path.append(G_1[int(move)])
            node.move(G_1[int(move)])
        return path, node

    # Attempt with 1 transformation
    for transformation, moveset in TRANSFORMATION_LIST:
        moves = get_table_2_moves(transformation(corners))
        if moves != None:
            for move in moves:
                path.append(G_1[moveset[int(move)]])
                node.move(G_1[moveset[int(move)]])
            return path, node
        
    # Attempt with 2 transformations
    for transformation_1, moveset_1 in TRANSFORMATION_LIST:
        for transformation_2, moveset_2 in TRANSFORMATION_LIST:
                moves = get_table_2_moves(transformation_2(transformation_1(corners)))
                if moves != None:
                    for move in moves:
                        path.append(G_1[moveset_2[moveset_1[int(move)]]])
                        node.move(G_1[moveset_2[moveset_1[int(move)]]])
                    return path, node
                
    raise Exception("Phase 2 Broken")