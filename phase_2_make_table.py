from cube_3 import Cube_3
from Assets.node_3 import Node
from Assets.stack import Stack

def get_node_move(parent, move_num):
    if move_num == 0: return parent.U()
    if move_num == 1: return parent.U_Prime()
    if move_num == 2: return parent.D()
    if move_num == 3: return parent.D_Prime()
    if move_num == 4: return parent.L()
    if move_num == 5: return parent.L_Prime()
    if move_num == 6: return parent.R()
    if move_num == 7: return parent.R_Prime()
    if move_num == 8: return parent.F()
    if move_num == 9: return parent.F_Prime()
    if move_num == 10: return parent.B()
    if move_num == 11: return parent.B_Prime()
    else: raise Exception("Invalid Move!")

def find_states():
    start_node = Node(["XXXXXXXXX", "XXXXXXXXX", "XXXXXXXXX", "XXXXXXXXX", "XXXXXXXXX", "XXXXXXXXX"])
    
    print(branch(start_node, 4))
    

def branch(node, depth_left):
    print(depth_left)
    
    if depth_left <= 0:
        node.display()
        return
        
    for move in range(12):
        state = branch(Node(get_node_move(node, move), move), depth_left - 1)
        


find_states()