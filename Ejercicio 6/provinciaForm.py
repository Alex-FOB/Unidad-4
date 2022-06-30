import tkinter as tk

from tkinter import messagebox

from sqlalchemy import values

from provincia import Provincia

class ProvinciaForm(tk.LabelFrame):
    fields = ('Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos')
    def __init__(self, master, **kwargs):
        super().__init__(master, text='Provincia', padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    def viewStateProvinciaFormulario(self, provincia):
        values = (provincia.getNom(), provincia.getCap(), provincia.getHab(), provincia.getDept(), provincia.getTemp(), provincia.getSens(), provincia.getHum())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def crearProvinciaFromForm(self):
        values = [e.get() for e in self.entries]
        provincia = None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror('ERROR de validación', str(e), parent=self)
        return provincia
    def clean(self):
        for entry in self.entries:
            entry.delete(0, tk.END)