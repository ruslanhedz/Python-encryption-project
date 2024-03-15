from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import Funkcje


def brute_force_dectryption(path, path_save, name):
    for i in range(1, 256):
        key = i
        try:
            with open(path, 'rb') as file:
                data = bytearray(file.read())
        except FileNotFoundError:
            print("Takiego pliku nie ma!!!")
            return
        decrypted_data = bytearray(byte ^ key for byte in data)

        header = decrypted_data[0:8]
        hex_header = ' '.join(f'{byte:02X}' for byte in header)

        if Funkcje.is_png(hex_header):
            try:
                with open(path_save + "\\" + name + ".png", 'wb') as file:
                    file.write(decrypted_data)
            except:
                print("Jest błąd w zapisie adresu!!!")
                return
            break
        else:
            continue

def brute_force_decryption_BlowFish(path, path_save, name, password):
    try:
        file = open(path_save + "\\" + name + ".png", 'wb')
        file.close()
    except:
        print("Jest błąd w zapisie adresu!!!")
        return
    for i in range(0, 256):
        try:
            with open(path, 'rb') as image_file:
                encrypted_data = image_file.read()
        except FileNotFoundError:
            print("Takiego pliku nie istnieje!!!")
            return

        salt = i.to_bytes(1, byteorder='big')
        key = PBKDF2(str(password), salt, dkLen=4, count=1000000)
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)

        decrypted_data = cipher.decrypt(encrypted_data)

        try:
            decrypted_data = unpad(decrypted_data, Blowfish.block_size)
            header = decrypted_data[0:8]
            hex_header = ' '.join(f'{byte:02X}' for byte in header)
        except ValueError:
            # If unpad fails, it means the decryption was unsuccessful
            continue

        if Funkcje.is_png(hex_header):
            with open(path_save + "\\" + name + ".png", 'wb') as file:
                file.write(decrypted_data)
            break
        else:
            continue
