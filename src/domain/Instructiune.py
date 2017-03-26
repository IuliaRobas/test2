'''
Created on Dec 19, 2016

@author: User
'''

class Instructiune(object):
    '''
    classdocs
    '''


    def __init__(self, instrID, programID, instrType, resurse, durata):
        '''
        Constructor pt instructiune
        '''
        self.__instrID = instrID
        self.__programID = programID
        self.__instrType = instrType
        self.__resurse = resurse
        self.__durata = durata
      
    def __str__(self):
        '''
        functie de printare a unei instructiuni
        '''
        return 'instrID: {0}  programID: {1} instrType: {2} resurse: {3} durata: {4}'.format(self.__instrID, self.__programID, self.__instrType, self.__resurse, self.__durata)  
    @property
    def instrID(self):
        return self.__instrID
    @instrID.setter
    def instrID(self, newID):
        self.__instrID = newID
    @instrID.deleter
    def instrID(self):
        del self.__instrID  
     
    @property
    def programID(self):
        return self.__programID
    @programID.setter
    def programID(self, newID):
        self.__programID = newID
    @programID.deleter 
    def programID(self):
        del self.__programID
        
    @property
    def instrType(self):
        return self.__instrType
    @instrType.setter
    def instrType(self, newID):
        self.__instrType = newID
    @instrType.deleter 
    def instrType(self):
        del self.__instrType     
        
    @property
    def resurse(self):
        return self.__resurse
    @resurse.setter
    def resurse(self, newID):
        self.__resurse = newID
    @resurse.deleter 
    def resurse(self):
        del self.__resurse        
        
    @property
    def durata(self):
        return self.__durata
    @durata.setter
    def durata(self, newID):
        self.__durata = newID
    @durata.deleter 
    def durata(self):
        del self.__durata 