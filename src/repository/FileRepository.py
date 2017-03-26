'''
Created on Dec 19, 2016

@author: User
'''
from repository.Repository import Repository

class FileRepository(Repository):
    '''
    classdocs
    '''


    def __init__(self, fileName):
        Repository.__init__(self)
        self.__fileName = fileName
    
    def add(self, instructiune):
        Repository.add(self, instructiune)
        
    def __storeToFile(self):
        pass
#         f = open(self.__fileName, "w")
#         list = Repository.getAll(self)
#         for x in list:
#             xf = str
#             xf = xf + "\n"
#             f.write(xf)
#         f.close()
        