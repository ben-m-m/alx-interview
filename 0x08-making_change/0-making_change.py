#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize a dict to store minimum number of coins needed for each total
    dp = {}

    # Base case for 0 total
    dp[0] = 0

    for t in range(1, total + 1):
        dp[t] = float('inf')
        for coin in coins:
            if coin <= t:
                dp[t] = min(dp[t], dp[t - coin] + 1)
            else:
                break  # No need to check further if coins exceed currenttotal

    return dp[total] if dp[total] != float('inf') else -1
