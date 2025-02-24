import numpy as np
from numpy import cos, sin, pi, matmul

# Initial cube models are rotated around x axis by theta
theta = pi / 6
sin_theta = sin(theta)
cos_theta = cos(theta)

# Initial cube models are rotated around y axis by alpha
alpha = pi / 9
sin_alpha = sin(alpha)
cos_alpha = cos(alpha)




# Transformation matrix for rotation around x axis by a given angle
def matrix_x(angle):
    cos_angle = cos(angle)
    sin_angle = sin(angle)
    
    return np.array([
        [cos_angle + cos_alpha ** 2 * (1 - cos_angle),
        cos_alpha * sin_theta * sin_alpha * (1 - cos_angle) + cos_theta * sin_alpha * sin_angle,
        cos_alpha * -cos_theta * sin_alpha * (1 - cos_angle) + sin_theta * sin_alpha * sin_angle],

        [cos_alpha * sin_theta * sin_alpha * (1 - cos_angle) + -cos_theta * sin_alpha * sin_angle,
        cos_angle + (sin_theta * sin_alpha) ** 2 * (1 - cos_angle),
        sin_theta * sin_alpha * -cos_theta * sin_alpha * (1 - cos_angle) - cos_alpha * sin_angle],

        [cos_alpha * -cos_theta * sin_alpha * (1 - cos_angle) - sin_theta * sin_alpha * sin_angle,
        sin_theta * sin_alpha * -cos_theta * sin_alpha * (1 - cos_angle) + cos_alpha * sin_angle,
        cos_angle + -cos_theta * sin_alpha * -cos_theta * sin_alpha * (1 - cos_angle)]])


# Transformation matrix for rotation around y axis by a given angle
def matrix_y(angle):
    cos_angle = cos(angle)
    sin_angle = sin(angle)
    
    return np.array([
        [cos_angle,
        -sin_theta * sin_angle,
        cos_theta * sin_angle],

        [sin_theta * sin_angle,
        cos_angle + cos_theta ** 2 * (1 - cos_angle),
        cos_theta * sin_theta * (1 - cos_angle)],

        [-cos_theta * sin_angle,
        cos_theta * sin_theta * (1 - cos_angle),
        cos_angle + sin_theta * sin_theta * (1 - cos_angle)]])


# Transformation matrix for rotation around z axis by a given angle
def matrix_z(angle):
    cos_angle = cos(angle)
    sin_angle = sin(angle)

    return np.array([
        [cos_angle + sin_alpha ** 2 * (1 - cos_angle),
        sin_alpha * -sin_theta * cos_alpha * (1 - cos_angle) - cos_theta * cos_alpha * sin_angle,
        sin_alpha * cos_theta * cos_alpha * (1 - cos_angle) + -sin_theta * cos_alpha * sin_angle],

        [sin_alpha * -sin_theta * cos_alpha * (1 - cos_angle) + cos_theta * cos_alpha * sin_angle,
        cos_angle + (sin_theta * cos_alpha) ** 2 * (1 - cos_angle),
        -sin_theta * cos_alpha * cos_theta * cos_alpha * (1 - cos_angle) - sin_alpha * sin_angle],

        [sin_alpha * cos_theta * cos_alpha * (1 - cos_angle) + sin_theta * cos_alpha * sin_angle,
        -sin_theta * cos_alpha * cos_theta * cos_alpha * (1 - cos_angle) + sin_alpha * sin_angle,
        cos_angle + (cos_theta * cos_alpha) ** 2 * (1 - cos_angle)]])



# Returns given points after rotation about x axis
def rotate_x(angle, points):
    if angle == 0:
        return points
    
    rot_x = matrix_x(angle)
    return matmul(rot_x, points)

# Returns given points after rotation about y axis
def rotate_y(angle, points):
    if angle == 0:
        return points
    
    rot_y = matrix_y(angle)
    return matmul(rot_y, points)

# Returns fiven points after rotation about y axis
def rotate_z(angle, points):
    if angle == 0:
        return points

    rot_z = matrix_z(angle)
    return matmul(rot_z, points)