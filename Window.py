import tkinter as tk


class Window(tk.Frame):
    def __init__(self,window) -> None:
        super().__init__(window)
        window.title('Practica 1')
        window.geometry('850x650')
        window.config(background='sky blue')

        self.lblcurso = tk.Label(window,text='Nombre del Curso: Lab. Lenguajes Formales y de Programación',font='Arial 16 bold', 
                                    background='sky blue')
        self.lblcurso.place(x=100, y=30)

        self.lblstudent = tk.Label(window,text='Nombre del Estudiante: Robin Omar Buezo Díaz', font='Arial 16 bold', background='sky blue')
        self.lblstudent.place(x=100, y= 70)

        self.lblcarne = tk.Label(window,text='Carné del Estudiante: 201944994', font='Arial 16 bold', background='sky blue')
        self.lblcarne.place(x=100, y=110)

        window.mainloop()
