import decoder
import encoder
import random

def add_noise(codeword, num_errors=2):
    """
    Introduce noise by randomly changing up to `num_errors` positions in the codeword.
    """
    noisy = codeword.copy()
    indices = random.sample(range(len(codeword)), k=num_errors)
    
    for idx in indices:
        old_val = noisy[idx]
        field = type(old_val)
        # Pick a different value randomly
        options = list(field.elements)
        options.remove(old_val)
        noisy[idx] = random.choice(options)
    
    return noisy

if __name__ == "__main__":
    message = "ABCD"
    codeword = encoder.encoder(message)
    print("Original codeword:", codeword)

    corruptesd_codeword = add_noise(codeword, num_errors=2)
    print("Noisy codeword:", corruptesd_codeword)

    print("\n--- Decoding ---")
    # possible_meessages = decoder.decoder(corruptesd_codeword)
    
    print("--- The end ---")
    # for possible_meessage in possible_meessages:
    #     print(possible_meessage)