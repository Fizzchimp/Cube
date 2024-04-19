from cube import Cube
from node import Node

def binSearch(list, node):
    mid = len(list) // 2
    midItem = list[mid]

    if midItem == node:
        return True
    
    elif len(list) == 1:
        return False
    
    elif nodeCompare(midItem, node):
        return binSearch(list[mid + 1:], node)
    
    elif not nodeCompare(midItem, node):
        return binSearch(list[:mid], node)
    

def nodeCompare(node1, node2):
    list1, list2 = "".join(node1.cube.cube), "".join(node2.cube.cube)
    index = 0
    value1 = value2 = 0
    while value1 == value2:
        value1, value2 = ord(list1[index]), ord(list2[index])
        index += 1
    return True if value1 < value2 else False