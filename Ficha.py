from Dado import *

class Ficha:
    color = ""
    posicion = 0

    #no era parte del modelo, pero la Ficha necesita usar un dado
    #este atributo se define cuando definimos relaciones entre clases
    #lo que veremos más adelante en el curso
    dado = Dado(6)
    
    
    def __init__(self, color):
        self.color = color
        self.posicion = 0
        return 
    
    def avanzar(self):
        #aquí se vuelve claro por qué necesitamos un dado
        pasos = self.dado.lanzar()
        self.posicion += pasos
        print(f"\nEs el turno de la ficha: {self.color} ")
        input("\nPresione la tecla ENTER para lanzar el dado...")
        print(f"\nEl dado muestra el número: {pasos}, la casilla actual de la ficha es: {self.posicion} \n")
        return
    
    def ubicarEnTablero(self, pM):
        if self.posicion%8 == 0 and self.posicion <=63:
            pM[(self.posicion//8)-1][-1] += f"-{self.color}"
        elif self.posicion//8 <= 7 and self.posicion%8<=7:
            pM[self.posicion//8][(self.posicion%8)-1] += f"-{self.color}"
        else:
            pM[-1][-1] += f"{self.color}"
        return pM
    