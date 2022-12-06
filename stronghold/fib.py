# Solution to Rabbits and Recurrence Relations problem from Rosalind.com
# See https://rosalind.info/problems/fib/
# First solved June 2020, revised Sept 2022

def calc_rabbit_pop(generations, litter_size):
    """
    Calculate for F_n = F_n-1 + k*F_n-2 where n is generations
    and k it number of offspring produced by a mating pair.
    """

    total, mating = 1, 1 
    for i in range(generations-2): # starting with 2nd generation
        mating, total = total, mating*litter_size + total
    return total