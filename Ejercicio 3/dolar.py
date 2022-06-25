class Dolar:
    __nombre = None
    __compra = None
    __venta = None
    def __init__(self, nombre, compra, venta):
        try:
            self.__nombre = str(nombre)
            self.__compra = float(compra.replace(',', '.'))
            self.__venta = float(venta.replace(',', '.'))
        except ValueError:
            print('ERROR: dolar invalido')
    def __str__(self):
        return '{} Compra:{} Venta:{}'.format(self.__nombre, self.__compra, self.__venta)
    def getNom(self):
        return self.__nombre
    def getCompra(self):
        return self.__compra
    def getVenta(self):
        return self.__venta