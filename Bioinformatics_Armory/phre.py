from Bio import SeqIO
import sys

def count_less_than_min(filename):
	with open(filename) as handle:
		
		min_score = int(handle.readline())
		
		count = 0
		for record in SeqIO.parse(handle, "fastq"):
			scores = record.letter_annotations["phred_quality"]
			if sum(scores)/len(scores) < min_score:
				count += 1

	return count


if __name__ == '__main__':
	filename = sys.argv[1]
	res = count_less_than_min(filename) 
	print(res)
