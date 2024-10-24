import time

from Thistlethwaite.phase_1 import phase_1
from Thistlethwaite.phase_2 import phase_2
from Thistlethwaite.phase_3 import phase_3
from Thistlethwaite.phase_4 import phase_4

from cube_3 import Cube3
# Function to organise solving the cube
def thistle_solve(start_cube):
    print(start_cube.cube)
    # Phase 1
    timer = time.time()
    phase_1_moves, G_1_state = phase_1(start_cube) 
    print(f"Phase 1 finished in {round(time.time() - timer, 4)}s")
    print(phase_1_moves)
    print(G_1_state)
    

    # Phase 2
    timer = time.time()
    phase_2_moves, G_2_node = phase_2(G_1_state)
    print(f"Phase 2 finished in {round(time.time() - timer, 4)}s")
    print(phase_2_moves)
    print(G_2_node.cube)



    timer = time.time()
    phase_3_moves, G_3_cube = phase_3(G_2_node)
    print(f"Phase 3 finished in {round(time.time() - timer, 4)}s")
    print("Phase 3 cube:")
    print(G_3_cube.cube)

    phase_4_moves = phase_4(G_3_cube)
    print("Phase 4 moves:", phase_4_moves)
    return phase_1_moves + phase_2_moves + phase_3_moves + phase_4_moves

cube = Cube3(['WWBGWRRBR', 'GWWBGWBRR', 'GRBBRYYBB', 'WGRGBOOOO', 'YROGOOGOO', 'GYYYYWWYY'])
print(thistle_solve(cube))