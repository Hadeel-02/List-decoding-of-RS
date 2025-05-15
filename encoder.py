import galois
import utilities

def generate_mgs():
    msg = str(input("please enter your msg (exactly {utilties.K} chars): "))[:utilities.k]
    return msg

def msg_as_poly(msg):
    if len(msg) != utilities.k:
      raise KeyError("Message must be at exactly length K")
    msg_list =[ord(ch) for ch in msg]
    print(f"msg_list : {msg_list}")
    msg_coeffs = msg_list
    poly = galois.Poly(msg_coeffs, order="asc",  field=utilities.GF)
    return poly

def evaluate_code_word(poly):
    codeword = [poly(eval_pt) for eval_pt in utilities.EVALUATION_POINTS ] 
    return  codeword

def encoder(msg):
    poly = msg_as_poly(msg)
    codeword = evaluate_code_word(poly)
    return codeword