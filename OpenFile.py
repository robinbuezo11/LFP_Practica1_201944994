import sys
from tkinter import messagebox as msgbx

class OpenFile:

    def readFile(ruta):   #Metodo para leer el archivo
        f = None
        try:
            f = open(ruta,'r', encoding='utf-8')
            file = f.read()
        except:
            msgbx.showerror("ERROR",sys.exc_info())
        finally:
            if f is not None:
                f.close()
                return file
            else:
                return None
