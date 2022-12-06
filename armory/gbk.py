from Bio import Entrez
import sys

def esearch_organism_date(
					organism,
					start,
					end, 
					database='nucleotide',
					email='jpaulmcgann@gmail.com'
					):

	Entrez.email = email
	handel = Entrez.esearch(
							db=database,
							term=f'{organism}[Organism] AND ({start}[PDAT] : {end}[PDAT])'
						)
	record  = Entrez.read(handel)

	return record

if __name__ == '__main__':

	filename = sys.argv[1]
	lines = open(filename).read().split("\n")

	record = query_organism_date(lines[0], lines[1], lines[2])
	print(record["Count"])
