from cube_3 import Cube_3

MOVE_KEYS = ("L", "L2", "L'", "F2", "R", "R2", "R'", "B2", "U2", "D2")


def read_table(index):
    with open("tableinput_3.txt", "r") as table:
        moves = table.readlines()[index][16:38].replace("  ", " ").split(" ")
        for i, move in enumerate(moves):
            try: moves[i] = MOVE_KEYS[int(move) - 1]
            except: pass
        return moves
            

                


cube = Cube_3(["cccc-cccc", "---------", "aaaa-aaaa", "---------", "aaaa-aaaa", "cccc-cccc"])
for move in read_table(3):
    print(move, end = ", ")
    cube.move(move)

cube.display()