import numpy as np
from numpy import cos, sin, pi, matmul
from Display.matrices import *


class Model_2:
    def __init__(self):
        self.points = np.array([ 
            ### Top Cubies
            [  # Back Left
                [ 0, -1, -1,  0, -1, -1,  0],
                [-1, -1, -1, -1,  0,  0,  0],
                [ 0,  0,  1,  1,  0,  1,  1]
            ],
            [ # Back Right
                [ 0,  0,  1,  1,  0,  1,  1],
                [-1, -1, -1, -1,  0,  0,  0],
                [ 0,  1,  1,  0,  1,  1,  0]
            ],
            [ # Front Left
                [ 0,  0, -1, -1,  0, -1, -1],
                [-1, -1, -1, -1,  0,  0,  0],
                [ 0, -1, -1,  0, -1, -1,  0]
            ],
            [ # Front Right
                [ 0,  1,  1,  0,  1,  1,  0],
                [-1, -1, -1, -1,  0,  0,  0],
                [ 0,  0, -1, -1,  0, -1, -1]
            ],

            ### Bottom Cubies
            [ # Front Left
                [ 0, -1, -1,  0, -1, -1,  0],
                [ 1,  1,  1,  1,  0,  0,  0],
                [ 0,  0, -1, -1,  0, -1, -1]
            ],
            [ # Front Right
                [ 0,  0,  1,  1,  0,  1,  1],
                [ 1,  1,  1,  1,  0,  0,  0],
                [ 0, -1, -1,  0, -1, -1,  0]
            ],
            [ # Back Left
                [ 0,  0, -1, -1,  0, -1, -1],
                [ 1,  1,  1,  1,  0,  0,  0],
                [ 0,  1,  1,  0,  1,  1,  0]
            ],
            [ # Back Right
                [ 0,  1,  1,  0,  1,  1,  0],
                [ 1,  1,  1,  1,  0,  0,  0],
                [ 0,  0,  1,  1,  0,  1,  1]
            ]
        ], dtype = "float64")

        for i, quad in enumerate(self.points):
            self.points[i] = rotateX(theta, rotateY(alpha, quad))


        self.xPhase = 0
        self.yPhase = 0
        self.zPhase = 0

        self.uPhase = 0
        self.dPhase = 0
        self.fPhase = 0
        self.bPhase = 0
        self.rPhase = 0
        self.lPhase = 0

    
    def getPoints(self):
        return [rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.bPhase, self.points[0]))),
                rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.bPhase, self.points[1]))),
                rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.fPhase, self.points[2]))),
                rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.fPhase, self.points[3]))),
                rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.fPhase, self.points[4]))),
                rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.fPhase, self.points[5]))),
                rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.bPhase, self.points[6]))),
                rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.bPhase, self.points[7])))]

    def isMoving(self):
        if any((self.xPhase, self.yPhase, self.zPhase, self.uPhase, self.dPhase, self.fPhase, self.bPhase, self.lPhase, self.rPhase)):
            return True
        
    def phaseUpdate(self, increment):
        # Y Phase
        if self.yPhase < 0:
            if self.yPhase < -increment: self.yPhase += increment
            else: self.yPhase = 0

        elif self.yPhase > 0:
            if self.yPhase > increment: self.yPhase -= increment
            else: self.yPhase = 0

        # X Phase
        elif self.xPhase < 0:
            if self.xPhase < -increment: self.xPhase += increment
            else: self.xPhase = 0

        elif self.xPhase > 0:
            if self.xPhase > increment: self.xPhase -= increment
            else: self.xPhase = 0

        # Z Phase
        elif self.zPhase < 0:
            if self.zPhase < -increment: self.zPhase += increment
            else: self.zPhase = 0

        elif self.zPhase > 0:
            if self.zPhase > increment: self.zPhase -= increment
            else: self.zPhase = 0

        # U Phase
        elif self.uPhase < 0:
            if self.uPhase < -increment: self.uPhase += increment
            else: self.uPhase = 0

        elif self.uPhase > 0:
            if self.uPhase > increment: self.uPhase -= increment
            else: self.uPhase = 0

        # D Phase
        elif self.dPhase < 0:
            if self.dPhase < -increment: self.dPhase += increment
            else: self.dPhase = 0

        elif self.dPhase > 0:
            if self.dPhase > increment: self.dPhase -= increment
            else: self.dPhase = 0

        # F Phase
        elif self.fPhase < 0:
            if self.fPhase < -increment: self.fPhase += increment
            else: self.fPhase = 0

        elif self.fPhase > 0:
            if self.fPhase > increment: self.fPhase -= increment
            else: self.fPhase = 0

        # B Phase
        elif self.bPhase < 0:
            if self.bPhase < -increment: self.bPhase += increment
            else: self.bPhase = 0

        elif self.bPhase > 0:
            if self.bPhase > increment: self.bPhase -= increment
            else: self.bPhase = 0

        # L Phase
        elif self.lPhase < 0:
            if self.lPhase < -increment: self.lPhase += increment
            else: self.lPhase = 0

        elif self.lPhase > 0:
            if self.lPhase > increment: self.lPhase -= increment
            else: self.lPhase = 0

        # R Phase
        elif self.rPhase < 0:
            if self.rPhase < -increment: self.rPhase += increment
            else: self.rPhase = 0

        elif self.rPhase > 0:
            if self.rPhase > increment: self.rPhase -= increment
            else: self.rPhase = 0