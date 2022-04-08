import sre_compile

def PintarCuadrado(ancho: int, alto: int, caracter: str) -> None:
    for i in range(alto):
        print(ancho * (caracter + (" ")))

def PintarTriangulo(ancho: int, caracter: str) -> None:
    cont : int= 1
    for i in range(ancho):
        resultado = ancho - cont
        print((" ")*resultado + (caracter + " ")* cont)
        cont += 1

def PintarTrianguloInvertido(ancho: int, caracter: str) -> None:
    cont : int= ancho
    for i in range(ancho):
        resultado = ancho - cont
        print((" ")*resultado + (caracter + " ")* cont)
        cont -= 1

print("Elija lo que desea pintar ")
print("1.Cuadrado, 2.Triangulo, 3.Triangulo Invertido")

opcion:int = int(input())

if(opcion == 1):
    print("Ingrese el ancho del cuadrado")
    ancho:int = int(input())
    print("Ingrese el alto del cuadrado")
    alto:int=int(input())
    print("Ingrese su caracter")
    caracter:str=str(input())
    PintarCuadrado(ancho,alto,caracter)
elif(opcion==2):
    print("Ingrese el ancho del cuadrado")
    ancho:int = int(input())
    print("Ingrese su caracter")
    caracter:str=str(input())
    PintarTriangulo(ancho,caracter)
elif(opcion==3):
    print("Ingrese el ancho del cuadrado")
    ancho:int = int(input())
    print("Ingrese su caracter")
    caracter:str=str(input())
    PintarTriangulo(ancho,caracter)



