from ast import Try
from cube_3 import Cube3
import random as rnd

MOVE_KEYS = ("L", "L2", "L'", "F2", "R", "R2", "R'", "B2", "U2", "D2")



def read_table(page_num, line_index):
    moves_1, moves_2 = read_line(page_num, line_index)
    
    for i, move in enumerate(moves_1):
        try: moves_1[i] = MOVE_KEYS[int(move) - 1]
        except: 
            print("UNRECOGNISED MOVE", page_num, line_index, 1)
            raise Exception
            
    for i, move in enumerate(moves_2):
        try: moves_2[i] = MOVE_KEYS[int(move) - 1]
        except:
            print("UNRECOGNISED MOVE", page_num, line_index, 1)
            raise Exception
            
    return moves_1, moves_2


def read_page_1(line_index):
    with open("phase_3_page_1.txt", "r") as table:
        line = table.readlines()[line_index]
        moves1 = line[16:38].replace("  ", " ").split(" ")
        moves2 = line[47:].replace("  ", " ").split(" ")
        return moves1, moves2
        

def read_line(page_num, line_index):
    with open(f"phase_3_page_{page_num}.txt", "r") as table:
        line = table.readlines()[line_index]
        
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
        print(line)      
                
    return moves_1, moves_2




for i in range(7):
    for j in range(69):
        cube =  Cube3(["111111111", "---------", "000000000", "---------", "000000000", "111111111"])
        moves_1, moves_2 = read_table(i + 1, j)
        for move in moves_2:
            cube.move(move)

        cube.display()
