import numpy as np
from numpy import cos, sin

class CubeModel:
    def __init__(self, length):
        self.points = [
                        [
                            [0     , length, length, 0     , 0     , length, length, 0     ],
                            [length, length, length, length, 0     , 0     , 0     , 0     ],
                            [0     , 0     , length, length, 0     , 0     , length, length]
                         ]
            
            ]
     
    def __getitem__(self, index):
        return self.points[index]