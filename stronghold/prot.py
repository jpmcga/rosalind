# Solution for Translating RNA into Protein by Rosalind.com
# See https://rosalind.info/problems/prot/
# Solved May 2020, revised October 2022

from utils import codon_table

def translate_rna(seq: str) -> str:

    assert len(seq) % 3 == 0, "Input length must be multiple of 3."

    # Check first codon is start, last is stop. 
    assert codon_table[seq[0:3]] == "M" \
        and codon_table[seq[-3:]] == "Stop", "Input must have start/stop codons."

    return (
        "".join([codon_table[seq[p:p+3]] for p in range(len(seq))[::3]][:-1])
    )


if __name__ == '__main__':
    import sys

    with open(sys.argv[1]) as i:
        seq = i.read().rstrip()

    print(translate_rna(seq)) 