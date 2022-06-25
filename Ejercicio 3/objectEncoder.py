import json

from pathlib import Path

from dolar import Dolar

from manejador import Manejador

class ObjectEncoder:
    def crearManejador(self, lista):
        respuesta = None
        if(lista != None):
            control = Manejador()
            for dic in lista:
                dolar = dic['casa']
                if(dolar != None):
                    unDolar = Dolar(dolar['nombre'], dolar['compra'], dolar['venta'])
                    control.addDolar(unDolar)
        if(control != None):
            respuesta = control
        return respuesta
    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding = 'UTF-8') as fuente:
            lista= json.load(fuente)
            fuente.close()
            return lista