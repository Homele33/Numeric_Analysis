#Kobi Alen - 318550985
#Matan Kahlon - 316550458
#Een Cohen - 318351004
#
import numpy as np
def linearEquation(pt1,pt2,xf):
    one=float(pt1[1]-pt2[1])
    two=float(pt1[0]-pt2[0])
    three=float(pt2[1]*pt1[0]-pt1[1]*pt2[0])
    four=float(pt1[0]-pt2[0])
    result=(xf*(one/two))+(three/four)
    return result

def linearInter(tuplesList,x):
    left=(-10000000000,0)
    right=(10000000000,0)
    for tuple in tuplesList[1:]:
        if(left[0]<tuple[0]<x):
            left=tuple
        if(right[0]>tuple[0]>x):
            right=tuple
    return linearEquation(right,left,x)

def polynomialInter(vectorX,x):
    fx=vectorX[0]+vectorX[1]*x+vectorX[2]*(x**2)
    return fx

def vectorX(pl):
    matrix=np.array([[1,pl[0][0],pl[0][0]**2],
                     [1,pl[1][0],pl[1][0]**2],
                     [1,pl[2][0],pl[2][0]**2]])
    
    vecB=np.array([pl[0][1], pl[1][1], pl[2][1]])
    solution = np.linalg.solve(matrix, vecB)
    return solution

def lagrange_interpolation(x_values, y_values):
    def L(i, x):
        result = 1
        for j in range(len(x_values)):
            if j != i:
                result *= (x - x_values[j]) / (x_values[i] - x_values[j])
        return result
    
    def P(x):
        result = 0
        for i in range(len(x_values)):
            result += y_values[i] * L(i, x)
        return result
    
    return P

def main():
    while (True):
        option=int(input("Choose the option you want: \n1. Linear Interpolation\n2. Polynomial Interpolation\n3. Lagrange Interpolation\n4. Exit\n"))
        match option:
            case 1:
                pointList1=[(0,0),(1,0.8415),(2,0.9093),(3,0.1411),(4,-0.7568),(5,-0.9589),(6,-0.2794)]
                x1=2.5
                print("Y: %.4f" % linearInter(pointList1,x1),f" Estimate for {x1}\n")
            case 2:
                x2=2.5
                pointList2=[(1,0.8415),(2,0.9093),(3,0.1411)]
                print("Y: %.4f"%polynomialInter(vectorX(pointList2),x2),f" Estimate for {x2}\n") 
            case 3:
                x_values = [1, 2, 4]
                y_values = [1, 0, 1.5]
                x3 = 3
                interpolating_polynomial = lagrange_interpolation(x_values, y_values)
                print(f"P({x3}) = {interpolating_polynomial(x3):.4f} Estimate for {x3}\n")
            case 4:
                break


if __name__ == "__main__":
    main()