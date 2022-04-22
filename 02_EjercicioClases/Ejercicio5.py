class Persona:
    def __init__(self):
        self.nombre = str(input("Ingrese su nombre: "))
        self.edad = int(input("Ingrese su edad: "))
    
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese su sueldo:"))

    def imprimir(self):
        print(super().imprimir())
        print("Su sueldo es:",self.sueldo)

    def Debe_Pagar_Impuestos(self):
        if(self.sueldo>=3000):
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")

p1 = Persona()
p1.imprimir

print("            ")

e1 = Empleado()
e1.imprimir()
e1.Debe_Pagar_Impuestos()

