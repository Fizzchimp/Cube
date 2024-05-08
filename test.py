import numpy as np

point = [1, 1, 1]

angle = np.pi
rotY = np.array([[np.cos(angle), 0, np.sin(angle)],
                 [0, 1, 0],
                 [-np.sin(angle), 0, np.cos(angle)]])

newPoint = np.matmul(rotY, point)
print(newPoint)