from Bio import SeqIO
import sys


def convert_seq_files(
	in_handle,
	out_handle,
	in_format='fastq',
	out_format='fasta'):

	records = SeqIO.parse(in_handle, in_format)
	count = SeqIO.write(records, out_handle, out_format)
	return 


if __name__ == '__main__':

	try:
		convert_seq_files(sys.argv[1], sys.argv[2])
		print(f"converted to {sys.argv[2]}")
	except IndexError:
		print("Enter input file, output file")
