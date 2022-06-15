#!/usr/bin/python3
"""
A prime game
"""


def isWinner(x, nums):
    """
    Gets the winner of a prime game with 'x' amount of rounds.
    """
    players = ('Maria', 'Ben')
    winners = []
    if nums:
        nums_len = len(nums)
    else:
        nums_len = 0

    if nums_len == 0:
        return None

    for i in range(x):
        if nums:
            digit = nums[i % nums_len]
        else:
            digit = 0
        n_nums = list(range(1, digit + 1, 1))
        prime_num = 2
        amt_turns = 0

        while True:
            nums_removed = False
            prime_multiples = list(range(prime_num, digit + 1, prime_num))
            for p in prime_multiples:
                if p in n_nums:
                    n_nums.remove(p)
                    nums_removed = True
            amt_turns += 1
            if nums_removed:
                for j in n_nums:
                    if j > prime_num:
                        prime_num = j
                        break
            else:
                break
        winners.append(players[amt_turns % 2])
    maria_wins = winners.count(players[0])
    ben_wins = winners.count(players[1])

    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return 'Maria'
    else:
        return 'Ben'
