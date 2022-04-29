meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
while True:
    try:
        num = int(input("Ingrese el numero de su mes: "))
        print("Su mes es: ", meses[num - 1])
    except IndexError:
        print("Por favor ingrese un numero dentro del rango de los meses")
    except ValueError:
        print("Por favor ingrese un numero")