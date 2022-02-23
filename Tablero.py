from Ficha import *
def crearTablero(pcolumnas):
    tabla = []
    for i in range(pcolumnas):
        fila = []
        while len(fila) < pcolumnas:
            fila.append("")
        tabla.append(fila)
    return tabla

def agregarEspacios(string, tamano):
    """
    Funcionamiento: Sirve para que el string ingresado tenga un tamaño específico con espacios en blanco
    Entradas:
    string(str): Es el texto a modificar tamaño
    tamano(int): Es la cantidad de caracteres de espacio vacío a agregar
    Salidas: Es el string modificado
    """
    return (str(string) + (' ' * tamano))[:tamano]

class Tablero:

    #Defina aquí los atributos de Tablero
    tabla = list
    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno
    listaFichas = list

    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self, plistaFichas):
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase
        self.tabla = crearTablero(8)
        self.listaFichas = plistaFichas
        return
    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
    def imprimirTablero(self):
        print("═"*175)
        for fila in self.tabla:
            for casilla in fila:
                print(agregarEspacios(casilla, 21), end="║")
            print(("\n") + "═"*175)

    def revisarGanador(self):
        for fichita in self.listaFichas:
            if fichita.posicion >= 63:
                return True
        return False
    
    def actualizarTabla(self, plistaFichas):
        self.tabla = crearTablero(8)
        for jugador in plistaFichas:
            jugador.ubicarEnTablero(self.tabla)
        self.imprimirTablero()

    def sacarGanador(self):
        for elemento in self.listaFichas:
            if elemento.posicion >= 63:
                return elemento.color
        return ""
    
######################        
# PROGRAMA PRINCIPAL #
######################
fichasActuales = []
contador = 1
print("Los colores de las fichas serán: \n1. Rosa \n2. Rojo \n3. Azul \n4. Verde \n¡Cada ficha inicia en la posición 0!\n")
for color in ["Rosa", "Rojo", "Azul", "Verde"]:
    fichaN = Ficha(color)
    fichasActuales.append(fichaN)
juego = Tablero(fichasActuales)
while not juego.revisarGanador():
    for jugador in juego.listaFichas:
        jugador.avanzar()
        if contador != 1: juego.actualizarTabla(fichasActuales)
        else: jugador.ubicarEnTablero(juego.tabla), juego.imprimirTablero()
        if jugador.posicion >= 63:
            break
    contador += 1
    print()
print(f"El juego se ha acabado, ganador: {juego.sacarGanador()}")