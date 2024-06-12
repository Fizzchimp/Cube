import numpy as np
from numpy import cos, sin, pi, matmul

alpha = pi / 9
sinAlph = sin(alpha)
cosAlph = cos(alpha)

theta = pi / 6
sinThet = sin(theta)
cosThet = cos(theta)

def rotateX(angle, points):
    if angle == 0:
        return points
    angle = angle / 180 * pi
    cosAngle = cos(angle)
    sinAngle = sin(angle)
    
    rotX = np.array([[cosAngle + cosAlph ** 2 * (1 - cosAngle),
            cosAlph * sinThet * sinAlph * (1 - cosAngle) + cosThet * sinAlph * sinAngle,
            cosAlph * -cosThet * sinAlph * (1 - cosAngle) + sinThet * sinAlph * sinAngle],

            [cosAlph * sinThet * sinAlph * (1 - cosAngle) + -cosThet * sinAlph * sinAngle,
            cosAngle + (sinThet * sinAlph) ** 2 * (1 - cosAngle),
            sinThet * sinAlph * -cosThet * sinAlph * (1 - cosAngle) - cosAlph * sinAngle],

            [cosAlph * -cosThet * sinAlph * (1 - cosAngle) - sinThet * sinAlph * sinAngle,
            sinThet * sinAlph * -cosThet * sinAlph * (1 - cosAngle) + cosAlph * sinAngle,
            cosAngle + -cosThet * sinAlph * -cosThet * sinAlph * (1 - cosAngle)]])
    return matmul(rotX, points)

def rotateY(angle, points):
    if angle == 0:
        return points
    angle = angle / 180 * np.pi
    cosAngle = cos(angle)
    sinAngle = sin(angle)
    
    rotY = np.array([[cosAngle,
            -sinThet * sinAngle,
            cosThet * sinAngle],

            [sinThet * sinAngle,
            cosAngle + cosThet ** 2 * (1 - cosAngle),
            cosThet * sinThet * (1 - cosAngle)],

            [-cosThet * sinAngle,
            cosThet * sinThet * (1 - cosAngle),
            cosAngle + sinThet * sinThet * (1 - cosAngle)]])
    return matmul(rotY, points)

def rotateZ(angle, points):
    if angle == 0:
        return points
    angle = angle / 180 * np.pi
    cosAngle = cos(angle)
    sinAngle = sin(angle)

    rotZ = np.array([[cosAngle + sinAlph ** 2 * (1 - cosAngle),
             sinAlph * -sinThet * cosAlph * (1 - cosAngle) - cosThet * cosAlph * sinAngle,
             sinAlph * cosThet * cosAlph * (1 - cosAngle) + -sinThet * cosAlph * sinAngle],

             [sinAlph * -sinThet * cosAlph * (1 - cosAngle) + cosThet * cosAlph * sinAngle,
             cosAngle + (sinThet * cosAlph) ** 2 * (1 - cosAngle),
             -sinThet * cosAlph * cosThet * cosAlph * (1 - cosAngle) - sinAlph * sinAngle],

             [sinAlph * cosThet * cosAlph * (1 - cosAngle) - -sinThet * cosAlph * sinAngle,
             -sinThet * cosAlph * cosThet * cosAlph * (1 - cosAngle) + sinAlph * sinAngle,
             cosAngle + (cosThet * cosAlph) ** 2 * (1 - cosAngle)]])
    return matmul(rotZ, points)


class CubeModel:
    def __init__(self, length):
        self.points = np.array([ 
                        ### Top Cubies
                        [  # Back Left
                            [0      , -length, -length, 0      , -length, -length, 0      ],
                            [-length, -length, -length, -length, 0      , 0      , 0      ],
                            [0      , 0      ,  length,  length, 0      ,  length,  length]
                        ],
                        [ # Back Right
                            [0      , 0      ,  length, length , 0      ,  length,  length],
                            [-length, -length, -length, -length, 0      , 0      , 0      ],
                            [0      ,  length,  length, 0      ,  length,  length, 0      ]
                        ],
                        [ # Front Left
                            [0      , 0      , -length, -length, 0      , -length, -length],
                            [-length, -length, -length, -length, 0      , 0      , 0      ],
                            [0      , -length, -length, 0      , -length, -length, 0      ]
                        ],
                        [ # Front Right
                            [0      ,  length,  length, 0      ,  length,  length, 0      ],
                            [-length, -length, -length, -length, 0      , 0      , 0      ],
                            [0      , 0      , -length, -length, 0      , -length, -length]
                        ],

                        ### Bottom Cubies
                        [ # Front Left
                            [0      , -length, -length, 0      , -length, -length, 0      ],
                            [ length,  length,  length,  length, 0      , 0      , 0      ],
                            [0      , 0      , -length, -length, 0      , -length, -length]
                        ],
                        [ # Front Right
                            [0      , 0      ,  length,  length, 0      ,  length,  length],
                            [ length,  length,  length,  length, 0      , 0      , 0      ],
                            [0      , -length, -length,  0     , -length, -length, 0      ]
                        ],
                        [ # Back Left
                            [0      , 0      , -length, -length, 0      , -length, -length],
                            [ length,  length,  length,  length, 0      , 0      , 0      ],
                            [0      ,  length,  length,  0     ,  length,  length, 0      ]
                        ],
                        [ # Back Right
                            [0      ,  length,  length, 0      ,  length,  length, 0      ],
                            [ length,  length,  length,  length, 0      , 0      , 0      ],
                            [0      ,  0     ,  length,  length, 0      ,  length,  length]
                        ]
                    ])
        
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
        if self.yPhase < 0: self.yPhase += increment
        elif self.yPhase > 0: self.yPhase -= increment

        elif self.xPhase < 0: self.xPhase += increment
        elif self.xPhase > 0: self.xPhase -= increment

        elif self.zPhase < 0: self.zPhase += increment
        elif self.zPhase > 0: self.zPhase -= increment

        elif self.uPhase < 0: self.uPhase += increment
        elif self.uPhase > 0: self.uPhase -= increment

        elif self.dPhase < 0: self.dPhase += increment
        elif self.dPhase > 0: self.dPhase -= increment

        elif self.fPhase < 0: self.fPhase += increment
        elif self.fPhase > 0: self.fPhase -= increment

        elif self.bPhase < 0: self.bPhase += increment
        elif self.bPhase > 0: self.bPhase -= increment

        elif self.lPhase < 0: self.lPhase += increment
        elif self.lPhase > 0: self.lPhase -= increment

        elif self.rPhase < 0: self.rPhase += increment
        elif self.rPhase > 0: self.rPhase -= increment