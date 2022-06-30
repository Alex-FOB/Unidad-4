from repositorioProvincias import RepositorioProvincias

from objectEncoder import ObjectEncoder

from controlador import Controlador

from provinciasView import ProvinciasView

def main():
    json = ObjectEncoder('Ejercicio 6/datos.json')
    repo = RepositorioProvincias(json)
    vista = ProvinciasView()
    ctrl = Controlador(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.exitSaveData()
if __name__ == '__main__':
    main()