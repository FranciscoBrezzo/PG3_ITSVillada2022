print("Ingrese una palabra")
palabra = str(input())


def ContVocales(palabra):
    cont = 0
    for i in palabra:
        if i.lower() in "aeiou":
            cont += 1
    print("Su palabra tiene " + str(cont) + " vocales")


ContVocales(palabra)
