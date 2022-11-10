# Solution for Creating a Distance Matrix by Rosalind.com
# See https://rosalind.info/problems/pdst/
# Solved July 2020, revised November 2022

import itertools as it
from utils.utils import fasta_to_dict, get_hamming

def pairwise_pdistance(lst: list):
    '''Returns list of p-distences for every combination of list of strings'''

    return [get_hamming(s1, s2)/len(lst[0]) for s1, s2 in it.product(lst, repeat=2)]

def main():
    import sys

    if len(sys.argv) > 1:
        seqs = list(fasta_to_dict(sys.argv[1]).values())    
        size = len(seqs)
        res = pairwise_pdistance(seqs)

        for i in range(len(res))[::size]:
            print(" ".join([f"{v:.5f}" for v in res[i:i+size]]))
    else:
        print("Please supply input file path.")

if __name__ == '__main__':
    main()


