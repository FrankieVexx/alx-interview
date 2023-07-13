#!/usr/bin/python3
'''Minimum operations interview test.
'''


def minOperations(n):
    '''Find fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    count = 0
    copied = 0
    completed = 1
    while completed < n:
        if copied == 0:
            copied = completed
            completed += copied
            count += 2
        elif n - completed > 0 and (n - completed) % completed == 0:
            copied = completed
            completed += copied
            count += 2
        elif copied > 0:
            completed += copied
            count += 1
    return count
