from cube_3 import Cube3

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
        print(moves_1, "\n", moves_2, "\n", sep = "")    
                
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
        

def write_tables():
    
    #for i in range(70):
    i = 3
    cube = Cube3(["-1-111-1-", "---------", "-0-000-0-", "---------", "-0-000-0-", "-1-111-1-"])
    moves_1, moves_2 = read_table(1, i)
        
    for move in moves_1:
        cube.move(move)
        
    sides_key = ""
    face = cube[0]
    for side in (1, 3, 5, 7):
        if face[side] == face[4]: sides_key += "-"
        else: sides_key += "X"
    sides_key += "\n"
    
    for face in (cube[2],  cube[4]):
        for side in (3, 5):
            if face[side] == face[4]: sides_key += "-"
            else: sides_key += "X"
            
    sides_key += "\n"
            
    face = cube[5]
    for side in (1, 3, 5, 7):
        if face[side] == face[4]: sides_key += "-"
        else: sides_key += "X"
    
    cube.display()
    print(sides_key + " : " + " ".join(moves_1))
            
write_tables()
