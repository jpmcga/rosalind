# Solution for Enumerating k-mers Lexicographically by Rosalind.com
# See https://rosalind.info/problems/lexf/
# Solved July 2020, revised December 2022

from itertools import product; import sys

def order_kmers_lex(alphabet, num):

	return list(product(alphabet.split(), repeat=num))

def main():

	out_f = "results/result_lexf.txt"

	with open(sys.argv[1]) as in_hand, open(out_f, "w") as out_hand:
		alphabet, num  = [x.rstrip() for x in in_hand.readlines()]
		res = '\n'.join(''.join(x) for x in order_kmers_lex(alphabet, int(num)))

		out_hand.write(res)

if __name__ == '__main__':
	main()