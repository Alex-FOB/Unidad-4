from cgitb import handler
import tkinter as tk

class ProvinciaList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.listBox = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.listBox.yview)
        self.listBox.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listBox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    def insertar(self, provincia, index = tk.END):
        text = '{}'.format(provincia.getNom())
        self.listBox.insert(index, text)
    def bind_doble_click(self, callback):
        handler = lambda _:callback(self.listBox.curselection()[0])
        self.listBox.bind('<Double-Button-1>', handler)