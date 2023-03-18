# Transitions and Transversions by Rosalind.com
# See https://rosalind.info/problems/tran/
# Solved March 2023

from collections import Counter

def tran(s1: str, s2: str) -> int:

    cnts = Counter([tuple(sorted((s1[i], s2[i])))
            for i in range(len(s1)) if s1[i] != s2[i]])

    purines = sum([cnts[('A', 'G')], cnts[('C', 'T')]])
    pyrimidines = (sum([cnts[('G', 'T')], cnts[('A', 'T')],
                        cnts[('C', 'G')], cnts[('A', 'C')]]))

    return purines / pyrimidines

if __name__ == '__main__':
    import sys
    from utils import fasta_to_list

    s1, s2 = fasta_to_list(sys.argv[1])
    print(f'{tran(s1, s2):.11f}')
