class RepositorioProvincias:
    __json = None
    __manejador = None
    def __init__(self, json):
        self.__json = json
        diccionario = self.__json.leerJSONArchivo()
        self.__manejador = self.__json.decodificarDiccionario(diccionario)
    def getListaProvincias(self):
        return self.__manejador.getProvincias()
    def addProvincia(self, provincia):
        self.__manejador.addProvincia(provincia)
        return provincia
    def saveDatos(self):
        self.__json.saveJSONArchivo(self.__manejador.toJSON())