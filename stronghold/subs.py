# Solution for Finding a Motif in DNA by Rosalind.com
# See https://rosalind.info/problems/subs/
# Solved June 2020, revised November 2022

def find_motif_locs(s1, s2):
    """Returns list of positions (1-based) of substring (s2) in string (s1)"""

    if s2 in s1:
        return [p+1 for p in range(len(s1)) if s1[p:].startswith(s2)]
    else:
        return "Substring not in string."

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as file:
        s1, s2 = file.read().strip().split('\n')
        print(' '.join([str(p) for p in find_motif_locs(s1, s2)]))


