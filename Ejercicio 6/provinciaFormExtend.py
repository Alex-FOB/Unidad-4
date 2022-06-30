import tkinter as tk

from provinciaForm import ProvinciaForm

class ProvinciaFormExtend(ProvinciaForm):
    fields = ('Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos', 'Temperatura', 'Sensación térmica', 'Humedad')
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        return super().crearCampo(field) 