mylist = [43,143,243,343]
print("Ingrese un numero de la lista")
numero = int(input())


def ObtenerPosicion(lista,numero):
    i = int
    for i in mylist:
        if i == numero:
            posicion = str(lista.index(i))
            print("El numero que elegiste se encuentra en la posicion "+ posicion)

ObtenerPosicion(mylist,numero)
