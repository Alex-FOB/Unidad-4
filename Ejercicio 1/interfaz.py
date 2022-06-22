import tkinter as tk

from tkinter import Toplevel, ttk, font

class Interfaz(tk.Tk):
    __peso = None
    __altura = None
    __resultado = None
    __estado = None
    def __init__(self):
        super().__init__()
        super().title('Ejercicio 1')
        fuente = font.Font(weight='bold')
        #INICIALIZACIÓN
        self.__peso = tk.StringVar()
        self.__altura = tk.StringVar()
        self.__resultado = tk.StringVar()
        self.__estado = tk.StringVar()
        self.__resultado.set('----')
        self.__estado.set('Sin resultado')
        self.frame1 = tk.Frame(self, borderwidth=2, relief='groove')
        self.frame2 = tk.Frame(self.frame1, borderwidth=1, relief='groove')
        self.titulo = tk.Label(self.frame1, text='Calculadora de IMC', font=('bold', 20))
        self.separ1 = ttk.Separator(self.frame1, orient=tk.HORIZONTAL)
        self.separ2 = ttk.Separator(self.frame1, orient=tk.HORIZONTAL)
        self.separ3 = ttk.Separator(self.frame1, orient=tk.HORIZONTAL)
        self.cmLBL = tk.Label(self.frame1, text='cm', font=fuente)
        self.kgLBL = tk.Label(self.frame1,text='kg', font=fuente)
        self.alturaLBL = tk.Label(self.frame1, text='Altura', font=fuente)
        self.pesoLBL = tk.Label(self.frame1, text='Peso', font=fuente)
        self.textLBL = tk.Label(self.frame2, text='Tu Indice de Masa Corporal (IMC) es', font=fuente)
        self.resultLBL = tk.Label(self.frame2, textvariable=self.__resultado, font=fuente)
        self.stateLBL = tk.Label(self.frame2, textvariable=self.__estado, font=('bold', 18))
        self.ctext1 = tk.Entry(self.frame1, textvariable=self.__altura, font=fuente)
        self.ctext2 = tk.Entry(self.frame1, textvariable=self.__peso, font=fuente)
        self.boton1 = tk.Button(self.frame1, text='Calcular', command=self.calcular)
        self.boton2 = tk.Button(self.frame1, text='Limpiar', command=self.limpiar)
        self.boton1.configure(bg='#98FF98')
        self.boton2.configure(bg='#98FF98')
        #ESTILO
        self.frame1.configure(bg='white')
        self.frame2.configure(bg='white')
        self.titulo.configure(bg='white')
        self.alturaLBL.configure(bg='white')
        self.pesoLBL.configure(bg='white')
        self.cmLBL.configure(bg='grey')
        self.kgLBL.configure(bg='grey')
        self.textLBL.configure(bg='white')
        self.resultLBL.configure(bg='white')
        self.stateLBL.configure(bg='white')
        #COLOCACIÓN
        self.frame1.grid(column=0, row=0)
        self.titulo.grid(column=2,row=0, padx=5, pady = 5)
        self.separ1.grid(column=0, row=1, columnspan=4, padx=5, pady = 5, ipadx=300)
        self.alturaLBL.grid(column=0, row=2, padx=5, pady = 5)
        self.ctext1.grid(column=1, row=2, columnspan=3, padx=5, pady = 5, ipadx=200)
        self.cmLBL.grid(column=4, row=2)
        self.separ2.grid(column=0,row=3, columnspan=4, padx=5, pady = 5, ipadx=300)
        self.pesoLBL.grid(column=0, row=4, padx=5, pady = 5)
        self.ctext2.grid(column=1,row=4, columnspan=3, padx=5, pady = 5, ipadx=200)
        self.kgLBL.grid(column=4, row=4)
        self.separ3.grid(column=0, row=5, columnspan=4, padx=5, pady = 5, ipadx=300)
        self.boton1.grid(column=1, row=6, padx=5, pady = 5, ipadx=50)
        self.boton2.grid(column=3, row=6, padx=5, pady = 5, ipadx=50)
        self.frame2.grid(column=1, row=8, columnspan=3, padx=5, pady = 5)
        self.textLBL.grid(column=0, row=0, padx=5, pady = 5)
        self.resultLBL.grid(column=1, row=0, padx=5, pady = 5)
        self.stateLBL.grid(column=0, row=1, columnspan=1, padx=5, pady = 5)
        self.ctext1.focus_set()
    def calcular(self):
        try:
            peso = float(self.__peso.get())
            altura = float(self.__altura.get())/100
            resultado = peso/(altura*2)
            self.cambioFondo(resultado)
            self.__resultado.set('{:.3}'.format(resultado))
        except ValueError:
            self.error()
    def limpiar(self):
        self.__peso.set('')
        self.__altura.set('')
        self.__resultado.set('----')
        self.cambioFondo(-1)
        self.ctext1.focus_set()
    def cambioFondo(self, resultado):
        if(resultado < 18.5 and resultado > 0):
            self.__estado.set('Peso inferior al normal')
            self.frame2.configure(bg='#FDFD96')
            self.textLBL.configure(bg='#FDFD96')
            self.resultLBL.configure(bg='#FDFD96')
            self.stateLBL.configure(bg='#FDFD96')
        elif(resultado < 25 and resultado > 18.5):
            self.__estado.set('Peso normal')
            self.frame2.configure(bg='#98FF98')
            self.textLBL.configure(bg='#98FF98')
            self.resultLBL.configure(bg='#98FF98')
            self.stateLBL.configure(bg='#98FF98')
        elif(resultado < 30 and resultado > 25):
            self.__estado.set('Peso superior al normal')
            self.frame2.configure(bg='#FDFD96')
            self.textLBL.configure(bg='#FDFD96')
            self.resultLBL.configure(bg='#FDFD96')
            self.stateLBL.configure(bg='#FDFD96')
        elif(resultado < 0):
            self.frame2.configure(bg='white')
            self.textLBL.configure(bg='white')
            self.resultLBL.configure(bg='white')
            self.stateLBL.configure(bg='white')
        else:
            self.__estado.set('Obesidad')
            self.frame2.configure(bg='#FF6961')
            self.textLBL.configure(bg='#FF6961')
            self.resultLBL.configure(bg='#FF6961')
            self.stateLBL.configure(bg='#FF6961')
    #AÑADIDO-----------------------------------------------------------------------
    def error(self):
        self.ventanaError()
        self.limpiar()
    def ventanaError(self):
        self.__error = Toplevel()
        self.__error.geometry('250x150+50+50')
        self.__error.resizable(0,0)
        self.__error.title('ERROR')
        label = ttk.Label(self.__error, text='ERROR: el valor ingresado es inválido')
        boton = ttk.Button(self.__error, text='Cerrar', command=self.__error.destroy)
        label.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        boton.pack(side=tk.BOTTOM, padx=20, pady=20)
        self.__error.transient(master=self)
        self.__error.grab_set()
        self.wait_window(self.__error)
        def testApp():
            mi_app = Interfaz()
            return 0