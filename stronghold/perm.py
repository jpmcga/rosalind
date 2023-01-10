# Solution for Enumerating Gene Orders by Rosalind.com
# See https://rosalind.info/problems/perm/
# Solved June 2020, revised December 2022

from itertools import permutations

def permutate_int(n):

	return list(permutations(list(range(1, n+1)))) # shift for 1-indexing

if __name__ == '__main__':

	permutations = permutate_int(int(input()))
	res = f'{len(permutations)}\n'
	for perm in permutations:
		res += ' '.join([str(i) for i in perm]) + '\n'
		
	with open('results/result_perm.txt', 'w') as out:
		out.write(res[:-1])