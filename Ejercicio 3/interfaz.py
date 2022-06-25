from functools import partial

import tkinter as tk

from tkinter import Toplevel, ttk, font, messagebox

class Interfaz(tk.Tk):
    __manejador = None
    __dolar = None
    __nombre = None
    def __init__(self, manejador):
        super().__init__()
        super().title('Ejercicio 3')
        fuente = font.Font(font='Arial', weight='normal')
        #INICIALIZACIÓN
        self.__manejador = manejador
        self.__dolar = tk.StringVar()
        self.__nombre = tk.StringVar()
        self.frame = tk.Frame(self, borderwidth=2, relief='groove')
        self.tituloLBL = tk.Label(self.frame, text='Conversor de Moneda', font=('Arial', 20))
        self.separador = ttk.Separator(self.frame, orient=tk.HORIZONTAL)
        self.boton1 = tk.Button(self.frame, text='Dolar Oficial', command=partial(self.calcularVentana, 0))
        self.boton2 = tk.Button(self.frame, text='Dolar Blue', command=partial(self.calcularVentana, 1))
        self.boton3 = tk.Button(self.frame, text='Dolar Mayorista Banco', command=partial(self.calcularVentana, 2))
        self.boton4 = tk.Button(self.frame, text='Dolar BCRA de Referencia', command=partial(self.calcularVentana, 3))
        self.boton5 = tk.Button(self.frame, text='Dolar Banco Nacional Billete', command=partial(self.calcularVentana, 4))
        self.boton6 = tk.Button(self.frame, text='Dolar Banco Nación Público', command=partial(self.calcularVentana, 5))
        #COLOCACIÓN
        self.frame.grid(column=0, row=0)
        self.tituloLBL.grid(column=0, row=0, padx=5, pady=5, sticky='NSEW')
        self.separador.grid(column=0, row=1, padx=5, pady=5, ipadx=200)
        self.boton1.grid(column=0, row=2, padx=5, pady=5, ipadx=100)
        self.boton2.grid(column=0, row=3, padx=5, pady=5, ipadx=100)
        self.boton3.grid(column=0, row=4, padx=5, pady=5, ipadx=100)
        self.boton4.grid(column=0, row=5, padx=5, pady=5, ipadx=100)
        self.boton5.grid(column=0, row=6, padx=5, pady=5, ipadx=100)
        self.boton6.grid(column=0, row=7, padx=5, pady=5, ipadx=100)
    def calcularVentana(self, band):
        if(band == 0):
            self.__nombre.set('Oficial')
            self.newVentana()
        elif(band == 1):
            self.__nombre.set('Blue')
            self.newVentana()
        elif(band == 2):
            self.__nombre.set('Mayorista Bancos')
            self.newVentana()
        elif(band == 3):
            self.__nombre.set('BCRA de Referencia')
            self.newVentana()
        elif(band == 4):
            self.__nombre.set('Banco Nación Billete')
            self.newVentana()
        elif(band == 5):
            self.__nombre.set('Banco Nación Público')
            self.newVentana()
    def calcularDolar(self, *args):
        if(self.__dolar.get() != ''):
            try:
                nombre = self.__nombre.get()
                dolar = float(self.__dolar.get())
                pesos = self.__manejador.calcular(nombre, self.__modo, dolar)
                pesos = round(pesos, 2)
                self.__resultado.set('Es equivalente a  {}'.format(pesos))
            except ValueError:
                messagebox.showerror(title='ERROR: valor inválido', message='Debe ingresar un valor numérico')
                self.__resultado.set('Es equivalente a ')
        else:
            self.__resultado.set('Es equivalente a ')
    def newVentana(self):
        self.__ventana1 = Toplevel()
        #self.__ventana1.geometry('250x150+50+50')
        self.__ventana1.resizable(0,0)
        self.__ventana1.title(self.__nombre)
        #CONTENIDO------------------------------------------------------------------------------
        self.boton1 = tk.Button(self.__ventana1, text='Calcular dolar de compra', command=partial(self.newVentanaCalculo, 0)).grid(column=0, row=0, padx=5, pady=5, ipadx=30)
        self.boton2 = tk.Button(self.__ventana1, text='Calcular dolar de venta', command=partial(self.newVentanaCalculo, 1)).grid(column=0, row=1, padx=5, pady=5, ipadx=30)
        #---------------------------------------------------------------------------------------
        self.__ventana1.transient(master=self)
        self.__ventana1.grab_set()
        self.wait_window(self.__ventana1)#modificar
        def testApp():
            mi_app = Interfaz()
            return 0
    def newVentanaCalculo(self, modo):
        self.__dolar.set('')
        self.__ventana2 = Toplevel()
        #self.__ventana2.geometry('275x125+50+50')
        self.__ventana2.resizable(0,0)
        self.__ventana2.title('Calcular: '+ self.__nombre.get())
        #CONTENIDO------------------------------------------------------------------------------
        self.__resultado = tk.StringVar()
        self.__modo = modo
        self.__resultado.set('Es equivalente a ')
        fuente = font.Font(font='Arial', weight='normal')
        self.LBL1 = tk.Label(self.__ventana2, text='Dólares', font=fuente).grid(column=1, row=0, padx=5, pady=5)
        self.LBL2 = tk.Label(self.__ventana2, textvariable=self.__resultado, font=fuente).grid(column=0, row=1, padx=5, pady=5, sticky='W')
        self.LBL3 = tk.Label(self.__ventana2, text='Pesos', font=fuente).grid(column=1, row=1, padx=5, pady=5)
        self.boton = tk.Button(self.__ventana2, text='Salir', command=self.__ventana2.destroy).grid(column=0, row=2, padx=5, pady=5, columnspan=2)
        self.ctext = tk.Entry(self.__ventana2, textvariable=self.__dolar, font=fuente).grid(column=0, row=0, padx=5, pady=5)
        #---------------------------------------------------------------------------------------
        self.__ventana2.transient(master=self)
        self.__ventana2.grab_set()
        self.__dolar.trace('w', self.calcularDolar)
        self.wait_window(self.__ventana2)#modificar
        def testApp():
            mi_app = Interfaz()
            return 0