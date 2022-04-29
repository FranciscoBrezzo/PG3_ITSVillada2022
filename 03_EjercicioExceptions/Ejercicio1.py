while True:
    try:
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        resultado = num1 + num2
        print("El resultado de su suma es: ", resultado)
    except ValueError:
        print("Por favor ingrese valores de tipo numerico")
    
