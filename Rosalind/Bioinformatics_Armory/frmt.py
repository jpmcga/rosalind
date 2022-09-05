#!/usr/local/bin/python3.8
from Bio import Entrez, SeqIO
import sys


def shortest_fasta(ids, email = ""):

	Entrez.email = email
	handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
	shortest = min(list(SeqIO.parse(handle, "fasta")) , key=len).format('fasta')
	handle.close()

	return shortest


def get_ids(filename):

	file = open(filename)
	ids = file.read().strip()
	file.close()
	
	return ids


def save_fasta(fasta, output_file):
	file = open(output_file, "w")
	file.write(fasta)
	file.close()

	return


if __name__ == '__main__':

	filename = sys.argv[1]
	save_fasta(shortest_fasta(get_ids(filename)), f"{filename[:-4]}_result.txt")
