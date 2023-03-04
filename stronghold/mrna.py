# Solution for Inferring mRNA from Protein by Rosalind.com
# See https://rosalind.info/problems/mrna/
# Solved Sept 2020, revised March 2023

from utils import codon_table
from collections import Counter
from functools import reduce

def gene_combinations(protein: str) -> str:    
    counts = Counter(codon_table.values())
    return reduce(lambda a,b: a*b, [counts[aa] for aa in protein]) * 3 % 1000000

if __name__ == '__main__':
    import sys
    print(gene_combinations(open(sys.argv[1]).read().rstrip()))