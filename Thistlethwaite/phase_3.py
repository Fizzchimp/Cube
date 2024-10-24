from Assets.node_3 import Node
from Thistlethwaite.transformations import *


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
print(ALLOWED_ORBITS)

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
        return cube, ALLOWED_ORBITS.index(orbits), None
    
    transformed_cube = Node()
    
    # Try with one transformation
    for i, transformation in enumerate(FIXED_ORBITS_TRANSFORMATIONS):
        transformed_cube.cube = getattr(cube, transformation)()
        orbits = get_orbits(transformed_cube)
        
        if orbits in ALLOWED_ORBITS:
            return transformed_cube, ALLOWED_ORBITS.index(orbits), (i, -1)
    
    # Try with two transformations
    for i, transformation_1 in enumerate(FIXED_ORBITS_TRANSFORMATIONS):
        for j, transformation_2 in enumerate(FIXED_ORBITS_TRANSFORMATIONS):
            transformed_cube.cube = getattr(Node(getattr(cube, transformation_1)()), transformation_2)()
            orbits = get_orbits(transformed_cube)
            
            if orbits in ALLOWED_ORBITS:
               return transformed_cube, ALLOWED_ORBITS.index(orbits), (i, j)
            
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
        table = read_table_3("Thistlethwaite/Tables/phase_3_no_corners.txt")
        transformations = [
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
        
    elif table_num == 1:
        table = read_table_3("Thistlethwaite/Tables/phase_3_two_corners.txt")    
        transformations = [("reflect_YZ", REF_YZ)]
        
    elif table_num == 2:
        table = read_table_3("Thistlethwaite/Tables/phase_3_four_corners.txt")
        transformations = [
            ("reflect_YZ", REF_YZ),
            ("X_2", ROT_X_2)]
    
    # Try with no transformations
    sides = phase_3_sides_key(cube)
    for line in table:
        if sides == line[:14]:
            test_cube = Node(cube.cube)
            moves = line[17:].strip("\n").split(" ")
            for move in moves:
                test_cube.move(move)
                
            if test_corner_permutation(test_cube) == True:
                test_cube.display()
                return moves
            
    # Try with transformations
    print("Trying with transformations")
    for transformation, moveset in transformations:
       transformed_cube = Node(getattr(cube, transformation)())
       sides = phase_3_sides_key(transformed_cube)
       for line in table:
           if sides == line[:14]:
            test_cube = Node(transformed_cube.cube)
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

    


PHASE_3_TRANSFORMATIONS = (
    REF_XY,
    REF_XZ,
    REF_YZ,
    ROT_X_PRIME,
    ROT_X,
    ROT_Y_2,
    ROT_Z_2,
    {None : None})


def phase_3(G_2_state):
    phase_3_moves = []
    corner_orbits = get_orbits(G_2_state)
    # print("Orbits: ", corner_orbits)
    
    cube = Node(G_2_state)
    orbit_moves = fix_orbits(corner_orbits)
    for move in orbit_moves:
        phase_3_moves.append(G_2[move])
        cube.move(G_2[move])
        
    
    print("Moves: ", phase_3_moves)
    
    transformed_cube, table_num, transformation_indexes = get_fixed_orbits(cube)
    print("Transformations:", transformation_indexes)
    

    moves = get_table_3_moves(transformed_cube, table_num)
    print("Untransformed moves:", moves)
    
    
    if transformation_indexes != None:
        transformation_1 = PHASE_3_TRANSFORMATIONS[transformation_indexes[0]]
        transformation_2 = PHASE_3_TRANSFORMATIONS[transformation_indexes[1]]
        
        for move in moves:
            if move in transformation_2.keys(): move = transformation_2[move]
            if move in transformation_1.keys(): move = transformation_1[move]
             
            phase_3_moves.append(move)
            cube.move(move)   
    else:
        for move in moves:
            phase_3_moves.append(move)
            cube.move(move)
    
    print("Phase 3 moves:", phase_3_moves)
    
    return phase_3_moves, cube


node = Node(['OWRYWOWYO', 'GBGGGGBGB', 'RRWYRRYOY', 'BBBBBBGGG', 'WRYWOOOOY', 'RYRRYWOWW'])
phase_3(node)