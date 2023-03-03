# Calculating Protein Mass by Rosalind.com
# See https://rosalind.info/problems/prtm/
# Solved Sept 2020, revised Oct 2022

from utils import aa_mass_table

def calc_peptide_mass(peptide):

    return sum(aa_mass_table[aa] for aa in peptide)

if __name__ == "__main__":
    import sys
    
    with open(sys.argv[1]) as f:
        print("%.3f" % calc_peptide_mass(f.read().rstrip()))
