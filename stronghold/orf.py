# Solution for Open Reading Frames by Rosalind.com
# See https://rosalind.info/problems/orf/
# Solved Sept 2020, revised March 2023

import re
from typing import List
from utils import fasta_to_list, reverse_comp, transcribe, translate


def get_orfs(seq: str, rc: bool=True) -> List[str]:
    
    if rc:
        seq = '\n'.join([seq, reverse_comp(seq)])
    
    return [match[0] for match in re.findall('(?=(ATG(...)*?(TAG|TAA|TGA)))', seq)]


if __name__ == '__main__':
    import sys
    orfs = get_orfs(fasta_to_list(sys.argv[1])[0])
    for p in {translate(transcribe(orf)) for orf in orfs}:
        print(p)
