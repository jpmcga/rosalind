from itertools import product
import sys

def order_kmers_lex(alphabet, num):

	lst = alphabet.split()
	return list(product(lst, repeat=num))

def main():

	in_handle = open(sys.argv[1])
	alphabet = in_handle.readline().strip()
	num = int(in_handle.readline())
	lst = order_kmers_lex(alphabet, num)
	res = '\n'.join(''.join(x) for x in lst)

	out_handle = open(sys.argv[2], "w")
	out_handle.write(res)
	out_handle.close()

if __name__ == '__main__':
	main()