import math
import numpy as np
import matplotlib.pyplot as plt
from hackatone.question_13.q131 import q131_root 
from hackatone.question33.lagrange_interpolation import y_interpolate 
from hackatone.question12.simpsonRule import integral


def first(L):
    D=4.86+0.018*L
    return D

def second(L):
    D=L/3000
    return D

def third(L):
    A0= 0.0047
    A1=0.0023
    A2=0.000043
    D=L*(A0+A1*np.log(L)+A2*pow(np.log(L),2))
    return D


def fourth(L):
    exp = 4 / 3
    D=4.2 + 0.0015*pow(L, exp)
    return D


def fifth(L):
    return 0.069 + 0.00156 * L + 0.00000047 * pow(L, 2)



if __name__ == '__main__':
    # Calculate a single L value

    L13 = round(q131_root * 900)
    L33 = round(y_interpolate * 750)
    L12 = round(integral * 650)

