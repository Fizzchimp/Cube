import numpy as np
from Display.matrices import *



class Model_3():
    def __init__(self):
        # 3D Matrix of all the corner cubies
        self.corners = np.array([
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
            [ # Back Left
                [-1/3, -1  , -1  , -1/3, -1  , -1  , -1/3,    0, -1,  0],
                [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,  1/3,    1,  0,  0],
                [ 1/3,  1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  0,  1]
            ],
            [ # Back Right
                [ 1/3,  1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  0,  1],
                [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,  1/3,    1,  0,  0],
                [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,  1/3,    0,  1,  0]
            ],
            [ # Front Left
                [-1/3, -1/3, -1  , -1  , -1/3, -1  , -1  ,    0,  0, -1],
                [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,  1/3,    1,  0,  0],
                [-1/3, -1  , -1  , -1/3, -1  , -1  , -1/3,    0, -1,  0]
            ],
            [ # Front Right
                [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,  1/3,    0,  1,  0],
                [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,  1/3,    1,  0,  0],
                [-1/3, -1/3, -1  , -1  , -1/3, -1  , -1  ,    0,  0, -1]
            ]
        ], dtype = "float64")

        for i, quad in enumerate(self.corners):
            self.corners[i] = rotateX(theta, rotateY(alpha, quad))

        # 3D Matrix of all the side cubies
        self.sides = np.array([
                ### Top sides
                [ # Back                                 | Depth Points
                    [-1/3, -1/3,  1/3,  1/3, -1/3,  1/3,    0,  0],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3,   -1,  0],
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  1]
                ],
                [ # Left
                    [-1/3, -1  , -1  , -1/3, -1  , -1  ,    0, -1],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3,   -1,  0],
                    [-1/3, -1/3,  1/3,  1/3, -1/3,  1/3,    0,  0]
                ],
                [ # Right
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  1],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3,   -1,  0],
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0]
                ],
                [ # Front
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3,   -1,  0],
                    [-1/3, -1  , -1  , -1/3, -1  , -1  ,    0, -1]
                ],
                ### Middle sides
                [ # Back Left
                    [-1  , -1  , -1  , -1  , -1/3, -1/3,   -1,  0],
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0],
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  1]
                ],
                [ # Back Right
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  1],
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0],
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,    1,  0]
                ],
                [ # Front Left
                    [-1/3, -1  , -1  , -1/3, -1  , -1  ,    0, -1],
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0],
                    [-1  , -1  , -1  , -1  , -1/3, -1/3,   -1,  0] 
                ],
                [ # Front Right
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,    1,  0],
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0],
                    [-1/3, -1  , -1  , -1/3, -1  , -1  ,    0, -1]
                ],
                # Bottom sides
                [ # Back
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0],
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,    1,  0],
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  1]
                ],
                [ # Left
                    [-1/3, -1  , -1  , -1/3, -1  , -1  ,    0, -1],
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,    1,  0],
                    [-1/3, -1/3,  1/3,  1/3, -1/3,  1/3,    0,  0]
                ],
                [ # Right
                    [ 1/3,  1  ,  1  ,  1/3,  1  ,  1  ,    0,  1],
                    [ 1  ,  1  ,  1  ,  1  ,  1/3,  1/3,    1,  0],
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0]
                ],
                [ # Front
                    [ 1/3,  1/3, -1/3, -1/3,  1/3, -1/3,    0,  0],
                    [1  ,   1  ,  1  ,  1  ,  1/3,  1/3,    1,  0],
                    [-1/3, -1  , -1  , -1/3, -1  , -1  ,    0, -1]
                ]
            ], dtype = "float64") 
        
        for i, quad in enumerate(self.sides):
            self.sides[i] = rotateX(theta, rotateY(alpha, quad))

        # 3D Matrix of all the centre cubies
        self.centres = np.array([
                [ # Upper                    | Depth Points
                    [ 1/3, -1/3, -1/3,  1/3,    0],
                    [-1  , -1  , -1  , -1  ,   -1],
                    [-1/3, -1/3,  1/3,  1/3,    0]
                ],
                [ # Left
                    [-1  , -1  , -1  , -1  ,   -1],
                    [-1/3,  1/3,  1/3, -1/3,    0],
                    [-1/3, -1/3,  1/3,  1/3,    0]
                ],
                [ # Front
                    [ 1/3,  1/3, -1/3, -1/3,    0],
                    [-1/3,  1/3,  1/3, -1/3,    0],
                    [-1  , -1  , -1  , -1  ,   -1]
                ],
                [ # Right
                    [ 1  ,  1  ,  1  ,  1  ,    1],
                    [-1/3,  1/3,  1/3, -1/3,    0],
                    [ 1/3,  1/3, -1/3, -1/3,    0]
                ],
                [ # Back
                    [-1/3, -1/3,  1/3,  1/3,    0],
                    [-1/3,  1/3,  1/3, -1/3,    0],
                    [ 1  ,  1  ,  1  ,  1  ,    1]
                ],
                [ # Downward
                    [ 1/3,  1/3, -1/3, -1/3,    0],
                    [ 1  ,  1  ,  1  ,  1  ,    1],
                    [ 1/3, -1/3, -1/3,  1/3,    0]
                ]
            ], dtype = "float64")
        
        for i, quad in enumerate(self.centres):
            self.centres[i] = rotateX(theta, rotateY(alpha, quad))
            
        self.xPhase = 0
        self.yPhase = 0
        self.zPhase = 0

        self.uPhase = 0
        self.ePhase = 0
        self.dPhase = 0
        
        self.rPhase = 0
        self.mPhase = 0
        self.lPhase = 0
        
        self.fPhase = 0
        self.sPhase = 0
        self.bPhase = 0
        

    def isMoving(self):
        if any((self.xPhase, self.yPhase, self.zPhase, self.uPhase, self.ePhase, self.dPhase, self.rPhase, self.mPhase, self.lPhase, self.fPhase, self.sPhase, self.bPhase)):
            return True
        
        else: return False

    def getPoints(self):
        corners = [rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.bPhase, self.corners[0]))),
                   rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.bPhase, self.corners[1]))),
                   rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.fPhase, self.corners[2]))),
                   rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.fPhase, self.corners[3]))),
                   
                   rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.bPhase, self.corners[4]))),
                   rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.bPhase, self.corners[5]))),
                   rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.fPhase, self.corners[6]))),
                   rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.fPhase, self.corners[7])))]
        
        sides = [rotateX(self.xPhase + self.mPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.bPhase, self.sides[0]))),
                 rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.sPhase, self.sides[1]))),
                 rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.sPhase, self.sides[2]))),
                 rotateX(self.xPhase + self.mPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.fPhase, self.sides[3]))),
                 
                 rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.ePhase, rotateZ(self.zPhase + self.bPhase, self.sides[4]))),
                 rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.ePhase, rotateZ(self.zPhase + self.bPhase, self.sides[5]))),
                 rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.ePhase, rotateZ(self.zPhase + self.fPhase, self.sides[6]))),
                 rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.ePhase, rotateZ(self.zPhase + self.fPhase, self.sides[7]))),
                 
                 rotateX(self.xPhase + self.mPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.bPhase, self.sides[8]))),
                 rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.sPhase, self.sides[9]))),
                 rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.sPhase, self.sides[10]))),
                 rotateX(self.xPhase + self.mPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.fPhase, self.sides[11])))]
        
        centres = [rotateX(self.xPhase + self.mPhase, rotateY(self.yPhase + self.uPhase, rotateZ(self.zPhase + self.sPhase, self.centres[0]))),
                   
                   rotateX(self.xPhase + self.lPhase, rotateY(self.yPhase + self.ePhase, rotateZ(self.zPhase + self.sPhase, self.centres[1]))),
                   rotateX(self.xPhase + self.mPhase, rotateY(self.yPhase + self.ePhase, rotateZ(self.zPhase + self.fPhase, self.centres[2]))),
                   rotateX(self.xPhase + self.rPhase, rotateY(self.yPhase + self.ePhase, rotateZ(self.zPhase + self.sPhase, self.centres[3]))),
                   rotateX(self.xPhase + self.mPhase, rotateY(self.yPhase + self.ePhase, rotateZ(self.zPhase + self.bPhase, self.centres[4]))),
                   
                   rotateX(self.xPhase + self.mPhase, rotateY(self.yPhase + self.dPhase, rotateZ(self.zPhase + self.sPhase, self.centres[5])))]
        
        return corners, sides, centres

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
            
        
        # M Phase
        elif self.mPhase < 0:
            if self.mPhase < -increment: self.mPhase += increment
            else: self.mPhase = 0

        elif self.mPhase > 0:
            if self.mPhase > increment: self.mPhase -= increment
            else: self.mPhase = 0
            
        # E Phase
        elif self.ePhase < 0:
            if self.ePhase < -increment: self.ePhase += increment
            else: self.ePhase = 0

        elif self.ePhase > 0:
            if self.ePhase > increment: self.ePhase -= increment
            else: self.ePhase = 0
            
        # S Phase
        elif self.sPhase < 0:
            if self.sPhase < -increment: self.sPhase += increment
            else: self.sPhase = 0

        elif self.sPhase > 0:
            if self.sPhase > increment: self.sPhase -= increment
            else: self.sPhase = 0
