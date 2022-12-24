# Solution for Computing GC Content by Rosalind.com
# See https://rosalind.info/problems/gc/
# Solved June 2020, revised December 2022

from utils.utils import get_gc

def highest_gc(sequences: dict) -> tuple:
    '''Returns name and gc content of sequence with highest gc.'''

    winner, percent = '', 0.0
    for item in sequences.items():
        name, seq = item[0], item[1]
        gc = get_gc(seq)
        if gc > percent:
            winner, percent = name, gc
    
    return winner, percent

if __name__ == '__main__':
	import sys
	from utils.utils import fasta_to_dict

	winner, percent = highest_gc(fasta_to_dict(sys.argv[1]))
	print(winner); print(f'{percent:.2f}')