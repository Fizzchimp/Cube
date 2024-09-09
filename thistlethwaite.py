from cube_3 import Cube_3
from Assets.cqueue import Queue
from Assets.node_3 import Node
from Assets.stack import Stack
import time


# Moveset to get from G0 -> G1
G_0 = ("U", "U_Prime", "D", "D_Prime",
       "L", "L_Prime", "R", "R_Prime",
       "F", "F_Prime", "B", "B_Prime")


# Moveset to get from G1 -> G2
G_1 = ("L", "L_Prime", "L_2",
       "R", "R_Prime", "R_2", 
       "F", "F_Prime", "F_2",
       "B", "B_Prime", "B_2", 
       "U_2", "D_2")


CORNERS = (((1, 0), (4, 2), (0, 0)),
           ((1, 2), (0, 6), (2, 0)),
           ((1, 6), (5, 6), (4, 8)),
           ((1, 8), (2, 6), (5, 1)),
           
           ((3, 0), (2, 2), (0, 8)),
           ((3, 2), (0, 2), (4, 0)),
           ((3, 6), (5, 2), (2, 8)),
           ((3, 8), (4, 6), (5, 8)))


# Return the state of a node after applied move
def get_node_move(parent, move_num, move_set):
    try: return getattr(parent, move_set[move_num])()
    except IndexError: raise Exception("Invalid Move!")


# Phase 1
def side_check(cube):
    # Flip all side peices to be "good" (can be returned home without the use of an odd number of quater turns of U or D)    
    facePattern1 = (3, 7, 5, 1)
    facePattern2 = (3, 1, 5, 7)
    groups = ((cube[2][4], cube[4][4]), (cube[1][4], cube[3][4]))

    for i in range(4):
        side_peices = ((cube[i + 1][1], cube[0][facePattern1[i]]),
                       (cube[i + 1][3], cube[(i + 3) % 4 + 1][5]),
                       (cube[i + 1][7], cube[5][facePattern2[i]]))

        # Decision tree for 'Good' and 'Bad' Peices
        for peice in side_peices:
            if peice[0] in groups[(i) % 2]: return False
            elif peice[1] in groups[(i + 1) % 2]: return False
    return True

def phase_1_iddfs(start_state):
    # IDDFS to get to G1
    start_node = Node(start_state, -1)
    if side_check(start_state): return start_node

    for i in range(7):
        print("Depth:", i)
        node_stack = Stack(i + 1)
        node_stack.push(Node(start_node.U(), 0, start_node))

        exhausted = False
        while not exhausted:

            # Branch down to required depth
            if not node_stack.is_full():
                parent = node_stack.peek()
                node_stack.push(Node(parent.U(), 0, parent))

            else:
                # Retreive the youngest node
                current_node = node_stack.pop()
                current_movement = current_node.movement

                parent = current_node.parent

                # Check if the current node is correct
                if side_check(current_node):
                    node_stack.push(current_node)
                    return current_node
                
            
                # Push D movement (Last move can only be U or D)
                if current_movement == 0:
                    node_stack.push(Node(parent.D(), 2, parent))

                # If current branch exhausted remove node and change upper branch
                else:
                    top = True
                    for j in range(i):
                        parent = node_stack.pop()
                        if parent.movement <= 10:
                            top = False
                            break
                    if top:
                        exhausted = True
                    else:
                        node_stack.push(Node(get_node_move(parent.parent, parent.movement + 1, G_0), parent.movement + 1, parent.parent))


# Phase 2
def UD_side_check(cube):
    group_c = (cube[0][4], cube[5][4])
    if cube[1][3] in group_c and cube[1][5] in group_c and cube[3][3] in group_c and cube[3][5] in group_c: return True
    return False

def get_UD_slice(start_node):
    # To get UD slice correct
    for i in range(6):
        print("Depth:", i)
        node_stack = Stack(i + 1)
        node_stack.push(Node(start_node.L(), 0, start_node))

        exhausted = False
        while not exhausted:

            # Branch down to required depth
            if not node_stack.is_full():
                parent = node_stack.peek()
                node_stack.push(Node(parent.L(), 0, parent))

            else:
                # Retreive the youngest node
                current_node = node_stack.pop()
                current_movement = current_node.movement

                parent = current_node.parent

                # Check if the current node is correct
                if UD_side_check(current_node):
                    return current_node
                
            
                if current_movement <= 12:
                    node_stack.push(Node(get_node_move(parent, current_movement + 1, G_1), current_movement + 1, parent))

                # If current branch exhausted remove node and change upper branch
                else:
                    top = True
                    for j in range(i):
                        parent = node_stack.pop()
                        if parent.movement <= 10:
                            top = False
                            break
                    if top:
                        exhausted = True
                    else:
                        node_stack.push(Node(get_node_move(parent.parent, parent.movement + 1, G_1), parent.movement + 1, parent.parent))

def get_corners(node):
    state = ""
    target_colours = (node[1][4], node[3][4])
    
    for corner in CORNERS:
        for i in range(3):
            if node[corner[i][0]][corner[i][1]] in target_colours:
                state += str(i)
                break

    return state




def test_table():
    move_list = []
    with open("Tables/phase_2.txt", "r") as table:
        lines = table.readlines()
        for table_num in [431, 65, 229]:
            moves = lines[table_num][11:].strip("\n").split(" ")
            if move_list == []:
                for move in moves: move_list.append(move)
            else:
                for move in move_list:
                    if move not in moves: move_list.remove(move)
            for i, move in enumerate(moves):
                moves[i] = G_1[int(move)]
            print(moves)



def find_path(start_state):
    # Phase 1
    node = phase_1_iddfs(start_state)
    if node == None: return "Cannot Solve!"
    path = []
    while node.parent != None:
        move = G_0[node.movement]
        path.append(move)
        node = node.parent
    phase_1 = path[::-1]
    print("Phase one complete")
    
    # Phase 2
    node = get_UD_slice(Node(start_state))
    if node == None: return "Cannot Solve!"
    path = []
    while node.parent != None:
        move = G_1[node.movement]
        path.append(move)
        node = node.parent
    phase_2 = path[::-1]
    return phase_1, phase_2


# Superflip:
#cube = Cube_3(["WOWGWBWRW", "GWGOGRGYG", "RWRGRBRYR", "BWBRBOBYB", "OWOBOGOYO", "YRYGYBYOY"])
#cube.move('U', 'L', 'D', "F'", "R'", "B'", 'U')

# cube = Cube_3(["OGGWWWOYY", "GRGWGRYBW", "WOOYROORR", "BBRGBBWGG", "WWYROORYB", "BGBOYYRBY"])
cube = Cube_3()
cube.scramble()
# cube.display()

#time1 = time.time()
#print(find_path(cube.cube))
#print("Time:", time.time() - time1)

test_table()