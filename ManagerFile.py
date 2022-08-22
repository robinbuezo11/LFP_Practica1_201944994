from tkinter import messagebox as msgbx
from Course import Course

class ManagerFile:
    def __init__(self) -> None:
        self.__data = []

    #----------------------- Functions ----------------------------
    def openFile(self,ruta):   #Metodo para leer el archivo
        f = None
        try:
            if(ruta[len(ruta)-4:len(ruta)]) in ['.lfp','.LFP','.csv','.CSV']:
                f = open(ruta,'r', encoding='utf-8')
                file = f.readlines()

                data = self.__readFile(file)
                if data is None:
                    f.close()
                    return
            else:
                msgbx.showerror('ERROR','Extensión de archivo no válida')
                return
        except Exception as ex:
            msgbx.showerror("ERROR",'Error en la carga, revise que los datos y la ruta de su archivo sean correctos.')
        finally:
            if f is not None:
                f.close()
                self.__data = data
                msgbx.showinfo('Archivo Cargado','El archivo se cargó exitosamente')
                return data
            else:
                return

    def __readFile(self, file):
        iterator = 0
        for line in file:
            file[iterator] = line.split(',')
            if len(file[iterator]) != 7:
                msgbx.showerror('Error','El archivo no contiene la cantidad de datos correcta en la linea: ',line)
                return
            
            if file[iterator][6][len(file[iterator][6])-1:len(file[iterator][6])] == '\n':
                file[iterator][6] = file[iterator][6][:len(file[iterator][6])-1]

            try:
                for char in file[iterator][0]:
                    int(char)

                file[iterator][3] = int(file[iterator][3])
                if file[iterator][3] not in (1,0):
                    msgbx.showerror('Error', 'El campo obligatorio debe ser\n 0 -> Opcional\n1 -> Obligatorio')
                    return

                file[iterator][4] = int(file[iterator][4])
                if file[iterator][4]>10 or file[iterator][4]<1:
                    msgbx.showerror('Error', 'El campo semestre debe ser un entero entre 1 y 10')
                    return

                file[iterator][5] = int(file[iterator][5])

                file[iterator][6] = int(file[iterator][6])
                if file[iterator][6] not in (1,0,-1):
                    msgbx.showerror('Error', 'El campo Estado debe ser\n 0 -> Aprobado\n1 -> Cursando\n-1 -> Pendiente')
                    return
            except Exception as e:
                msgbx.showerror('Error', "Los valores de Código, Obligatorio, Semestre, Créditos y Estado deben ser números enteros")
                return
            iterator += 1

        data = []
        
        for addline in file:
            course = Course(addline[0], addline[1], addline[2], addline[3], addline[4], addline[5], addline[6])
            end = False
            iter=0
            while not end:
                if len(data) == 0:
                    data.append(course)
                    end = True
                else:
                    while iter<len(data) and not end:
                        if data[iter].getCode() == course.getCode()    :
                            data.pop(iter)
                            data.append(course)
                            end = True
                        else:
                           iter+=1
                            
                    if not end:
                        data.append(course)
                        end = True
        return data

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def addCourse(self, course):
        try:
            for char in course.getCode():
                int(char)

            if course.getOptional() not in (1,0):
                msgbx.showerror('Error', 'El campo obligatorio debe ser\n 0 -> Opcional\n1 -> Obligatorio')
                return

            if course.getSemester()>10 or course.getSemester()<1:
                msgbx.showerror('Error', 'El campo semestre debe ser un entero entre 1 y 10')
                return

            if course.getStatus() not in (1,0,-1):
                msgbx.showerror('Error', 'El campo Estado debe ser\n 0 -> Aprobado\n1 -> Cursando\n-1 -> Pendiente')
                return
        except Exception as e:
            #msgbx.showerror('Error',e)
            msgbx.showerror('Error', "Los valores de Campo, Obligatorio, Semestre, Créditos y Estado deben ser números enteros")
            return

        end = False
        i=0
        while not end:
            if len(self.__data) == 0:
                self.__data.append(course)
                end = True
            else:
                while i<len(self.__data) and not end:
                    if self.__data[i].getCode() == course.getCode()    :
                            self.__data.pop(i)
                            self.__data.append(course)
                            msgbx.showinfo('Actualizado', 'El código ya existía y se actualizó con los nuevos valores')
                            return
                    else:
                        i+=1
                            
                if not end:
                    self.__data.append(course)
                    end = True
        return True

    def getCourse(self, code):
        for course in self.__data:
            if course.getCode() == code:
                return course
        msgbx.showinfo(message='Curso no encontrado')

    def updateCourse(self, code, newcourse):
        try:
            for char in newcourse.getCode():
                int(char)

            if newcourse.getOptional() not in (1,0):
                msgbx.showerror('Error', 'El campo obligatorio debe ser\n 0 -> Opcional\n1 -> Obligatorio')
                return

            if newcourse.getSemester()>10 or newcourse.getSemester()<1:
                msgbx.showerror('Error', 'El campo semestre debe ser un entero entre 1 y 10')
                return

            if newcourse.getStatus() not in (1,0,-1):
                msgbx.showerror('Error', 'El campo Estado debe ser\n 0 -> Aprobado\n1 -> Cursando\n-1 -> Pendiente')
                return
        except Exception as e:
            #msgbx.showerror('Error',e)
            msgbx.showerror('Error', "Los valores de Campo, Obligatorio, Semestre, Créditos y Estado deben ser números enteros")
            return

        for course in self.__data:
            if course.getCode() == code:
                course.setCode(newcourse.getCode())
                course.setName(newcourse.getName())
                course.setRequisite(newcourse.getRequisite())
                course.setOptional(newcourse.getOptional())
                course.setSemester(newcourse.getSemester())
                course.setCredits(newcourse.getCredits())
                course.setStatus(newcourse.getStatus())
                return True

    def deleteCourse(self, code):
        iterator = 0
        for course in self.__data:
            if course.getCode() == code:
                self.__data.pop(iterator)
                msgbx.showinfo('Eliminado', 'Curso eliminado exitosamente')
                return course
            iterator += 1
        msgbx.showinfo(message='Curso no encontrado')

    def getApprovedCredits(self):
        credits = 0
        for course in self.__data:
            if course.getStatus() == 0:
                credits += course.getCredits()
        return credits

    def getStudyingCredits(self):
        credits = 0
        for course in self.__data:
            if course.getStatus() == 1:
                credits += course.getCredits()
        return credits

    def getPendingCredits(self):
        credits = 0
        for course in self.__data:
            if course.getOptional() == 1 and course.getStatus() == -1:
                credits += course.getCredits()
        return credits

    def getCreditsUntil(self, semester):
        credits = 0
        for course in self.__data:
            if course.getSemester() <= semester and course.getOptional() == 1:
                credits += course.getCredits()
        return credits

    def getCreditsApprovSem(self, semester):
        credits = 0
        for course in self.__data:
            if course.getStatus() == 0 and course.getSemester() == semester:
                credits += course.getCredits()
        return credits

    def getCreditsStudySem(self, semester):
        credits = 0
        for course in self.__data:
            if course.getStatus() == 1 and course.getSemester() == semester:
                credits += course.getCredits()
        return credits

    def getCreditsPendSem(self, semester):
        credits = 0
        for course in self.__data:
            if course.getStatus() == -1 and course.getSemester() == semester and course.getOptional() == 1:
                credits += course.getCredits()
        return credits 

