from Assets.node_3 import Node
from Assets.stack import Stack

table_2 = open("phase_2.txt", "w")
table_2.write("Hello!\n")
    
G_2 = ("L", "L_Prime", "L_2",
       "R", "R_Prime", "R_2", 
       "F", "F_Prime", "F_2",
       "B", "B_Prime", "B_2", 
       "U_2", "D_2")


def get_node_move(parent, move_num):
    print(G_2[move_num])
    if move_num <= 13: return getattr(parent, G_2[move_num])()
    else: raise Exception("Invalid Move!")


def find_states():
    start_node = Node(["1-2---1-2", "0-0S-S0-0", "1-2S-S2-1", "0-0S-S0-0", "1-2S-S2-1", "1-2---1-2"])
    
    branch(start_node, 4)
    

def branch(node, depth_left):
    
    if depth_left <= 0:
        # node.display()
        if node[1][3] == "S" and node[1][5] == "S" and node[2][3] == "S" and node[2][5] == "S" and node[3][3] == "S" and node[3][5] == "S" and node[4][3] == "S" and node[4][5] == "S":
            table_2.write("YASS\n")
        return
        
    for move in range(2):
        state = branch(Node(get_node_move(node, move), move), depth_left - 1)
        


find_states()