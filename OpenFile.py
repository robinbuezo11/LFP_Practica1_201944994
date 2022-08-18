import sys
from tkinter import messagebox as msgbx

class OpenFile:

    def readFile(ruta):   #Metodo para leer el archivo
        f = None
        try:
            f = open(ruta,'r', encoding='utf-8')
            if(ruta[len(ruta)-3:len(ruta)]) in ['lfp','LFP','csv','CSV']:
                file = f.read()
            else:
                msgbx.showerror('ERROR','Extensión de archivo no válida')
        except:
            msgbx.showerror("ERROR",sys.exc_info())
        finally:
            if f is not None:
                f.close()
                return file
            else:
                return None
