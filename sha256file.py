import hashlib

nonce = 0
key = 'f3q4uszyt67cfatq'
pad = hashlib.sha256(str(nonce) + key).digest()

# encrypt
plaintext = 'the quick brown fox jumped over.'
ciphertext = ''
for i in range(32):
    ciphertext += chr(ord(pad[i]) ^ ord(plaintext[i]))

# ciphertext = '\x1bf\x13\r\x0c\xc4\x18`\x129\x16\x12|\x96\xa7\xc2\xf5E_\x97\xc2\x010\x88]j\xce\xe3x\x14\xe8\xb6'

# decrypt
plaintext = ''
for i in range(32):
    plaintext += chr(ord(pad[i] ^ ord(ciphertext[i])))

# plaintext = 'the quick brown fox jumped over.'