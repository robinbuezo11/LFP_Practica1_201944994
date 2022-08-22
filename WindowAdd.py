import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx
from ManagerFile import ManagerFile
from Course import Course

class WindowAdd(tk.Frame):
    def __init__(self, master, mngfile = ManagerFile(), callback = None) -> None:
        self.__mngfile = mngfile
        super().__init__(master)
        master.title('Agregar Curso')
        master.geometry('700x580')
        master.config(background='sky blue')
        master.resizable(False,False)

        self.callback = callback

        #----------------------------- Entrys -----------------------------

        self.__entrycode = tk.Entry(master)
        self.__entrycode.place(x=200, y=40, relwidth=0.65, height=25)

        self.__entryname = tk.Entry(master)
        self.__entryname.place(x=200, y=100, relwidth=0.65, height=25)

        self.__entryrequisite = tk.Entry(master)
        self.__entryrequisite.place(x=200, y=160, relwidth=0.65, height=25)

        self.__entrysemester = tk.Entry(master)
        self.__entrysemester.place(x=200, y=220, relwidth=0.65, height=25)

        self.__entryoptional = tk.Entry(master)
        self.__entryoptional.place(x=200, y=280, relwidth=0.65, height=25)

        self.__entrycredit = tk.Entry(master)
        self.__entrycredit.place(x=200, y=340, relwidth=0.65, height=25)

        self.__entrystatus = tk.Entry(master)
        self.__entrystatus.place(x=200, y=400, relwidth=0.65, height=25)


        #----------------------------- Labels ----------------------------

        self.__lblcode = ttk.Label(master, text='Código:', background='sky blue', font='Arial 14 bold')
        self.__lblcode.place(x=50, y=41,)

        self.__lblname = ttk.Label(master, text='Nombre:', background='sky blue', font='Arial 14 bold')
        self.__lblname.place(x=50, y=101,)

        self.__lblrequisite = ttk.Label(master, text='Prerrequisitos:', background='sky blue', font='Arial 14 bold')
        self.__lblrequisite.place(x=50, y=161,)

        self.__lblsemester = ttk.Label(master, text='Semestre:', background='sky blue', font='Arial 14 bold')
        self.__lblsemester.place(x=50, y=221,)

        self.__lbloptional = ttk.Label(master, text='Obligatorio:', background='sky blue', font='Arial 14 bold')
        self.__lbloptional.place(x=50, y=281,)

        self.__lblcredit = ttk.Label(master, text='Créditos:', background='sky blue', font='Arial 14 bold')
        self.__lblcredit.place(x=50, y=341,)

        self.__lblstatus = ttk.Label(master, text='Estado:', background='sky blue', font='Arial 14 bold')
        self.__lblstatus.place(x=50, y=401,)

        #------------------------------------------- Buttons -----------------------------------------------
        
        self.__buttonadd = ttk.Button(master, text='Agregar', command=self.__actButtonAdd)

        self.__buttonadd.place(x=350, y=480)

        self.__buttonadd = ttk.Button(master, text='Regresar', command=self.__actButtonExit)
        self.__buttonadd.place(x=550, y=480)

        #---------------- Mostrar ventana ------------------------

        master.focus()
        master.grab_set()

    def __actButtonAdd(self):
        try:
            course = Course(self.__entrycode.get(), self.__entryname.get(), self.__entryrequisite.get(), int(self.__entryoptional.get()), 
                            int(self.__entrysemester.get()), int(self.__entrycredit.get()), int(self.__entrystatus.get()))
            if self.__mngfile.addCourse(course):
                msgbx.showinfo('Agregado', 'Curso agregado exitosamente')
                self.callback()
                self.master.destroy()
        except Exception as e:
            msgbx.showerror('Error', 'Error al intentar agregar el curso, revise sus valores')


    def __actButtonExit(self):
        self.master.destroy()
