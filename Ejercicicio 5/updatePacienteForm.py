import tkinter as tk

from tkinter import messagebox

from paciente import Paciente

from pacienteForm import PacienteForm

class UpdatePacienteForm(PacienteForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.botonSave = tk.Button(self, text='Guardar')
        self.botonDelete = tk.Button(self, text='Borrar')
        self.botonIMC = tk.Button(self, text='Ver IMC')
        self.botonSave.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.botonDelete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.botonIMC.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
    def bind_save(self, callback):
        self.botonSave.config(command=callback)
    def bind_delete(self, callback):
        self.botonDelete.config(command=callback)
    def bind_IMC(self, callback): #REVISAR
        self.botonIMC.config(command=callback)