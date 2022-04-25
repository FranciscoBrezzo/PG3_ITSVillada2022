class Familia:
    def __init__(self):
        self.nomP = str(input("Ingrese el nombre del padre:"))
        self.nomM = str(input("Ingrese el nombre de la madre:"))
        self.cont = int(input("Ingrese la cantidad de hijos que tiene:"))
        self.listH = list = []
        for x in range(self.cont):
            hijo = input("Ingrese el nombre de los hijos:")
            self.listH.append(hijo)


    def __str__(self) -> str:
        return f"El nombre del padre es: {self.nomP}, el nombre de la madre es: {self.nomM}, y los nombres de los hijos son: {self.listH}"

        

f1 = Familia()
print(f1)