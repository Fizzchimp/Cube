import numpy as np
from numpy import pi
from Display.matrices import *


class Model2():
    def __init__(self, centre):
        # 3D Matrix of all cube facelets
        self.faces = self.generate_model()

        # Phase attributes indicate angle of rotation in radians of each part of the model
        self.x_phase = 0
        self.y_phase = 0
        self.z_phase = 0

        self.u_phase = 0
        self.d_phase = 0
        
        self.r_phase = 0
        self.l_phase = 0
        
        self.f_phase = 0
        self.b_phase = 0

        # Determines where on the screen the cube is drawn
        self.centre = centre
        

    # Generates each face of the model from one central defined face
    def generate_model(self):
        # Define U face
        u_face = [
            (
                [-1,  0,  0, -1,  0],
                [-1, -1, -1, -1, -1],
                [ 1,  1,  0,  0,  0]
            ),
            (
                [ 0,  1,  1,  0,  0],
                [-1, -1, -1, -1, -1],
                [ 1,  1,  0,  0,  0]
            ),
            (
                [-1,  0,  0, -1,  0],
                [-1, -1, -1, -1, -1],
                [ 0,  0, -1, -1,  0]
            ),
            (
                [ 0,  1,  1,  0,  0],
                [-1, -1, -1, -1, -1],
                [ 0,  0, -1, -1,  0]
            )]

        l_face = []
        f_face = []
        r_face = []
        b_face = []
        d_face = []

        # Offset face rotation slightly to give 3d view
        for i, facelet in enumerate(u_face):
            u_face[i] = rotateX(theta, rotateY(alpha, facelet))
        
        # Translates U face using rotation matrices to create all 5 other faces
        for i, facelet in enumerate(u_face):
            l_face.append(rotateY(pi / 2, rotateX(pi / 2, u_face[i])))
            f_face.append(rotateX(pi / 2, u_face[i]))
            r_face.append(rotateY(-pi / 2, rotateX(pi / 2, u_face[i])))
            b_face.append(rotateY(pi, rotateX(pi / 2, u_face[i])))
            d_face.append(rotateX(pi, u_face[i]))

        return np.array([u_face, l_face, f_face, r_face, b_face, d_face])
    

    # Returns the matrix of points based on their current rotation phases
    def get_points(self):
        points = [[None for i in range(4)] for i in range(6)]

        # U Face
        for i, row_phase in enumerate((self.b_phase, self.f_phase)):
            for j, col_phase in enumerate((self.l_phase, self.r_phase)):
                points[0][i * 2 + j] = rotateX(self.x_phase + col_phase, rotateY(self.y_phase + self.u_phase, rotateZ(self.z_phase + row_phase, self.faces[0][i * 2 + j])))

        # L Face
        for i, row_phase in enumerate((self.u_phase, self.d_phase)):
            for j, col_phase in enumerate((self.b_phase, self.f_phase)):
                points[1][i * 2 + j] = rotateX(self.x_phase + self.l_phase, rotateY(self.y_phase + row_phase, rotateZ(self.z_phase + col_phase, self.faces[1][i * 2 + j])))

        # F Face
        for i, row_phase in enumerate((self.u_phase, self.d_phase)):
            for j, col_phase in enumerate((self.l_phase, self.r_phase)):
                points[2][i * 2 + j] = rotateX(self.x_phase + col_phase, rotateY(self.y_phase + row_phase, rotateZ(self.z_phase + self.f_phase, self.faces[2][i * 2 + j])))
        
        # R Face
        for i, row_phase in enumerate((self.u_phase, self.d_phase)):
            for j, col_phase in enumerate((self.f_phase, self.b_phase)):
                points[3][i * 2 + j] = rotateX(self.x_phase + self.r_phase, rotateY(self.y_phase + row_phase, rotateZ(self.z_phase + col_phase, self.faces[3][i * 2 + j])))
        
        # B Face
        for i, row_phase in enumerate((self.u_phase, self.d_phase)):
            for j, col_phase in enumerate((self.r_phase, self.l_phase)):
                points[4][i * 2 + j] = rotateX(self.x_phase + col_phase, rotateY(self.y_phase + row_phase, rotateZ(self.z_phase + self.b_phase, self.faces[4][i * 2 + j])))
        
        # D Face
        for i, row_phase in enumerate((self.f_phase, self.b_phase)):
            for j, col_phase in enumerate((self.l_phase, self.r_phase)):
                points[5][i * 2 + j] = rotateX(self.x_phase + col_phase, rotateY(self.y_phase + self.d_phase, rotateZ(self.z_phase + row_phase, self.faces[5][i * 2 + j])))

        return points
    

    # Update each phase attribute (used in animating model rotation)
    def update_phase(self, increment):
        for phase in ("x", "y", "z", "u", "d", "r", "l", "f", "b"):
            # Get the current phase value
            cur_phase = getattr(self, phase + "_phase")

            if cur_phase < 0:
                if cur_phase < -increment: setattr(self, phase + "_phase", cur_phase + increment) # Decrease until equal to 0
                else: setattr(self, phase + "_phase", 0) # End of animation so set phase to 0

            elif cur_phase > 0:
                if cur_phase > increment: setattr(self, phase + "_phase", cur_phase - increment) # Increase until equal to 0
                else: setattr(self, phase + "_phase", 0) # End of animation so set phase to 0

    # Returns true if any part of the model is moving (phase != 0)
    def is_moving(self):
        if any((self.x_phase, self.y_phase, self.z_phase, self.u_phase, self.d_phase, self.r_phase, self.l_phase, self.f_phase, self.b_phase)):
            return True
        return False