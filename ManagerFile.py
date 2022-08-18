import sys
from tkinter import messagebox as msgbx

class ManagerFile:
    def __init__(self) -> None:
        self.__file = None

    #----------------------- Functions ----------------------------

    def getFile(self):
        return self.__file

    def setFile(self, file):
        self.__file = file
        msgbx.showinfo('Archivo Cargado','El archivo se cargó exitosamente')
