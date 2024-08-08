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

plaintext = "1n1 m3d1um l0h b4ng k0k b1s4 b4ng k4mu j4g0 b4ng3t b4ng"
a = 5
b = 8

ciphertext = encrypt(plaintext, a, b)
print(f"Ciphertext: {ciphertext}")
