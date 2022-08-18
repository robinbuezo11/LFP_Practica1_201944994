import tkinter as tk
from ManagerFile import ManagerFile

class WindowList(tk.Frame):
    def __init__(self, master, mfile=ManagerFile()) -> None:
        super().__init__(master)
        master.title('Listar Cursos')
        master.geometry('850x650')
        master.config(background='sky blue')
        master.resizable(False,False)

        lbldata = tk.Label(master,background='sky blue', text=mfile.getFile())
        lbldata.pack()

        master.focus()
        master.grab_set()
