#!/Users/jamesm/opt/anaconda3/bin/python3

# Solution for Data Formats by Rosalind.com
# See https://rosalind.info/problems/frmt/
# Solved Aug 2020, revised Jan 2023

from Bio import Entrez, SeqIO

def shortest_fasta(ids, email = ''):

    Entrez.email = email
    handle = Entrez.efetch(db='nucleotide', id=ids, rettype='fasta')
    shortest = min(list(SeqIO.parse(handle, 'fasta')) , key=len).format('fasta')
    handle.close()

    return shortest


if __name__ == '__main__':
    import sys

    filename = sys.argv[1]
    outname = 'results/result_frmt.txt'
    with open(filename) as input, open(outname, 'w') as out:
        fasta = shortest_fasta(input.read().strip())
        out.write(fasta)