import sys
from utils import basepair_table

def reverse_complement(seq):
    '''
	Input nucleotide string, return reverse complement.
    '''
    return ''.join([ basepair_table[bp] for bp in seq.upper()[::-1]])


if __name__ == '__main__':
	try:
		print(reverse_complement(open(sys.argv[1]).read().strip()))
	except IndexError:
		print('Add filepath')
