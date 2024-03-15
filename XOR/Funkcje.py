import random

def random_key():
    key = random.randint(1, 256)
    return key

def is_png(header):
    if header == "89 50 4E 47 0D 0A 1A 0A": return True
    else: return False