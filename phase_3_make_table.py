from cube_3 import Cube3
from random import choice

MOVE_KEYS = ("L", "L2", "L'", "F2", "R", "R2", "R'", "B2", "U2", "D2")
INVERSE_KEYS = ("L'", "L2", "L", "F2", "R'", "R2", "R", "B2", "U2", "D2")

def sort_key(line):
    return line[:14]

# Takes a line from an input table and converts it into two lists of moves
def read_line(line):
    # Split string into 2 movesets
    line = line[4:].split("   ")
    i = 0
    while i < len(line):
        if line[i] == "": line.pop(i)
        else: i += 1

    if line[0] == "-": moves_1 = []
    else: moves_1 = line[0].strip("\n").strip(" ").replace("  ", " ").split(" ")
    try: moves_2 = line[1].strip("\n").strip(" ").replace("  ", " ").split(" ")
    except IndexError: moves_2 = []
    # print(moves_1, "\n", moves_2, "\n", sep = "")    
                
    return moves_1, moves_2


def test_input_tables():
    for i in range(7):
        for j in range(70):
            moves_1, moves_2 = read_table(i + 1, j)
    
            if i <= 1: face_1, face_2 = "1111", "1111"
            elif 1 < i <= 3: face_1, face_2 = "0011", "0011"
            elif 4 <= i:face_1, face_2 = "0101", "1111"
            
            if moves_1 != []:
                cube =  Cube3(["111111111", "---------", "000000000", "---------", "000000000", "111111111"])
                for move in moves_1:
                    cube.move(move)
                if cube[0][0] != face_1[0] or cube[0][2] != face_1[1] or cube[0][6] != face_1[2] or cube[0][8] != face_1[3] or cube[5][0] != face_2[0] or cube[5][2] != face_2[1] or cube[5][6] != face_2[2] or cube[5][8] != face_2[3]:
                    cube.display()
                    raise Exception(f"UH OH: page {i + 1}, line {j + 1}, moveset 1")

            if moves_2 != []:
                cube =  Cube3(["111111111", "---------", "000000000", "---------", "000000000", "111111111"])
                for move in moves_2:
                    cube.move(move)
                if cube[0][0] != face_1[0] or cube[0][2] != face_1[1] or cube[0][6] != face_1[2] or cube[0][8] != face_1[3] or cube[5][0] != face_2[0] or cube[5][2] != face_2[1] or cube[5][6] != face_2[2] or cube[5][8] != face_2[3]:
                    cube.display()
                    raise Exception(f"UH OH: page {i + 1}, line {j + 1}, moveset 2")

# Splits each line in an input table and returns them as a list
def get_table_text(table_num):
    with open(f"phase_3_page_{table_num}.txt", "r") as table:
        lines = table.readlines()
        for i, line in enumerate(lines):
            lines[i] = read_line(line)
    return lines

# Takes cube input and converts it to sides key to be written
def get_sides_key(cube):

    sides_key = ""
    face = cube[0]
    for side in (1, 3, 5, 7):
        if face[side] == face[4]: sides_key += "-"
        else: sides_key += "X"
    sides_key += "|"
    
    for face in (cube[2],  cube[4]):
        for side in (3, 5):
            if face[side] == face[4]: sides_key += "-"
            else: sides_key += "X"
            
    sides_key += "|"
            
    face = cube[5]
    for side in (1, 3, 5, 7):
        if face[side] == face[4]: sides_key += "-"
        else: sides_key += "X"
    
    return sides_key

# Writes the new move tables
def write_tables():
    with open("Tables/phase_3_no_corners.txt", "w") as table:
            lines = get_table_text(1) + get_table_text(2)
            new_lines = []
            for movesets in lines:
                for j in range(2):
                    cube = Cube3(["-1-111-1-", "---------", "-0-000-0-", "---------", "-0-000-0-", "-1-111-1-"])
                    inverse_moves = []
                    
                    for move in movesets[j]:
                        cube.move(MOVE_KEYS[int(move) - 1])
                        inverse_moves.append(INVERSE_KEYS[int(move) - 1])

                    sides_key = get_sides_key(cube)
                    new_lines.append(sides_key + " : " + " ".join(inverse_moves[::-1]) + "\n")
            new_lines = sorted(new_lines, key = sort_key)
            for line in new_lines:
                table.write(line)
                    

def test_corner_permutation(cube):
    face_pairs = ((cube[0], cube[5]), (cube[1], cube[3]), (cube[2], cube[4]))
                  
    for face_1, face_2 in face_pairs:
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
        
    return True



moveset = ("U2", "D2", "F2", "B2", "L2", "R2")

for i in range(10000):        
    cube = Cube3()
    # cube.move("R", "L2", "D2" "F2" "R" "L'" "F2" "L'")
    for i in range(20):
       move = choice(moveset)
       cube.move(move)
       print(move, end = ", ")

    # moves = "F2 R2 L' U2 L2 F2 L U2 L2 F2 L'"
    # for move in moves.split(" ")[::-1]:
    #     cube.move(move)
   
    cube.display()
    test = test_corner_permutation(cube)
    print(test)
    if test == False: raise Exception("False")


