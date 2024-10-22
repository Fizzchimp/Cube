from node_3 import Node

def iddfs(start_cube, key, moveset, max_depth):
    start_node = Node(start_cube.cube)
    if key(start_node): return [], start_node
    