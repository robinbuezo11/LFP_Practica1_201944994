from ManagerFile import ManagerFile
import tkinter as tk
from tkinter import messagebox as msgbx
from tkinter import ttk
from WindowAdd import WindowAdd

class WindowManager(tk.Frame):
    def __init__(self, master, mngfile = ManagerFile()) -> None:
        self.__mfile = mngfile
        super().__init__(master)
        master.title('Gestionar Cursos')
        master.geometry('1200x700')
        master.config(background='sky blue')
        master.resizable(False,False)

        #----------------------------- Entry -----------------------------

        self.__entrycourse = tk.Entry(master)
        self.__entrycourse.place(x=350, y=20, relwidth=0.2, height=25)

        #------------------------------ Buttons --------------------------------

        self.__btnsearch = ttk.Button(master, text='Buscar', command=self.__searchvalue)
        self.__btnsearch.place(x=650, y=20, relwidth=0.1)

        self.__buttonadd = ttk.Button(master, text='Agregar Cursos', command=self.__actButtonAdd)
        self.__buttonadd.place(x=100, y=615)

        self.__buttonedit = ttk.Button(master, text='Editar Curso', command=self.__actButtonEdit)
        self.__buttonedit.place(x=550, y=615)

        self.__buttondelete = ttk.Button(master, text='Eliminar Curso', command=self.__actButtonDelete)
        self.__buttondelete.place(x=1055, y=20)

        self.__buttonexit = ttk.Button(master, text='Regresar', command=self.__actButtonExit)
        self.__buttonexit.place(x=1055, y=615)

        #----------------------------- Tabla -----------------------------
        
        columns = ('Código','Nombre','Prerrequisitos','Obligatorio','Semestre','Créditos','Estado')
        self.__table = ttk.Treeview(master,columns=columns,show='headings')

        self.__table.column('#1',width=33,anchor='center')
        self.__table.column('#2',width=133)
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

        #self.__table.grid(row=0,column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.__table.place(x=10,y=70,relwidth=0.98,relheight=0.75)

        """#----------------- Scrollbar -------------------

        self.__scroll = tk.Scrollbar(self.__table, command=self.__table.yview_scroll)
        self.__scroll.pack(side=RIGHT,fill=Y)"""
        
        #---------------- Mostrar ventana ------------------------
        master.focus()
        master.grab_set()

        self.__setvalues()

    #----------------------- Actions -----------------------------

    def __actButtonAdd(self):
        WindowAdd(tk.Toplevel(self))
    
    def __actButtonEdit(self):
        if self.__table.selection_get is not None:
            WindowAdd(tk.Toplevel(self,code=self.__table.item(self.__table.selection_get())))
        else:
            msgbx.showwarning('Null', 'Seleccione el elemento a actualizar')

    def __actButtonDelete(self):
        msgbx.showinfo('Action','Has presionado el boton Eliminar')

    def __actButtonExit(self):
        self.master.destroy()

    
    #------------------------- Functions -------------------------

    def __setvalues(self):
        if self.__mfile.getFile() is not None:
            for d in self.__mfile.getFile():
                self.__table.insert('',tk.END,values=d,text=d[0])
        else:
            msgbx.showwarning('Vacío','No hay ningún dato')

    def __searchvalue(self):
        for d in self.__table.get_children():
            if self.__table.item(d)['text'] == self.__entrycourse.get():
                self.__table.focus(d)
                self.__table.selection_set(d)
                return
        msgbx.showwarning('Null','El curso no existe')
        self.__table.selection_clear()

