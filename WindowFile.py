import tkinter as tk
from tkinter import ttk
from OpenFile import *

class WindowFile(tk.Frame):
    def __init__(self, master, callback=None) -> None:
        super().__init__(master)
        master.title('Cargar Archivo')
        master.geometry('600x200')
        master.config(background='sky blue')
        master.resizable(False,False)

        self.callback = callback

        #-------------------- Labels --------------------

        self.__lblruta = tk.Label(master, text='Ruta: ', font='Arial 12 bold', background='sky blue')
        self.__lblruta.place(x=25, y=40)

        #------------------- Entrys -------------------

        self.__entryfile = tk.Entry(master, width=75)
        self.__entryfile.place(x=100, y=41)

        #------------------- Buttons -------------------

        self.__btncharge = ttk.Button(master, text='Cargar', width=10, command=self.__charge)
        self.__btncharge.place(x=220, y=120)

        self.__btnback = ttk.Button(master, text='Regresar', width=10, command=self.__back)
        self.__btnback.place(x=450, y=120)

        #---------------- Mostrar ventana --------------
        master.focus()
        master.grab_set()
    

    #---------------------- Actions ---------------------------

    def __charge(self):
        if OpenFile.readFile(self.__entryfile.get()) is not None:
            self.callback(OpenFile.readFile(self.__entryfile.get()))
            self.master.destroy()


    def __back(self):
        self.master.destroy()