import numpy as np

mat_30 = [[1, 2, -2],
             [1, 1, 1],
             [2, 2, 1]]

vector_30 = [7, 2, 5]

mat_27 = [[-1, 3, 1],
             [4, 1, -1],
             [2, 2, 5]]

vector_27 = [-4, 5, 1]


def gaussian_elimination(A, b):
    """
    Perform Gaussian Elimination to solve a system of linear equations.
    """
    N = len(A)
    augmented_matrix = [A[i] + [b[i]] for i in range(N)]
    singular_flag = forward_substitution(augmented_matrix)
    if singular_flag != -1:
        return handle_singular_matrix(augmented_matrix, singular_flag)

    return backward_substitution(augmented_matrix)


def handle_singular_matrix(mat, singular_flag):
    """
    Handle cases where the matrix is singular.
    """
    N = len(mat)
    if mat[singular_flag][N]:
        return "Singular Matrix (Inconsistent System)"
    else:
        return "Singular Matrix (May have infinitely many solutions)"


def swap_rows(mat, i, j):
    """
    Swap rows i and j in the matrix.
    """
    mat[i], mat[j] = mat[j], mat[i]


def forward_substitution(mat):
    """
    Perform forward substitution to reduce the matrix to upper triangular form.
    Returns the index of the row where the matrix is singular, or -1 if the matrix is non-singular.
    """
    N = len(mat)
    for k in range(N):
        pivot_row = find_pivot_row(mat, k)
        if mat[pivot_row][k] == 0:
            return k  # Matrix is singular

        if pivot_row != k:
            swap_rows(mat, k, pivot_row)

        eliminate_column(mat, k)

    return -1


def find_pivot_row(mat, k):
    """
    Find the row with the largest pivot in column k.
    """
    N = len(mat)
    pivot_row = k
    for i in range(k + 1, N):
        if abs(mat[i][k]) > abs(mat[pivot_row][k]):
            pivot_row = i
    return pivot_row


def eliminate_column(mat, k):
    """
    Eliminate the elements in column k below the diagonal.
    """
    N = len(mat)
    for i in range(k + 1, N):
        multiplier = mat[i][k] / mat[k][k]
        for j in range(k + 1, N + 1):
            mat[i][j] -= mat[k][j] * multiplier
        mat[i][k] = 0


def backward_substitution(mat):
    """
    Perform backward substitution to solve for the unknowns.
    """
    N = len(mat)
    x = np.zeros(N)

    for i in range(N - 1, -1, -1):
        x[i] = mat[i][N]
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]
        x[i] /= mat[i][i]

    return x.tolist()


def get_val():
    solution27 = gaussian_elimination(mat_27, vector_27)
    solution30 = gaussian_elimination(mat_30, vector_30)
    print("Solution 27:")
    print(solution27)
    print("Solution 30:")
    print(solution30[1])


get_val()