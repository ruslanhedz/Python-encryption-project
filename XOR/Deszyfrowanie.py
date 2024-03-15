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

