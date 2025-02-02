import numpy as np
import matplotlib.pyplot as plt
from question_13.q131 import main as q13
from question33.lagrange_interpolation import main as q33
from question12.simpsonRule import main as q12
from Question5 import main as q5
from questions30_27.lu_decomposition import main as q27_30




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
    L30, L27 = q27_30()

    L13 = round(q13() * 900)
    L33 = round( q33()* 750)
    L12 = round(q12() * 650)
    L5 = round(q5() * 2000)
    L27 = round(L27 * 400)
    L30 = round(L30* 600)

    list_L = [L12, L30, L13, L33, L27, L5]
    list_D1 = [first(L12), first(L30), first(L13), first(L33), first(L27), first(L5)]
    list_D2 = [second(L12), second(L30), second(L13), second(L33), second(L27), second(L5)]
    list_D3 = [third(L12), third(L30), third(L13), third(L33), third(L27), third(L5)]
    list_D4 = [fourth(L12), fourth(L30), fourth(L13), fourth(L33), fourth(L27), fourth(L5)]
    list_D5 = [fifth(L12), fifth(L30), fifth(L13), fifth(L33), fifth(L27), fifth(L5)]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(list_L, list_D1, marker='o', linestyle='-', label='D1')
    plt.plot(list_L, list_D2, marker='s', linestyle='--', label='D2')
    plt.plot(list_L, list_D3, marker='^', linestyle='-.', label='D3')
    plt.plot(list_L, list_D4, marker='d', linestyle=':', label='D4')
    plt.plot(list_L, list_D5, marker='x', linestyle='-', label='D5')

    # Labels and title
    plt.xlabel("L values")
    plt.ylabel("D values")
    plt.title("Graph of D functions against L")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

