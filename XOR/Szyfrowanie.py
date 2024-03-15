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




