# Solution for k-Mer Composition by Rosalind.com
# See https://rosalind.info/problems/kmer/
# Solved Sept 2020, revised March 2023

import re

from itertools import product
from typing import List

def get_kmers(seq: str, k: int) -> List[int]:
    '''Return counts of all kmers in seq, listed lexographicly.
    Probably faster with collections.Counter, but used regex.
    '''

    return [
    len(re.findall(f'(?=({s}))', seq))
    for s in sorted([''.join(s) for s in list(product('ATCG', repeat=4))])
]

if __name__ == '__main__':
    import sys
    from utils import fasta_to_list

    for count in get_kmers(fasta_to_list(sys.argv[1])[0], 4):
        print(count, end=' ')
