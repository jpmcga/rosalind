from utils import aa_mass_table
import sys

def calc_peptide_mass(peptide):
	
	return sum(aa_mass_table[aa] for aa in peptide)

if __name__ == "__main__":
	file_name = sys.argv[1]
	peptide = open(file_name).read().rstrip()
	print("%.3f" % calc_peptide_mass(peptide))
