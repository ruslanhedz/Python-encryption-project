from Crypto.Protocol.KDF import PBKDF2
import random
import secrets

def random_key():
    key = random.randint(1, 256)
    return key

def random_32_key(password):
    salt = secrets.token_bytes(1)
    key = PBKDF2(str(password), salt, dkLen=4, count=1000000)
    return key

def is_png(header):
    if header == "89 50 4E 47 0D 0A 1A 0A": return True
    else: return False
