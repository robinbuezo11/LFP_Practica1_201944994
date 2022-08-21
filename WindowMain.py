import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx
from ManagerFile import ManagerFile
from WindowFile import WindowFile
from WindowManager import WindowManager
from WindowCounting import WindowCounting

class WindowMain(ttk.Frame):
    def __init__(self,master) -> None:
        super().__init__(master)
        master.title('Practica 1')
        master.geometry('700x550')
        master.config(background='sky blue')
        master.resizable(False,False)

        self.__mngfile = ManagerFile()

        #--------------------------------- Labels -------------------------------------------

        self.__lblcurso = ttk.Label(master,text='Lenguajes Formales y de Programación A+',font='Arial 16 bold', 
                                    background='sky blue')
        self.__lblcurso.place(x=50, y=30)

        self.__lblstudent = ttk.Label(master,text='Robin Omar Buezo Díaz', font='Arial 16 bold', background='sky blue')
        self.__lblstudent.place(x=50, y= 70)

        self.__lblcarne = ttk.Label(master,text='201944994', font='Arial 16 bold', background='sky blue')
        self.__lblcarne.place(x=50, y=110)

        #--------------------------------- buttons --------------------------------------------

        self.__buttonfile = ttk.Button(master, text='Cargar Archivo', width=20, command=self.__actButtonFile)
        self.__buttonfile.place(x=260, y=200)

        self.__buttonmanage = ttk.Button(master, text='Gestionar Cursos', width=20, command=self.__actButtonManage)
        self.__buttonmanage.place(x=260, y=270)

        self.__buttoncounting = ttk.Button(master, text='Conteo de Créditos', width=20, command=self.__actButtonCounting)
        self.__buttoncounting.place(x=260, y=340)

        self.__buttonexit = ttk.Button(master, text='Salir', width=20, command=self.__actButtonExit)
        self.__buttonexit.place(x=260, y=410)

        #--------------------------------- Style ---------------------------------------------

        self.__style = ttk.Style(self)
        self.__style.configure('TButton', font=('Arial',12,'bold'), background='sky blue')



    #----------------------- Actions -----------------------------

    def __actButtonFile(self):
        WindowFile(tk.Toplevel(),self.__mngfile)

    def __actButtonManage(self):
        WindowManager(tk.Toplevel(),self.__mngfile)
    
    def __actButtonCounting(self):
        WindowCounting(tk.Toplevel(),self.__mngfile)

    def __actButtonExit(self):
        self.master.destroy()
