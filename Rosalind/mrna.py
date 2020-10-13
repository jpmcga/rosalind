from utils import codon_table
import sys

def count_dict_values(d):
	'''
	Takes a dict; returns a dict where each key is a value from input
	dict and each value is a count of the original values.
	'''

	count_d = {}
	for v in d.values():
		if v not in count_d:
			count_d[v] = 1
		else:
			count_d[v] += 1

	return count_d


def protein_to_rna_mod(protein, n):

	codon_counts = count_dict_values(codon_table)

	product = 1
	for char in protein:
		product *= codon_counts[char]

	return product * 3 % n


def main():
	protein = open(sys.argv[1]).read().strip()
	print(protein_to_rna_mod(protein, int(sys.argv[2])))


if __name__ == '__main__':
	main()
	