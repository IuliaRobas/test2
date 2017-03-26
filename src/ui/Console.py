'''
Created on Dec 19, 2016

@author: User
'''
import cmd

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, instrController):
        '''
        Constructor
        '''
        self.__instrController = instrController
     
    def __printMenu(self):
        print("1. Add instruction ")
        print("2. Print instructions ")
        print("3. Print programIDs")
        print("4. Print resurse/programID")
        print("5. Print coresXprograms")
        print("6. Print durataXprogram")
        print("0. Exit\n")
        
    def __uiPrintDurataXProgram(self):
        d= self.__instrController.durataPerProgram()
        for el in d.keys():
            print(d[el])
    def __uiPrintProgramIDs(self):
        prIDs = self.__instrController.determinePrograms()
        for prID in prIDs:
            print(prID)
        
    def __readCommand(self):
        cmd = int(input("Option: "))
        return cmd
    
    def __uiAddInstruction(self):
        instrID = int(input("instrID: "))
        programID = int(input("programID: "))
        instrType = input("instrType: ")
        resurse = int(input("resurse: "))
        durata = int(input("durata: "))
        self.__instrController.add(instrID, programID, instrType, resurse, durata)
     
    def __uiPrintInstructions(self):
        instructions = self.__instrController.getAll()
        for instruction in instructions:
            print(instruction)
    def __initData(self):
        self.__instrController.setUp()
        
    def __uiPrintResursePerProgram(self):
        resurse = self.__instrController.getResursePerProgram()
        for resursa in resurse.values():
            print(resursa)
            
    def __uiPrintCoresXPrograms(self):
        l = self.__instrController.getCoresXPrograms()
        for el in l:
            print("Core {0}: program {1}".format(el[0],el[1]))
                          
    def runApp(self):
        
        commands = {1:self.__uiAddInstruction, 2:self.__uiPrintInstructions, 3:self.__uiPrintProgramIDs, 4:self.__uiPrintResursePerProgram,
                    5: self.__uiPrintCoresXPrograms, 6:self.__uiPrintDurataXProgram}
        self.__initData()
        while True:
            self.__printMenu()
            cmd = self.__readCommand()
            if cmd == 0:
                print("Bye!")
                break
            commands [cmd]()
            print('\n')

            
        