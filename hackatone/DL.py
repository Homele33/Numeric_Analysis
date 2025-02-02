import math
import numpy as np
import matplotlib.pyplot as plt
from hackatone.question_13.q131 import q131_root 
from hackatone.question33.lagrange_interpolation import y_interpolate 
from hackatone.question12.simpsonRule import integral
from hackatone.Question5 import secant_root
from hackatone.questions30_27.lu_decomposition import q27_lu_decomposition, q30_lu_decomposition


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
    L5 = round(secant_root * 2000)
    L27 = round(q27_lu_decomposition * 400)
    L30 = round(q30_lu_decomposition * 600)


    list_L = [L13, L33, L12, L5,]
    list_D1 = [first(L13), first(L33), first(L12), first(L5), first(L27), first(L30)]
    list_D2 = [second(L13), second(L33), second(L12), second(L5), second(L27), second(L30)]
    list_D3 = [third(L13), third(L33), third(L12), third(L5), third(L27), third(L30)]
    list_D4 = [fourth(L13), fourth(L33), fourth(L12), fourth(L5), fourth(L27), fourth(L30)]
    list_D5 = [fifth(L13), fifth(L33), fifth(L12), fifth(L5), fifth(L27), fifth(L30)]

