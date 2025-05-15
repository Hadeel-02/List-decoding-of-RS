import utilities
import sympy as sp
from galois import Poly
import itertools
from sage.all import *
'''
1. Interpolation
'''

def build_monomials():
    # Q = a + x + y + xy + x^2y + xy^2 ...
    # the monomials: all the possible combinations of powers of x and y that can appear in Q(x,y) up to the degree limits
    s = utilities.s
    monomials = [(i, j) for i in range(s + 1) for j in range(s + 1)]
    return monomials

def build_interpolation_matrix(pairs, monomials):
    # pairs refer to the (alpha, y) where;
    # - alpha is the evaluation point
    # - y is the code character (it might be corrupted after adding the noise)
    
    A = []  # the interpolation matrix
    for alpha, y in pairs:
        row = []
        for (i, j) in monomials:
            val = alpha**i * y**j
            row.append(int(val))
        A.append(row)
    
    return sp.Matrix(A)

def solve_zero_space(matrix):
    zero_vectors = matrix.nullspace()
    if not zero_vectors:
        raise Exception("No non-zero solution found for the interpolation matrix.")
    
    for vec in zero_vectors:
        if any(c != 0 for c in vec):
            return [utilities.GF(int(c % utilities.p)) for c in vec]
    
    return []  # Return empty if no valid solution is found.

def construct_Q(codeword):
    '''
    Construct Q(x,y) with deg_x, deg_y <= root(n) that for all point (x,y) = (alpha, y) Q(x,y) = 0.
    Returns a dictionary {(i,j): coefficient}.
    '''
    pairs = zip(codeword, utilities.EVALUATION_POINTS)
    monomials = build_monomials()
    A = build_interpolation_matrix(pairs, monomials)
    Q_coeffs = solve_zero_space(A)
    
    # Now we return Q_coeffs as a dictionary
    Q_dict = {}
    for idx, coeff in enumerate(Q_coeffs):
        Q_dict[monomials[idx]] = coeff

    return Q_dict

'''
2. Factorization
'''

def evaluate_Q_at_poly(Q_dict, f_poly):
    """
    Plug y = f(x) into Q(x,y), and return the result as a univariate polynomial.
    Q_dict: {(i,j): GF element}
    f_poly: f(x) as a galois.Poly
    """
    GF = f_poly.field
    x_poly = Poly.Identity(GF)
    result = Poly.Zero(GF)

    for (i, j), coeff in Q_dict.items():
        # Calculate each term separately and add them to result
        term = coeff * (x_poly ** i) * (f_poly ** j)
        result += term

    return result

def find_candidate_messages(Q_dict):
    """
    Try all f(x) of degree < k and return those where Q(x, f(x)) = 0
    """
    GF = utilities.GF
    k = utilities.k
    candidates = []

    elements = list(GF.elements)

    for coeffs in itertools.product(elements, repeat=k):
        f = Poly(coeffs, field=GF)
        result = evaluate_Q_at_poly(Q_dict, f)
        if result == Poly.Zero(GF):
            candidates.append(f)

    return candidates

def decoder(codeword):
    '''
    This function decodes the noisy codeword back to the possible original message(s).
    '''
    Q = construct_Q(codeword)  # Construct Q(x, y) from the noisy codeword.
    possible_messages = find_candidate_messages(Q)  # Pass Q to find_candidate_messages

    return possible_messages