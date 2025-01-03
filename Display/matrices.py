import numpy as np
from numpy import cos, sin, pi, matmul

# Initial cube models are rotated around x axis by theta
theta = pi / 6
sinThet = sin(theta)
cosThet = cos(theta)

# Initial cube models are rotated around y axis by alpha
alpha = pi / 9
sinAlph = sin(alpha)
cosAlph = cos(alpha)




# Transformation matrix for rotation around x axis by a given angle
def matrixX(angle):
    cosAngle = cos(angle)
    sinAngle = sin(angle)
    
    return np.array([
        [cosAngle + cosAlph ** 2 * (1 - cosAngle),
        cosAlph * sinThet * sinAlph * (1 - cosAngle) + cosThet * sinAlph * sinAngle,
        cosAlph * -cosThet * sinAlph * (1 - cosAngle) + sinThet * sinAlph * sinAngle],

        [cosAlph * sinThet * sinAlph * (1 - cosAngle) + -cosThet * sinAlph * sinAngle,
        cosAngle + (sinThet * sinAlph) ** 2 * (1 - cosAngle),
        sinThet * sinAlph * -cosThet * sinAlph * (1 - cosAngle) - cosAlph * sinAngle],

        [cosAlph * -cosThet * sinAlph * (1 - cosAngle) - sinThet * sinAlph * sinAngle,
        sinThet * sinAlph * -cosThet * sinAlph * (1 - cosAngle) + cosAlph * sinAngle,
        cosAngle + -cosThet * sinAlph * -cosThet * sinAlph * (1 - cosAngle)]])


# Transformation matrix for rotation around y axis by a given angle
def matrixY(angle):
    cosAngle = cos(angle)
    sinAngle = sin(angle)
    
    return np.array([
        [cosAngle,
        -sinThet * sinAngle,
        cosThet * sinAngle],

        [sinThet * sinAngle,
        cosAngle + cosThet ** 2 * (1 - cosAngle),
        cosThet * sinThet * (1 - cosAngle)],

        [-cosThet * sinAngle,
        cosThet * sinThet * (1 - cosAngle),
        cosAngle + sinThet * sinThet * (1 - cosAngle)]])


# Transformation matrix for rotation around z axis by a given angle
def matrixZ(angle):
    cosAngle = cos(angle)
    sinAngle = sin(angle)

    return np.array([
        [cosAngle + sinAlph ** 2 * (1 - cosAngle),
        sinAlph * -sinThet * cosAlph * (1 - cosAngle) - cosThet * cosAlph * sinAngle,
        sinAlph * cosThet * cosAlph * (1 - cosAngle) + -sinThet * cosAlph * sinAngle],

        [sinAlph * -sinThet * cosAlph * (1 - cosAngle) + cosThet * cosAlph * sinAngle,
        cosAngle + (sinThet * cosAlph) ** 2 * (1 - cosAngle),
        -sinThet * cosAlph * cosThet * cosAlph * (1 - cosAngle) - sinAlph * sinAngle],

        [sinAlph * cosThet * cosAlph * (1 - cosAngle) + sinThet * cosAlph * sinAngle,
        -sinThet * cosAlph * cosThet * cosAlph * (1 - cosAngle) + sinAlph * sinAngle,
        cosAngle + (cosThet * cosAlph) ** 2 * (1 - cosAngle)]])



# Returns given points after rotation about x axis
def rotateX(angle, points):
    if angle == 0:
        return points
    
    rotX = matrixX(angle)
    return matmul(rotX, points)

# Returns given points after rotation about y axis
def rotateY(angle, points):
    if angle == 0:
        return points
    
    rotY = matrixY(angle)
    return matmul(rotY, points)

# Returns fiven points after rotation about y axis
def rotateZ(angle, points):
    if angle == 0:
        return points

    rotZ = matrixZ(angle)
    return matmul(rotZ, points)