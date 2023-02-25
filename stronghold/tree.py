# Error Completing a Tree by Rosalind.com
# See https://rosalind.info/problems/tree/
# Solved July 2020, revised February 2023

def edges_to_complete(path):
    '''Return number of edges required to complete tree with n
    nodes and provided adjacency list.'''
    with open(path) as f:
        n, edges = int(f.readline()), f.readlines()
    return n - 1 - len(edges)

if __name__ == '__main__':
    import sys
    print(edges_to_complete(sys.argv[1]))