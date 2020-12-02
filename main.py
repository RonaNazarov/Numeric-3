import numpy


def get_eqs():
    print("Please enter the number of equations you would like to enter:")
    num_eqs = int(input())
    matrix = []
    for i in range(1, num_eqs + 1):
        print("Please enter the factors of equation number " + str(i) + ":")
        eq = []
        for j in range(1, num_eqs + 1):
            print("Please enter the factor of the " + str(j) + " element:")
            eq.append(float(input()))
        matrix.append(eq)

    return matrix


def get_b_vector(matrix):
    rows = len(matrix)
    b = []
    for i in range(1, rows + 1):
        print("Please enter for what equation number " + str(i) + " = :")
        b.append(float(input()))
    return b


def matrix_has_dominant_diagonal(matrix):
    rows_cols = len(matrix)
    for i in range(0, rows_cols):
        par_in_diagonal = abs(matrix[i][i])  # The parameter in row i that's in the diagonal
        sum_row_without_par = 0
        for j in range(0, rows_cols):
            if i != j:
                sum_row_without_par += abs(matrix[i][j])
        if sum_row_without_par > par_in_diagonal:
            return False
    return True


def jacobs_method(A, b, max_iterations):
    if not matrix_has_dominant_diagonal(A):
        print("The matrix diagonal is not dominant")
        return

    epsilon = 0.001
    x = prev_x = numpy.zeros(len(A))
    for i in range(0, max_iterations):
        for j in range(0, len(A)):
            sum_row = b[j]
            for k in range(0, len(A)):
                if j != k:
                    sum_row -= A[j][k] * prev_x[k]
            x[j] = sum_row / A[j][j]
        if x[0] - prev_x[0] < epsilon:
            return x
    return x


def gauss_method(A, b, max_iterations):
    if not matrix_has_dominant_diagonal(A):
        print("The matrix diagonal is not dominant")
        return

    epsilon = 0.001
    x = prev_x = numpy.zeros(len(A))
    for i in range(0, max_iterations):
        for j in range(0, len(A)):
            sum_row = b[j]
            for k in range(0, len(A)):
                if j != k:
                    sum_row -= A[j][k] * x[k]
            prev_x[x] = x[j]
            x[j] = sum_row / A[j][j]
        if x[0] - prev_x[0] < epsilon:
            return x
    return x


A = get_eqs()
b = get_b_vector()
print(jacobs_method(A, b, 20))
print(gauss_method(A, b, 20))