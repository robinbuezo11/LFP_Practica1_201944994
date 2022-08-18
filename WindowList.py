import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx
from ManagerFile import ManagerFile

class WindowList(tk.Frame):
    def __init__(self, master, mfile=ManagerFile()) -> None:
        self.__mngfile = mfile
        super().__init__(master)
        master.title('Listar Cursos')
        master.geometry('1200x600')
        master.config(background='sky blue')
        #master.resizable(False,False)

        #----------------------------- Tabla -----------------------------
        
        columns = ('Código','Nombre','Prerrequisitos','Obligatorio','Semestre','Créditos','Estado')
        self.__table = ttk.Treeview(master,columns=columns,show='headings')

        self.__table.column('#1',width=83,anchor='center')
        self.__table.column('#2',width=83,anchor='center')
        self.__table.column('#3',width=83,anchor='center')
        self.__table.column('#4',width=83,anchor='center')
        self.__table.column('#5',width=83,anchor='center')
        self.__table.column('#6',width=83,anchor='center')
        self.__table.column('#7',width=83,anchor='center')
        
        self.__table.heading('#1',text='Código')
        self.__table.heading('#2',text='Nombre')
        self.__table.heading('#3',text='Prerrequisitos')
        self.__table.heading('#4',text='Obligatorio')
        self.__table.heading('#5',text='Semestre')
        self.__table.heading('#6',text='Créditos')
        self.__table.heading('#7',text='Estado')

        self.__setvalues()

        #self.__table.grid(row=0,column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.__table.place(x=10,y=10,relwidth=0.98,relheight=0.96)

        master.focus()
        master.grab_set()

    def __setvalues(self):
        if self.__mngfile.getFile() is not None:
            for d in self.__mngfile.getFile():
                self.__table.insert('',tk.END,values=d)
        else:
            msgbx.showwarning('Vacío','No hay ningún dato')
