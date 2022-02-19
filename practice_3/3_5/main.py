# 3.5: "Цезарь"

def encrypt_caesar(message, shear):
    alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
    encrypted_Message = ''
    for i in message:
        place = alphabet_RU.find(i)
        new_place = place + shear
        if i in alphabet_RU:
            encrypted_Message += alphabet_RU[new_place]
        else:
            encrypted_Message += i
    return encrypted_Message


def decrypt_caesar(message, shear):
    alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
    decrypted_Message = ''
    for i in message:
        place = alphabet_RU.find(i)
        new_place = place - shear
        if i in alphabet_RU:
            decrypted_Message += alphabet_RU[new_place]
        else:
            decrypted_Message += i
    return decrypted_Message


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
