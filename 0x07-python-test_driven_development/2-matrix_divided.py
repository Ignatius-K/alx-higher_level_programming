#!/usr/bin/python3

"""Matrix manipulation"""


def matrix_divided(matrix, div):
    """Divide matrix

    Args:
        matrix (list<list<int>>): The matrix to Divide
        div (int): The divisor

    Return:
        updated matrix

    Raises:
        TypeError: If matrix does not pass validation
        TypeError: If divisor does not pass validation
    """
    validate_matrix(matrix)
    validate_divisor(div)
    divided_matrix = []
    for row_index, row in enumerate(matrix):
        divided_matrix.append([])
        for element_index, element in enumerate(row):
            dividend = element / div
            divided_matrix[row_index].append(float(format(dividend, ".2f")))
    return (divided_matrix)


def validate_matrix(matrix):
    """Validate matrix

        Note: Checks if matrix is list,
            its elements are lists with same length

    Args:
        matrix (list<list<int>>): The matrix to validate
    """
    matrix_message = ("matrix must be a matrix "
                      "(list of lists) of integers/floats"
                      )
    row_message = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list):
        raise TypeError(matrix_message)
    temp_row_length = set()
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_message)
        temp_row_length.add(int(len(row)))
        for element in row:
            try:
                validate_number(element)
            except TypeError:
                raise TypeError(matrix_message)
    if len(temp_row_length) > 1:
        raise TypeError(row_message)


def validate_divisor(divisor):
    """Validate divisor

    Args:
        divisor (int): The divisor
    """
    validate_number(divisor)
    if divisor == 0:
        raise ZeroDivisionError("division by zero")


def validate_number(number):
    """Validate a number

    Args:
        number (int | float): The number to validate
    """
    if not (isinstance(number, int) or isinstance(number, float)):
        raise TypeError("div must be a number")
    int(number)  # HACK: Test if not NaN
