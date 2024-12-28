import time

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
    start_time = time.time()
    phase_1_moves, G_1_node = phase_1(start_node) 
    print(f"Phase 1 finished in {round((time.time() - start_time) * 1000, 2)} ms")

    # Phase 2
    timer = time.time()
    phase_2_moves, G_2_node = phase_2(G_1_node)
    print(f"Phase 2 finished in {round((time.time() - timer) * 1000, 2)} ms")
    # print("Phase 2 node:", G_2_node.cube)


    # Phase 3
    timer = time.time()
    phase_3_moves, G_3_cube = phase_3(G_2_node)
    print(f"Phase 3 finished in {round((time.time() - timer) * 1000, 2)} ms")


    # Phase 4
    timer = time.time()
    phase_4_moves = phase_4(G_3_cube)
    print(f"Phase 4 finished in {round((time.time() - timer) * 1000, 2)} ms\n")


    print(f"Solved in {round((time.time() - start_time) * 1000, 2)} ms\n")
    return phase_1_moves + phase_2_moves + phase_3_moves + phase_4_moves


node = Node()
for i in range(1000):
    node.scramble()
    print(thistle_solve(node))