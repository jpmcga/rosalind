# Solution for Fibonacci Numbers by Rosalind.com
# See https://rosalind.info/problems/fibo/
# Solved December 2022

import math
import sys

def binet(n):

    if type(n) != int:
        try:
            n = int(n)
        except:
            return "Input must be integer."

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        isqrt5 = 1/math.sqrt(5)
        return round(isqrt5*((1+math.sqrt(5))/2)**n - \
            isqrt5*((1-math.sqrt(5))/2)**n)

if __name__ == '__main__':
    print(binet(sys.argv[1]))
    