import galois
import math
## encoder
''' Some CONSTANS 
 - q is prime number
 - k is the length of given message
 - n is the length of the codeword (total symbols after encoding)
 -  p is prime power -- the size of the choosen field
 - the relation between the above constans is:
    k <= n <= p
'''
''' IMPORTANT NOTE:
    since we are converting each letter to its value in the ascii table we ensure that p is at least 128
'''
p = 257
k = 4
n = 10
GF = galois.GF(p)
EVALUATION_POINTS = [alpha for alpha in range(n)]

## decoder
'''
 s <= ⌊√n⌋ <= s+1
 - choosing s to be the square root of n ensures that the degree of Q with respect to and y is at most √n
 - count the unkowns: in a bivariate polynomial with deg_x, deg_y  <= s has (s+1)^2 cofficients

'''
s = math.floor(math.sqrt(n))
monomials = [(i,j) for i in range(s+1) for j in range(s+1)]
M = len(monomials)  # (s+1)^2