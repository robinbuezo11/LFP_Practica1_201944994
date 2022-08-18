import sys
from tkinter import messagebox as msgbx

class ManagerFile:
    def __init__(self,file=None) -> None:
        self.__file = file

    #----------------------- Functions ----------------------------

    def getFile(self):
        return self.__file

    def setFile(self, file):
        self.__file = file
        msgbx.showinfo('Archivo Cargado','El archivo se cargó exitosamente')
