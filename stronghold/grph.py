#!/usr/bin/env python3.8

# Solution for Overlap Graphs by Rosalind.com
# See https://rosalind.info/problems/grph/
# Solved June 2020, revised January 2023

from collections import defaultdict
from typing import List, Tuple

from utils import fasta_to_dict


def get_overlaping_seqs(
    filepath: str,
    k: int=3
) -> List[Tuple[str,str]]:
    '''Given a fasta file with multiple sequences, returns a list of all pairs
    of sequences with k overlapping bases.
    '''

    seq_dict = fasta_to_dict(filepath)
    prefix_dict = defaultdict(list)
    [prefix_dict[seq[:k]].append(id) for id, seq in seq_dict.items()]
    
    return [
        (p_id, s_id) for p_id, seq in seq_dict.items()
        for s_id in prefix_dict[seq[-k:]]
    ]

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file',
        '-f',
        required=True,
        dest='file'
    )
    parser.add_argument(
        '--out',
        '-o',
        dest='out',
        default='results/result_grph.txt'
    )
    parser.add_argument(
        '--kmer',
        '-k',
        dest='k',
        default=3
    )

    args = parser.parse_args()

    with open(args.out, 'w') as out:
        for pair in get_overlaping_seqs(args.file, args.k)
            out.write(f'{pair[0]} {pair[1]}\n') 
