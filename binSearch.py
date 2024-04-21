from cube import Cube
from node import Node

def binSearch(list, node):
    mid = len(list) // 2
    print(mid, len(list))
    midItem = list[mid]

    if midItem.cube.cube == node.cube.cube:
        return True
    
    elif len(list) == 1:
        return False
    
    elif midItem.cube.cube < node.cube.cube:
        return binSearch(list[mid + 1:], node)
    
    elif midItem.cube.cube > node.cube.cube:
        return binSearch(list[:mid], node)
    


node1 = Node(Cube())
arr = [Node(Cube()) for i in range(10)]
for i in range(9):
    arr[i + 1].cube.scramble()