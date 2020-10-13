from collections import defaultdict

def dna_to_rna(string):
    string = string.upper()
    string = string.replace("T", "U")
    
    return string

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
