from many_time_pad import strxor, toascii, tohex
import random


def key_gen(length):
    return ''.join(str((random.randint(0, 1) + random.randint(0, 1)) % 2) for x in range(length))


def encrypt(message, key=None):
    if key is None:
        gen = key_gen(len(message)*2)
        return strxor(tohex(message), tohex(gen))

    return strxor(message, toascii(key))


def decrypt(cipher, key):
    return strxor(cipher, key)

if __name__ == '__main__':
    message = 'I am the best'
    real_key = key_gen(len(message)*2)
    encryption = encrypt(message, real_key)
    print('Encrypted cipher: ' + tohex(encryption))
    print('Decrypted cipher: ' + decrypt(encryption, toascii(real_key)))

