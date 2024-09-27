from cube_3 import Cube3

MOVE_KEYS = ("L", "L2", "L'", "F2", "R", "R2", "R'", "B2", "U2", "D2")



def read_table(table_index, line_index):
    moves_1, moves_2 = PAGE_FUNCS[table_index - 1](line_index)
    for i, move in enumerate(moves_1):
        try: moves_1[i] = MOVE_KEYS[int(move) - 1]
        except: pass
            
    for i, move in enumerate(moves_2):
        try: moves_2[i] = MOVE_KEYS[int(move) - 1]
        except: pass
            
    return moves_1, moves_2


def read_page_1(line_index):
    with open("phase_3_page_1.txt", "r") as table:
        line = table.readlines()[line_index]
        moves1 = line[16:38].replace("  ", " ").split(" ")
        moves2 = line[47:].replace("  ", " ").split(" ")
        return moves1, moves2
        
            

                

def read_page_2(line_index):
    with open ("phase_3_page_2.txt", "r") as table:
        line = table.readlines()[line_index]
        moves1 = line[11:45].strip("   ").replace("  ", " ").split(" ")
        print(moves_1)
        

def read_line():

PAGE_FUNCS = (read_page_1, read_page_2)


for i in range(70):
    cube = Cube3(["cccc-cccc", "---------", "aaaa-aaaa", "---------", "aaaa-aaaa", "cccc-cccc"])
    moves_1, moves_2 = read_table(1, 3)
    for move in moves_1:
        print(move, end = ", ")
        cube.move(move)

    cube.display()