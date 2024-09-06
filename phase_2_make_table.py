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
        

def translate_table():
    with open("tableinput.txt", "r") as input_file:
        with open("Tables/phase_2.txt", "w") as table_file:
            for line in input_file.readlines():
                moves = line[:26].split(" ")
                node = Node(["1-1---1-1", "0-0S-S0-0", "2-2S-S2-2", "0-0S-S0-0", "2-2S-S2-2", "1-1---1-1"])
                move_string = ""

                for move in moves:
                    move_string = " " + str(CONVERSION[int(move)]) + move_string
                    node.cube = getattr(node, G_1[CONVERSION[int(move)]])()

                facelets = node[1][0] + node[1][2] + node[1][6] + node[1][8] + node[3][0] + node[3][2] + node[3][6] + node[3][8] + " :"
                table_file.write(facelets + move_string + "\n")
    


translate_table()