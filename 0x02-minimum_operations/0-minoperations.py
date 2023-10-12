#!/usr/bin/env python3
"""
Returns an integer
"""


def minOperations(n):
    """
    minimum operations
    """
    if n < 2:
        return 0

    count = 0
    opr = 2

    while n > 1:
        if not n % opr:
            n //= opr
            count += opr

        else:
            if opr == 2:
                opr += 1
            else:
                opr += 2

    return count
