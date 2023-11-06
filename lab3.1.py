ukr_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_0123456789"
ciphertext = "32, 927, 1, 346, 91, 304"

d = 1037
n = 1387

# Функція для обчислення a^b mod n
def modPow(a, b, n):
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        b = b // 2
        a = (a * a) % n
    return result

# Розбиваємо шифрограму на числа
encryptedNumbers = list(map(int, ciphertext.split(", ")))

# Дешифруємо кожне число та відображаємо його на відповідний символ
decryptedMessage = ""
for num in encryptedNumbers:
    decryptedCharCode = modPow(num, d, n)
    if decryptedCharCode < len(ukr_alphabet):
        decryptedMessage += ukr_alphabet[decryptedCharCode]
    else:
        print(f"Error: Decrypted char code {decryptedCharCode} is not in the alphabet range")
        break

print("Розшифрований текст:", decryptedMessage)
