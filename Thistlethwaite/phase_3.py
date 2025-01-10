from Assets.node_3 import Node
from Thistlethwaite.transformations import *
from Thistlethwaite.Tables.table import Table
from Thistlethwaite.phase_4 import phase_4


# Phase 3 Moveset
# G_2 = (
#     "L", "L_Prime", "L_2",
#     "R", "R_Prime", "R_2",
#     "F_2", "B_2", "U_2", "D_2")


### Phase 3
## Fix corner orbits

# Possible arrangements of corner orbits with corresponding moves
ORBIT_KEYS = {
    "00000000" : [],
    "10100000" : [],
    "11001100" : [],
    "10000100" : ["F_2"],
    "11000000" : ["L_2", "U_2"],
    "10101010" : ["L"],
    "10101100" : ["L", "F_2"],
    "11101000" : ["L_Prime", "U_2"],
    "11000011" : ["D_2"],
    "10100101" : ["R_2", "F_2"],
    "11100001" : ["L", "D_2"],
    "10101111" : ["L"],
    "11101101" : ["F_2", "R"],
    "11001111" : ["L", "R", "U_2"],
    "11111111" : ["L", "R"]}

# Calculates the orbits of all 8 corners
def get_orbits(cube):
    # Define group of top and bottom faces
    group_c = (cube[0][4], cube[5][4])
    corners = ""

    # Check top and bottom faces
    for face in (0, 5):
        # Check each corner of the face
        for index in (0, 2, 6, 8):
            # If facelet in correct group, corner is in orbit
            if cube[face][index] not in group_c: corners += "1"
            else: corners += "0"

    return corners


# Transformations used to fix orbits (node transformation, move transformation)
TRANSFORMATIONS = (
    ("reflect_XY", REF_XY),
    ("reflect_XZ", REF_XZ),
    ("reflect_YZ", REF_YZ),
    ("X", ROT_X_PRIME),
    ("X_Prime", ROT_X),
    ("X_2", ROT_X_2),
    ("Y_2", ROT_Y_2),
    ("Z_2", ROT_Z_2))


def fix_orbits(node):
    # Try with no transformations
    orbits = get_orbits(node) # Determine the orbits
    if orbits in ORBIT_KEYS.keys(): # If match is found, return corresponding moves
        return ORBIT_KEYS[orbits]
    
    # Try with one transformation
    for transformation, moveset in TRANSFORMATIONS:
        # Determine orbits of transformed node
        orbits = get_orbits(node.transformation(transformation))
        if orbits in ORBIT_KEYS.keys(): # If match found, transform and return moves
            transformed_moves = []
            for move in ORBIT_KEYS[orbits]:
                # Apply transformation if given in moveset
                if move in moveset.keys(): move = moveset[move]
                transformed_moves.append(move)
            return transformed_moves



    # Try with two transformations
    for transformation_1, moveset_1 in TRANSFORMATIONS:
        for transformation_2, moveset_2 in TRANSFORMATIONS:
            # Determine orbits of transformed node
            orbits = get_orbits(node.transformation(transformation_1, transformation_2))
            if orbits in ORBIT_KEYS.keys(): # If match is found, transform and return moves
                transformed_moves = []
                for move in ORBIT_KEYS[orbits]:
                    # Apply transformations if given in movesets
                    if move in moveset_2.keys(): move = moveset_2[move]
                    if move in moveset_1.keys(): move = moveset_1[move]
                    transformed_moves.append(move)
                return transformed_moves

                

    raise Exception("NOT SOLVED")



## Fixes sides and remaining corners
# Orbits found in move tables
ALLOWED_ORBITS = list(ORBIT_KEYS.keys())[:-12]

# Transformations used to look through move tables
#FIXED_ORBITS_TRANSFORMATIONS = [
#    "reflect_XY",
#    "reflect_XZ",
#    "reflect_YZ",
#    "X",
#    "X_Prime",
#    "X_2",
#    "Y_2",
#    "Z_2"]

# Decides which table to use and which transformations are applied
def get_fixed_orbits(cube):
    
    # Try with no transformation
    orbits = get_orbits(cube)
    if orbits in ALLOWED_ORBITS:
        return cube, ALLOWED_ORBITS.index(orbits), (dict(), dict())
    
    transformed_node = Node()
    
    # Try with one transformation
    for i, (transformation, moveset) in enumerate(TRANSFORMATIONS):
        transformed_node.cube = getattr(cube, transformation)()
        orbits = get_orbits(transformed_node)
        
        if orbits in ALLOWED_ORBITS:
            return transformed_node, ALLOWED_ORBITS.index(orbits), (moveset, dict())
    
    # Try with two transformations
    for i, (transformation_1, moveset_1) in enumerate(TRANSFORMATIONS):
        for j, (transformation_2, moveset_2) in enumerate(TRANSFORMATIONS):
            transformed_node.cube = getattr(Node(getattr(cube, transformation_1)()), transformation_2)()
            orbits = get_orbits(transformed_node)
            
            if orbits in ALLOWED_ORBITS:
               return transformed_node, ALLOWED_ORBITS.index(orbits), (moveset_1, moveset_2)
            
    raise Exception("No resulting orbits (phase 3)")


