#!/usr/bin/env python3
def climb_staircase(size, memory={0: 0, 1: 1, 2: 2, 3: 4}):
    """
    Compute the number of ways to climb a staircase.

    Parameters
    ----------
        size: int
            Number of steps in the staircase
    Returns
    -------
        nways: int
            Total number of ways to climb the staircase.
    """
    if size not in memory:
        # we can take 1, 2 or 3 steps and face the same problem with a smaller size.
        memory[size] = climb_staircase(
            size - 1) + climb_staircase(size - 2) + climb_staircase(size - 3)
    nways = memory[size]
    return nways


if __name__ == '__main__':
    # input from console
    # total number of staircases
    s = int(input())
    for _ in range(s):
        # size of each staircase
        size = int(input())
        print(climb_staircase(size))
