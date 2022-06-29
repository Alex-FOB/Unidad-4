import tkinter as tk

from pacienteList import PacienteList

from updatePacienteForm import UpdatePacienteForm

class PacientesView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lista de Pacientes')
        self.list = PacienteList(self, height=15)
        self.form = UpdatePacienteForm(self)
        self.boton = tk.Button(self, text='Agregar paciente')
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.boton.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        self.boton.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.selectPaciente)
        self.form.bind_save(ctrl.modPaciente)
        self.form.bind_IMC(ctrl.calcularIMC)
        self.form.bind_delete(ctrl.deletePaciente)
    def addPaciente(self, paciente):
        self.list.insertar(paciente)
    def modPaciente(self, paciente, index):
        self.list.mod(paciente, index)
    def deletePaciente(self, index):
        self.form.clean()
        self.list.delete(index)
    def getDetalles(self):
        return self.form.crearPacienteFromForm()
    def viewPacienteInForm(self, paciente):
        self.form.viewStatePacienteFormulario(paciente)