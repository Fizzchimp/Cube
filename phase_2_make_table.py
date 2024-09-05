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


def get_node_move(parent, move_num):
    if move_num <= 13: return getattr(parent, G_1[move_num])()
    else: raise Exception("Invalid Move!")


def find_states():
    start_node = Node(["1-2---1-2", "0-0S-S0-0", "1-2S-S2-1", "0-0S-S0-0", "1-2S-S2-1", "1-2---1-2"])
    branch(start_node, 6, "")
    print("Phase 2 table created")
    
def branch(node, depth_left, moveStr):
    
    if depth_left <= 0:
        # node.display()
        if node[1][3] == "S" and node[1][5] == "S" and node[2][3] == "S" and node[2][5] == "S" and node[3][3] == "S" and node[3][5] == "S" and node[4][3] == "S" and node[4][5] == "S":
            facelets = node[1][0] + node[1][2] + node[1][6] + node[1][8] + node[3][0] + node[3][2] + node[3][6] + node[3][8]
            if facelets != "00000000":
                table_2.write(f"{facelets}: {moveStr}\n")
        # else: table_2.write("Nay\n")
        return
        
    for move in range(13):
        state = branch(Node(get_node_move(node, move), move), depth_left - 1, moveStr + str(move))
        

def translate_table():
    with open("tableinput.txt", "r") as input_file:
        with open("phase_2.txt", "w") as table_file:
            for line in input_file.readlines():
                moves = line[:26].split(" ")
                node = Node(["1-2---1-2", "0-0S-S0-0", "1-2S-S2-1", "0-0S-S0-0", "1-2S-S2-1", "1-2---1-2"])
                move_string = ""

                for move in moves:
                    move_string = str(CONVERSION[int(move)]) + " " + move_string
                    node.cube = getattr(node, G_1[CONVERSION[int(move)]])()

                facelets = node[1][0] + node[1][2] + node[1][6] + node[1][8] + node[3][0] + node[3][2] + node[3][6] + node[3][8] + " : "
                table_file.write(facelets + move_string + "\n")
    


translate_table()