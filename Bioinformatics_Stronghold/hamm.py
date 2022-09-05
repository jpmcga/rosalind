import sys

def get_hamming(s1, s2):
	return sum([1 for pos in range(len(s1)) if s1[pos] != s2[pos]])

if __name__ == '__main__':
	input = open(sys.argv[1]).read().split('\n')
	print(get_hamming(input[0], input[1]))
