# Solution for Counting DNA Nucleotides by Rosalind.com
# See https://rosalind.info/problems/dna/
# Solved May 2020, revised October 2022

import sys

def count_nucleotides(string):
    '''Returns list with nucleotide counts in order A, C, G, T'''

    assert string.isalpha(), "Input must alphabet"

    return [string.upper().count(nuc) for nuc in ['A', 'C', 'G', 'T']]


if __name__ == '__main__':
    with open(sys.argv[1]) as i:
        string = i.read().rstrip()

    res = count_nucleotides(string)
    print(f"{res[0]} {res[1]} {res[2]} {res[3]}")
