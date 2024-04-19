from cube import Cube
from node import Node

def binSearch(list, node):
    mid = len(list) // 2
    midItem = list[mid]

    print(list, midItem)

    if midItem == node:
        return True
    
    elif len(list) == 1:
        return False
    
    elif midItem < node:
        return binSearch(list[mid + 1:], node)
    
    elif midItem > node:
        return binSearch(list[:mid], node)
    

def nodeCompare(node1, node2):
    list1, list2 = "".join(node1.cube.cube), "".join(node2.cube.cube)
    value1 = value2 = 0
    index = 0
    while value1 == value2:
        print(value1, value2)
        value1 += ord(list1[index])
        value2 += ord(list2[index])
        index += 1
    return True if value1 > value2 else False

node1 = Node(Cube())
node2 = Node(Cube())
for i in range(10):
    node1.cube.scramble()
    node2.cube.scramble()
    print(nodeCompare(node1, node2))