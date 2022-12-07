# Solution for Binary Search by Rosalind.com
# See https://rosalind.info/problems/bins/
# Solved with cheating Dec 2022, to be revised

import sys

def search_index(array, values):

    postitions = []
    for val in values:
        try:
            postitions.append(array.index(str(val)) + 1)
        except ValueError:
            postitions.append(-1)

    return postitions

if __name__ == '__main__':

    in_name = f"/Users/jamesmcgann/Downloads/{sys.argv[1]}"
    out_name = "./results/result_bins.txt"

    with open(in_name) as i_handle, open(out_name, 'w') as o_handle:
        array, values = [x.rstrip().split(' ') for x in i_handle.readlines()[-2:]]
        res = ''
        for pos in search_index(array, values):
            res += f'{pos} '
        o_handle.write(res)
