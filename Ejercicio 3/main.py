from dolar import Dolar

from manejador import Manejador

from interfaz import Interfaz

def lector():
    lista = [{"casa":{"nombre":"Oficial","compra":"123,050","venta":"129,050","agencia":"344","observaciones":{},"geolocalizacion":{"latitud":{},"longitud":{}},"telefono":"0810-666-4444","direccion":{},"decimales":"3"}},
                {"casa":{"nombre":"Blue","compra":"221,000","venta":"224,000","agencia":"380","observaciones":{},"geolocalizacion":{"latitud":{},"longitud":{}},"telefono":{},"direccion":{},"decimales":"3"}},
                {"casa":{"nombre":"Mayorista Bancos","compra":"123,860","venta":"124,060","agencia":"44","geolocalizacion":{"latitud":"-34.6033922","longitud":"-58.439710"},"telefono":"4556-8995","direccion":"Uruguay 4532","observaciones":{},"decimales":"3"}},
                {"casa":{"nombre":"BCRA de Referencia","compra":"122,465","venta":"129,049","agencia":"49","observaciones":{},"decimales":"3"}},
                {"casa":{"nombre":"Banco Nación Billete","compra":"122,750","venta":"128,750","agencia":"47","observaciones":{},"decimales":"3"}},
                {"casa":{"nombre":"Banco Nación Público","compra":"122,750","venta":"128,750","agencia":"210","observaciones":{},"decimales":"3"}}]
    control = Manejador()
    for casa in lista:
        if(casa['casa'] != None):
            dolar = casa['casa']
            unDolar = Dolar(dolar['nombre'], dolar['compra'], dolar['venta'])
            control.addDolar(unDolar)
    return control
if __name__ == '__main__':
    control = lector()
    app = Interfaz(control)
    app.mainloop()