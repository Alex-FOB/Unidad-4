import re

class Paciente:
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __ape = None
    __nom = None
    __telefono = None
    __altura = None
    __peso = None
    def __init__(self, apellido, nombre, telefono, altura, peso):
        self.__ape = self.validar(apellido, 'ERROR: apellido es requerido')
        self.__nom = self.validar(nombre, 'ERROR: nombre es requerido')
        self.__telefono = self.validarFormato(telefono, self.telefonoRegex, 'ERROR: teléfono es requerido')
        self.__altura = float(self.validar(str(altura), 'ERROR: altura es requerido').replace(',', '.'))
        self.__peso = float(self.validar(str(peso), 'ERROR: peso es requerido').replace(',', '.'))
    def getApe(self):
        return self.__ape
    def getNom(self):
        return self.__nom
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def validar(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def validarFormato(self, valor, regex, mensaje):
        if(not valor or not regex.match(valor)):
            raise ValueError(mensaje)
        return valor
    def toJSON(self):
        dic = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                apellido=self.__ape,
                nombre=self.__nom,
                telefono=self.__telefono,
                altura=self.__altura,
                peso=self.__peso
            )
        )
        return dic