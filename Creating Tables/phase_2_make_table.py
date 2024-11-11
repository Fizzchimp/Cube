from Assets.node_3 import Node


G_1 = ("L", "L_Prime", "L_2",
       "R", "R_Prime", "R_2", 
       "F", "F_Prime", "F_2",
       "B", "B_Prime", "B_2", 
       "U_2", "D_2")

CONVERSION = {11: 0, 12: 2, 13: 1, # L
              21: 6, 22: 8, 23: 7, # F
              31: 3, 32: 5, 33: 4, # R
              41: 9, 42: 11, 43: 10, # B
              51: 12, 52: 13} # U/D
        
INV_CONVERSION = {11: 1, 12: 2, 13: 0, # L
                  21: 7, 22: 8, 23: 6, # F
                  31: 4, 32: 5, 33: 3, # R
                  41: 10, 42: 11, 43: 9, # B
                  51: 12, 52: 13} # U/D


CORNER_CONVERSION = [0, 4, 5, 1, 3, 7, 6, 2]

def convert_corners(corners):
    new_corners = ""
    for new_pointer in CORNER_CONVERSION:
        new_corners += corners[new_pointer]

    return new_corners


def translate_table():
    with open("Creating Tables/tableinput_2.txt", "r") as input_file:
        with open("Thistlethwaite/Tables/phase_2.txt", "w") as table_file:
            incorrect = []
            to_write = []
            for index, line in enumerate(input_file.readlines()):
                moves = line[:26].split(" ")
                node = Node(["1S2---2S1", "0-0---0-0", "1S2---2S1", "0-0---0-0", "1S2---2S1", "1S2---2S1"])
                move_string = ""
                
                if moves[0][0] == "1":
                    node.move("F")
                    move_string += " F_Prime"
                    
                for move in moves:
                    move_string = " " + G_1[INV_CONVERSION[int(move)]] + move_string
                    node.cube = getattr(node, G_1[CONVERSION[int(move)]])()
                    

                corners = "".join(line[34:70].strip("\n").split("    "))
                converted_corners = convert_corners(corners)

                new_corners = node[1][0] + node[1][2] + node[1][6] + node[1][8] + node[3][0] + node[3][2] + node[3][6] + node[3][8]
                if new_corners != converted_corners:
                    print(corners, converted_corners, new_corners)
                    incorrect.append(index)

                to_write.append(new_corners + " :" + move_string + "\n")
                for face in(node[1], node[2], node[3], node[4]):
                    if face[3] != "S" or face[5] != "S":
                        incorrect.append(index)
                        break
            for line in to_write:
                table_file.write(line)
        print(incorrect)


def fix_line(line):
    moves = ["21"] + line[:26].split(" ")
    
    corners = "".join(line[34:70].strip("\n").split("    "))
    converted_corners = convert_corners(corners)
    
    for i, move in enumerate(moves):
        moves[i] = G_1[CONVERSION[int(move)]]
        
    for i in range(len(moves)):
        for move in G_1:
            new_moves = moves[:i] + [move] + moves[i + 1:]
            if test_node(new_moves, converted_corners): return new_moves
        
            
def test_node(moves, target_corners):
    node = Node(["1S2---2S1", "0-0---0-0", "1S2---2S1", "0-0---0-0", "1S2---2S1", "1S2---2S1"])
    for move in moves:
        node.move(move)
    
    new_corners = node[1][0] + node[1][2] + node[1][6] + node[1][8] + node[3][0] + node[3][2] + node[3][6] + node[3][8]
    
    if new_corners != target_corners: return False

    for face in(node[1], node[2], node[3], node[4]):
        if face[3] != "S" or face[5] != "S": return False
        
    return True
    

print(fix_line("12 22 51 52 31 22 32 21 31        0    1    1    0    2    0    0    2        2"))
translate_table()