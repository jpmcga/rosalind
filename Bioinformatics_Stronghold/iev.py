#!/usr/bin/env python3.8

from utils.utils import mendelian_dominance_table as mdt


def calc_dominant_offspring(mating_pairs, offspring=2):
    '''Given a space-delimited list of number of mating pairs for each of the 
    six Mendelian pairs in order (AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa),
    return expected number of offspring displaying the dominant phenotype.
    ''' 

    if len(mating_pairs) != 6:
        raise ValueError("Enter mating pairs as list in order 'AA-AA, AA-Aa, \
        AA-aa, Aa-Aa, Aa-aa, aa-aa")

    mp_dom_prob = dict(zip(sorted(mdt), mating_pairs))
    ratio_dominant = sum([mdt[i]*mp_dom_prob[i] for i in mp_dom_prob])

    return ratio_dominant * offspring


if __name__ == '__main__':

    mating_pairs = input('Input mating pair values: ').split()
    mating_pairs = [int(i) for i in mating_pairs]
    
    print(calc_dominant_offspring(mating_pairs))