# Get the key for table moves
def get_key(cube):
    sides_key = ["", "", ""]
    group_UD = (cube[0][4], cube[5][4])
    group_FB = (cube[2][4], cube[4][4])

    for i, face in enumerate((cube[0], cube[5])):
        for edge in (1, 3, 5, 7):
            if face[edge] in group_UD: sides_key[i * 2] += "-"
            else: sides_key[i * 2] += "X"
    
    for i, face in enumerate((cube[2], cube[4])):
        for edge in (3, 5):
            if face[edge] in group_FB: sides_key[1] += "-"
            else: sides_key[1] += "X"
    
    return "|".join(sides_key)

# Tests if the given node is in G_3
def test_corner_permutation(test_node):

    node = Node(test_node.cube)
    for face_1, face_2 in ((node[0], node[5]), (node[1], node[3]), (node[2], node[4])):
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
    
    node.move("X")
    for face_1, face_2 in ((node[0], node[5]), (node[1], node[3]), (node[2], node[4])):
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
        
    node.move("Z")
    for face_1, face_2 in ((node[0], node[5]), (node[1], node[3]), (node[2], node[4])):
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
    ROT_X_2,
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
    ("Y_2", ROT_Y_2),
    ("Z_2", ROT_Z_2))

# Try transformations to get the moves to solve the sides
def get_side_moves(node, table_num):
    corner_check = ("00000000", "10100000", "11001100")[table_num]
    table = TABLES[table_num]
    transformations = NO_CORNER_TRANSFORMATIONS
    
    # Try with no transformations
    moves = check_table(table, node)
    if moves != False: return moves
    
    # Try with 1 transformation
    for transformation, moveset in transformations:
        transformed_node = Node(getattr(node, transformation)())
        if get_orbits(transformed_node) != corner_check: continue
        moves = check_table(table, transformed_node)
        if moves != False:
            for i, move in enumerate(moves):
                if move in moveset.keys(): move = moveset[move]
                moves[i] = move
            
            return moves
    
    # Try with two transformations
    for transformation_1, moveset_1 in transformations:
        for transformation_2, moveset_2 in transformations:
            transformed_node = Node(getattr(Node(getattr(node, transformation_1)()), transformation_2)())
            if get_orbits(transformed_node) != corner_check: continue
            moves = check_table(table, transformed_node)
            if moves != False:
                for i, move in enumerate(moves):
                    if move in moveset_2.keys(): move = moveset_2[move]
                    if move in moveset_1.keys(): move = moveset_1[move]
                    
                    moves[i] = move
                return moves
            
    raise Exception("NO MOVES FOUND IN PHASE 3 TABLES")


TABLES = [
    Table("Thistlethwaite/Tables/phase_3_no_corners.txt"),
    Table("Thistlethwaite/Tables/phase_3_two_corners.txt"),
    Table("Thistlethwaite/Tables/phase_3_four_corners.txt")]

# Checks the table for moves to solve the given node
def check_table(table, node):
    key = get_key(node)
    
    for moves in table.search_table(key):
        test_node = Node(node.cube)
        for move in moves:
            test_node.move(move)

        # Checks if the solution is in G_3
        if test_corner_permutation(test_node):

            try:
                # I do not like this at all
                phase_4_moves = phase_4(Node(test_node.cube))
                return moves + phase_4_moves
            
            except: pass
            
    # If no solution is found, return false     
    return False

def phase_3(node):
    #print("Before corners:", node.cube)
    phase_3_moves = []
    
    # Fix orbits to be 1 of 3 possible states
    orbit_moves = fix_orbits(node)
    print(orbit_moves)

    for move in orbit_moves:
        phase_3_moves.append(move)
        node.move(move)
        
    
    
    # Transform node to be used in table
    transformed_node, table_num, move_transformations = get_fixed_orbits(node)
    
    # Get the moves to fix the transformed node
    moves = get_side_moves(transformed_node, table_num)
    
    # Transform moves to work on origional node
    for move in moves:
        # Undo second transformation
        if move in move_transformations[1].keys(): move = move_transformations[1][move]
        # Undo first transformation
        if move in move_transformations[0].keys(): move = move_transformations[0][move]

        phase_3_moves.append(move)
        node.move(move)
        
    return phase_3_moves
