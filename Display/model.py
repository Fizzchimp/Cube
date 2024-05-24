import numpy as np
from numpy import cos, sin, pi

alpha = pi / 9
theta = pi / 6
newAxis = [[np.cos(alpha),  np.sin(theta) * np.sin(alpha), -np.cos(theta) * np.sin(alpha)],
           [0            , cos(theta)                    , np.sin(theta)                 ],
           [np.sin(alpha), -np.sin(theta) * np.cos(alpha), np.cos(theta) * np.cos(alpha)]]

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
        
        for i, quad in enumerate(self.points):
            self.points[i] = rotateX(theta * 180 / pi, rotateY(alpha * 180 / pi, quad))

        self.xPhase = 0
        self.yPhase = 0
        self.zPhase = 0

        self.uPhase = 0
        self.dPhase = 0
        self.fPhase = 0
        self.bPhase = 0
        self.rPhase = 0
        self.lPhase = 0

    def __getitem__(self, index):
        return self.points[index]
    
    def getPoints(self):

        return [rotateX(self.xPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase, self.points[0]))),
                rotateX(self.xPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase, self.points[1]))),
                rotateX(self.xPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase, self.points[2]))),
                rotateX(self.xPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase, self.points[3]))),
                rotateX(self.xPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase, self.points[4]))),
                rotateX(self.xPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase, self.points[5]))),
                rotateX(self.xPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase, self.points[6]))),
                rotateX(self.xPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase, self.points[7])))]

    def isMoving(self):
        if self.xPhase != 0 or self.yPhase != 0 or self.zPhase != 0 or self.uPhase != 0 or self.dPhase != 0: return True