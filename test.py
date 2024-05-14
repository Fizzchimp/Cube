import numpy as np

iMat = [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]]


alpha = 20 / 180 * np.pi
theta = 30 / 180 * np.pi

newAxis = [[np.cos(alpha), 0, np.sin(alpha)],
           [np.sin(theta) * np.sin(alpha), np.cos(theta), -np.sin(theta) * np.cos(alpha)],
           [-np.cos(theta) * np.sin(alpha), np.sin(theta), np.cos(theta) * np.cos(alpha)]]

for x in newAxis:
    print(np.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2))
    print(x)