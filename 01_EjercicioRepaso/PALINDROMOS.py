print("Ingrese una palabra")
palabra = str(input())


def EsPalindromo(word):
    if str(word) == str(word)[::-1]:
        print("True")
    else:
        print("False")


EsPalindromo(palabra)
