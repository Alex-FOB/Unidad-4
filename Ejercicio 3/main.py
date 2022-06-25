from interfaz import Interfaz

from tkinter import messagebox

from objectEncoder import ObjectEncoder

import requests

def lectorAPI():
    API = "https://www.dolarsi.com/api/api.php?type=dolar"
    try:
        response = requests.get(API)
        if(response.status_code == 200):
            content = response.content
            file = open('Ejercicio 3/api.json', 'wb')
            file.write(content)
            file.close()
    except:
        messagebox.showerror(title='ERROR', message='ERROR: en la API')
if __name__ == '__main__':
    lectorAPI()
    jsonF = ObjectEncoder()
    lista = jsonF.leerJSONArchivo('Ejercicio 3/api.json')
    control = jsonF.crearManejador(lista)
    if(control != None):
        app = Interfaz(control)
        app.mainloop()