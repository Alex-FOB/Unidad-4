import tkinter as tk

from provinciaForm import ProvinciaForm

class NewProvincia(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = ProvinciaForm(self)
        self.boton = tk.Button(self, text='Confirmar', command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.boton.pack(pady=10)
    def confirmar(self):
        self.provincia = self.form.crearProvinciaFromForm()
        if self.provincia:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia