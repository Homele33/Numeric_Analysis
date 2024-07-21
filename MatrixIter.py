import copy
# Assignment by: David Darf, Eden Cohen, Nir Nissim Hazan, Kobi Alen, Matan Kahlon

input_mat = [[2, 1, 0],
             [1, 3, -1],
             [0, 1, 2]]

input_vec = [6, 0, 3]

input_margin = 0.001


def strong_diagonal(mat): # this function checks if the matrix has a strong diagonal, returns true if |arr[i][i]| > sum(|arr[i][j]|)
    for i in range(len(mat)):
        norm = 0
        for j in range(len(mat)):
            if i != j:
                norm += abs(mat[i][j])
        if abs(mat[i][i]) <= norm:
            return False
    return True


def iter_form(mat):  # deconstructs the matrix into diagonal and non diagonal matrixes
    diag_mat = init_diagonal_mat(mat)
    non_diag = copy.deepcopy(mat)
    for i in range(len(mat[0])):
        diag_mat[i][i] = mat[i][i]
        non_diag[i][i] = 0
    return diag_mat, non_diag


def init_diagonal_mat(mat): # initiallize a matrix of the same size
    diag_mat = []
    for i in range(len(mat)):
        diag_mat.append([])
        for j in range(len(mat[0])):
            diag_mat[i].append(0)
    return diag_mat


def init_sol_vector(mat): # initiallize a solution vector of the proper size
    vector = []
    for i in range(len(mat)):
        vector.append(0)
    return vector


def valid_solution(current_guess,next_guess): # checks if the differnce between the current solution and the last solution satisfy the threshold
    for i in range(len(current_guess)):
        if abs(next_guess[i] - current_guess[i]) > input_margin:
            return False
    return True


def jacobian_form(mat, vector): # solves a system of equation in jacobian iterative form
    if not strong_diagonal(mat): # test for strong diagonal
        return "Matrix does not have strong diagonal"

    def calc_next_guess(diagonal, leftover, guess, n_guess):
        for i in range(len(guess)):
            sum_line = sum(leftover[i][j] * guess[j] for j in range(len(guess))) # sums the current line values 
            n_guess[i] = (vector[i] - sum_line) / diagonal[i][i] # updates the next guess 
        print(n_guess)
    return get_solution(mat, calc_next_guess)


def gauss_seidel_form(mat, vector): # solves a system of equation in gauss seidel iterative form
    if not strong_diagonal(mat): # test for strong diagonal
        return "Matrix does not have strong diagonal"

    def calc_next_guess(diagonal, leftover, guess, n_guess):
        for i in range(len(guess)):
            for j in range(len(guess)):
                if i > j:
                    guess[i-1] = n_guess[i-1]
                sum_line = sum(leftover[i][j] * guess[j] for j in range(len(guess)))
                n_guess[i] = (vector[i] - sum_line) / diagonal[i][i]
                break
        print(n_guess)
    return get_solution(mat, calc_next_guess)


def get_solution(mat, calc_next_guess): # calculates the solution for the system, gets a calc_next_guess function that is form specific
    counter = 1
    current_guess = init_sol_vector(mat)
    next_guess = init_sol_vector(mat)
    diag_mat, leftover_mat = iter_form(mat)
    for i in range(len(current_guess)): # initiallize first guess
        current_guess[i] = 0
    calc_next_guess(diag_mat, leftover_mat, current_guess, next_guess)
    while not valid_solution(current_guess, next_guess): # as long as the threshold is not satisfied update the next guess and keep guessing
        counter += 1
        current_guess = next_guess.copy()
        calc_next_guess(diag_mat, leftover_mat, current_guess, next_guess)
    return f'Iteration: {counter}, \tSolution: {next_guess}'


def main():
    print("Matrix = ",input_mat, "\nSolution Vector = ", input_vec)
    print("\nJacobian calculation for linear equation:")
    print(jacobian_form(input_mat, input_vec))
    print("\nGauss seidel calculation for linear equation:")
    print(gauss_seidel_form(input_mat, input_vec))


main()
