import tkinter as tk

from functools import partial

from tkinter import font, messagebox

from fraccion import Fraccion

class Interfaz(tk.Tk):
    __in = None
    __out = None
    __band = None
    __bandF = None
    __num1 = None
    __num2 = None
    def __init__(self):
        super().__init__()
        super().title('Ejercicio 4')
        fuente = font.Font(font='Arial', weight='normal')
        #INICIALIZACIÓN
        self.__band = False
        self.__bandF = False
        self.__num1 = None
        self.__num2 = None
        self.__in = tk.StringVar()
        self.__out = tk.StringVar()
        self.frame1 = tk.Frame(self, borderwidth=2, relief='groove')
        self.frame2 = tk.Frame(self, borderwidth=2, relief='groove')
        self.ctext1 = tk.Entry(self.frame1, textvariable=self.__in, font=fuente, state='readonly')
        self.ctext2 = tk.Entry(self.frame1, textvariable=self.__out, font=fuente, state='readonly')
            #NUMÉRICOS
        self.boton0 = tk.Button(self.frame2, text='0', command=partial(self.ponerNum, '0'))
        self.boton1 = tk.Button(self.frame2, text='1', command=partial(self.ponerNum, '1'))
        self.boton2 = tk.Button(self.frame2, text='2', command=partial(self.ponerNum, '2'))
        self.boton3 = tk.Button(self.frame2, text='3', command=partial(self.ponerNum, '3'))
        self.boton4 = tk.Button(self.frame2, text='4', command=partial(self.ponerNum, '4'))
        self.boton5 = tk.Button(self.frame2, text='5', command=partial(self.ponerNum, '5'))
        self.boton6 = tk.Button(self.frame2, text='6', command=partial(self.ponerNum, '6'))
        self.boton7 = tk.Button(self.frame2, text='7', command=partial(self.ponerNum, '7'))
        self.boton8 = tk.Button(self.frame2, text='8', command=partial(self.ponerNum, '8'))
        self.boton9 = tk.Button(self.frame2, text='9', command=partial(self.ponerNum, '9'))
            #OPERACIÓN
        self.botonADD = tk.Button(self.frame2, text='+', command=partial(self.ponerOp, '+'))
        self.botonSUB = tk.Button(self.frame2, text='-', command=partial(self.ponerOp, '-'))
        self.botonMUL = tk.Button(self.frame2, text='*', command=partial(self.ponerOp, '*'))
        self.botonDIV = tk.Button(self.frame2, text='%', command=partial(self.ponerOp, '%'))
            #EXTRAS
        self.botonDEL = tk.Button(self.frame2, text='DEL', command=self.borrar1)
        self.botonAC = tk.Button(self.frame2, text='AC', command=self.borrarALL)
        self.botonFRAC = tk.Button(self.frame2, text='/', command=self.ponerFrac)
        self.botonRESULTADO = tk.Button(self.frame2, text='=', command=self.calcular)
        #COLOCACIÓN
        self.frame1.grid(column=0, row=0)
        self.ctext1.grid(column=0, row=0, padx=5, pady=5)
        self.ctext2.grid(column=0, row=1, padx=5, pady=5)
        self.frame2.grid(column=0, row=1)
            #OPERACIÓN
        self.botonADD.grid(column=0, row=0, padx=5, pady=5, ipadx=25)
        self.botonSUB.grid(column=1, row=0, padx=5, pady=5, ipadx=25)
        self.botonMUL.grid(column=0, row=1, padx=5, pady=5, ipadx=25)
        self.botonDIV.grid(column=1, row=1, padx=5, pady=5, ipadx=25)
            #NUMÉRICOS
        self.boton9.grid(column=2, row=2, padx=5, pady=5, ipadx=25)
        self.boton8.grid(column=1, row=2, padx=5, pady=5, ipadx=25)
        self.boton7.grid(column=0, row=2, padx=5, pady=5, ipadx=25)
        self.boton6.grid(column=2, row=3, padx=5, pady=5, ipadx=25)
        self.boton5.grid(column=1, row=3, padx=5, pady=5, ipadx=25)
        self.boton4.grid(column=0, row=3, padx=5, pady=5, ipadx=25)
        self.boton3.grid(column=2, row=4, padx=5, pady=5, ipadx=25)
        self.boton2.grid(column=1, row=4, padx=5, pady=5, ipadx=25)
        self.boton1.grid(column=0, row=4, padx=5, pady=5, ipadx=25)
        self.boton0.grid(column=1, row=5, padx=5, pady=5, ipadx=25)
            #EXTRAS
        self.botonDEL.grid(column=2, row=1, padx=5, pady=5, ipadx=20)
        self.botonAC.grid(column=2, row=0, padx=5, pady=5, ipadx=21)
        self.botonFRAC.grid(column=0, row=5, padx=5, pady=5, ipadx=25)
        self.botonRESULTADO.grid(column=2, row=5, padx=5, pady=5, ipadx=25)
        self.ctext2.focus_set()
        self.__out.set('Resultado:')
    def buscar(self, text, lista):
        band = -1
        i = 0
        while band == -1 and i < len(lista):
            if(lista[i] in text):
                band = i
            i+=1
        return band
    def crearFraccion(self, num):
        fraccion = None
        numerador = ''
        denominador = ''
        numerador = num[0]
        if(len(num) > 1):
            denominador = num[1]
        if(numerador == ''):
            numerador = '0'
        if(denominador == ''):
            denominador = '1'
        fraccion = Fraccion(int(numerador), int(denominador))
        return fraccion
    def validarCalculo(self, text):
        resultado = None
        lista = ['+', '-', '*', '%']
        op = self.buscar(text, lista)
        if(op != -1):
            text = text.split(lista[op])
            num1 = text[0]
            num2 = text[1]
            #VERIFICAR QUE ESTÁN VACÍAS
            if(num1 == ''):
                num1 = '0'
            if(num2 == ''):
                num2 = '0'
            #CREAR INSTACIAS DE Fracción
                #NUM1
            num1 = num1.split('/')
            self.__num1 = self.crearFraccion(num1)
                #NUM2
            num2 = num2.split('/')
            self.__num2 = self.crearFraccion(num2)
            resultado = lista[op]
        else:
            resultado = '='
            text = text.split('/')
            self.__num1 = self.crearFraccion(text)
        return resultado
    def validarOp(self, caracter):
        band = False
        if(caracter == '+'):
            band = True
        elif(caracter == '-'):
            band = True
        elif(caracter == '*'):
            band = True
        elif(caracter == '%'):
            band = True
        return band
    def validarFrac(self,text):
        band = False
        if('/' not in text or self.__bandF == False):
            band = True
            self.__bandF = True
        return band
    def ponerNum(self, num):
        text = self.__in.get()
        text += num
        self.__in.set(text)
    def ponerOp(self, op):
        text = self.__in.get()
        if(not self.__band):
            text += op
            self.__in.set(text)
            self.__band = True
            self.__bandF = False
    def ponerFrac(self):
        text = self.__in.get()
        if(self.validarFrac(text)):
            text += '/'
            self.__in.set(text)
            self.__band3 = False
    def borrar1(self):
        text = self.__in.get()
        if(len(text) != 0):
            rango = len(text)-1
            self.__in.set(text[0:rango])
            if(self.validarOp(text[rango])):
                self.__band = False
            if(text[rango] == '/'):
                self.__bandF = False
            self.__out.set('Resultado:')
    def borrarALL(self):
        self.__in.set('')
        self.__band = False
        self.__out.set('Resultado:')
    def calcular(self):
        resultado = 0
        text = self.__in.get()
        op = self.validarCalculo(text)
        if(op == '+'):
            resultado = self.__num1 + self.__num2
        elif(op == '-'):
            resultado = self.__num1 - self.__num2
        elif(op == '*'):
            resultado = self.__num1 * self.__num2
        elif(op == '%'):
            resultado = self.__num1 % self.__num2
        elif(op == '='):
            resultado = self.__num1
        resultado.simplificar()
        self.__out.set('Resultado: {}'.format(resultado))