# Solution for Introduction to Set Operations by Rosalind.com
# See https://rosalind.info/problems/seto/
# Solved October 5, 2022

import sys

def set_ops(s1: set, s2: set, parent: int):

	assert type(s1) == type(s2) == set, "s1, s2 must be sets"

	if max(s1) > parent or max(s2) > parent:
		raise ValueError("s1, s2 must be subsets of parent")

	s_parent = {ele for ele in range(parent+1)[1:]}

	union = s1 | s2
	intersection = s1 & s2
	s1subs2 = s1 - s2
	s2subs1 = s2 - s1
	s1c = s_parent - s1
	s2c = s_parent - s2

	return union, intersection, s1subs2, s2subs1, s1c, s2c


if __name__ == '__main__':

	with open(sys.argv[1]) as i:
		parent = int(i.readline().rstrip())
		s1 = eval(i.readline().rstrip())
		s2 = eval(i.readline().rstrip())

	with open("Bioinformatics_Stronghold/Results/solution_seto.txt", "w") as o:
		for val in set_ops(s1, s2, parent):
			o.write(f"{val}\n")

		
