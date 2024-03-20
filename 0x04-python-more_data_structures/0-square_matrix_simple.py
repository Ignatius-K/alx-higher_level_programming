def square_matrix_simple(matrix=[]):
    '''square of matrix

    Params:
        matrix: matrix to act on

    Return:
        Return a new matrix
    '''

    return [[number ** 2 for number in matrix_item] for matrix_item in matrix]
