# RNA Splicing by Rosalind.com
# See https://rosalind.info/problems/splc/
# Solved June 2020, revised March 2023

from functools import reduce
from typing import List

from utils import fasta_to_list, translate

def splice(premrna: str, introns: List[str]) -> str:
    '''Idea to use "reduce" from Rayan solution'''

    return reduce(lambda x,i: x.replace(i, ''), introns, premrna)

if __name__ == '__main__':
    import sys

    introns = fasta_to_list(sys.argv[1])
    print(translate(splice(introns.pop(0), introns)))