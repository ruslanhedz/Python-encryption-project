from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import Funkcje


def Encryption(path, path_save, name):
    key = Funkcje.random_key()
    try:
        with open(path, 'rb') as file:
            data = bytearray(file.read())
    except FileNotFoundError:
        print("Takiego pliku nie istenie!!!")
        return
    encrypted_data = bytearray(byte ^ key for byte in data)

    try:
        with open(path_save + "\\" + name + '.png', 'wb') as file:
            file.write(encrypted_data)
    except:
        print("Jest błąd z zapisie adresu zapisu!!!!")
        return

def Encryption_Blow_Fish(path, path_save, name, password):
    key = Funkcje.random_32_key(password)

    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    try:
        with open(path, 'rb') as image_file:
            image_data = image_file.read()
    except FileNotFoundError:
        print("Takiego pliku nie istnieje!!!")
        return

    padded_data = pad(image_data, Blowfish.block_size)

    encrypted_data = cipher.encrypt(padded_data)

    try:
        with open(path_save + "\\" + name + ".png", 'wb') as file:
            file.write(encrypted_data)
    except:
        print("Jest błąd z zapisem adresu zapisu!!!!")
        return

