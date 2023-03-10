# Solution to Independent Alleles problem from Rosalind.com
# See https://rosalind.info/problems/lia/
# Solved Sept 2022

import math


def binomial(
    trials: int,
    num_success: int,
    p_success: int
) -> int:
    '''
    Return the binomial probability P(X=1) given number of trials, 
    number of successes (X), and the probabilty of sucess.
    '''

    combs = math.comb(trials, num_success)

    return combs * p_success**num_success * (1-p_success)**(trials-num_success)


def cumulative_binomial_gte(
    trials: int,
    num_success: int,
    p_success: int
) -> int:
    '''
    Return the cumulative binomial probability that AT LEAST X success will
    occur P(X>=1) given number of trials, number of successes (X), and the
    probabilty of sucess.
    '''

    cumulative_prb = 0
    for i in range(num_success):
        cumulatiRve_prb += binomial(trials, i, p_success)

    return 1 - cumulative_prb


if __name__ == '__main__':

    offspring = 2**int(input("Enter generation number: "))
    double_hetero = int(input("Enter double hetero number: "))
    print(cumulative_binomial_gte(offspring, double_hetero, p_success=0.25)) 

    