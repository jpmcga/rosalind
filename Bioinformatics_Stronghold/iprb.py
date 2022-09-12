def calculate_dominant_probablity(k, m, n):
    '''Given a number of individuals homozygous dominant (k, AA), heterzygous 
    (Aa, m), and homozygous recessive (aa, n) for allele A in population t,
    return the probablity that two randomly selected individuals will 
    produce an offspring displaying the dominant phenotype.
    '''
    k, m, n = [int(i) for i in [k, m, n]]

    t = k + m + n

    # Formula: (k(k-1)+2km+2kn+mn+0.75m(m-1))/(t(t-1))	
    numerator = k*(k-1) + 2*k*m + 2*k*n + m*n + 0.75*m*(m-1)
    denominator = t*(t-1)

    return numerator/denominator


if __name__ == '__main__':
    import sys

    try:
        print(calculate_dominant_probablity(sys.argv[1],sys.argv[2],sys.argv[3])) 
    except IndexError:
        print("Enter numbers k m n")