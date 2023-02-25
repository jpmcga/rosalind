#!/usr/bin/env python3.8

# Genome Assembly as Shortest Superstring by Rosalind.com
# See https://rosalind.info/problems/long/
# Solved July 2020, revised February 2023

from collections import defaultdict
from typing import List
from utils import fasta_to_dict

def matched_strings(seqs: List[str]) -> List[str]:
    
    matches = defaultdict(str)
    length = len(seqs)
    
    for row in range(length):

        lead = seqs[row]
        mid_p = len(lead)//2
        suffix = lead[mid_p:]

        for col in range(length):
            follow = seqs[col]
            if lead == follow:
                continue
            elif suffix in follow:
                match = follow.find(suffix)
                if follow[:match] == lead[mid_p - len(follow[:match]):mid_p]:
                    matches[lead] = lead + follow[match + len(suffix):]                    

    return list(matches.values())

if __name__ == '__main__':
    import sys

    seqs = list(fasta_to_dict(sys.argv[1]).values())
    attempts = 0
    for x in range(len(seqs) - 1):
        seqs = matched_strings(seqs)
    print(seqs[0])


