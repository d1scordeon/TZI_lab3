import math

# Визначення функції для шифрування повідомлення за допомогою RSA
def rsa_encrypt(message, e, n, ukr_alphabet):
    encrypted_message = []
    for character in message:
        if character in ukr_alphabet:
            # Конвертація символу в його числовий код
            char_index = ukr_alphabet.index(character)
            # Шифрування за допомогою RSA
            encrypted_char = pow(char_index, e, n)
            encrypted_message.append(encrypted_char)
        else:
            raise ValueError(f"Character '{character}' not in the alphabet")
    return encrypted_message

# Ініціалізація змінних
p = 19
q = 73
n = p * q
phi = (p-1)*(q-1)

# Вибір значення e
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1

# Знаходження значення d
k = 4
d = ((k * phi) + 1) // e

# Алфавіт та повідомлення
ukr_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_0123456789"
message = "ВТБ17П"

# Шифрування повідомлення
encrypted_msg = rsa_encrypt(message, e, n, ukr_alphabet)

# Виведення результатів
print("e =", e)
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
print(f'Original message: {message}')
print(f'Encrypted message: {encrypted_msg}')



