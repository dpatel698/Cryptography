from Crypto.Cipher import AES

cbc1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
cbc_key1 = '140b41b22a29beb4061bda66b6747e14'
cbc2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
cbc_key2 = '140b41b22a29beb4061bda66b6747e14'

cbc_encryption = AES.new(cbc_key1, AES.MODE_CBC, 'This is an IV456')

print(cbc_encryption.encrypt('aaaaaaaaaaaaaaaa'))