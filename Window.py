import tkinter as tk
from tkinter import messagebox as msgbx

class Window(tk.Frame):
    def __init__(self,window) -> None:
        self.window = window
        super().__init__(self.window)
        self.window.title('Practica 1')
        self.window.geometry('850x650')
        self.window.config(background='sky blue')

        self.lblcurso = tk.Label(window,text='Lenguajes Formales y de Programación A+',font='Arial 16 bold', 
                                    background='sky blue')
        self.lblcurso.place(x=100, y=30)

        self.lblstudent = tk.Label(window,text='Robin Omar Buezo Díaz', font='Arial 16 bold', background='sky blue')
        self.lblstudent.place(x=100, y= 70)

        self.lblcarne = tk.Label(window,text='201944994', font='Arial 16 bold', background='sky blue')
        self.lblcarne.place(x=100, y=110)

        self.button = tk.Button(window, text='Cargar Archivo', width=20, height=2, background='SpringGreen3', font='Arial 12 bold',
                                    command=self.actButton)
        self.button.place(x=330, y=170)

        window.mainloop()

    def actButton(self):
        msgbx.showinfo('Action','Has presionado el boton')
