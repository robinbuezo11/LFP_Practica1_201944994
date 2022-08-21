import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx
from ManagerFile import ManagerFile
from Course import Course

class WindowUpdate(tk.Frame):
    def __init__(self, master, mngfile = ManagerFile(), course = Course(), callback = None) -> None:
        self.__mngfile = mngfile
        self.__course = course
        super().__init__(master)
        master.title('Actualizar Curso')
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

        self.__setEntrysValues()

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
        
        self.__buttonadd = ttk.Button(master, text='Actualizar', command=self.__actButtonUpdate)

        self.__buttonadd.place(x=350, y=480)

        self.__buttonadd = ttk.Button(master, text='Regresar', command=self.__actButtonExit)
        self.__buttonadd.place(x=550, y=480)

        #---------------- Mostrar ventana ------------------------

        master.focus()
        master.grab_set()

    def __actButtonUpdate(self):
        try:
            newcourse = Course(self.__entrycode.get(), self.__entryname.get(), self.__entryrequisite.get(), int(self.__entryoptional.get()), 
                            int(self.__entrysemester.get()), int(self.__entrycredit.get()), int(self.__entrystatus.get()))
            self.__mngfile.updateCourse(self.__course.getCode(), newcourse)
            self.callback()
            self.master.destroy()
        except Exception as e:
            msgbx.showerror('Error', e)

    def __actButtonExit(self):
        self.master.destroy()

    def __setEntrysValues(self):
        self.__entrycode.insert(0,self.__course.getCode())
        self.__entryname.insert(0,self.__course.getName())
        self.__entryrequisite.insert(0,self.__course.getRequisite())
        self.__entrysemester.insert(0,self.__course.getSemester())
        self.__entryoptional.insert(0,self.__course.getOptional())
        self.__entrycredit.insert(0,self.__course.getCredits())
        self.__entrystatus.insert(0,self.__course.getStatus())