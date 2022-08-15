from doctest import master
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx
from ManagerFile import *
from WindowFile import *

class WindowMain(ttk.Frame):
    def __init__(self,master) -> None:
        super().__init__(master)
        master.title('Practica 1')
        master.geometry('850x650')
        master.config(background='sky blue')
        master.resizable(False,False)

        self.__mngfile = ManagerFile()

        #--------------------------------- Labels -------------------------------------------

        self.__lblcurso = ttk.Label(master,text='Lenguajes Formales y de Programación A+',font='Arial 16 bold', 
                                    background='sky blue')
        self.__lblcurso.place(x=100, y=30)

        self.__lblstudent = ttk.Label(master,text='Robin Omar Buezo Díaz', font='Arial 16 bold', background='sky blue')
        self.__lblstudent.place(x=100, y= 70)

        self.__lblcarne = ttk.Label(master,text='201944994', font='Arial 16 bold', background='sky blue')
        self.__lblcarne.place(x=100, y=110)

        #--------------------------------- buttons --------------------------------------------

        self.__buttonfile = tk.Button(master, text='Cargar Archivo', width=20, height=2, font='Arial 12 bold', command=self.__actButtonFile)
        self.__buttonfile.place(x=330, y=200)

        self.__buttonmanage = tk.Button(master, text='Gestionar Cursos', width=20, height=2, font='Arial 12 bold', command=self.__actButtonManage)
        self.__buttonmanage.place(x=330, y=290)

        self.__buttoncounting = tk.Button(master, text='Conteo de Créditos', width=20, height=2, font='Arial 12 bold', command=self.__actButtonCounting)
        self.__buttoncounting.place(x=330, y=380)

        self.__buttonexit = tk.Button(master, text='Salir', width=20, height=2, font='Arial 12 bold', command=self.__actButtonExit)
        self.__buttonexit.place(x=330, y=470)


    #----------------------- Actions -----------------------------

    def __actButtonFile(self):
        WindowFile(tk.Toplevel(),callback=self.__mngfile.setFile)

    def __actButtonManage(self):
        msgbx.showinfo('Action','Has presionado el boton Gestion')
    
    def __actButtonCounting(self):
        msgbx.showinfo('Action','Has presionado el boton Conteo')

    def __actButtonExit(self):
        self.master.destroy()
