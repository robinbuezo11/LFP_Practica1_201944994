from audioop import add
import sys
from tkinter import messagebox as msgbx

class OpenFile:

    def readFile(ruta):   #Metodo para leer el archivo
        f = None
        try:
            f = open(ruta,'r', encoding='utf-8')
            if(ruta[len(ruta)-4:len(ruta)]) in ['.lfp','.LFP','.csv','.CSV']:
                file = f.readlines()

                iterador = 0
                for line in file:
                    file[iterador] = line.split(',')
                    iterador += 1

                data = []
                
                for addline in file:
                    end = False
                    i=0
                    while not end:
                        if len(data) == 0:
                            data.append(addline)
                            end = True
                        else:
                            while i<len(data) and not end:
                                if data[i][0] == addline[0]:
                                    data.pop(i)
                                    data.append(addline)
                                    end = True
                                else:
                                   i+=1
                            
                            if not end:
                                data.append(addline)
                                end = True

            else:
                msgbx.showerror('ERROR','Extensión de archivo no válida')
        except:
            msgbx.showerror("ERROR",sys.exc_info())
        finally:
            if f is not None:
                f.close()
                return data
            else:
                return None
