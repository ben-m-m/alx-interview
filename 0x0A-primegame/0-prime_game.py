#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take turns
choosing a prime number from the set and removing that number and
its multiples from the set.
The player that cannot make a move loses the game.
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
        Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
