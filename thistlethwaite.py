from cube_3 import Cube3
from Assets.node_3 import Node
from Assets.stack import Stack
from transformations import *
import time
import random


# Phase 1 Moveset
G_0 = (
    "U", "U_Prime", "D", "D_Prime",
    "L", "L_Prime", "R", "R_Prime",
    "F", "F_Prime", "B", "B_Prime")


# Phase 2 Moveset
G_1 = (
    "L", "L_Prime", "L_2",
    "R", "R_Prime", "R_2", 
    "F", "F_Prime", "F_2",
    "B", "B_Prime", "B_2", 
    "U_2", "D_2")

# Phase 3 Moveset
G_2 = (
    "L", "L_Prime", "L_2",
    "R", "R_Prime", "R_2",
    "F_2", "B_2", "U_2", "D_2")

# Phase 4 moveset
G_3 = (
    "L_2", "R_2",
    "F_2", "B_2",
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
    node = solve_sides(Node(start_state))
    if node == None: return "Cannot Solve!"
    end_state = node.cube

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
    with open("Tables/phase_2.txt") as table:
        for line in table.readlines():
            if line[:8] == corners:
                return line[11:].split(" ")
        
def phase_2(G_1_state):
    node = get_UD_slice(Node(G_1_state))
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
        

### Phase 3
## Fix corner orbits
ORBIT_MOVES = {
    "00000000" : [],
    "10100000" : [],
#    "10000010" : [],
    "11001100" : [],
    "10000100" : [6],
    "11000000" : [2, 8],
    "10101010" : [0],
    "10101100" : [0, 6],
    "11101000" : [1, 8],
    "11000011" : [9],
    "10100101" : [5, 6],
    "11100001" : [0, 9],
    "10101111" : [0],
    "11101101" : [6, 3],
    "11001111" : [0, 3, 8],
    "11111111" : [0, 3]}

def get_orbits(cube):
    group_c = (cube[0][4], cube[5][4])
    corners = ""

    for face in (0, 5):
        for index in (0, 2, 6, 8):
            if cube[face][index] not in group_c: corners += "1"
            else: corners += "0"

    return corners

# Transformations used in phase 2
TRANSFORMATIONS = (
    # Corners  |  Moves
    ("10325476", "4351026789"), # Reflection YZ
    ("23016745", "1024357689"), # Reflection XY
    ("67452301", "1024356798"), # Reflection XZ
    ("23456701", "0123458967"), # Rotation X Clockwise
    ("67012345", "0123459867"), # Rotation X Anticlockwise
    ("45670123", "0123457698"), # Rotation X 180
    ("76543210", "3450126798"), # Rotation Z 180
    ("32107654", "3450127689")) # Rotation Y 180

def transform_corners(corners, transformation):
    new_corners = ""
    for index in transformation:
        new_corners += corners[int(index)]
        
    return new_corners

def transform_moves(moves, move_keys):
    new_moves = []
    for move in moves:
        new_moves.append(int(move_keys[move]))
    
    return new_moves

def fix_orbits(corners):
    # Try with no transformations
    if corners in ORBIT_MOVES.keys():
        # print("No Transformation")
        return ORBIT_MOVES[corners]
    
    # Try with one transformation
    for index, (transformation, move_keys) in enumerate(TRANSFORMATIONS):
        transformed_corners = transform_corners(corners, transformation)
        if transformed_corners in ORBIT_MOVES.keys():
            # print("Transformation: ", index, transformed_corners)
            return transform_moves(ORBIT_MOVES[transformed_corners], move_keys)
       
    # Try with two transformations
    for index_1, (transformation_1, move_keys_1) in enumerate(TRANSFORMATIONS):
        for index_2, (transformation_2, move_keys_2) in enumerate(TRANSFORMATIONS):
            transformed_corners = transform_corners(transform_corners(corners, transformation_1), transformation_2)
            if transformed_corners in ORBIT_MOVES.keys():
                # print("Transformation: ", index_1, index_2, transformed_corners)
                return transform_moves(transform_moves(ORBIT_MOVES[transformed_corners], move_keys_1), move_keys_2)
            
    raise Exception("NOT SOLVED")



## Fixes sides and remaining corners

ALLOWED_ORBITS = list(ORBIT_MOVES.keys())[:3]
# Decides which table to use and which transformations are applied
def get_fixed_orbits(cube):
    transformed_cube = Cube3()
    
    # Try with no transformation
    orbits = get_orbits(cube)
    if orbits in ALLOWED_ORBITS:
        return cube, ALLOWED_ORBITS.index(orbits), None
    
    # Try with one transformation
    for index, transformation in enumerate(("reflect_XY", "reflect_XZ", "reflect_YZ", "X", "X_Prime", "Y_2", "Z_2")):
        transformed_cube.cube = getattr(cube, transformation)()
        orbits = get_orbits(transformed_cube)
        
        if orbits in ALLOWED_ORBITS:
            return transformed_cube, ALLOWED_ORBITS.index(orbits), index
            
    raise Exception("NO RESULTING ORBITS. TRY WITH 2 TRANSFORMATIONS?")


# Get the key for table moves
def phase_3_sides_key(cube):
    sides_key = ["", "", ""]
    group_UD = (cube[0][4], cube[5][4])
    group_FB = (cube[2][4], cube[4][4])

    for i, face in enumerate((cube[0], cube[5])):
        for edge in (1, 3, 5, 7):
            if face[edge] in group_UD:
                sides_key[i * 2] += "-"
            else: sides_key[i * 2] += "X"
    
    for i, face in enumerate((cube[2], cube[4])):
        for edge in (3, 5):
            if face[edge] in group_FB: sides_key[1] += "-"
            else: sides_key[1] += "X"
    
    return "|".join(sides_key)

# Returns the table from a file
def read_table_3(file_name):
    with open(file_name, "r") as table:
        return table.readlines()

# Finds moveset from table
def get_table_3_moves(cube, table_num):
    print("Table:", table_num)

    if table_num == 0:
        table = read_table_3("Tables/phase_3_no_corners.txt")
        transformations = [("reflect_YZ", REF_YZ)]
        
    elif table_num == 1:
        table = read_table_3("Tables/phase_3_two_corners.txt")    
        transformations = [("reflect_YZ", REF_YZ)]
        
    elif table_num == 2:
        table = read_table_3("Tables/phase_3_four_corners.txt")
        transformations = [("reflect_YZ", REF_YZ)]
    
    # Try with no transformations
    sides = phase_3_sides_key(cube)
    for line in table:
        if sides == line[:14]:
            test_cube = Cube3(cube.cube)
            moves = line[17:].strip("\n").split(" ")
            for move in moves:
                test_cube.move(move)
                
            if test_corner_permutation(test_cube) == True:
                test_cube.display()
                return moves
            
    # Try with transformations
    for transformation, moveset in transformations:
       transformed_cube = Cube3(getattr(cube, transformation)())
       sides = phase_3_sides_key(transformed_cube)
       for line in table:
           if sides == line[:14]:
            test_cube = Cube3(transformed_cube.cube)
            moves = line[17:].strip("\n").split(" ")
            for move in moves:
                test_cube.move(move)
                
            if test_corner_permutation(test_cube) == True:
                return moves
            

    raise Exception("NO MOVES FOUND IN PHASE 3 TABLES")

def test_corner_permutation(cube):
    for face_1, face_2 in ((cube[0], cube[5]), (cube[1], cube[3]), (cube[2], cube[4])):
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
    
    cube.move("X")
    for face_1, face_2 in ((cube[0], cube[5]), (cube[1], cube[3]), (cube[2], cube[4])):
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
        
    cube.move("Z")
    for face_1, face_2 in ((cube[0], cube[5]), (cube[1], cube[3]), (cube[2], cube[4])):
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
    return True

    


PHASE_3_TRANSFORMATIONS = (REF_XY, REF_XZ, REF_YZ, ROT_X_PRIME, ROT_X, ROT_Y_2, ROT_Z_2)


def phase_3(G_2_state):
    phase_3_moves = []
    corner_orbits = get_orbits(G_2_state)
    # print("Orbits: ", corner_orbits)
    
    cube = Cube3(G_2_state)
    orbit_moves = fix_orbits(corner_orbits)
    for move in orbit_moves:
        phase_3_moves.append(G_2[move])
        cube.move(G_2[move])
        
    
    print("Moves: ", phase_3_moves)
    
    transformed_cube, table_num, transformation_index = get_fixed_orbits(cube)
    print("Transformation:", transformation_index)
    

    moves = get_table_3_moves(transformed_cube, table_num)
    print("Untransformed moves:", moves)
    
    
    if transformation_index != None:
        transformation = PHASE_3_TRANSFORMATIONS[transformation_index]
        
        for move in moves:
            if move in transformation.keys():
                phase_3_moves.append(transformation[move])
                cube.move(transformation[move])
            else: 
                phase_3_moves.append(move)
                cube.move(move)
            
    else:
        for move in moves:
            phase_3_moves.append(move)
            cube.move(move)
    
    print("Phase 3 moves:", phase_3_moves)
    
    return phase_3_moves, cube




### Phase 4

## Fix corners
def corners_iddfs(cube):

    start_node = Node(cube.cube)
    if check_corners(start_node): return Stack(0), Cube3(start_node.cube)
    
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
                    node_stack.push(current_node)
                    return node_stack, Cube3(current_node.cube)
                
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
                        

    print("Corner search exhausted!")
                        
# Check if all the corners are home
def check_corners(node):
    for face in node.cube:
        if not (face[4] == face[0] == face[2] == face[6] == face[8]):
            return False
    return True

def check_solved(cube):
    for face in cube.cube:
        for peice in face:
            if peice != face[4]: return False
            
    return True


def sides_iddfs(cube):
    start_node = Node(cube.cube)
    if check_solved(start_node): return Stack(0)
    
    for i in range(12):
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
                current_movement  = current_node.movement
                
                parent = current_node.parent
                
                # Check if the current node is correct
                if check_solved(current_node):
                    node_stack.push(current_node)
                    return node_stack
                
                # Push next movement
                if current_movement < 5 and current_movement + 1 != parent.movement:node_stack.push(Node(getattr(parent, G_3[current_movement + 1])(), current_movement + 1, parent))
                elif current_movement < 4 and current_movement + 1 == parent.movement: node_stack.push(Node(getattr(parent, G_3[current_movement + 2])(), current_movement + 2, parent))
                
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

    print("Side search exhausted!")

## Fix sides
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
    with open("Tables/phase_4.txt", "r") as table:
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
    print("Trying no transformation")
    side_moves = read_table_4(cube)
    if side_moves != None:
        return side_moves
    
    # Try with one transformation
    print("Trying 1 transformation")
    for transformation, moveset in PHASE_4_TRANSFORMATIONS:
        side_moves = read_table_4(getattr(cube, transformation)())
        if side_moves != None:
            for i, move in enumerate(side_moves):
                if move in moveset.keys(): side_moves[i] = moveset[move]
            print(transformation)
            return side_moves
    
    # Try with two transformations
    print("Trying 2 transformations")
    for transformation_1, moveset_1 in PHASE_4_TRANSFORMATIONS:
            for transformation_2, moveset_2 in PHASE_4_TRANSFORMATIONS:
                side_moves = read_table_4(getattr(Cube3(getattr(cube, transformation_1)()), transformation_2)())
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
    print("Trying 3 transformations")
    for transformation_1, moveset_1 in PHASE_4_TRANSFORMATIONS:
        for transformation_2, moveset_2 in PHASE_4_TRANSFORMATIONS:
            for transformation_3, moveset_3 in PHASE_4_TRANSFORMATIONS:
                side_moves = read_table_4(getattr(Cube3(getattr(Cube3(getattr(cube, transformation_1)()), transformation_2)()), transformation_3)())
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
                    return side_moves

    # Try with four transformations
    print("Trying 4 transformations")
    for transformation_1, moveset_1 in PHASE_4_TRANSFORMATIONS:
        for transformation_2, moveset_2 in PHASE_4_TRANSFORMATIONS:
            for transformation_3, moveset_3 in PHASE_4_TRANSFORMATIONS:
                for transformation_4, moveset_4 in PHASE_4_TRANSFORMATIONS:
    raise Exception("No phase 4 table moves found")






def phase_4(cube):
    cube.display()
    corner_moves = []
    ## Get moves to fix the corners
    node_stack, cube = corners_iddfs(cube)

    while not node_stack.is_empty():
        node = node_stack.pop()
        corner_moves.append(G_3[node.movement])
        
    corner_moves = corner_moves[::-1]
    print("corner moves:", corner_moves)
    
    side_moves = try_transformations(cube)
                
    
    

    return corner_moves + side_moves

    
# Function to organise solving the cube
def thistle_solve(start_state):
    Cube3(start_state).display()
    # Phase 1
    timer = time.time()
    phase_1_moves, G_1_state = phase_1(start_state) 
    print(f"Phase 1 finished in {time.time() - timer}s")
    print(phase_1_moves)
    Cube3(G_1_state).display()
    

    # Phase 2
    timer = time.time()
    phase_2_moves, G_2_state = phase_2(G_1_state)
    print(f"Phase 2 finished in {time.time() - timer}s")
    print(phase_2_moves)
    Cube3(G_2_state).display()



    timer = time.time()
    phase_3_moves, G_3_cube = phase_3(G_2_state)
    print(f"Phase 3 finished in {time.time() - timer}s")
    print("Phase 3 cube:")
    G_3_cube.display()

    phase_4_moves = phase_4(G_3_cube)
    print("Phase 4 moves:", phase_4_moves)
    return phase_1_moves + phase_2_moves + phase_3_moves + phase_4_moves

cube = Cube3()
for i in range(1):
    print("==========\nSTARTING\n==========")
    cube.scramble()
    print(cube.cube)
    try:
        print(thistle_solve(cube))
        break
    except: print("Error")
    
print(i)