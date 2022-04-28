class Person:
    def __init__(self, nom):
        self.nombre = nom

    def imprimir(self):
        print(self.nombre)


p1 = Person("Pepe")
p1.imprimir()

p2 = Person("Juan")
p2.imprimir()
