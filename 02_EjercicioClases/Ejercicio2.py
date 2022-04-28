class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def calificar(self):
        if self.nota >= 6:
            print(self.nombre, "aprobo con", self.nota)
        else:
            print(self.nombre, "no aprobo con", self.nota)


a1 = Alumno("Pepe", 7)
a2 = Alumno("Juan", 4)

a1.imprimir()
a1.calificar()

a2.imprimir()
a2.calificar()
