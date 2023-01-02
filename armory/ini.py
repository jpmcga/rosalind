# Solution for Introduction to the Bioinformatics Armory by Rosalind.com
# See https://rosalind.info/problems/ini/
# Solved July 2020, revised Jan 2023

def count_nucleotides(sequence: str) -> list:
	'''Return list with counts of A,C,G,T, respectively'''

	return [sequence.upper().count(nuc) for nuc in list('ACGT')]

if __name__ == "__main__":
	a, c, g, t = count_nucleotides(input("Enter DNA sequence: "))
	print(f"{a} {c} {g} {t}")

