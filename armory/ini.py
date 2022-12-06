from Bio.Seq import Seq
import sys

def count_nucleotides(sequence):

	sequence = Seq(sequence)

	A = sequence.count("A")
	C = sequence.count("C") 
	G = sequence.count("G")
	T = sequence.count("T")

	return A, C, G, T

if __name__ == "__main__":
	
	filename = sys.argv[1]
	sequence = open(filename).read().strip()
	A, C, G, T = count_nucleotides(sequence)

	print(f"{A} {C} {G} {T}")

