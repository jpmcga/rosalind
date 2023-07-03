# Introduction to Random Strings by Rosalind.com
# See https://rosalind.info/problems/prob/
# Solved March 2023

import numpy as np
from typing import List

def get_gclookup(pct_gc: float) -> dict:
    
    return {
       'A' : (1 - pct_gc) / 2,
       'T' : (1 - pct_gc) / 2,
       'C' : pct_gc / 2,
       'G' : pct_gc / 2
    }

def prob_gc(seq: str, lookup: List[float]) -> float:

    return np.log10(np.prod([lookup[x] for x in seq]))

if __name__ == '__main__':
    import sys

    with open(sys.argv[1]) as file:
        seq, pcts = file.readline().rstrip(), file.readline().split()

        for pct in pcts:
            result = prob_gc(seq, get_gclookup(float(pct)))
            print(f'{result:.3f}', end=' ')
        print()