from Assets.node_3 import Node
from Thistlethwaite.transformations import *
from Thistlethwaite.Tables.table import Table
from Thistlethwaite.phase_4 import phase_4


# Phase 3 Moveset
# PHASE_3_MOVES = (
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
def get_orbits(node):
    # Define group of top and bottom faces
    group_c = (node[0][4], node[5][4])
    corners = ""

    # Check top and bottom faces
    for face in (0, 5):
        # Check each corner of the face
        for index in (0, 2, 6, 8):
            # If facelet in correct group, corner is in orbit
            if node[face][index] not in group_c: corners += "1"
            else: corners += "0"

    return corners


# Transformations used throughout phase 3
TRANSFORMATIONS = (
    ("reflect_XY", REF_XY),
    ("reflect_XZ", REF_XZ),
    ("reflect_YZ", REF_YZ),
    ("X", ROT_X_PRIME),
    ("X_Prime", ROT_X),
    ("X_2", ROT_X_2),
    ("Y_2", ROT_Y_2),
    ("Z_2", ROT_Z_2))

# Finds moves to fix the corner orbits of given node
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

# Decides which table to use and which transformations are applied
def get_fixed_orbits(node):
    
    # Try with no transformation
    orbits = get_orbits(node.cube) # Get the fixed orbits
    # If already in correct state, no transformation needed. Return table number and blank transformation dictionaries
    if orbits in ALLOWED_ORBITS: 
        return node, ALLOWED_ORBITS.index(orbits), (dict(), dict())
    
    
    # Try with one transformation
    for i, (transformation, moveset) in enumerate(TRANSFORMATIONS):
        # Get the transformed state
        transformed_state = node.transformation(transformation)
        
        # Get orbits of transformed state
        orbits = get_orbits(transformed_state)
        
        # If found in correct orbits, return transformed node, table number and the transformations applied
        if orbits in ALLOWED_ORBITS:
            return Node(transformed_state), ALLOWED_ORBITS.index(orbits), (moveset, dict())
    

    # Try with two transformations
    for i, (transformation_1, moveset_1) in enumerate(TRANSFORMATIONS):
        for j, (transformation_2, moveset_2) in enumerate(TRANSFORMATIONS):
            # Get the transformed state
            transformed_state = node.transformation(transformation_1, transformation_2)
            
            # Get orbits of transformed state
            orbits = get_orbits(transformed_state)
            
            # If found in correct orbits, return transformed node, table number and the transformations applied
            if orbits in ALLOWED_ORBITS:
               return Node(transformed_state), ALLOWED_ORBITS.index(orbits), (moveset_1, moveset_2)
            
    raise Exception("No fixed orbits found (something has gone VERY wrong) - Phase 3")


# Get the key for table moves
def get_key(state):
    # Side key consists of three strings: Top face sides, middle slice sides and bottom face sides
    sides_key = ["", "", ""]
    # Declare group of top and bottom faces
    group_UD = (state[0][4], state[5][4])
    # Declare group of front and back faces
    group_FB = (state[2][4], state[4][4])

    # Check all side pieces of top and bottom faces
    for i, face in enumerate((state[0], state[5])):
        for edge in (1, 3, 5, 7):
            # If facelet in group
            if face[edge] in group_UD: sides_key[i * 2] += "-"
            # If facelet not in group
            else: sides_key[i * 2] += "X"
    
    # Check all side pieces in middle slice of cube
    for i, face in enumerate((state[2], state[4])):
        for edge in (3, 5):
            # If facelet in group
            if face[edge] in group_FB: sides_key[1] += "-"
            # If facelet not in group
            else: sides_key[1] += "X"
    
    # Return the key as a string
    return "|".join(sides_key)


# Tests given node find some states not in G_3
def test_corner_permutation(test_node):

    # Try with origional cube
    node = Node(test_node.cube)
    # Check pattern of corners on each pair of faces
    for face_1, face_2 in ((node[0], node[5]), (node[1], node[3]), (node[2], node[4])):
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
    
    # Try with rotated cube
    node.move("X")
    # Check pattern of corners on each pair of faces
    for face_1, face_2 in ((node[0], node[5]), (node[1], node[3]), (node[2], node[4])):
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
        
    # Try with rotated cube
    node.move("Z")
    # Check pattern of corners on each pair of faces
    for face_1, face_2 in ((node[0], node[5]), (node[1], node[3]), (node[2], node[4])):
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
    
    # If returned true, does not necasserily mean state is in G_3, but has reduced number of states needed to try
    # I also do not like this function at all    
    return True


# Try transformations to get the moves to solve the sides
def get_side_moves(node, table_num):
    # Corners to check node is still valid after transformations are applied
    corner_check = ("00000000", "10100000", "11001100")[table_num]
    
    # Determine which table to use
    table = TABLES[table_num]
    
    # Try with no transformations
    moves = check_table(table, node)
    if moves != False: return moves
    
    # Try with 1 transformation
    for transformation, moveset in TRANSFORMATIONS:
        # Get the transformed state
        transformed_state = node.transformation(transformation)
        
        # Check if the state after transformations is still valid for the table
        if get_orbits(transformed_state) != corner_check: continue
        
        # Search table for corresponding moves
        moves = check_table(table, transformed_state) 
        if moves != False:
            # Transform returned moves to work for origional node
            for i, move in enumerate(moves):
                if move in moveset.keys(): move = moveset[move]
                moves[i] = move
            
            return moves
    
    # Try with two transformations
    for transformation_1, moveset_1 in TRANSFORMATIONS:
        for transformation_2, moveset_2 in TRANSFORMATIONS:
            # Get the transformed state
            transformed_state = node.transformation(transformation_1, transformation_2)
            
            # Check if the state after transformations is still valid for the table
            if get_orbits(transformed_state) != corner_check: continue
            
            # Search table for corresponding moves
            moves = check_table(table, transformed_state)
            if moves != False:
                # Transform returned moves to work for origional node
                for i, move in enumerate(moves):
                    if move in moveset_2.keys(): move = moveset_2[move]
                    if move in moveset_1.keys(): move = moveset_1[move]
                    
                    moves[i] = move
                return moves
    
    # If no entry in table found, cube is deemed unsolvable
    raise Exception("NO MOVES FOUND IN PHASE 3 TABLES")


TABLES = [
    Table("Thistlethwaite/Tables/phase_3_no_corners.txt"),
    Table("Thistlethwaite/Tables/phase_3_two_corners.txt"),
    Table("Thistlethwaite/Tables/phase_3_four_corners.txt")]

# Checks the table for moves to solve the given node
def check_table(table, state):
    # Calculate key from given node
    key = get_key(state)
    
    # Search table for matching keys (Should find 4)
    for moves in table.search_table(key):
        if moves == ['']: moves = []
        test_node = Node(state)
        
        # Perform moves on a test node
        for move in moves:
            test_node.move(move)

        # Checks if the test node is in G_3
        if test_corner_permutation(test_node):
            # If node passes the corner permutation test, attempt to execute phase 4 on the node.
            # I dont like this at all
            try:
                phase_4_moves = phase_4(Node(test_node.cube))
                return moves + phase_4_moves
            
            # If phase 4 fails, (no node found at maximum depth), try next set of moves found
            except: pass
            
    # If no solution is found, return false     
    return False

def phase_3(node):
    # List of returned moves
    phase_3_moves = []
    
    # Fix orbits to be 1 of 3 possible states
    orbit_moves = fix_orbits(node)
    
    # Execute moves on node
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

        # Add moves to the list
        phase_3_moves.append(move)
        #node.move(move)
        
    return phase_3_moves
