class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("Nombre:" ,self.nombre)
        print("Nota:",self.nota)

    def calificar(self):
        if(self.nota >= 6):
            print(self.nombre , "aprobo con" , self.nota)
        else:
            print(self.nombre ,"no aprobo con" , self.nota)

p1 = Alumno("Pepe",7)
p2 = Alumno("Juan",4)

p1.imprimir()
p1.calificar()

p2.imprimir()
p2.calificar()


