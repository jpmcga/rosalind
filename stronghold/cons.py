# Error Completing a Tree by Rosalind.com
# See https://rosalind.info/problems/tree/
# Solved July 2020, revised February 2023

import pandas as pd
from os import PathLike
from pathlib import Path
from typing import Union

from utils import fasta_to_list

def get_consensus(fasta: Union[str, PathLike]) -> (str, pd.DataFrame):
    '''Return consensus seq and profile matrix (as pandas DataFrame) for fasta.
    '''

    df = (
        pd.DataFrame([list(seq) for seq in fasta_to_list(fasta)])
        .apply(pd.value_counts)
        .fillna(0)
    )

    consensus = "".join(list(df.idxmax()))

    return consensus, df

if __name__ == '__main__':
    import sys

    with open(Path('stronghold/results/result_cons.txt').resolve(), 'w') as f:
        consensus, df = get_consensus(sys.argv[1])
        f.write(consensus)
        for i in df.index:
            f.write(f'{i}: {" ".join([str(int(x)) for x in list(df.xs(i))])}')
            
