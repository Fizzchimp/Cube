from cube_3 import Cube_3
from Assets.cqueue import Queue
from Assets.node_3 import Node
from Assets.stack import Stack
import time

def side_check(startState):
    ### Phase 1
    # Flip all side peices to be "good" (can be returned home without the use of an odd number of quater turns of U or D)    
    facePattern1 = (3, 7, 5, 1)
    facePattern2 = (3, 1, 5, 7)

    side_faces = [startState[i + 1] for i in range(4)]

    good = 0
    bad = 0

    for i, face in enumerate(side_faces):
        group_a = (side_faces[i][4], side_faces[(i + 2) % 4][4])
        group_b = (side_faces[(i + 1) % 4][4], side_faces[(i + 3) % 4][4])

        side_peices = ((face[1], startState[0][facePattern1[i]]),
                       (face[3], side_faces[(i + 3) % 4][5]),
                       (face[7], startState[5][facePattern2[i]]))

        # Decision tree for 'Good' and 'Bad' Peices
        for peice in side_peices:
            if peice[0] in group_a: good += 1
            elif peice[0] in group_b: bad += 1
            else:
                if peice[1] in group_a: bad += 1
                elif peice[1] in group_b: good += 1
                # else: print(peice)
    
    # print("Good: ", good, "\nBad: ", bad)
    if bad > 0:
        return False, good, bad
    return True, good, bad

            
def phase_1(startState):
    # BFS to Find path
    node_queue = Queue(999999)

    current_node = Node(startState)
    while current_node.generation <= 7:
        if current_node.movement == "U" or current_node.movement == "D" or current_node.movement == "U'" or current_node.movement == "D'":
            if side_check(current_node)[0]:
                return current_node
        
        next_generation = current_node.generation + 1

        if current_node.movement != "U'": node_queue.enqueue(Node(current_node.U(), current_node, "U", next_generation))
        if current_node.movement != "U": node_queue.enqueue(Node(current_node.U_Prime(), current_node, "U'", next_generation))

        if current_node.movement != "D'": node_queue.enqueue(Node(current_node.D(), current_node, "D", next_generation))
        if current_node.movement != "D": node_queue.enqueue(Node(current_node.D_Prime(), current_node, "D'", next_generation))
        
        if current_node.movement != "R'": node_queue.enqueue(Node(current_node.R(), current_node, "R", next_generation))
        if current_node.movement != "R": node_queue.enqueue(Node(current_node.R_Prime(), current_node, "R'", next_generation))

        if current_node.movement != "L'": node_queue.enqueue(Node(current_node.L(), current_node, "L", next_generation))
        if current_node.movement != "L": node_queue.enqueue(Node(current_node.L_Prime(), current_node, "L'", next_generation))

        if current_node.movement != "F'": node_queue.enqueue(Node(current_node.F(), current_node, "F", next_generation))
        if current_node.movement != "F": node_queue.enqueue(Node(current_node.F_Prime(), current_node, "F'", next_generation))

        if current_node.movement != "B'": node_queue.enqueue(Node(current_node.B(), current_node, "B", next_generation))
        if current_node.movement != "B": node_queue.enqueue(Node(current_node.B_Prime(), current_node, "B'", next_generation))

        current_node = node_queue.dequeue()


def phase_1_IDDFS(start_state):
    start_node = Node(start_state)
    depth = 0
    while depth <= 7:
        result = IDDFS(start_node, depth)
        if result != None: return result
        depth += 1


def phase_1_iddfs(start_state):
    parent = Node(start_state)

    node_stack = Stack(7)
    node_stack.push(parent)

    current_node = Node(parent.U(), parent, "U", 1)

    depth = 0

    while current_depth <= max_depth:

        if current_node.movement not in ("U", "U'", "D", "D'"):
            check = side_check(current_node)
            if check[0]:
                return current_node
            
        if current_node.movement == "U":
            current_node = Node(parent.U_Prime(), parent, "U'")
        
        elif current_node.movement == "U'":
            current_node = Node(parent.D(), parent, "D")

        elif current_node.movement == "D":
            current_node = Node(parent.D_Prime(), parent, "D'")

        elif current_node.movement == "D'":
            current_node = Node(parent.L(), parent, "L")
        
        elif current_node.movement == "L":
            current_node = Node(parent.L_Prime(), parent, "L")
        
        elif current_node.movement == "L'":
            current_node = Node(parent.R(), parent, "R")
        
        elif current_node.movement == "R":
            current_node = Node(parent.R_Prime(), parent, "R'")

        elif current_node.movement == "R'":
            current_node = Node(parent.F(), parent, "F")
        
        elif current_node.movement == "F":
            current_node = Node(parent.F_Prime(), parent, "F'")

        elif current_node.movement == "F'":
            current_node = Node(parent.B(), parent, "B")

        elif current_node.movement == "B":
            current_node = Node(parent.B_Prime(), parent, "B'")

        elif current_node.movement == "B'":
            # parent = current_node
            # node_stack.push(parent)
            # current_node = Node(parent.U(), parent, "U")
            # current_depth += 1
 



# cube = Cube_3(["WOWGWBWRW", "GWGOGRGYG", "RWRGRBRYR", "BWBRBOBYB", "OWOBOGOYO", "YRYGYBYOY"])
cube = Cube_3()
cube.move("U")
# cube.scramble()
cube.display()
print(side_check(cube))

node = phase_1_IDDFS(cube)

print(side_check(node))
node.display()
path = []
if node == None:
    print(None)

else:
    while node.parent != None:
        path.append(node.movement)
        node = node.parent
    path = path[::-1]

print(path)

for move in path:
    cube.move(move)

print(side_check(cube))