import numpy as np



angle = np.pi / 2
rotY = np.array([[np.cos(angle), 0, np.sin(angle)],
                 [0, 1, 0],
                 [-np.sin(angle), 0, np.cos(angle)]])

length = 1
points = [
    [length, length, -length, -length, length, length, -length, -length],
    [length, length, length, length, -length, -length, -length, -length],
    [length, -length, -length, length, length, -length, -length, length]]
        

print(np.matmul(rotY, points))
