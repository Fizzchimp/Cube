import numpy as np
length = 1

def rotateTest(theta, alpha, points):
    theta, alpha = theta / 180 * np.pi, alpha / 180 * np.pi
    rotTest = [[np.cos(theta), np.sin(theta) * np.sin(alpha), -np.sin(theta) * np.cos(alpha)],
               [0, np.cos(alpha), -np.sin(alpha)],
               [-np.sin(theta), np.sin(theta) * np.sin(alpha), -np.cos(theta) * np.cos(alpha)]]
    
    return np.matmul(rotTest, points)

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

cubePoints = [
            [length, length, -length, -length, length, length, -length, -length],
            [length, length, length, length, -length, -length, -length, -length],
            [length, -length, -length, length, length, -length, -length, length]]

newPoints = rotateTest(90, 90, cubePoints)
newPoints1 = rotateX(90, rotateY(90, cubePoints))

for i in range(8):
    print(newPoints[0][i], newPoints[1][i], newPoints[2][i])
    print(newPoints1[0][i], newPoints1[1][i], newPoints1[2][i])
    print("---------------")