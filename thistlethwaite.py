from cube_3 import Cube_3
from Assets.cqueue import Queue
from Assets.node_3 import Node
from Assets.stack import Stack
import time

MOVE_KEYS = ("U", "D", "L", "R", "F", "B")


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
                    return node_stack
                
            
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
                        node_stack.push(Node(get_node_move(parent.parent, parent.movement + 1, G_1), parent.movement + 1, parent.parent))


# Phase 2
def test_table(table_num):
    with open("Tables/phase_2.txt", "r") as table:
        moves = table.readlines()[table_num][11:].strip("\n").split(" ")
        print(moves)
        for i, move in enumerate(moves):
            moves[i] = G_1[int(move)]
        print(moves)



def find_path(start_state):
    node_stack = phase_1_iddfs(start_state)
    path = []
    while not node_stack.is_empty():
        node = node_stack.pop()
        move = MOVE_KEYS[node.movement // 2] + ("'" if node.movement % 2 == 1 else "")
        path.append(move)
    return path[::-1]

# Superflip:
cube = Cube_3(["WOWGWBWRW", "GWGOGRGYG", "RWRGRBRYR", "BWBRBOBYB", "OWOBOGOYO", "YRYGYBYOY"])

# cube = Cube_3(["OGGWWWOYY", "GRGWGRYBW", "WOOYROORR", "BBRGBBWGG", "WWYROORYB", "BGBOYYRBY"])
# cube = Cube_3()
# cube.scramble()
# cube.display()

#time1 = time.time()
#print(find_path(cube.cube))
#print("Time:", time.time() - time1)

test_table(1)