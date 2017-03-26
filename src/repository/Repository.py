'''
Created on Dec 19, 2016

@author: User
'''
from domain.Exceptions import ProgramException

class RepositoryException(ProgramException):
    pass
class Repository(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._instructiuni = {}
    
    def add(self, instructiune):
        '''functie de adaugare instructiune
        input: instructiune de tip Instructiune
        raises: RepositoryException daca id de instructiune exista deja
        output: lista de instructiune cu elementul adaugat
        '''
        if instructiune.instrID in self._instructiuni:
            raise RepositoryException("instrID alreaady existent!")
        self._instructiuni[instructiune.instrID] = instructiune
        
    def getAll(self):
        '''
        functie de returnare a listei de instructiuni
        output: instructiunile sub forma de lista
        '''
        return [x for x in self._instructiuni.values()]
            
            
        
        