from utils.utils import fasta_to_dict, reverse_comp


def find_palindromes(
    string: str,
    min: int=4,
    max: int=12
) -> list:

    res = []
    for p in range(len(string)): # only search half the total len
        for i in range(int(min/2), int(max/2)+1): # for (max-min)/2+1 iters
            if string[p:p+i] == reverse_comp(string[p+i : p+(i*2)]):
                res.append((p+1, i*2))
    return res


if __name__ == '__main__':
    import sys
    with open('stronghold/results/result_revp.txt', 'w') as outf:
        string = list(fasta_to_dict(sys.argv[1]).values())[0]
        for res in find_palindromes(string):
            outf.write(f"{res[0]} {res[1]} \n")