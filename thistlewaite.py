from cube_3 import Cube_3

def phase_1(startState):
    ### Phase 1
    # Flip all side peices to be "good" (can be returned home without the use of an odd number of quater turns of U or D)    
    facePattern1 = (3, 7, 5, 1)
    facePattern2 = (3, 1, 5, 7)

    side_faces = [startState[i + 1] for i in range(4)]

    good = 0
    bad = 0

    for i, face in enumerate(side_faces):
        group_a = (side_faces[i][4], side_faces[(i + 2) % 4][4])
        group_b = (side_faces[(i + 1) % 4][4], side_faces[(i + 3) % 4][4])

        side_peices = ((face[1], startState[0][facePattern1[i]]),
                       (face[3], side_faces[(i + 3) % 4][5]),
                       (face[7], startState[5][facePattern2[i]]))

        # Decision tree for 'Good' and 'Bad' Peices
        for peice in side_peices:
            if peice[0] in group_a: good += 1
            elif peice[0] in group_b: bad += 1
            else:
                if peice[1] in group_a: bad += 1
                elif peice[1] in group_b: good += 1
                # else: print(peice)
    
    print("Good: ", good, "\nBad: ", bad)
            


# cube = Cube_3(["YGWGWOBRO", "BORWRYROY", "YWWBBRGYW", "BYGBOWGRY", "RYOOGGOBB", "RROBYGWWG"])
# cube.display()
cube = Cube_3()
# cube.scramble()
phase_1(cube)