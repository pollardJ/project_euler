# This file contains functions that are helpful for solving Project Euler problems.
# It will grow as we get further into the problem sets.

import numpy as np


def is_int(x):
    """Checks if the passed number has a factional component."""
    if x - int(x) != 0:
        return False
    else:
        return True


def palindrome(n):
    """Checks if the passed number is a palidrome."""
    num = n
    r = 0
    while num > 0:
        d = num % 10
        r = r * 10 + d
        num = int(num / 10)
    if r == n:
        return True
    else:
        return False


def seive(n):
    """Returns a list of primes less than n."""
    potentials = {i: True for i in range(2, int(n) + 1)}
    bound = int(np.sqrt(n))
    for i in range(2, bound + 1):
        if potentials[i]:
            for j in range(i ** 2, int(n) + 1, i):
                potentials[j] = False
    primes = [f for f in potentials.keys() if potentials[f]]
    return primes

# EOF
