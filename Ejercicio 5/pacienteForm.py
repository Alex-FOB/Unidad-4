import tkinter as tk

from tkinter import messagebox

from paciente import Paciente

class PacienteForm(tk.LabelFrame):
    fields = ('Apellido', 'Nombre', 'Teléfono', 'Altura', 'Peso')
    def __init__(self, master, **kwargs):
        super().__init__(master, text='Paciente', padx=10, pady=10, **kwargs)
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
    def viewStatePacienteFormulario(self, paciente):
        values = (paciente.getApe(), paciente.getNom(), paciente.getTelefono(), paciente.getAltura(), paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def crearPacienteFromForm(self):
        values = [e.get() for e in self.entries]
        paciente = None
        try:
            paciente = Paciente(*values)
        except ValueError as e:
            messagebox.showerror('ERROR de Validación', str(e), parent=self)
        return paciente
    def clean(self):
        for entry in self.entries:
            entry.delete(0, tk.END)