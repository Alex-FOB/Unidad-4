from repositorioPacientes import RepositorioPacientes

from pacientesView import PacientesView

from controlador import Controlador

from objectEncoder import ObjectEncoder

def main():
    json = ObjectEncoder('Ejercicio 5/pacientes.json')
    repo = RepositorioPacientes(json)
    vista = PacientesView()
    ctrl = Controlador(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.exitSaveData()
if __name__ == '__main__':
    main()