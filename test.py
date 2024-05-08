import numpy as np

points = [[1, 1, 1],
          [1, 1, -1]]
angle = np.pi / 2
rotY = np.array([[np.cos(angle), 0, np.sin(angle)],
                 [0, 1, 0],
                 [-np.sin(angle), 0, np.cos(angle)]])

def rotateY(point):
    print(point)
    return np.matmul(rotY, point)

vFunc = np.vectorize(rotateY)
newPoints = vFunc(points)
print(list(newPoints))