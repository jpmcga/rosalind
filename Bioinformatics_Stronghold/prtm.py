from utils.utils import aa_mass_table
import sys

def calc_peptide_mass(peptide):
	
	return sum(aa_mass_table[aa] for aa in peptide)

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		print("%.3f" % calc_peptide_mass(f.read().rstrip()))

