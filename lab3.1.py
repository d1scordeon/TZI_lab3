def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def decrypt(ciphertext, p, q, e, alphabet):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)

    # Decrypt the ciphertext
    decrypted_numbers = [pow(c, d, n) for c in ciphertext]

    # Convert numbers to characters using the alphabet
    decrypted_message = ''.join(alphabet[num % len(alphabet)] for num in decrypted_numbers) # Use modulo to wrap around the alphabet

    return decrypted_message

# Given values
ciphertext = [377, 754, 1310, 1, 1233, 35, 1045] # The list of encrypted integers
p = 19
q = 73
e = 5  # The encryption key (exponent)

# Ukrainian alphabet
ukr_alphabet = "АБВГҐДЕЄЖЗИЇЙКЛМНОПРСТУФХЦЧШЩЬІЮЯ_0123456789"

# Perform decryption
plaintext = decrypt(ciphertext, p, q, e, ukr_alphabet)
print("Decrypted message:", plaintext)
