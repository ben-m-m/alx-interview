#!/usr/bin/python3
""" making change"""


def makeChange(coins, total):
    """ make change function"""
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: no coins needed for total of 0

    for i in range(1, total + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)

    if dp[total] == total + 1:
        return -1  # Total cannot be met by any number of coins
    else:
        return dp[total]
