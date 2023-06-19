# Solution for Enumerating Oriented Gene Orderings by Rosalind.com
# See https://rosalind.info/problems/sign/
# Solved June 2023

import itertools

from scipy.special import factorial
from typing import List

def get_signed_permutations(n: int) -> List[List[int]]:

    perms = list(itertools.permutations(list(range(1, n+1)), n))
    signs =  list(itertools.product([1, -1], repeat=n))

    result = []
    for perm in perms:
        for sign in signs:
            result.append([perm[i] * sign[i] for i in range(len(perm))])
    
    return result

if __name__ == "__main__":
    import sys
    
    n = int(sys.argv[1])

    print(int(factorial(n) * pow(2, n)))
    for signed_perm in get_signed_permutations(n):
        for i in range(len(signed_perm)):
            print(signed_perm[i], end=" ")
        print()