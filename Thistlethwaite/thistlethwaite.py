import time

import random

from Thistlethwaite.phase_1 import phase_1
from Thistlethwaite.phase_2 import phase_2
from Thistlethwaite.phase_3 import phase_3
from Thistlethwaite.phase_4 import phase_4

#from cube_3 import Cube3
from Assets.node_3 import Node


# Function to organise solving the cube
def thistle_solve(start_cube):
    start_node = Node(start_cube.cube)
    print("\nStarting state:", start_node.cube, "\n")
    
    # Phase 1
    timer = time.time()
    phase_1_moves, G_1_node = phase_1(start_node) 
    print(f"Phase 1 finished in {round((time.time() - timer) * 1000, 2)} ms")
    

    # Phase 2
    timer = time.time()
    phase_2_moves, G_2_node = phase_2(G_1_node)
    print(f"Phase 2 finished in {round((time.time() - timer) * 1000, 2)} ms")


    # Phase 3
    timer = time.time()
    phase_3_moves, G_3_cube = phase_3(G_2_node)
    print(f"Phase 3 finished in {round((time.time() - timer) * 1000, 2)} ms")


    # Phase 4
    timer = time.time()
    phase_4_moves = phase_4(G_3_cube)
    print(f"Phase 4 finished in {round((time.time() - timer) * 1000, 2)} ms\n")


    return phase_1_moves + phase_2_moves + phase_3_moves + phase_4_moves

    
node = Node(['YYWOWWWYR', 'BBGGGGBBG', 'RRYRRYOOO', 'BGBBBGGBG', 'OOOOOYRRW', 'WWYWYRRWY'])
# print(thistle_solve(node))

G_1 = (
    "L", "L_Prime", "L_2",
    "R", "R_Prime", "R_2", 
    "F", "F_Prime", "F_2",
    "B", "B_Prime", "B_2", 
    "U_2", "D_2")

G_2 = (
    "L", "L_Prime", "L_2",
    "R", "R_Prime", "R_2",
    "F_2", "B_2", "U_2", "D_2")

G_3 = (
    "L_2", "R_2",
    "F_2", "B_2",
    "U_2", "D_2")

# for i in range(10000):
#     node = Node()
#     for j in range(20):
#         node.move(G_2[random.randint(0, 9)])       

#     print(i, thistle_solve(node))