# Introduction to Matching Random Motifs by Rosalind.com
# See https://rosalind.info/problems/rstr/
# Solved July 2023

import math

def rstr(N: int, x: float, s: str) -> float:

    return 1 - pow((1 - math.prod([x/2 if i in "GC" else (1 - x)/2 for i in s])), N)

if __name__ == "__main__":
    N = int(input("Enter N: "))
    x = float(input("Enter x (GC%): "))
    s = input("Enter s (string): ")

    print(f"{rstr(N, x, s):.3f}")