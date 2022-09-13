from collections import defaultdict


basepair_table = {'A': 'T',
               'T': 'A',
               'C': 'G',
               'G': 'C'
               }

mendelian_dominance_table = {'AA-AA' : 1,
                        'AA-Aa' : 1,
                        'AA-aa' : 1,
                        'Aa-Aa' : 0.75,
                        'Aa-aa' : 0.5,
                        'aa-aa' : 0
}
   
def dna_to_rna(string):
    string = string.upper()
    string = string.replace("T", "U")
    
    return string

def reverse_comp(string):
    
    string = string.upper()
    
    dct = {'A': 'T',
           'T': 'A',
           'C': 'G',
           'G': 'C'}
    
    new_string = ""
    for char in string[::-1]:
        new_string = new_string + dct[char]
    
    return new_string

def fasta_to_dict(filename):

    file = open(f"{filename}")

    # Get dict from fasta
    sequences = defaultdict(str)

    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            name = line.strip('>')
        else:
            sequences[name] = sequences[name] + line
    
    return sequences

codon_table = {'UUU' : 'F',
        'UUC' : 'F',
        'UUA' : 'L',
        'UUG' : 'L',
        'UCU' : 'S',
        'UCC' : 'S',
        'UCA' : 'S',
        'UCG' : 'S',
        'UAU' : 'Y',
        'UAC' : 'Y',
        'UAA' : 'Stop',
        'UAG' : 'Stop',
        'UGU' : 'C',
        'UGC' : 'C',
        'UGA' : 'Stop',
        'UGG' : 'W',
        'CUU' : 'L',
        'CUC' : 'L',
        'CUA' : 'L',
        'CUG' : 'L',
        'CCU' : 'P',
        'CCC' : 'P',
        'CCA' : 'P',
        'CCG' : 'P',
        'CAU' : 'H',
        'CAC' : 'H',
        'CAA' : 'Q',
        'CAG' : 'Q',
        'CGU' : 'R',
        'CGC' : 'R',
        'CGA' : 'R',
        'CGG' : 'R',
        'AUU' : 'I',
        'AUC' : 'I',
        'AUA' : 'I',
        'AUG' : 'M',
        'ACU' : 'T',
        'ACC' : 'T',
        'ACA' : 'T',
        'ACG' : 'T',
        'AAU' : 'N',
        'AAC' : 'N',
        'AAA' : 'K',
        'AAG' : 'K',
        'AGU' : 'S',
        'AGC' : 'S',
        'AGA' : 'R',
        'AGG' : 'R',
        'GUU' : 'V',
        'GUC' : 'V',
        'GUA' : 'V',
        'GUG' : 'V',
        'GCU' : 'A',
        'GCC' : 'A',
        'GCA' : 'A',
        'GCG' : 'A',
        'GAU' : 'D',
        'GAC' : 'D',
        'GAA' : 'E',
        'GAG' : 'E',
        'GGU' : 'G',
        'GGC' : 'G',
        'GGA' : 'G',
        'GGG' : 'G'
        }

aa_mass_table = {'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
        }
