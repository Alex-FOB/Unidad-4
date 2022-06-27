from paciente import Paciente

from manejador import Manejador

from objectEncoder import ObjectEncoder

class RepositorioPacientes:
    __json = None
    __manejador = None
    def __init__(self, json):
        self.__json = json
        diccionario = self.__json.leerJSONArchivo()
        self.__manejador = self.__json.decodificarDiccionario(diccionario)
    def getListaPacientes(self):
        return self.__manejador.getPacientes()
    def addPaciente(self, paciente):
        self.__manejador.addPaciente(paciente)
        return paciente
    def modPaciente(self, paciente):
        self.__manejador.modPaciente(paciente)
        return paciente
    def deletePaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)
    def saveDatos(self):
        self.__json.saveJSONArchivo(self.__manejador.toJSON())