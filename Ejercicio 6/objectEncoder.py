import json

from pathlib import Path

from manejador import Manejador

from provincia import Provincia

class ObjectEncoder:
    __pathArchi = None
    def __init__(self, pathArchi):
        self.__pathArchi = pathArchi
    def decodificarDiccionario(self, diccionario):
        if '__class__' not in diccionario:
            return diccionario
        else:
            class_name = diccionario['__class__']
            class_ = eval(class_name)
            if(class_name == 'Manejador'):
                pacientes = diccionario['provincias']
                manejador = class_()
                for i in range(len(pacientes)):
                    dicPacientes = pacientes[i]
                    class_name = dicPacientes.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dicPacientes['__atributos__']
                    unPaciente = class_(**atributos)
                    manejador.addProvincia(unPaciente)
        return manejador
    def saveJSONArchivo(self, diccionario):
        with Path(self.__pathArchi).open('w', encoding = 'UTF-8') as destino:
            json.dump(diccionario, destino, indent = 4)
            destino.close()
    def leerJSONArchivo(self):
        with Path(self.__pathArchi).open(encoding = 'UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario