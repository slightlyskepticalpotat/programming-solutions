original_solution = '''#!/usr/bin/env python3
# requires pycryptodome
import base64
import hashlib
import os
import time

time1 = time.time()

from Crypto.Cipher import AES


class Cipher:
    def __init__(self, key):
        i = os.urandom(1)[0] % 29
        self.key = base64.urlsafe_b64encode(hashlib.sha256(key).digest()[i:i + 3] * 8) # only 3 bytes are actually used

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB) # ecb mode is already unsecure
        return base64.urlsafe_b64encode(cipher.encrypt(raw))

    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * (AES.block_size - len(s) % AES.block_size).to_bytes(1, 'big')

    def decrypt(self, key, message):
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.decrypt(message)


cipher = Cipher(os.urandom(256))

# with open('flag.txt', 'rb') as f:
    # flag = f.read()

to_decrypt = base64.urlsafe_b64decode("53rW_RiyUiwXq3PD7E4RHJuzjlHbw4YmG8wNRILXEQdBFiJZlpI2WjD_kNeQAUYG")

for i in range(256):
    print((i/256)*100)
    for j in range(256):
        for k in range(256):
            key = base64.urlsafe_b64encode(bytes([i, j, k]) * 8) # repeated 8 times
            try:
                flag = cipher.decrypt(key, to_decrypt).decode()
                if "ctf" in flag:
                    print(flag)
            except:
                pass
time2 = time.time()

print(time2-time1)''' # took 4 minutes on my computer

print("ctf{AES_is_on1y_secure_if_prop3r1y_used}")