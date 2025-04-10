def caesar_cipher(text, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = []
    for i in text:
        if i in alphabet:
            new_index = (alphabet.index(i) + shift) % len(alphabet)
            result.append(alphabet[new_index])
        else:
            result.append(i)
    return ''.join(result)


message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
encrypted = caesar_cipher(message, shift)
print("Зашифрованное сообщение:", encrypted)
