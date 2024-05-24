import numpy as np
from numpy import cos, sin, pi

alpha = pi / 9
theta = pi / 6
newAxis = [[cos(alpha), sin(theta) * sin(alpha), cos(theta) * sin(alpha)],
           [0         , cos(theta)             , sin(theta)             ],
           [sin(alpha), sin(theta) * cos(alpha), cos(theta) * cos(alpha)]]

def rotateX(angle, points):
    angle = angle / 180 * pi
    axis = newAxis[0]
    rotX = [[cos(angle) + axis[0] * axis[0] * (1 - cos(angle)),
            axis[0] * axis[1] * (1 - cos(angle)) - axis[2] * sin(angle),
            axis[0] * axis[2] * (1 - cos(angle)) + axis[1] * sin(angle)],

            [axis[0] * axis[1] * (1 - cos(angle)) + axis[2] * sin(angle),
            cos(angle) + axis[1] * axis[1] * (1 - cos(angle)),
            axis[1] * axis[2] * (1 - cos(angle)) - axis[0] * sin(angle)],

            [axis[0] * axis[2] * (1 - cos(angle)) - axis[1] * sin(angle),
            axis[1] * axis[2] * (1 - cos(angle)) + axis[0] * sin(angle),
            cos(angle) + axis[2] * axis[2] * (1 - cos(angle))]]
    return np.matmul(rotX, points)


def rotateY(angle, points):
    angle = angle / 180 * np.pi
    axis = newAxis[1]
    rotY = [[np.cos(angle) + axis[0] * axis[0] * (1 - np.cos(angle)),
            axis[0] * axis[1] * (1 - np.cos(angle)) - axis[2] * np.sin(angle),
            axis[0] * axis[2] * (1 - np.cos(angle)) + axis[1] * np.sin(angle)],

            [axis[0] * axis[1] * (1 - np.cos(angle)) + axis[2] * np.sin(angle),
            np.cos(angle) + axis[1] * axis[1] * (1 - np.cos(angle)),
            axis[1] * axis[2] * (1 - np.cos(angle)) - axis[0] * np.sin(angle)],

            [axis[0] * axis[2] * (1 - np.cos(angle)) - axis[1] * np.sin(angle),
            axis[1] * axis[2] * (1 - np.cos(angle)) + axis[0] * np.sin(angle),
            np.cos(angle) + axis[2] * axis[2] * (1 - np.cos(angle))]]

    return np.matmul(rotY, points)


def rotateZ(angle, points):
    angle = angle / 180 * np.pi
    axis = newAxis[2]
    rotZ = [[np.cos(angle) + axis[0] * axis[0] * (1 - np.cos(angle)),
            axis[0] * axis[1] * (1 - np.cos(angle)) - axis[2] * np.sin(angle),
            axis[0] * axis[2] * (1 - np.cos(angle)) + axis[1] * np.sin(angle)],

            [axis[0] * axis[1] * (1 - np.cos(angle)) + axis[2] * np.sin(angle),
            np.cos(angle) + axis[1] * axis[1] * (1 - np.cos(angle)),
            axis[1] * axis[2] * (1 - np.cos(angle)) - axis[0] * np.sin(angle)],

            [axis[0] * axis[2] * (1 - np.cos(angle)) - axis[1] * np.sin(angle),
            axis[1] * axis[2] * (1 - np.cos(angle)) + axis[0] * np.sin(angle),
            np.cos(angle) + axis[2] * axis[2] * (1 - np.cos(angle))]]

    return np.matmul(rotZ, points)

class CubeModel:
    def __init__(self, length):
        self.points = [ 
                        ### Top Cubies
                        [
                            [0      ,  length,  length, 0      ,  length,  length, 0      ],
                            [-length, -length, -length, -length, 0      , 0      , 0      ],
                            [0      , 0      , -length, -length, 0      , -length, -length]
                        ],
                        [
                            [0      , 0      , -length, -length, 0      , -length, -length],
                            [-length, -length, -length, -length, 0      , 0      , 0      ],
                            [0      , -length, -length, 0      , -length, -length, 0      ]
                        ],
                        [
                            [0      , -length, -length, 0      , -length, -length, 0      ],
                            [-length, -length, -length, -length, 0      , 0      , 0      ],
                            [0      , 0      ,  length,  length, 0      ,  length,  length]
                        ],
                        [
                            [0      , 0      ,  length, length , 0      ,  length,  length],
                            [-length, -length, -length, -length, 0      , 0      , 0      ],
                            [0      ,  length,  length, 0      ,  length,  length, 0      ]
                        ],
                        # Bottom Cubies
                        [
                            [0      , 0      ,  length,  length, 0      ,  length,  length],
                            [ length,  length,  length,  length, 0      , 0      , 0      ],
                            [0      , -length, -length,  0     , -length, -length, 0      ]
                        ],
                        [
                            [0      ,  length,  length, 0      ,  length,  length, 0      ],
                            [ length,  length,  length,  length, 0      , 0      , 0      ],
                            [0      ,  0     ,  length,  length, 0      ,  length,  length]
                        ],
                        [
                            [0      , 0      , -length, -length, 0      , -length, -length],
                            [ length,  length,  length,  length, 0      , 0      , 0      ],
                            [0      ,  length,  length,  0     ,  length,  length, 0      ]
                        ],
                        [
                            [0      , -length, -length, 0      , -length, -length, 0      ],
                            [ length,  length,  length,  length, 0      , 0      , 0      ],
                            [0      , 0      , -length, -length, 0      , -length, -length]
                        ]
            
            ]
        
        self.xPhase = 0
        self.yPhase = 0
        self.zPhase = 0
     
    def __getitem__(self, index):
        return self.points[index]
    
    def getPoints(self):
        points = self.points
        
        if self.xPhase != 0:
            for i, quadrant in enumerate(self.points):
                points[i] = rotateX(self.xPhase, quadrant)
                
        elif self.yPhase != 0:
            for i, quadrant in enumerate(self.points):
                points[i] = rotateY(self.yPhase, quadrant)
                
        elif self.zPhase != 0:
            for i, quadrant in enumerate(self.points):
                points[i] = rotateZ(self.zPhase, points)
                

        if self.yPhase < 0: self.yPhase += 1
        if self.yPhase > 0: self.yPhase -= 1

        if self.xPhase < 0: self.xPhase += 1
        if self.xPhase > 0: self.xPhase -= 1

        if self.zPhase < 0: self.zPhase += 1
        if self.zPhase > 0: self.zPhase -= 1
        print(self.xPhase, self.yPhase, self.zPhase)
        return points
                
