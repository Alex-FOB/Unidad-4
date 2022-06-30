class Provincia:
    __nom = None #Nombre
    __cap = None #Capital
    __hab = None #Cantidad de habitantes
    __dept = None #Cantidad de departamentos/partidos
    __temp = None
    __sens = None
    __hum = None
    def __init__(self, nombre, capital, habitantes, departamentos, temperatura = 0.0, sensacion = 0.0, humedad = 0.0):
        self.__nom = str(nombre)
        self.__cap = str(capital)
        self.__hab = int(habitantes)
        self.__dept = int(departamentos)
        self.__temp = float(temperatura)
        self.__sens = float(sensacion)
        self.__hum = float(humedad)
    def setInfoDemo(self, temperatura, sensacion, humedad):
        self.__temp = float(temperatura)
        self.__sens = float(sensacion)
        self.__hum = float(humedad)
    def getNom(self):
        return self.__nom
    def getCap(self):
        return self.__cap
    def getHab(self):
        return self.__hab
    def getDept(self):
        return self.__dept
    def getTemp(self):
        return self.__temp
    def getSens(self):
        return self.__sens
    def getHum(self):
        return self.__hum
    def toJSON(self):
        dic = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre = self.__nom,
                capital = self.__cap,
                habitantes = self.__hab,
                departamentos = self.__dept,
                temperatura = self.__temp,
                sensacion = self.__sens,
                humedad = self.__hum
            )
        )
        return dic