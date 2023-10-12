#!/usr/bin/env python3
"""
Returns an integer
"""


def minOperations(n):
    """
    minimum operations
    """
    if n <= 1:
        return 0

    count = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            count += divisor
            n = n // divisor
        divisor += 1

    return count
