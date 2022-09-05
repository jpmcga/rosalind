from itertools import product
import sys

def order_kmers_lex(alphabet, num):

	alphabet = alphabet.split()
	a_str = "".join(alphabet)
	a_str_srt = "".join(sorted(alphabet))

	lst = []
	for i in range(1,num+1):
		prod = list(product(alphabet, repeat=num))
		lst.extend(prod)

	lst = [''.join(x) for x in lst]
	lst.sort(key=lambda x: (x, len(x)))

	trans_tab = lst[0].maketrans(a_str_srt, a_str)
	new = [x.translate(trans_tab) for x in lst]

	return new


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