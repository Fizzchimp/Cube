import pygame
import os
import math
def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix

    else:
        print("columns of the first matrix must be equal to the rows of the second matrix")
        return None

os.environ["SDL_VIDEO_CENTERED"]='1'
black, white, blue  = (20, 20, 20), (230, 230, 230), (0, 154, 255)
width, height = 1920, 1080

pygame.init()
pygame.display.set_caption("3D cube Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

angle = 0
cube_position = [width//2, height//2]
scale = 600
speed = 0.01
points = [n for n in range(8)]

points[0] = [[-1], [-1], [1]]
points[1] = [[1], [-1], [1]]
points[2] = [[1], [1], [1]]
points[3] = [[-1], [1], [1]]
points[4] = [[-1], [-1], [-1]]
points[5] = [[1], [-1], [-1]]
points[6] = [[1], [1], [-1]]
points[7] = [[-1], [1], [-1]]


def connect_point(i, j, k):
    a = k[i]
    b = k[j]
    pygame.draw.line(screen, black, (a[0], a[1]), (b[0], b[1]), 2)

run = True
while run:
    clock.tick(fps)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    index = 0
    projected_points = [j for j in range(len(points))]

    rotation_x = [[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]]

    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]]

    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                  [math.sin(angle), math.cos(angle), 0],
                  [0, 0 ,1]]

    for point in points:
        rotated_2d = matrix_multiplication(rotation_y, point)
        rotated_2d = matrix_multiplication(rotation_x, rotated_2d)
        rotated_2d = matrix_multiplication(rotation_z, rotated_2d)
        distance = 5
        z = 1/(distance - rotated_2d[2][0])
        projection_matrix = [[z, 0, 0],
                            [0, z, 0]]
        projected_2d = matrix_multiplication(projection_matrix, rotated_2d)

        x = int(projected_2d[0][0] * scale) + cube_position[0]
        y = int(projected_2d[1][0] * scale) + cube_position[1]
        projected_points[index] = [x, y]
        pygame.draw.circle(screen, blue, (x, y), 10)
        index += 1
    #draw edges
    for m in range(4):
        connect_point(m, (m+1)%4, projected_points)
        connect_point(m+4, (m+1)%4 + 4, projected_points)
        connect_point(m, m+4, projected_points)

    angle += speed
    pygame.display.update()

pygame.quit()
    