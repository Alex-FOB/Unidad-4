from obtenerAPI import ObtenerAPI

class Manejador:
    indice = 0
    __provincias = None
    __api = None
    def __init__(self):
        self.__provincias = []
        self.__api = ObtenerAPI()
    def addProvincia(self, provincia):
        provincia.rowid = Manejador.indice
        #---------------------------------
        self.startAPI(provincia)
        dic = self.getDic()
        self.setCondicionMeteo(provincia, dic)
        #---------------------------------
        Manejador.indice += 1
        self.__provincias.append(provincia)
    def getProvincias(self):
        return self.__provincias
    def getIndice(self, provincia):
        band = False
        i = 0
        while not band and i < len(self.__provincias):
            if(self.__provincias[i].rowid == provincia.rowid):
                band = True
            else:
                i += 1
        return i
    #def setInfoDemo(self, provincia, temp, sens, hum):
        #indice = self.getIndice(provincia)
        #self.__provincias[indice].setInfoDemo(temp, sens, hum)
    def startAPI(self, nombre):
        self.__api.run(nombre)
    def getDic(self):
        return self.__api.getResultado()
    def setCondicionMeteo(self, provincia, dic):
        temperatura = dic['main']['temp']
        sensacion = dic['main']['feels_like']
        humedad = dic['main']['humidity']
        provincia.setInfoDemo(temperatura, sensacion, humedad)

    def toJSON(self):
        dic = dict(
            __class__=self.__class__.__name__,
            provincias=[provincia.toJSON()for provincia in self.__provincias]
        )
        return dic