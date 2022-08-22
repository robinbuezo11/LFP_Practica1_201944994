from turtle import back
from ManagerFile import ManagerFile
import tkinter as tk
from tkinter import messagebox as msgbx
from tkinter import ttk
from WindowAdd import WindowAdd
from WindowUpdate import WindowUpdate

class WindowManager(tk.Frame):
    def __init__(self, master, mngfile = ManagerFile()) -> None:
        self.__mngfile = mngfile
        super().__init__(master)
        master.title('Gestionar Cursos')
        master.geometry('1200x700')
        master.config(background='sky blue')
        master.resizable(False,False)

        #----------------------------- Entry -----------------------------

        self.__entrycourse = tk.Entry(master)
        self.__entrycourse.place(x=550, y=20, relwidth=0.2, height=25)

        #----------------------------- Label -----------------------------

        self.__lblinfo = ttk.Label(master, background='sky blue', font='Arial 8 bold', foreground='red3',
            text='PRERREQUISITOS: \tcodigo1;codigo2\nOBLIGATORIO: \t\t1 -> Si, 0 -> No\nESTADO: \t\t1 -> Cursando, 0 -> Aprobado, -1 -> Pendiente')
        self.__lblinfo.place(x=10, y=10)

        #------------------------------ Buttons --------------------------------

        self.__btnsearch = ttk.Button(master, text='Buscar', command=self.__searchvalue)
        self.__btnsearch.place(x=850, y=20, relwidth=0.1)

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

        self.__setvalues()

    #----------------------- Actions -----------------------------

    def __actButtonAdd(self):
        WindowAdd(master=tk.Toplevel(self), mngfile=self.__mngfile, callback=self.__setvalues)
    
    def __actButtonEdit(self):
        if self.__table.item(self.__table.focus())['text'] != '':
            course = self.__mngfile.getCourse(self.__table.item(self.__table.focus())['text'])
            if course is not None:
                WindowUpdate(tk.Toplevel(self), self.__mngfile, course, callback=self.__setvalues)
        else:
            msgbx.showwarning('Null', 'Seleccione el elemento a actualizar')
            self.master.focus()
            self.master.grab_set()

    def __actButtonDelete(self):
        if self.__table.item(self.__table.focus())['text'] != '':
            course = self.__mngfile.getCourse(self.__table.item(self.__table.focus())['text'])
            if course is not None:
                self.__mngfile.deleteCourse(course.getCode())
                self.__setvalues()
            else:
                msgbx.showwarning('Null','El curso no existe')
        else:
            msgbx.showwarning('Null', 'Seleccione el elemento a eliminar')
            self.master.focus()
            self.master.grab_set()

    def __actButtonExit(self):
        self.master.destroy()

    
    #------------------------- Functions -------------------------

    def __setvalues(self):
        self.__table.delete(*self.__table.get_children())
        if self.__mngfile.getData() is not None:
            for d in self.__mngfile.getData():
                self.__table.insert('',tk.END,values=(d.getCode(),d.getName(),d.getRequisite(),d.getOptional(),d.getSemester(),d.getCredits(),
                                        d.getStatus()), text=d.getCode())
            self.master.focus()
            self.master.grab_set()
        else:
            msgbx.showwarning('Vacío','No hay ningún dato')
            self.master.focus()
            self.master.grab_set()

    def __searchvalue(self):
        for d in self.__table.get_children():
            if self.__table.item(d)['text'] == self.__entrycourse.get():
                self.__table.focus(d)
                self.__table.selection_set(d)
                return
        msgbx.showwarning('Null','El curso no existe')
        self.__setvalues()
        