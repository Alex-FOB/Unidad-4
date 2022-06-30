from newProvincia import NewProvincia

class Controlador:
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.selection = -1
        self.provincias = list(repo.getListaProvincias())
    def crearProvincia(self):
        nuevoProvincia = NewProvincia(self.vista).show()
        if nuevoProvincia:
            provincia = self.repo.addProvincia(nuevoProvincia)
            self.provincias.append(provincia)
            self.vista.addProvincia(provincia)
    def selectProvincia(self, index):
        self.selection = index
        provincia = self.provincias[index]
        self.vista.viewProvinciaInForm(provincia)
    def start(self):
        for provincia in self.provincias:
            self.vista.addProvincia(provincia)
        self.vista.mainloop()
    def exitSaveData(self):
        self.repo.saveDatos()