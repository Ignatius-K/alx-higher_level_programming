#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """Pascal Triangle

    Args:
        n: The number of rows

    Return:
        (list<list>): List of list integers for a Pascal triangle
    """
    tri = []
    if n <= 0:
        return (tri)

    for i in range(n):
        row_number = i + 1
        row = []
        previous_row = tri[i-1] if i > 0 else []
        for j in range(row_number):
            if j == 0 or j == row_number - 1:
                value = 1
            else:
                value = previous_row[j] + previous_row[j - 1]
            row.append(value)
        tri.append(row)

    return (tri)
