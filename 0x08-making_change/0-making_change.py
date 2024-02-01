#!/usr/bin/python3
""" making change"""


def makeChange(coins, total):
    """ make change function"""
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: no coins needed for total of 0

    for c in coins:
        for i in range(c, total + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[total] if dp[total] != total + 1 else -1
