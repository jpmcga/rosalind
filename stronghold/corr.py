# Error Correction in Reads by Rosalind.com
# See https://rosalind.info/problems/corr/
# Solved August 2020, revised February 2023

from collections import Counter
from typing import List, Tuple
from utils import fasta_to_dict, get_hamming, reverse_comp

def get_corrections(reads: List[str]) -> Tuple[str,str]:

    counts = Counter(reads) + Counter([reverse_comp(read) for read in reads])
    goods = {item[0] for item in counts.items() if int(item[1]) > 1}
    bads = set(reads) - goods

    result = []
    for bad in bads:
        for good in goods:
            if get_hamming(bad, good) == 1:
                result.append((bad, good))

    return result


if __name__ == '__main__':
    import sys
    result = get_corrections(fasta_to_dict(sys.argv[1]).values())
    with open('./results/result_corr.txt', 'w') as o:
        for correction in result:
            o.write(f'{correction[0]}->{correction[1]}\n')