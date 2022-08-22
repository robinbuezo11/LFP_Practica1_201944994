from ManagerFile import ManagerFile
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx

class WindowCounting(tk.Frame):
    def __init__(self, master, mngfile = ManagerFile()) -> None:
        self.__mngfile = mngfile
        super().__init__(master)
        master.title('Conteo de Créditos')
        master.geometry('700x550')
        master.config(background='sky blue')
        master.resizable(False,False)

        #----------------------------- Labels ----------------------------

        self.__lblapproved = ttk.Label(master, text='Créditos Aprobados:', background='sky blue', font='Arial 14 bold')
        self.__lblapproved.place(x=50, y=41,)

        self.__lblapprovedcount = ttk.Label(master, text=self.__mngfile.getApprovedCredits(), background='sky blue', font='Arial 14 bold', foreground='red3')
        self.__lblapprovedcount.place(x=255, y=41,)

        self.__lblstudying = ttk.Label(master, text='Créditos Cursando:', background='sky blue', font='Arial 14 bold')
        self.__lblstudying.place(x=50, y=101,)

        self.__lblstudyingcount = ttk.Label(master, text=self.__mngfile.getStudyingCredits(), background='sky blue', font='Arial 14 bold', foreground='red3')
        self.__lblstudyingcount.place(x=255, y=101,)

        self.__lblpending = ttk.Label(master, text='Créditos Pendientes:', background='sky blue', font='Arial 14 bold')
        self.__lblpending.place(x=50, y=161,)

        self.__lblpendingcount = ttk.Label(master, text=self.__mngfile.getPendingCredits(), background='sky blue', font='Arial 14 bold', foreground='red3')
        self.__lblpendingcount.place(x=255, y=161,)

        self.__lblrequired = ttk.Label(master, text='Créditos Obligatorios hasta semestre', background='sky blue', font='Arial 14 bold')
        self.__lblrequired.place(x=50, y=221,)

        self.__lblsemester = ttk.Label(master, text='Créditos del Semestre', background='sky blue', font='Arial 14 bold')
        self.__lblsemester.place(x=50, y=371,)

        self.__lblsemapprov = ttk.Label(master, text='Créditos: ', background='sky blue', font='Arial 12 bold')
        self.__lblsemapprov.place(x=250, y=281,)

        self.__lblsemapprov = ttk.Label(master, text='Aprobados: ', background='sky blue', font='Arial 11 bold')
        self.__lblsemapprov.place(x=50, y=441,)

        self.__lblsemstudy = ttk.Label(master, text='Asignados: ', background='sky blue', font='Arial 11 bold')
        self.__lblsemstudy.place(x=260, y=441,)

        self.__lblsempend = ttk.Label(master, text='Pendientes: ', background='sky blue', font='Arial 11 bold')
        self.__lblsempend.place(x=470, y=441,)

        self.__lbluntilsemcount = ttk.Label(master, text='', font='Arial 14 bold', foreground='red3', width=8, background='sky blue')
        self.__lbluntilsemcount.place(x=340, y=281)

        self.__lblsemapprovcount = ttk.Label(master, text='', font='Arial 12 bold', foreground='red3', width=5, background='sky blue')
        self.__lblsemapprovcount.place(x=150, y=441)

        self.__lblsemstudycount = ttk.Label(master, text='', font='Arial 12 bold', foreground='red3', width=5, background='sky blue')
        self.__lblsemstudycount.place(x=360, y=441)

        self.__lblsempendcount = ttk.Label(master, text='', font='Arial 12 bold', foreground='red3', width=5, background='sky blue')
        self.__lblsempendcount.place(x=570, y=441)

        #----------------------------- Comboboxs -----------------------------

        self.__entrysemrequired = ttk.Combobox(master, state='readonly', values=[1,2,3,4,5,6,7,8,9,10])
        self.__entrysemrequired.set(1)
        self.__entrysemrequired.place(x=410, y=221, width=40, height=30)

        self.__entrysem = ttk.Combobox(master, state='readonly', values=[1,2,3,4,5,6,7,8,9,10])
        self.__entrysem.set(1)
        self.__entrysem.place(x=270, y=371, width=40, height=30)

        master.focus()
        master.grab_set()

        #----------------------------- Buttons ---------------------------------

        self.__btnsemrequired = ttk.Button(master, text='Contar', command=self.__requiredCount)
        self.__btnsemrequired.place(x=470, y=221)

        self.__btnsem = ttk.Button(master, text='Contar', command=self.__semCount)
        self.__btnsem.place(x=470, y=371)

        self.__buttonexit = ttk.Button(master, text='Regresar', command=self.__actButtonExit)
        self.__buttonexit.place(x=570, y=500)


    #----------------------- Actions -----------------------------

    def __requiredCount(self):
        try:
            self.__lbluntilsemcount['text'] = self.__mngfile.getCreditsUntil(int(self.__entrysemrequired.get()))
        except Exception as e:
            msgbx.showerror('Error', e)

    def __semCount(self):
        try:
            self.__lblsemapprovcount['text'] = self.__mngfile.getCreditsApprovSem(int(self.__entrysem.get()))
            self.__lblsemstudycount['text'] = self.__mngfile.getCreditsStudySem(int(self.__entrysem.get()))
            self.__lblsempendcount['text'] = self.__mngfile.getCreditsPendSem(int(self.__entrysem.get()))
        except Exception as e:
            msgbx.showerror('Error', e)

    def __actButtonExit(self):
        self.master.destroy()
    
