import sys
from tkinter import messagebox as msgbx

class OpenFile:
    def __init__(self) -> None:
        pass

    def readFile(self, ruta):   #Metodo para leer el archivo
        try:
            f = open(ruta,'r', encoding='utf-8')
            file = f.read()
        except:
            msgbx.showerror("ERROR",sys.exc_info())
        finally:
            f.close()
        
        return file
