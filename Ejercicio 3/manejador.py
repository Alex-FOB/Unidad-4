class Manejador:
    __dolars = None
    def __init__(self):
        self.__dolars = []
    def addDolar(self, dolar):
        self.__dolars.append(dolar)
    def calcular(self, nombre, modo, dolar):
        pesos = 0.0
        i = 0
        band = False
        while not band and i < len(self.__dolars):
            dato = self.__dolars[i]
            if(dato.getNom() == nombre):
                if(modo == 0):
                    pesos = dolar * dato.getCompra()
                elif(modo == 1):
                    pesos = dolar * dato.getVenta()
            i += 1
        return pesos
    def mostrar(self):
        for dolar in self.__dolars:
            print(dolar)