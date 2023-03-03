import re

from collections import defaultdict
from os import PathLike
from typing import List, TextIO, Union

   
def test_nucleotides(string: str):
    '''Check all characters in string are one of A,T,C,G.'''
    assert all(ele.upper() in list('ATCGU') for ele in string),\
                    'Input must be DNA nucleotides'

def transcribe_dna(dna_seq: str) -> str:
    try:
        dna_seq = dna_seq.upper().rstrip()
    except TypeError:
        'Input must be a string'
    test_nucleotides(dna_seq)

    return dna_seq.replace('T', 'U')

def translate(seq: str) -> str:

    seq = seq.upper()
    test_nucleotides(seq)
    
    if 'T' in seq:
        assert 'U' not in seq, 'Input must be either DNA or RNA'
        seq = seq.replace('T', 'U')

    assert len(seq) % 3 == 0, 'Input length must be multiple of 3.'
    assert codon_table[seq[0:3]] == 'M', 'Input must begin with start condon.'
    assert codon_table[seq[-3:]] == 'Stop', 'Input must end with stop codon.'

    return (
        "".join([codon_table[seq[p:p+3]] for p in range(len(seq))[::3]][:-1])
    )

def get_hamming(s1: str, s2: str) -> int:
    assert len(s1) == len(s2), 'Strings must be same length!'
    return sum([1 for pos in range(len(s1)) if s1[pos] != s2[pos]])

def get_gc(seq: str) -> float:
    seq = seq.upper()
    return ((seq.count('G') + seq.count('C')) / len(seq)) * 100

def reverse_comp(dna_seq: str) -> str:
    test_nucleotides(dna_seq)
    return ''.join([basepair_table[bp] for bp in dna_seq.upper()[::-1]])

def parse_fasta(entry: Union[TextIO, List[str]]) -> dict:
    '''Iterate through file or list of each line of a fasta and return
    dict with {id : sequence}.
    '''
    sequences = defaultdict(str)
    for line in entry:
        if line.startswith('>'):
            name = line.strip('>').rstrip()
        else:
            sequences[name] += line.rstrip()
    return sequences

def fasta_to_dict(fasta: Union[str, PathLike]) -> dict:
    '''Passes either a filepath or string to parse_fasta'''
    
    if '>' in fasta:
        return parse_fasta(fasta.split('\n'))    
    elif '.' in fasta:
        with open(fasta) as file:
            return parse_fasta(file)
    return 'Check filepath'

def fasta_to_list(fasta: Union[str, PathLike]) -> List[str]:
    '''Returns list of strings from fasta file.'''

    with open(fasta) as file:
        return [
            seq.replace('\n', '') for seq in re.split('>\w*\\n', file.read())
            if len(seq) > 0
        ]    

basepair_table = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

mendelian_dominance_table = {
    'AA-AA' : 1,
    'AA-Aa' : 1,
    'AA-aa' : 1,
    'Aa-Aa' : 0.75,
    'Aa-aa' : 0.5,
    'aa-aa' : 0
}

codon_table = {
    'UUU' : 'F',
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

aa_mass_table = {
    'A': 71.03711,
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

