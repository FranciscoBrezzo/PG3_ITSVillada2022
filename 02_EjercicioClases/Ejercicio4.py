class Operacion:
    def __init__(self):
        self.num1 = int(input("Ingrese primer numero: "))
        self.num2 = int(input("Ingrese segundo numero: "))
        self.Suma()
        self.Resta()
        self.Multiplicacion()
        self.Division()

    def Suma(self):
        resultado = self.num1 + self.num2
        print("El resultado de su suma es ", resultado)

    def Resta(self):
        resultado = self.num1 - self.num2
        print("El resultado de su resta es ", resultado)

    def Multiplicacion(self):
        resultado = self.num1 * self.num2
        print("El resultado de su multiplicacion es ", resultado)

    def Division(self):
        resultado = self.num1 / self.num2
        print("El resultado de su division es ", resultado)


o1 = Operacion()
