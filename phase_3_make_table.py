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
                
    return moves_1, moves_2


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



# Translates the old table moves into new tables
def translate_moves(lines):
    new_lines = []
    for movesets in lines:
        for moveset in movesets:
            if moveset != []:
                cube = Cube3(["-1-111-1-", "---------", "-0-000-0-", "---------", "-0-000-0-", "-1-111-1-"])
                inverse_moves = []
                    
                for move in moveset:
                    cube.move(MOVE_KEYS[int(move) - 1])
                    inverse_moves.append(INVERSE_KEYS[int(move) - 1])

                sides_key = get_sides_key(cube)
                new_lines.append(sides_key + " : " + " ".join(inverse_moves[::-1]) + "\n")
    return sorted(new_lines, key = sort_key)


# Writes the new move tables
def write_tables():
    with open("Tables/phase_3_no_corners.txt", "w") as table:
        table.write("----|----|---- : \n")    
        for line in translate_moves(get_table_text(1) + get_table_text(2)):
            table.write(line)
    
    with open("Tables/phase_3_two_corners.txt", "w") as table:
        for line in translate_moves(get_table_text(3) + get_table_text(4)):
            table.write(line)
           
    with open("Tables/phase_3_four_corners.txt", "w") as table:
        for line in translate_moves(get_table_text(5) + get_table_text(6) + get_table_text(7)):
            table.write(line)
                    

def test_corner_permutation(cube):
    face_pairs = ((cube[0], cube[5]), (cube[1], cube[3]), (cube[2], cube[4]))
                  
    for face_1, face_2 in face_pairs:
        if (face_1[0] == face_1[2]) ^ (face_2[0] == face_2[2]): return False
        if (face_1[0] == face_1[6]) ^ (face_2[0] == face_2[6]): return False
        if (face_1[0] == face_1[8]) ^ (face_2[0] == face_2[8]): return False
        
    return True


write_tables()

