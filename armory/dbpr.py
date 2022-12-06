from Bio import ExPASy
from Bio import SwissProt
import sys

def get_bio_processes(protein):

	processes = []
	handle = ExPASy.get_sprot_raw(protein)
	record = SwissProt.read(handle)
	for ref in record.cross_references:
		if ref[0] == 'GO':
			if ref[2].startswith('P'):
				processes.append(ref[2].split(":")[1])

	return processes

if __name__ == '__main__':

	filename = sys.argv[1]
	protein = open(filename).read()
	processes = get_bio_processes(protein)

	for process in processes:
		print(process)
