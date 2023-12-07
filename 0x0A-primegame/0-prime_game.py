def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def optimal_move(nums):
    for num in reversed(nums):
        if is_prime(num):
            return num
    return None

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_player = "Maria"

        while n > 1:
            move = optimal_move(list(range(1, n + 1)))

            if move is None:
                break

            n -= move

            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"

        if current_player == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

