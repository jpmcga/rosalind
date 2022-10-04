# Solution for Generate the k-mer Composition of a String by Rosalind.com
# See https://rosalind.info/problems/ba3a/
# Solved July 2020, revised October 2022

import sys

def get_kmer(string: str, kmer, alpha=True):
    '''Return a list of all substrings (kmers) in string of lenght kmer, from the beginning
    of the string until length(string) - k.  If sorted = true, returns the substrings in
    lexicographic order'''

    res = [string[pos:pos + kmer] for pos in range(len(string) - kmer + 1)]
    if alpha == True:
        return sorted(res)
    return res


if __name__ == '__main__':

    with open(sys.argv[1]) as i:        
        kmer = int(i.readline().rstrip())
        string = i.readline().rstrip()

    with open('solutions/solution_ba3a.txt', 'w') as o:
        for item in get_kmer(string, kmer):
            o.write(f'{item}\n')
