from Assets.node_3 import Node
from Assets.stack import Stack



def get_node_move(parent, move_num, move_set):
    try: return getattr(parent, move_set[move_num])()
    except IndexError: raise Exception("Invalid Move!")

# Phase 1 Moveset
PHASE_1_MOVES = (
    "U", "U_Prime", "D", "D_Prime",
    "L", "L_Prime", "R", "R_Prime",
    "F", "F_Prime", "B", "B_Prime")

### Phase 1
def side_check(cube):
    # Flip all side peices to be "good" (can be returned home without the use quater turns U or D)    
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

def solve_sides_iddfs(start_node):
    # IDDFS to get to G1
    if side_check(start_node): return start_node

    for i in range(7):
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
                        node_stack.push(Node(get_node_move(parent.parent, parent.movement + 1, PHASE_1_MOVES), parent.movement + 1, parent.parent))

def phase_1(start_node):
    node = solve_sides_iddfs(start_node)
    if node == None: return "Cannot Solve!"
    G1_node = node

    path = []
    while node.parent != None:
        move = PHASE_1_MOVES[node.movement]
        path.append(move)
        node = node.parent

    return path[::-1], G1_node