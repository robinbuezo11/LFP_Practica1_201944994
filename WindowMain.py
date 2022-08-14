import tkinter as tk
from tkinter import messagebox as msgbx

class WindowMain(tk.Frame):
    def __init__(self,window) -> None:
        self.window = window
        super().__init__(self.window)
        self.window.title('Practica 1')
        self.window.geometry('850x650')
        self.window.config(background='sky blue')
        self.window.resizable(False,False)

        #----------------------------------Labels--------------------------------------------

        self.lblcurso = tk.Label(self.window,text='Lenguajes Formales y de Programación A+',font='Arial 16 bold', 
                                    background='sky blue')
        self.lblcurso.place(x=100, y=30)

        self.lblstudent = tk.Label(self.window,text='Robin Omar Buezo Díaz', font='Arial 16 bold', background='sky blue')
        self.lblstudent.place(x=100, y= 70)

        self.lblcarne = tk.Label(self.window,text='201944994', font='Arial 16 bold', background='sky blue')
        self.lblcarne.place(x=100, y=110)

        #----------------------------------buttons---------------------------------------------

        self.buttonfile = tk.Button(self.window, text='Cargar Archivo', width=20, height=2, background='SpringGreen3', font='Arial 12 bold',
                                    command=self.actButtonFile)
        self.buttonfile.place(x=330, y=200)

        self.buttonmanage = tk.Button(self.window, text='Gestionar Cursos', width=20, height=2, background='SpringGreen3', font='Arial 12 bold',
                                    command=self.actButtonManage)
        self.buttonmanage.place(x=330, y=290)

        self.buttoncounting = tk.Button(self.window, text='Conteo de Créditos', width=20, height=2, background='SpringGreen3', font='Arial 12 bold',
                                    command=self.actButtonCounting)
        self.buttoncounting.place(x=330, y=380)

        self.buttonexit = tk.Button(self.window, text='Salir', width=20, height=2, background='SpringGreen3', font='Arial 12 bold',
                                    command=self.actButtonExit)
        self.buttonexit.place(x=330, y=470)

        #---------------------------------Show Window--------------------------------

        window.mainloop()

    #-----------------------Actions-----------------------------

    def actButtonFile(self):
        msgbx.showinfo('Action','Has presionado el boton Cargar')

    def actButtonManage(self):
        msgbx.showinfo('Action','Has presionado el boton Gestion')
    
    def actButtonCounting(self):
        msgbx.showinfo('Action','Has presionado el boton Conteo')

    def actButtonExit(self):
        self.window.destroy()
