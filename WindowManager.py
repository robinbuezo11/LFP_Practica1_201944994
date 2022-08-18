from ManagerFile import ManagerFile
import tkinter as tk
from tkinter import messagebox as msgbx
from tkinter import ttk
from WindowList import WindowList

class WindowManager(tk.Frame):
    def __init__(self, master, mfile = ManagerFile()) -> None:
        self.__mfile = mfile
        super().__init__(master)
        master.title('Gestionar Cursos')
        master.geometry('400x600')
        master.config(background='sky blue')
        master.resizable(False,False)

        #------------------------------ Buttons --------------------------------

        self.__buttonlist = ttk.Button(master, text='Listar Cursos', width=20, command=self.__actButtonList)
        self.__buttonlist.place(x=110, y=80)

        self.__buttonadd = ttk.Button(master, text='Agregar Cursos', width=20, command=self.__actButtonAdd)
        self.__buttonadd.place(x=110, y=180)

        self.__buttonedit = ttk.Button(master, text='Editar Curso', width=20, command=self.__actButtonEdit)
        self.__buttonedit.place(x=110, y=280)

        self.__buttondelete = ttk.Button(master, text='Eliminar Curso', width=20, command=self.__actButtonDelete)
        self.__buttondelete.place(x=110, y=380)

        self.__buttonexit = ttk.Button(master, text='Regresar', width=20, command=self.__actButtonExit)
        self.__buttonexit.place(x=110, y=480)
        
        #---------------- Mostrar ventana --------------
        master.focus()
        master.grab_set()


    #----------------------- Actions -----------------------------

    def __actButtonList(self):
        WindowList(tk.Toplevel(self),self.__mfile)

    def __actButtonAdd(self):
        msgbx.showinfo('Action','Has presionado el boton Agregar')
    
    def __actButtonEdit(self):
        msgbx.showinfo('Action','Has presionado el boton Editar')

    def __actButtonDelete(self):
        msgbx.showinfo('Action','Has presionado el boton Eliminar')

    def __actButtonExit(self):
        self.master.destroy()
