import tkinter as tk

class CalcularIMC(tk.Toplevel):
    def __init__(self, parent, imc, estado):
        super().__init__(parent)
        self.imc = tk.StringVar()
        self.estado = tk.StringVar()
        self.imc.set('{}'.format(imc))
        self.estado.set('{}'.format(estado))
        self.lbl1 = tk.Label(self, text='IMC')
        self.lbl2 = tk.Label(self, text='Composición Corporal')
        self.ctext1 = tk.Entry(self, textvariable=self.imc, state='readonly')
        self.ctext2 = tk.Entry(self, textvariable=self.estado, state='readonly')
        self.boton = tk.Button(self, text='Volver', command=self.destroy)
        self.lbl1.grid(column=0, row=0, padx=5, pady=5)
        self.ctext1.grid(column=1, row=0, padx=5, pady=5, ipadx=10)
        self.lbl2.grid(column=0, row=1, padx=5, pady=5)
        self.ctext2.grid(column=1, row=1, padx=5, pady=5, ipadx=10)
        self.boton.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
    def show(self):
        self.grab_set()
        self.wait_window()