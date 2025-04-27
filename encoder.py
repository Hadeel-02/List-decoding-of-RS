import galois

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
P = 971
K = 4
N = 10
GF = galois.GF(P)
EVALUATION_POINTS = [alpha for alpha in range(N)]

def generate_mgs():
    msg = str(input("please enter your msg (exactly {K} chars): "))[:K]
    return msg

def msg_as_poly(msg):
    if len(msg) != K:
      raise KeyError("Message must be at exactly length K")
    msg_list =[ord(ch) for ch in msg]
    print(f"msg_list : {msg_list}")
    msg_coeffs = msg_list
    poly = galois.Poly(msg_coeffs, order="asc",  field=GF)
    return poly

def evaluate_code_word(poly):
    codeword = [poly(eval_pt) for eval_pt in EVALUATION_POINTS ] 
    return  codeword

def encoder(msg):
    poly = msg_as_poly(msg)
    codeword = evaluate_code_word(poly)
    return codeword