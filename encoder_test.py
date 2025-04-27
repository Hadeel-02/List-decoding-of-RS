import encoder
import numpy as np

# Message	Codeword
# ABCD	[65, 266, 38, 760, 898, 860, 83, 917, 857, 311]
# TEST	[84, 320, 255, 393, 267, 381, 268, 432, 406, 694]
# 1234	[49, 202, 769, 120, 509, 306, 794, 343, 236, 785]
# WXYZ	[87, 354, 368, 669, 826, 408, 926, 7, 133, 873]
message_to_codeword ={ "ABCD" : [65, 266, 38, 760, 898, 860, 83, 917, 857, 311],
                       "TEST" : [84, 320, 255, 393, 267, 381, 268, 432, 406, 694],
                       "1234"   :	[49, 202, 769, 120, 509, 306, 794, 343, 236, 785],
                       "WXYZ" : [87, 354, 368, 669, 826, 408, 926, 7, 133, 873]
                       }

def run_tests():
    isSuccess = True
    print("________ Test encoder ________")
    for msg in message_to_codeword:
        codeword = encoder.encoder(msg)
        # if not np.array_equal(message_to_codeword[msg], codeword):
        if not message_to_codeword[msg] ==codeword:
            isSuccess = False
            print("---- Test failed ----")
        else:
            print("---- Test Pass ----")
        
        print(f"msg: {msg}")
        print(f"Expected output: {message_to_codeword[msg]}")
        print(f"Output: {codeword}")

    if isSuccess:
        print("------ Passed all Tests ------")
    

if __name__ == "__main__":
    run_tests()