
class Course:
    def __init__(self, code=None, name=None, requisite=None, optional=None, semester=None, credits=None, status=None) -> None:
        self.__code = code
        self.__name = name
        self.__requisite = requisite
        self.__optional = optional
        self.__semester = semester
        self.__credits = credits
        self.__status = status

    #---------------------------------- getters ------------------------------
    def getCode(self):
        return self.__code
    
    def getName(self):
        return self.__name

    def getRequisite(self):
        return self.__requisite

    def getOptional(self):
        return self.__optional
    
    def getSemester(self):
        return self.__semester

    def getCredits(self):
        return self.__credits
    
    def getStatus(self):
        return self.__status

    #-------------------------------- setters -----------------------------------
    def setCode(self, code):
        self.__code = code
    
    def setName(self, name):
        self.__name = name

    def setRequisite(self, requisite):
        self.__requisite = requisite

    def setOptional(self, optional):
        self.__optional = optional
    
    def setSemester(self, semester):
        self.__semester = semester

    def setCredits(self, credits):
        self.__credits = credits
    
    def setStatus(self, status):
        self.__status = status
