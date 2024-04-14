import pygame as pg
from display import Display
from cube import Cube
from cqueue import Queue
from node import Node

class World:
    def __init__(self):
        window = Display(700, 700)
    

    def solve(self, startCube):
        solved = False

        nodeQ = Queue(999)
        nodeQ.enqueue(Node(startCube.cube))

        visitedQ = Queue(999)
        while not solved:



world = World()