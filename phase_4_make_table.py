from cube_3 import Cube3

MOVE_KEYS = ("L_2", "F_2", "R_2", "B_2", "U_2", "D_2")

def translate_table(lines):
    moves = [[] for i in range(177)]
    for i, line in enumerate(lines):
        if line[27] == " ": numbers = line[1:24].split(" ")
        else: numbers = line[1:28].split(" ")
        for j in numbers:
            moves[i].append(MOVE_KEYS[int(j) - 1])

    return moves


def get_key(state):
    key = ""
    for face in state:
        for side in (1, 3, 5, 7):
            if face[side] == face[4]: key += "-"
            else: key += "X"
        key += "|"

    return key[:-1]
        

def make_table():
    with open("Creating Tables/phase_4_input.txt", "r") as file:
        lines = translate_table(file.readlines())


    for i, line in enumerate(lines):
        cube = Cube3()
        for move in line:
            cube.move(move)
        
        key = get_key(cube.cube)
        lines[i] = (key + " : " + " ".join(line[::-1]) + "\n")


    # Extra cases
    lines = sorted(lines)
    lines[-1] = "XXXX|XXXX|XXXX|XXXX|XXXX|XXXX : L_2 R_2 F_2 B_2 U_2 D_2"

    with open("Thistlethwaite/Tables/phase_4.txt", "w") as table:
        for line in lines:
            table.write(line)


make_table()