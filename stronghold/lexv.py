# Ordering Strings of Varying Length Lexicographically by Rosalind.com
# See https://rosalind.info/problems/lexv/
# Solved July 2020, revised March 2023

import itertools
from typing import List

def lexv(string: str, length: int) -> List[str]:

    string = string.replace(' ', '')

    strings = []
    for i in range(1, length+1):
        strings.extend(list(itertools.product(string, repeat=i)))
    strings = [''.join(s) for s in strings]

    lookup = str.maketrans(string, ''.join(sorted(string)))

    return sorted(strings, key=lambda x: x.translate(lookup))

if __name__ == '__main__':
	import sys

	with open(sys.argv[1]) as file, open('results/result_lexv.txt', 'w') as out:
		string, length = file.readline().rstrip(), int(file.readline().rstrip())
		for x in lexv(string, length):
			out.write(f'{x}\n')
