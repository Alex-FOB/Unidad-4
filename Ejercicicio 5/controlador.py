from newPaciente import NewPaciente

from calcularIMC import CalcularIMC

class Controlador:
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.selection = -1
        self.pacientes = list(repo.getListaPacientes())
    def crearPaciente(self):
        nuevoPaciente = NewPaciente(self.vista).show()
        if nuevoPaciente:
            paciente = self.repo.addPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.addPaciente(paciente)
    def selectPaciente(self, index):
        self.selection = index
        paciente = self.pacientes[index]
        self.vista.viewPacienteInForm(paciente)
    def modPaciente(self):
        if(self.selection == -1):
            return
        rowid = self.pacientes[self.selection].rowid
        detallesPaciente = self.vista.getDetalles()
        detallesPaciente.rowid = rowid
        paciente = self.repo.modPaciente(detallesPaciente)
        self.pacientes[self.selection] = paciente
        self.vista.modPaciente(paciente, self.selection)
        self.selection = -1
    def calcularIMC(self):
        if(self.selection == -1):
            return
        paciente = self.pacientes[self.selection]
        imc = self.repo.calcularIMC(paciente)
        imc = round(imc, 2)
        estado = self.repo.estado(imc)
        CalcularIMC(self.vista, imc, estado).show()
    def deletePaciente(self):
        if(self.selection == -1):
            return
        paciente = self.pacientes[self.selection]
        self.repo.deletePaciente(paciente)
        self.pacientes.pop(self.selection)
        self.vista.deletePaciente(self.selection)
        self.selection = -1
    def start(self):
        for paciente in self.pacientes:
            self.vista.addPaciente(paciente)
        self.vista.mainloop()
    def exitSaveData(self):
        self.repo.saveDatos()