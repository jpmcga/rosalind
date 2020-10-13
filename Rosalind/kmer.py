import itertools
import sys

filename = sys.argv[1]
seq = []
with open(filename) as file:
	file.readline()
	for line in file:
		seq.append(line.strip())
	seq = ''.join(seq)

perms = list(itertools.product('ATCG', repeat = 4))
perms = sorted([''.join(x) for x in perms])

counts = [0 for item in perms]
dic = dict(zip(perms, counts))

for x in range(len(seq)):
	kmer = seq[x:x+4]
	if len(kmer) == 4:
		dic[kmer] += x

for value in dic.values():
	print(value, end = ' ')