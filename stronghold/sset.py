# Solution for Counting Subsets by Rosalind.com
# See https://rosalind.info/problems/sset/
# Solved October 5, 2022

import sys

def count_subsets(set_length: int):

	return 2 ** set_length % 1e6


if __name__ == '__main__':

	with open(sys.argv[1]) as i:
		sets = int(i.read().rstrip())
		print(count_subsets(sets))
