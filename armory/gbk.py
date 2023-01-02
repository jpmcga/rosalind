# Solution for GenBank Introduction by Rosalind.com
# See https://rosalind.info/problems/gbk/
# Solved Aug 2020, revised Jan 2023

from Bio import Entrez

def esearch_organism_date(
                        organism,
                        start,
                        end,
                        email = 'jpaulmcgann@gmail.com',
                        database='nucleotide',
                        ):

    Entrez.email = email
    handle = Entrez.esearch(
                    db=database,
                    term=f'{organism}[Organism] AND ({start}[PDAT] : {end}[PDAT])'
                    )

    return Entrez.read(handle)

if __name__ == '__main__':
    import sys

    with open(sys.argv[1]) as file:
        organism, start, end = file.read().rstrip().split("\n")

    record = esearch_organism_date(organism, start, end)
    print(record["Count"])
