import tkinter as tk

from tkinter import ttk, font, messagebox

class Interfaz(tk.Tk):
    __sinIVA = None
    __IVA = None
    __conIVA = None
    __band = None
    def __init__(self):
        super().__init__()
        super().title('Ejercicio 2')
        fuente = font.Font(font='Arial', weight='normal')
        #INICIALIZACIÓN
        self.__sinIVA = tk.StringVar()
        self.__IVA = tk.StringVar()
        self.__conIVA = tk.StringVar()
        self.__band = tk.IntVar()
        self.frame = tk.Frame(self, borderwidth=2, relief='groove')
        self.tituloLBL = tk.Label(self.frame, text='Cálculo de IVA', font=('Arial', 20))
        self.sinLBL = tk.Label(self.frame, text='Precio sin IVA', font=fuente)
        self.ivaLBL = tk.Label(self.frame, text='IVA', font=fuente)
        self.conLBL = tk.Label(self.frame, text='Precio con IVA', font=fuente)
        self.ctext1 = tk.Entry(self.frame, textvariable=self.__sinIVA, font=fuente)
        self.ctext2 = tk.Entry(self.frame, textvariable=self.__IVA, font=fuente, state='disabled')
        self.ctext3 = tk.Entry(self.frame, textvariable=self.__conIVA, font=fuente, state='disabled')
        self.boton1 = tk.Button(self.frame, text='Calcular', command=self.calcular)
        self.boton2 = tk.Button(self.frame, text='Salir', command=quit)
        self.iva1 = ttk.Radiobutton(self.frame, text='IVA 21%', value=0, variable=self.__band)
        self.iva2 = ttk.Radiobutton(self.frame, text='IVA 10.5%', value=1, variable=self.__band)
        self.separador = ttk.Separator(self.frame, orient=tk.HORIZONTAL)
        #ESTILO
        self.boton1.configure(bg='#98FF98')
        self.boton2.configure(bg='#FF6961')
        #COLOCACIÓN
        self.frame.grid(column=0, row=0)
        self.tituloLBL.grid(column=1, row=0, padx=5, pady=5, sticky='NSEW')
        self.separador.grid(column=0, row=1, padx=5, pady=5, ipadx=300, columnspan=3)
        self.sinLBL.grid(column=0, row=2, padx=6, pady=5)
        self.ctext1.grid(column=1, row=2, padx=5, pady=5, columnspan=2, sticky='NSEW')
        self.iva1.grid(column=0, row=3, padx=6, pady=5, sticky='W')
        self.iva2.grid(column=0, row=4, padx=6, pady=5, sticky='W')
        self.ivaLBL.grid(column=0, row=5, padx=6, pady=5)
        self.ctext2.grid(column=1, row=5, padx=5, pady=5, columnspan=2, sticky='NSEW')
        self.conLBL.grid(column=0, row=6, padx=6, pady=5)
        self.ctext3.grid(column=1, row=6, padx=5, pady=5, columnspan=2, sticky='NSEW')
        self.boton1.grid(column=0, row=7, padx=6, pady=5, ipadx=30)
        self.boton2.grid(column=2, row=7, padx=6, pady=5, ipadx=30)
        self.__band.set(-1)
        self.ctext1.focus()
    def  calcular(self):
        try:
            if(self.__band.get() == 0):
                iva = float(self.__sinIVA.get())*0.21
                resultado = float(self.__sinIVA.get()) + iva
                self.__IVA.set('{}'.format(iva))
                self.__conIVA.set('{}'.format(resultado))
            elif(self.__band.get() == 1):
                iva = float(self.__sinIVA.get())*0.105
                resultado = float(self.__sinIVA.get()) + iva
                self.__IVA.set('{}'.format(iva))
                self.__conIVA.set('{}'.format(resultado))
            else:
                iva = float(self.__sinIVA.get())*0.21
                resultado = float(self.__sinIVA.get()) + iva
                self.__IVA.set('0')
                self.__conIVA.set('No hay resultado')
        except ValueError as e:
            messagebox.showerror('ERROR: valor ingresado', str(e),parent=self)