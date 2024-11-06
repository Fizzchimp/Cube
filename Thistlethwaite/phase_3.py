from Assets.node_3 import Node
from Thistlethwaite.transformations import *
from Thistlethwaite.phase_4 import phase_4


# Phase 3 Moveset
G_2 = (
    "L", "L_Prime", "L_2",
    "R", "R_Prime", "R_2",
    "F_2", "B_2", "U_2", "D_2")

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

ALLOWED_ORBITS = list(ORBIT_MOVES.keys())[:-12]

FIXED_ORBITS_TRANSFORMATIONS = [
    "reflect_XY",
    "reflect_XZ",
    "reflect_YZ",
    "X",
    "X_Prime",
    "Y_2",
    "Z_2"]

# Decides which table to use and which transformations are applied
def get_fixed_orbits(cube):
    
    # Try with no transformation
    orbits = get_orbits(cube)
    if orbits in ALLOWED_ORBITS:
        return cube, ALLOWED_ORBITS.index(orbits), (-1, -1)
    
    transformed_node = Node()
    
    # Try with one transformation
    for i, transformation in enumerate(FIXED_ORBITS_TRANSFORMATIONS):
        transformed_node.cube = getattr(cube, transformation)()
        orbits = get_orbits(transformed_node)
        
        if orbits in ALLOWED_ORBITS:
            return transformed_node, ALLOWED_ORBITS.index(orbits), (i, -1)
    
    # Try with two transformations
    for i, transformation_1 in enumerate(FIXED_ORBITS_TRANSFORMATIONS):
        for j, transformation_2 in enumerate(FIXED_ORBITS_TRANSFORMATIONS):
            transformed_node.cube = getattr(Node(getattr(cube, transformation_1)()), transformation_2)()
            orbits = get_orbits(transformed_node)
            
            if orbits in ALLOWED_ORBITS:
               return transformed_node, ALLOWED_ORBITS.index(orbits), (i, j)
            
    raise Exception("NO RESULTING ORBITS. TRY WITH 3 TRANSFORMATIONS? I thought I already fixed this :(")


# Get the key for table moves
def get_key(cube):
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

# Tests if the given node is in G_3
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

    

PHASE_3_TRANSFORMATIONS = (
    REF_XY,
    REF_XZ,
    REF_YZ,
    ROT_X_PRIME,
    ROT_X,
    ROT_Y_2,
    ROT_Z_2,
    {None : None}) # No transformation


NO_CORNER_TRANSFORMATIONS = (
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
    ("Z_2", ROT_Z_2))

TWO_CORNER_TRANSFORMATIONS = (
    ("reflect_YZ", REF_YZ),
    ("Y_2_X", ROT_X_PRIME_Y_2))

FOUR_CORNER_TRANSFORMATIONS = (
    ("X_2", ROT_X_2),
    ("reflect_YZ", REF_YZ))

# Try transformations to get the moves to solve the sides
def get_side_moves(node, table_num):
    table = get_table(table_num)
    transformations = (NO_CORNER_TRANSFORMATIONS, TWO_CORNER_TRANSFORMATIONS, FOUR_CORNER_TRANSFORMATIONS)[table_num]
    
    # Try with no transformations
    # print("TRYING NO TRANSFORMATIONS")
    moves = check_table(table, node)
    if moves != False: return moves
    
    # Try with 1 transformation
    # print("TRYING UNO TRANSFORMATION")
    for transformation, moveset in transformations:
        transformed_node = Node(getattr(node, transformation)())
        moves = check_table(table, transformed_node)
        if moves != False:
            for i, move in enumerate(moves):
                if move in moveset.keys(): move = moveset[move]
                moves[i] = move
                
            return moves
    
    # Try with two transformations
    # print("TRYING DOS TRANSFORMAITONS")    
    for transformation_1, moveset_1 in transformations:
        for transformation_2, moveset_2 in transformations:
            transformed_node = Node(getattr(Node(getattr(node, transformation_1)()), transformation_2)())
            moves = check_table(table, transformed_node)
            if moves != False:
                for i, move in enumerate(moves):
                    if move in moveset_2.keys(): move = moveset_2[move]
                    if move in moveset_1.keys(): move = moveset_1[move]
                    
                    moves[i] = move
                print("TWO TRANSFORMATIONS:", transformation_1, transformation_2)
                return moves

    raise Exception("NO MOVES FOUND IN PHASE 3 TABLES")        

# Returns table from specified table_number
def get_table(table_num):
    if table_num == 0:
        with open("Thistlethwaite/Tables/phase_3_no_corners.txt", "r") as table:
            return table.readlines()
    
    if table_num == 1:
        with open("Thistlethwaite/Tables/phase_3_two_corners.txt", "r") as table:
            return table.readlines()
        
    if table_num == 2:
        with open("Thistlethwaite/Tables/phase_3_four_corners.txt", "r") as table:
            return table.readlines()


# Checks the table for moves to solve the given node
def check_table(table, node):
    key = get_key(node)
    
    # Checks through each line in the table
    for line in table:
        
        # Check if key matches item in table
        if line[:14] == key:
            moves = line[17:].strip("\n").split(" ")
            test_node = Node(node.cube)
            for move in moves:
                test_node.move(move)
            
            # Checks if the solution is in G_3 (WONT KNOW IF THIS WORKS FULLY UNTIL PHASE 3 IS FIXED)
            if test_corner_permutation(test_node):
                print("Corner Permutation test success")
                try:
                    phase_4(test_node)
                    return moves
                
                except: pass
            
    # If no solution is found, return false        
    return False

def phase_3(node):
    phase_3_moves = []
    
    # Fix orbits to be 1 of 3 possible states
    corner_orbits = get_orbits(node)
    #print("Orbits: ", corner_orbits)
    
    orbit_moves = fix_orbits(corner_orbits)
    for move in orbit_moves:
        phase_3_moves.append(G_2[move])
        node.move(G_2[move])
        
    
    # print("Corner moves: ", phase_3_moves)
    
    # Transform node to be used in table
    transformed_node, table_num, transformation_indexes = get_fixed_orbits(node)
    # print("Transformations:", transformation_indexes)
    
    # Get the moves to fix the transformed node
    moves = get_side_moves(transformed_node, table_num)
    # print("Untransformed moves:", moves)
    
    # Transform moves to work on origional node
    transformation_1 = PHASE_3_TRANSFORMATIONS[transformation_indexes[0]]
    transformation_2 = PHASE_3_TRANSFORMATIONS[transformation_indexes[1]]
        
    for move in moves:
        if move in transformation_2.keys(): move = transformation_2[move]
        if move in transformation_1.keys(): move = transformation_1[move]

        phase_3_moves.append(move)
        node.move(move)
    
    print("Phase 3 moves:", phase_3_moves)
    
    return phase_3_moves, node


node = Node(['RWWWWRRWW', 'BBBBGGBBB', 'WOOYRWORY', 'GBGGBGGGG', 'RRYROOYOO', 'YYRYYOWYO'])
#print(phase_3(node))