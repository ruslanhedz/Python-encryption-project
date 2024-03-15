import Szyfrowanie
import Deszyfrowanie

if __name__=="__main__":
    while True:
        try:
            program = int(input("Wybierz program:\n1.Szyfrowanie zdjęcia;\n"
                        "2.Deszyfrowanie zdjęcia;\n3.Wyłączyć program.\n"))
        except ValueError:
            print("Wpisałeś złą odpowiedź!!!")
            continue

        if program < 1 or program > 3:
            print("Takiego wyboru nie ma!!!")
            continue

        if program == 1:
            path_png = input("Wpisz adres zdjęcia(wpisać należy w formacie D:\\\\path...): ")
            encryption_path = input("Wpisz adres gdzie trzeba zapisać zdjęcie(wpisać należy w formacie D:\\\\path...): ")
            name = input("Wpisz nazwę pod którą trzeba zapisać zdjęcie: ")
            Szyfrowanie.Encryption(path_png, encryption_path, name)
        elif program == 2:
            path_encryption = input("Wpisz adres zdjęcia zaszyfrowanego(wpisać należy w formacie D:\\\\path...): ")
            decryption_path = input("Wpisz adres gdzie trzeba zapisać deszyfrowany obraz(wpisać należy w formacie D:\\\\path...): ")
            name = input("Wpisz nazwę pod którą trzeba zapisać zdjęcie: ")
            Deszyfrowanie.brute_force_dectryption(path_encryption, decryption_path, name)
        else:
            break