# Solution for Introduction to Alternative Splicing by Rosalind.com
# See https://rosalind.info/problems/aspc/
# Solved June 2023

import math

def sum_combinations(n: int, m: int) -> int:
    """Return the sum of combinations from m to n"""    
    return sum([math.comb(n, k) for k in range(m, n+1)]) % pow(10, 6)

if __name__ == "__main__":
    import sys

    print(sum_combinations(int(sys.argv[1]), int(sys.argv[2])))