class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.list = [int(lado1),int(lado2),int(lado3)]

    def LadoMayor(self):
        print(max(self.list))
    
    def EsEquilatero(self):
        if(self.lado1 == self.lado2 and self.lado1 == self.lado3):
            print("Su triangulo es equilatero")
        else:
            print("Su triangulo no es equilatero")


t1 = Triangulo(5,5,7)
t1.LadoMayor()
t1.EsEquilatero()

