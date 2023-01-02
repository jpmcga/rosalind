# Solution for Finding a Shared Motif by Rosalind.com
# See https://rosalind.info/problems/lcsm/
# Solved June 2020, revised Jan 2023


def lcsm(strings: list) -> str:
    '''Return longest common substring from list of strings'''

    seed = min(strings, key=len) # Solution can't be longer than shortest string
    longest = '' 
    position, length = 0, 2 # assume longest > 1bp
    seq = seed[position : position + length]

    while seq:
        if all([seq in string for string in strings]) and len(seq) > len(longest):
            longest = seq
            length += 1
        else:
            position += 1
        seq = seed[position : position + length]

    return longest

if __name__ == '__main__':
    import sys
    from utils.utils import fasta_to_dict
    
    strings = fasta_to_dict(sys.argv[1]).values()
    print(lcsm(strings))
