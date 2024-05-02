from node import Node
from mergesort import mergeSort
from binsearch import binSearch

for i in range(100):
    nodes = []
    for j in range(1000):
        nodes.append(Node())
        nodes[-1].scramble()

    myNode = Node()
    myNode.scramble()
    #nodes.append(myNode)

    nodes = mergeSort(nodes)
    print(binSearch(nodes, myNode), i)