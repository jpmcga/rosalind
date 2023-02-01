#!/usr/bin/env python3.8

# Solution for Finding a Protein Motif by Rosalind.com
# See https://rosalind.info/problems/mprt/
# Solved June 2020, revised January 2023

import re
from urllib.request import urlopen
from urllib.error import HTTPError
from typing import List, Pattern


def uniport_to_sequence(uniport_id: str) -> str:
    '''Given a uniprot ID, returns tuple (id, sequence); attempts with given
    ID, if 404 error, tries first string in ID ie. x in x_y_z.
    '''
    url = f'http://www.uniprot.org/uniprot/uniprot_id.fasta'
    try:
        # From Laperche Sylvain solution
        responce = urlopen(url.replace('uniprot_id', uniport_id)) 
    except HTTPError:
        uniport_id = uniport_id.split('_')[0]
        responce = urlopen(url.replace('uniprot_id', uniport_id))
        
    seq = ''.join(responce.read().decode('utf-8').split('\n')[1:])
    
    return seq


def find_motif(
    uniport_id: str,
    sequence: str,
    motif: Pattern
) -> List[int]:
    '''Given an id, a sequence as a string, and compiled regex expression,
    returns list of 1-indexed match start positions.  To capute overlapping 
    matches, use regex 'lookahead' (see https://stackoverflow.com/questions/5616822).
    '''

    positions = []
    for match in re.finditer(motif, sequence):
        positions.append(match.start() + 1)
    
    return positions


if __name__ == '__main__':
    import sys

    motif = re.compile(r'(?=(N[^P][ST][^P]))')

    with open(sys.argv[1]) as file:
        ids = [line.rstrip() for line in file.readlines()]

    for id in ids:
        positions = find_motif(id, uniport_to_sequence(id), motif)
        if len(positions) > 0:
            print(id)
            print(*positions, sep=' ') # From Laperche Sylvain solution

