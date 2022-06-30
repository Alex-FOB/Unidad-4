import tkinter as tk

from provinciaList import ProvinciaList

from provinciaFormExtend import ProvinciaFormExtend

class ProvinciasView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lista de Provincias')
        self.list = ProvinciaList(self, height=15)
        self.form = ProvinciaFormExtend(self)
        self.boton = tk.Button(self, text='Agregar provincia')
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.boton.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        self.boton.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.selectProvincia)
    def addProvincia(self, provincia):
        self.list.insertar(provincia)
    def getDetalles(self):
        return self.form.crearProvinciaFromForm()
    def viewProvinciaInForm(self, provincia):
        self.form.viewStateProvinciaFormulario(provincia)