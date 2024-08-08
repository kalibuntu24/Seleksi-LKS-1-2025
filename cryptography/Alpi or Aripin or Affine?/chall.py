import string

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            x = ord(char.upper()) - 65
            y = (a * x + b) % 26
            ciphertext += chr(y + 65)
        else:
            ciphertext += char
    return ciphertext

plaintext = "REDACTED"
a = 5
b = 8

ciphertext = encrypt(plaintext, a, b)
print(f"Ciphertext: {ciphertext}")
