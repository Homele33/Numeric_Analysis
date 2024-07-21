import copy
# Assignment by: David Darf, Eden Cohen, Nir Nissim Hazan, Kobi Alen, Matan Kahlon

size = 3
I = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

input_mat = [[1, -1, -2],
             [2, -3, -5],
             [-1, 3, 5]]

input_vector = [1, 2, 3]


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


def get_inverse(mat):  # returns inverse function
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

    return reduce_matrix(I, mat)  # returns a call to reduce matrix with input matrix and I


def get_norm(mat):  # returns the norm of the matrix
    norm = 0
    for i in range(len(mat)):
        temp = 0  # holds the value of the current row norm
        for j in range(len(mat)):
            temp += abs(mat[i][j])
        norm = max(norm, temp)  # updates norm every time a bigger one is calculated
    return norm


def lu_decomposition(): # decomposes the input matrix into a LU form
    length = len(input_mat[0])
    lower = I.copy()
    upper = input_mat.copy()
    for j in range(length):
        for i in range(j + 1, length):
            lower[i][j] = upper[i][j] / upper[j][j]
            for k in range(j, length):
                upper[i][k] -= lower[i][j] * upper[j][k]

    return lower, upper


def forward_substitution(lower, b): # solves for variables from the top row to the bottom.
    result = init_sol_vector(lower) # initiallize solution vector
    for i in range(len(result)):
        sum_y = 0
        for j in range(i):
            sum_y += lower[i][j] * result[j]
        result[i] = b[i] - sum_y
    return result


def backward_substitution(upper, y): # solves for variables sequentially from the bottom row to the top.
    result = init_sol_vector(upper)# initiallize solution vector
    for i in range(len(result)-1, -1, -1): 
        sum_x = 0.0
        for j in range(i+1, len(result)):
            sum_x += upper[i][j] * result[j]
        result[i] = (y[i] - sum_x) / upper[i][i]
    return result


def solve_lu_decomposition(lower, upper, b): # returns the system of equations result
    v = forward_substitution(lower, b)
    result = backward_substitution(upper, v)
    return result


def init_sol_vector(mat): 
    vector = []
    for i in range(len(mat)):  # init result array
        vector.append(0)
    return vector


def main():
    print("\nInput matrix:")
    print(input_mat)
    inverse = get_inverse(input_mat)  # A^-1
    print("Inverse matrix:")
    print(inverse)
    lower, upper = lu_decomposition()
    print("\nMatrix:")
    print(input_mat)
    print("Vector:",)
    print(input_vector)
    solution = solve_lu_decomposition(lower, upper, input_vector)
    print("Solution vector:")
    print(solution)


main()
