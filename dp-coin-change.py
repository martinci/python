#!/usr/bin/env python3


def make_change(coins, n, memory):
    """
    Computes number of ways to make change.

    Parameters
    ----------
        coins: array
            Available values of coins.
        n: int
            Amount of money to return.
    Returns
    -------
        nways: int
            Number of ways to make chanfe for n.
    """
    ncoins = len(coins)
    if ncoins == 0:
        if n != 0:
            return 0
        return 1
    if (ncoins, n) not in memory:
        max_coin = (n - n % coins[0]) / coins[0]
        max_coin = int(max_coin)
        memory[ncoins, n] = sum([make_change(coins[1:], n - coins[0] * k)
                                 for k in range(max_coin + 1)])
    nways = memory[ncoins, n]
    return nways


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    coins = list(map(int, input().strip().split()))
    memory = {}
    for l in range(m):
        memory[l + 1, 0] = 1
    print(make_change(coins, n, memory))
