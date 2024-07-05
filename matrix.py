import copy
# Eden Cohen
# David Darf
# Nir Hazan
size = 3
I = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

input_mat = [[1, -1, -2],
             [2, -3, -5],
             [-1, 3, 5]]


def mat_mult(mat_a, mat_b):  # matrix multiplication function, returns result of mat_a*mat_b
    res = []
    for i in range(len(mat_a)):  # init result array
        res.append([])
        for j in range(len(mat_b[0])):
            res[i].append(0)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                res[i][j] += mat_a[i][k] * mat_b[k][j]
    return res


def get_inverse():  # returns inverse function
    inverse = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]]

    def prep_lead(elem, mat, index):  # making the pivot digit 1 for simpler row operations
        nonlocal inverse
        try:
            coeff = 1/mat[index][index]
        except ZeroDivisionError:
            print("Given matrix does not have an inverse")
            return 0
        elem[index][index] *= coeff
        inverse = mat_mult(elem, inverse)
        return mat_mult(elem, mat)

    def reduce_column(elem, mat, index):  # reducing by column to echelon form
        nonlocal inverse
        for i in range(len(mat)):  # if the leading variable belongs to the current row, continue to next row
            if i == index:
                continue
            coeff = -mat[i][index]
            elem[i][index] = coeff  # updating the coefficient to elementary matrix
            mat = mat_mult(elem, mat)
            inverse = mat_mult(elem, inverse)
            elem[i][index] = 0
        return mat

    def reduce_matrix(elem, mat):  # reducing the matrix by columns, returns the inverse
        for i in range(len(mat)):
            ret_val = prep_lead(copy.deepcopy(elem), mat, i)  # normalizing the leading variable
            if ret_val == 0:  # returns 0 if matrix does not have an inverse
                return 0
            mat = ret_val
            mat = reduce_column(elem, mat, i)  # reducing column of leading variable
        return inverse

    return reduce_matrix(I, input_mat)  # returns a call to reduce matrix with input matrix and I


def get_norm(mat):  # returns the norm of the matrix
    norm = 0
    for i in range(len(mat)):
        temp = 0  # holds the value of the current row norm
        for j in range(len(mat)):
            temp += abs(mat[i][j])
        norm = max(norm, temp)  # updates norm every time a bigger one is calculated
    return norm


def main():
    inverse = get_inverse()  # A^-1
    mat_norm = get_norm(input_mat)  # ||A||
    inverse_norm = get_norm(inverse)  # ||A^-1||
    print(mat_norm * inverse_norm)  # prints ||A|| * ||A^-1||