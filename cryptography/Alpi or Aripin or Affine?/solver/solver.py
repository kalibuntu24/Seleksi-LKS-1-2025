import string

def mod_inverse(a, m):
    # Returns the modular multiplicative inverse of a under modulo m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    m = 26
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - 65  # Assuming ciphertext is uppercase
            x = (a_inv * (y - b)) % m
            plaintext += chr(x + 65)
        else:
            plaintext += char
    return plaintext

ciphertext = "1V1 Q3X1EQ L0R N4VM G0G N1U4 N4VM G4QE B4M0 N4VM3Z N4VM"
a = 5
b = 8

decrypted_message = affine_decrypt(ciphertext, a, b)
if decrypted_message:
    print(f"Decrypted message: {decrypted_message}")
