import numpy as np
from Display.matrices import *



class Model_3():
    def __init__(self):
        self.points = np.array([
            ### Corners
                # Top corners
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
                [ # Front Left
                    [-1/3, -1/3, -1  , -1  , -1/3, -1  , -1  ,    0,  0, -1],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3, -1/3,   -1,  0,  0],
                    [-1/3, -1  , -1  , -1/3, -1  , -1  , -1/3,    0, -1,  0]                  
                ],
                [ # Front Right
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,  1/3,    0,  1,  0],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3, -1/3,   -1,  0,  0],
                    [-1/3, -1/3, -1  , -1  , -1/3, -1  , -1  ,    0,  0, -1]
                ],
                # Bottom corners
                [ # Front Left
                    [-1/3, -1/3, -1  , -1  , -1/3, -1  , -1  ,    0,  0, -1],
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,  1/3,    1,  0,  0],
                    [-1/3, -1  , -1  , -1/3, -1  , -1  , -1/3,    0, -1,  0]
                ],
                [ # Front Right
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,  1/3,    0,  1,  0],
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,  1/3,    1,  0,  0],
                    [-1/3, -1/3, -1  , -1  , -1/3, -1  , -1  ,    0,  0, -1]
                ],
                [ # Back Left
                    [-1/3, -1  , -1  , -1/3, -1  , -1  , -1/3,    0, -1,  0],
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,  1/3,    1,  0,  0],
                    [ 1/3,  1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  0,  1]
                ],
                [ # Back Right
                    [ 1/3,  1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  0,  1],
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,  1/3,    1,  0,  0],
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,  1/3,    0,  1,  0]
                ]
            
            ### Middle Peices
            ], dtype = "float64")

        for i, quad in enumerate(self.points):
            self.points[i] = rotateX(theta, rotateY(alpha, quad))


        self.xPhase = 0
        self.yPhase = 0
        self.zPhase = 0

    def isMoving(self):
        if self.xPhase != 0: return True
        elif self.yPhase != 0: return True
        elif self.zPhase != 0: return True
        
        else: return False

    def getPoints(self):
        corners = [rotateX(self.xPhase, rotateY(self.yPhase, rotateZ(self.zPhase, self.points[0]))),
                   rotateX(self.xPhase, rotateY(self.yPhase, rotateZ(self.zPhase, self.points[1]))),
                   rotateX(self.xPhase, rotateY(self.yPhase, rotateZ(self.zPhase, self.points[2]))),
                   rotateX(self.xPhase, rotateY(self.yPhase, rotateZ(self.zPhase, self.points[3]))),
                   rotateX(self.xPhase, rotateY(self.yPhase, rotateZ(self.zPhase, self.points[4]))),
                   rotateX(self.xPhase, rotateY(self.yPhase, rotateZ(self.zPhase, self.points[5]))),
                   rotateX(self.xPhase, rotateY(self.yPhase, rotateZ(self.zPhase, self.points[6]))),
                   rotateX(self.xPhase, rotateY(self.yPhase, rotateZ(self.zPhase, self.points[7])))]
        
        return corners

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