print("Ingrese un año")
año = int(input())


def EsBisiesto(año):
    if not año % 4 and (año % 100 or not año % 400):
        print("El año " + str(año) + " es un año bisiesto")
    else:
        print("El año " + str(año) + " no es un año bisiesto")


EsBisiesto(año)
