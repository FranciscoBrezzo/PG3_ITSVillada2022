while True:
    try:
        dato = input("Ingrese un texto:")
        datos = open('03_EjercicioExceptions/texto.txt', 'a')
    
        if dato.isnumeric():
            datos.write(int(dato))
        else:
            datos.write(dato)

        decision = input("Quiere continuar agregando texto? (S/N): ")
        if decision == "si":
            continue
        elif decision == "no":
            break
        else:
            print("ingrese una opcion valida")

    except TypeError:
        print("ingrese un valor que no contenga un numero")
        