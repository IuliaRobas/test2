'''
Created on Dec 19, 2016

@author: User
'''
import unittest
from controller.Controller import Controller
from repository.Repository import Repository
from domain.Instructiune import Instructiune


class TestController(unittest.TestCase):


    def setUp(self):
        self.__repo = Repository()
        self.__ctrl = Controller(self.__repo)
        self.__instructiune =  Instructiune(1, 1, "I", 10, 15)


    def tearDown(self):
        pass


    def testName(self):
        assert(len(self.__ctrl.getAll()) == 0)
        self.__ctrl.add(self.__instructiune.instrID, self.__instructiune.programID, self.__instructiune.instrType, self.__instructiune.resurse, self.__instructiune.durata)
        assert(len(self.__ctrl.getAll()) == 1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()