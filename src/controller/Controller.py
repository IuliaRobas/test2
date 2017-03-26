'''
Created on Dec 19, 2016

@author: User
'''
from domain.Exceptions import ProgramException
from domain.Instructiune import Instructiune

class ControllerException(ProgramException):
    pass

class Controller(object):
    '''
    legatura intre consola si repository
    '''


    def __init__(self, instrRepo):
        '''
        Constructor
        '''
        self.__repo = instrRepo
        self.__cores = {"c1": 50, "c2":100}
    
    def add(self, instrID, programID, instrType, resurse, durata):
        '''
        input: campurile unei instructiuni
        output: adaugarea instructiunii in lista de instructiuni
        '''
        instructiune = Instructiune(instrID, programID, instrType, resurse, durata)
        self.__repo.add(instructiune)
        
    def getAll(self):
        '''
        output: lista de instructiuni
        '''
        return self.__repo.getAll()
    
    def determinePrograms(self):
        '''
        output: lista cu programsIDs
        '''
        programsIDs = []
        instructions = self.__repo.getAll()
        for instruction in instructions:            
            if instruction.programID not in programsIDs:
                programsIDs.append(instruction.programID)
        return programsIDs
    
    def getResursePerProgram(self):
        programsIDs = self.determinePrograms()
        instructions = self.__repo.getAll()
        resurse = {}
        for programID in programsIDs:
            resurse [programID] = []
        durate = {}
        for programID in programsIDs:
            durate[programID] = []
            
        for instruction in instructions:
            if instruction.instrType != "F":
                resurse[instruction.programID].append(instruction.resurse)
                durate[instruction.programID].append(instruction.durata)
#             elif instruction.instrType == "F":
#                 durate[instruction.programID].append(instruction.durata)
                
        for programID in programsIDs:
            sumaResurse = sum(resurse[programID])
            resurse[programID] = sumaResurse
            
        return resurse               
     
    def durataPerProgram(self):
        programsIDs = self.determinePrograms()
        instructions = self.__repo.getAll()
        durate = {}
        for programID in programsIDs:
            durate[programID] = []
            
        for instruction in instructions:
            durate[instruction.programID].append(instruction.durata)        
        with open("fisier","w") as f:
                 
            for programID in programsIDs:
                sumaDurata = sum(durate[programID])
                durate[programID] = sumaDurata
                f.write(str(programID) + " " + str(durate[programID]))
                
            
        
        return durate
                 
    def getCoresXPrograms(self):
        cores = self.__cores
        resurse = self.getResursePerProgram()
        coresXprograms = []
        for resursaKey in resurse.keys():
            for coreKey in self.__cores.keys():
                if resurse[resursaKey] < cores[coreKey]:
                    coresXprograms.append([coreKey, resursaKey])
                    
        return coresXprograms
            
        
    def setUp(self):
        self.__repo.add(Instructiune(4, 1, "I", 10, 15))
        self.__repo.add(Instructiune(5, 1, "I", 15, 20))
        self.__repo.add(Instructiune(6, 1, "F", 20, 25))
        self.__repo.add(Instructiune(1, 2, "I", 15, 15))
        self.__repo.add(Instructiune(2, 2, "I", 15, 20))
        self.__repo.add(Instructiune(3, 2, "F", 20, 25))
        
        
        