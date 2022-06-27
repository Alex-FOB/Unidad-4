from paciente import Paciente

class Manejador:
    indice = 0
    __pacientes = None
    def __init__(self):
        self.__pacientes = []
    def getIndice(self, paciente):
        band = False
        i = 0
        while not band and i < len(self.__pacientes):
            if(self.__pacientes[i].rowid == paciente.rowid):
                band = True
            else:
                i += 1
        return i
    def addPaciente(self, paciente):
        paciente.rowid = Manejador.indice
        Manejador.indice += 1
        self.__pacientes.append(paciente)
    def getPacientes(self):
        return self.__pacientes
    def deletePaciente(self, paciente):
        indice = self.getIndice(paciente)
        self.__pacientes.pop(indice)
    def updatePaciente(self, paciente):
        indice = self.getIndice(paciente)
        self.__pacientes[indice] = paciente
    def toJSON(self):
        dic = dict(
            __class__=self.__class__.__name__,
            pacientes=[paciente.toJSON()for paciente in self.__pacientes]
        )
        return dic