import numpy as np
from numpy import cos, sin, pi, matmul

alpha = pi / 9
sinAlph = sin(alpha)
cosAlph = cos(alpha)

theta = pi / 6
sinThet = sin(theta)
cosThet = cos(theta)

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



def rotateX(angle, points):
    if angle == 0:
        return points
    
    rotX = matrixX(angle)
    return matmul(rotX, points)

def rotateY(angle, points):
    if angle == 0:
        return points
    
    rotY = matrixY(angle)
    return matmul(rotY, points)

def rotateZ(angle, points):
    if angle == 0:
        return points

    rotZ = matrixZ(angle)
    return matmul(rotZ, points)