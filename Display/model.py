import numpy as np
from numpy import cos, sin

class CubeModel:
    def __init__(self, length):
        bdr = length / 20
        self.points = [ 
                        ### Top Cubies
                        [
                            [0      ,  length - bdr,  length - bdr, 0      ,  length - bdr,  length - bdr, 0      ],
                            [-length + bdr, -length + bdr, -length + bdr, -length + bdr, 0      , 0      , 0      ],
                            [0      , 0      , -length + bdr, -length + bdr, 0      , -length + bdr, -length + bdr]
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
     
    def __getitem__(self, index):
        return self.points[index]