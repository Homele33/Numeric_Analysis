import math
import numpy as np


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
    L = 1.385360544*900
    print(f"First model: D = {first(L)}")
    print(f"Second model: D = {second(L)}")
    print(f"Third model: D = {third(L)}")
    print(f"Fourth model: D = {fourth(L)}")
    print(f"Fifth model: D = {fifth(L)}")