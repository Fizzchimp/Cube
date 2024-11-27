import time

import random

from Thistlethwaite.phase_1 import phase_1
from Thistlethwaite.phase_2 import phase_2
from Thistlethwaite.phase_3 import phase_3
from Thistlethwaite.phase_4 import phase_4, bfs_sides

#from cube_3 import Cube3
from Assets.node_3 import Node


# Function to organise solving the cube
def thistle_solve(start_cube):
    start_node = Node(start_cube.cube)
    print("Start state:", start_node.cube)
    
    # Phase 1
    timer = time.time()
    phase_1_moves, G_1_node = phase_1(start_node) 
    print(f"Phase 1 finished in {round(time.time() - timer, 4)}s")
    print(phase_1_moves)
    print("G1 state:", G_1_node.cube, "\n\n")
    

    # Phase 2
    timer = time.time()
    phase_2_moves, G_2_node = phase_2(G_1_node)
    print(f"Phase 2 finished in {round(time.time() - timer, 4)}s")
    print(phase_2_moves)
    print("G2 state:", G_2_node.cube, "\n\n")


    timer = time.time()
    phase_3_moves, G_3_cube = phase_3(G_2_node)
    print(f"Phase 3 finished in {round(time.time() - timer, 4)}s")
    print(phase_3_moves)
    print("G3 state:", G_3_cube.cube, "\n\n")


    phase_4_moves = phase_4(G_3_cube)
    print("Phase 4 moves:", phase_4_moves)
    return phase_1_moves + phase_2_moves + phase_3_moves + phase_4_moves


node = Node()
for i in range(0):
    node.scramble()
    print(thistle_solve(node))
    
# G_3 = (
#     "L_2", "R_2",
#     "F_2", "B_2",
#     "U_2", "D_2")

# # # node = Node(['WWWWWWYWY', 'GGBBGBGGB', 'RRRORROOO', 'GBBGBGGBB', 'OOOOORRRR', 'YYYYYYWYW'])
# # node = Node()
# # for i in range(100):
# #     for i in range(20):
# #         node.move(G_3[random.randint(0, 5)])

# #     print(node.cube)
# #     start_node, end_node = bfs_sides(node.cube)
# #     path = []


# #     if start_node == None:
# #         print("No path found")

# #     else:
# #         while start_node.parent != None:
# #             path.append(G_3[start_node.movement])
# #             start_node = start_node.parent
# #         path = path[::-1]

# #         while end_node.parent != None:
# #             path.append(G_3[end_node.movement])
# #             end_node = end_node.parent


# #     for move in path: node.move(move)
# #     print(path)
# #     print(node.cube)