from node import Node
from mergesort import mergeSort
from binsearch import binSearch

nodes = []
for i in range(100000):
    nodes.append(Node())
    nodes[-1].scramble()

myNode = Node()
myNode.scramble()
nodes.append(myNode)

nodes = mergeSort(nodes)
print(myNode)
print(binSearch(nodes, myNode))