from Bio.Seq import Seq
from collections import defaultdict

# s = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
#l = ['ATCGGTCGAA', 'ATCGGTCGAGCGTGT']

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

seqs = list(fasta_to_dict('../../../Downloads/rosalind_splc.txt').values())
mrna = seqs.pop(0)

for intron in seqs:
	loc = mrna.find(intron)
	mrna = mrna[:loc] + mrna[loc + len(intron):]

mrna = Seq(mrna)
print(mrna.translate(to_stop = True))


