# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 22:01:14 2020

@author: tsoyg
"""

from base64 import b64decode
from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder

def decrypt(cyphertext, key, iv):
    global encoder
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    pad_text = aes.decrypt(cyphertext)
    return pad_text

encoder = PKCS7Encoder()
chipertext = b64decode("8eGx3qm2qkJNIY0kNsSwkw==")
key = 'fqIhyykbTjNQ2QdQlBOISw=='
iv = '8119745113154120'
# key = key.encode('utf-8')
# iv = iv.encode('utf-8')
print("chipertext: '%s'" % chipertext)
print("Key: '%s'" % key) 
print("IV: '%s'" % iv)
decrypted = decrypt(chipertext, key, iv) 
print("encrypted: '%s'" % decrypted)