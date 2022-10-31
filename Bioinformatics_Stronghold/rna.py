# Solution for Transcribing DNA into RNA by Rosalind.com
# See https://rosalind.info/problems/rna/
# Solved June 2020, revised October 2022

import sys

def transcribe_dna(dna_seq: str):
    try:
        dna_seq = dna_seq.upper().rstrip()
    except TypeError:
        "Input must be a string"
    assert all(ele in list("ATCG") for ele in dna_seq),\
                    "Input must be DNA nucleotides"

    return dna_seq.replace("T", "U")

def main():
    if len(sys.argv) > 1:
        print(transcribe_dna(open(sys.argv[1]).read()))
    else:
        print("Please supply input file path.")


if __name__ == '__main__':
    main()