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
    start_time = time.time() # Start timing
    phase_1_moves, G_1_node = phase_1(start_node)
    # Displays how long the program took to solve
    # print(f"Phase 1 finished in {round((time.time() - start_time) * 1000, 2)} ms") 


    # Phase 2
    timer = time.time()# Start timing
    phase_2_moves, G_2_node = phase_2(G_1_node)
    # Displays how long the program took to solve
    # print(f"Phase 2 finished in {round((time.time() - timer) * 1000, 2)} ms")



    # Phase 3 (and 4)
    timer = time.time()# Start timing
    phase_3_moves = phase_3(G_2_node) # Gets phase 3 aswell as phase 4 moves
    # Displays how long the program took to solve
    # print(f"Phase 3 finished in {round((time.time() - timer) * 1000, 2)} ms")


    # I do not like this
    # # Phase 4
    # timer = time.time()
    # phase_4_moves = phase_4(G_3_cube)
    # print(f"Phase 4 finished in {round((time.time() - timer) * 1000, 2)} ms\n")


    # Display total amount of time to solve whole cube
    print(f"Solved in {round((time.time() - start_time), 2)} ms\n")
    
    return phase_1_moves + phase_2_moves + phase_3_moves, time.time() - start_time


# node = Node()
# times =[]
# paths = []
# max_time = 0
# max_path = 0

# for i in range(1000):
#     node.scramble()
#     path, time_taken = thistle_solve(node)
#     times.append(time_taken)
#     if time_taken > max_time: max_time = time_taken
    
#     paths.append(len(path))
#     if len(path) > max_path: max_path = len(path)

#     print("Average time:", round(sum(times) / len(times) * 1000, 2), "| Maximum time:", round(max_time * 1000, 2))
#     print("Average path length:", (sum(paths) // len(paths)), "| Maximum path length:", max_path)
