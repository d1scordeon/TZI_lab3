import math

ukr_alphabet = "АБВГҐДЕЄЖЗИЇЙКЛМНОПРСТУФХЦЧШЩЬІЮЯ_0123456789"
alphabet_index = {ukr_alphabet[i]: i for i in range(len(ukr_alphabet))}
index_alphabet = {i: ukr_alphabet[i] for i in range(len(ukr_alphabet))}

# RSA setup
p = 19
q = 73
n = p * q
phi = (p - 1) * (q - 1)

e = 5
while math.gcd(e, phi) != 1:
    e += 1

# Calculating the multiplicative inverse of e modulo phi for decryption
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

d = modinv(e, phi)

# RSA encryption function
def rsa_encrypt(message, e, n):
    cipher = []
    for char in message:
        if char in alphabet_index:
            cipher_number = pow(alphabet_index[char], e, n)
            cipher.append(cipher_number)
        else:
            raise ValueError(f"Character '{char}' not in the alphabet!")
    return cipher


# Encrypt the given message
message = "ВТБ17П"
encrypted_message = rsa_encrypt(message, e, n)
print(f"Original message: {message}")
print(f"Modulus: {n}")
print(f"Encryption key: {e}")
print(f"Decryption Key: {d}")
print(f"Encrypted message: {encrypted_message}")

