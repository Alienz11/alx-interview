#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given
    amount total,from a a pile of coins of different values.
    """

    if total <= 0:
        return 0
    coins_left = total
    coins_count = 0
    coins_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while coins_left > 0:
        if coins_index >= n:
            return -1
        if coins_left - sorted_coins[coins_index] >= 0:
            coins_left -= sorted_coins[coins_index]
            coins_count += 1
        else:
            coins_index += 1
    return coins_count
