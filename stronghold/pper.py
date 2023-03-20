# Solution for Partial Permutations by Rosalind.com
# See https://rosalind.info/problems/pper/
# Solved March 2023

from functools import reduce

def partial_permutations(n: int, k: int) -> int:
    return reduce(lambda x, y: x * y, range(n - k + 1, n + 1)) % 1000000

if __name__ == '__main__':
    
    n = int(input('Input n:'))
    k = int(input('Input k:'))
    print(partial_permutations(n, k))