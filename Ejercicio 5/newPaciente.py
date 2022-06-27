import tkinter as tk

from pacienteForm import PacienteForm

class NewPaciente(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente = None
        self.form = PacienteForm(self)
        self.boton = tk.Button(self, text='Confirmar', command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.boton.pack(pady=10)
        def confirmar(self):
            self.paciente = self.form.crearPacienteFromForm()
            if self.paciente:
                self.destroy()
        def show(self):
            self.grab_set()
            self.wait_window()
            return self.paciente