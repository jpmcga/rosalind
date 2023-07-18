# Solution for Expected Number of Restriction Sites by Rosalind.com
# See https://rosalind.info/problems/eval/
# Solved July 2023

import math

def expected(n: int, s: str, pct: float) -> float:
    p = math.prod([pct/2 if c in "GC" else (1 - pct)/2 for c in s]) 
    return  p * (n - (len(s) - 1))

if __name__ == "__main__":
    import sys

    with open(sys.argv[1], "r") as f:
        n, s, array = [line.strip() for line in f.readlines()]
        array = [float(i) for i in array.split()]
        for pct in array:
            print(round(expected(int(n), s, pct), 3), end=" ")