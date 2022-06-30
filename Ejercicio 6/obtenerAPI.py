from dataclasses import replace
import json

from urllib.request import urlopen

class ObtenerAPI:
    __resultado = None
    def __init__(self):
        self.__resultado = None
    def run(self, provincia): 
        nombre = provincia.getNom().lower()
        nombre = nombre.replace(' ', '%20')
        url_template = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=162d6d508fe73993d884f30133d57b1a'.format(nombre)
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
    def getResultado(self):
        return self.__resultado