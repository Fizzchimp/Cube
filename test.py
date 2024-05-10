import numpy as np

def rotateX(angle, points):
    angle = angle / 180 * np.pi
    rotX = [[1, 0, 0],
            [0, np.cos(angle), -np.sin(angle)],
            [0, np.sin(angle), np.cos(angle)]]
        
    return np.matmul(rotX, points)
        
def rotateY(angle, points):
    angle = angle / 180 * np.pi
    rotY = [[np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]]
        
    return np.matmul(rotY, points)
    
def rotateZ(angle, points):
    angle = angle / 180 * np.pi
    rotZ = [[np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]]
        
    return np.matmul(rotZ, points)

axis = rotateX(30, rotateY(20, [0, 0, 1]))

angle = np.pi / 2

r = [[np.cos(angle) + axis[0] ** 2 * (1 - np.cos(angle)),
      axis[0] * axis[1] * (1 - np.cos(angle)) - axis[2] * np.sin(angle),
      axis[0] * axis[2] * (1 - np.cos(angle)) + axis[1] * np.sin(angle)],
     
     [axis[0] * axis[1] * (1 - np.cos(angle)) + axis[2] * np.sin(angle),
      np.cos(angle) + axis[1] ** 2 * (1 - np.cos(angle)),
      axis[1] * axis[2] * (1 - np.cos(angle)) - axis[1] * np.sin(angle)],
     
     [axis[0] * axis[2] * (1 - np.cos(angle)) - axis[1] * np.sin(angle),
      axis[1] * axis[2] * (1 - np.cos(angle)) + axis[0] * np.sin(angle),
      np.cos(angle) + axis[2] ** 2 * (1 - np.cos(angle))]]

    