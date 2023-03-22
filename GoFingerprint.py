import sys
import numpy as np
from Cellule import Cellule

def distance_between_cellules(c1:Cellule, c2:Cellule) -> float:
    return abs(c1.somme() - c2.somme())

if __name__ == '__main__':

    # Initialisation of data
    # Cellules
    tf = np.empty((3, 3), dtype=Cellule)
    tf[0][0] = Cellule([-38, -27, -54, -13])
    tf[0][1] = Cellule([-74, -62, -48, -33])
    tf[0][2] = Cellule([-13, -28, -12, -40])

    tf[1][0] = Cellule([-34, -27, -38, -41])
    tf[1][1] = Cellule([-64, -48, -72, -35])
    tf[1][2] = Cellule([-45, -37, -20, -15])

    tf[2][0] = Cellule([-17, -50, -44, -33])
    tf[2][1] = Cellule([-27, -28, -32, -45])
    tf[2][2] = Cellule([-30, -20, -60, -40])

    # Mobile terminal
    tm = Cellule([-26, -42, -13, -46])

    # k closest cases [distance, i, j]
    k_cases = np.zeros((9, 3))
    
    # The real position of the device
    real_position = []

    k=0
    # Coordinates of current point
    # Compute all distances
    for i in range(3):
        for j in range(3):
            # Computation of real position
            # i = {0, 2, 4,...} (x2)
            # position about center of the case (-1)
            k_cases[k] = [distance_between_cellules(tf[i][j], tm), 1 if i==0 else i*2-1, 1 if j==0 else j*2-1]

            # If the distance is zero so it's the same position
            if distance_between_cellules(tf[i][j], tm) == 0:

                print("\nThe best case:")
                print(k_cases[k])

                x = 1 if i==0 else i*2-1
                y = 1 if j==0 else j*2-1

                real_position = [x, y]

                print("\nThe real position of the device:")
                print(real_position)

                break
            k=k+1

        if len(real_position) != 0 : break

    if len(real_position) != 0 : sys.exit()
        
    # Sort items according to the distances
    k_cases = k_cases[k_cases[:, 0].argsort()]
    # Get four best
    k_cases = np.delete(k_cases, range(4,9), 0)
    
    print("\nThe best 4 cases:")
    print(k_cases)

    """
    OM = a1*OE1 + a2*OE2 + a3*OE3 + a1*OE4 => xM = a1*xOE1 + a2*xOE2 + ...
    a2 = d1/d2 x a1 ...
    a1 + a2 + a3 + a4 = 1 => a1 + d1/d2*a1 + d1/d3*a3 + d1/d4*a4 = 1
                          => (1 + d1/d2 + d1/d3 + d1/d4) * a1 = 1
                          => a1 = 1 / (1 + d1/d2 + d1/d3 + d1/d4)

    """

    a1 = 1. / (1. + k_cases[0][0]/k_cases[1][0] + k_cases[0][0]/k_cases[2][0] + k_cases[0][0]/k_cases[3][0])
    a2 = k_cases[0][0]/k_cases[1][0] * a1
    a3 = k_cases[0][0]/k_cases[2][0] * a1
    a4 = k_cases[0][0]/k_cases[3][0] * a1

    #print(a1, a2, a3, a4, a1+a2+a3+a4)

    x = a1*k_cases[0][1] + a2*k_cases[1][1] + a1*k_cases[2][1] + a1*k_cases[3][1]
    y = a1*k_cases[0][2] + a2*k_cases[1][2] + a1*k_cases[2][2] + a1*k_cases[3][2]

    real_position = [x, y]

    print("\nThe real position of the device:")
    print(real_position)