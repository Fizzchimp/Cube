import numpy as np
from Display.matrices import *



class Model_3():
    def __init__(self):
        self.points = np.array([
            ### Top Cubies
                [  # Back Left                                 | Depth Points
                    [-1/3, -1  , -1  , -1/3, -1  , -1  , -1/3,    0, -1,  0],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3, -1/3,   -1,  0,  0],
                    [ 1/3,  1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  0,  1]
                ],
                [ # Back Right
                    [ 1/3,  1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  0,  1],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3, -1/3,   -1,  0,  0],
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,  1/3,    0,  1,  0]
                ],
                [ # Front Right
                    [],
                    [],
                    []
                ]
            ], dtype = "float64")

        for i, quad in enumerate(self.points):
            self.points[i] = rotateX(theta, rotateY(alpha, quad))


        self.xPhase = 0
        self.yPhase = 0
        self.zPhase = 0

    def isMoving(self):
        if self.xPhase != 0: return True
        elif self.yPhase != 0: return True
        elif self.yPhase != 0: return True
        
        else: return False

    def getPoints(self):
        if self.isMoving() == 0: return self.points

    def phaseUpdate(self, thing):
        pass