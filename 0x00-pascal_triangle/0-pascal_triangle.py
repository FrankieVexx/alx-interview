#!/usr/bin/python3
"""
printing pascal's triangle
"""


def pascal_triangle(n):
    """
    iterate throuhg rows and print items
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prv_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prv_row[j - 1] + prv_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
