# Solution for Mortal Fibonacci Rabbits by Rosalind.com
# See https://rosalind.info/problems/fibd/
# Solved December 2022

import sys

def mortal_rabbits(n, m):

    if n <= 0:
        raise ValueError("Gt 1 month please")
    elif n == 1:
        return 1

    gens = [1] + [0] * (m-1) # Init first generation with 1,0,0

    for i in range(n-1):
        cp = [0]*m # Make a copy array
        cp[0] = sum(gens[1:]) # New equals sum of mature
        for i in range(m-1): 
            cp[i+1] = gens[i] # Shift all generations up 
        gens = cp # Set initial array to new array
    
    return sum(gens)

if __name__ == '__main__':
    print(mortal_rabbits(int(sys.argv[1]), int(sys.argv[2])))