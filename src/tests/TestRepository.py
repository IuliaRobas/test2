'''
Created on Dec 19, 2016

@author: User
'''
import unittest
from repository.Repository import Repository
from domain.Instructiune import Instructiune

class TestRepository(unittest.TestCase):


    def setUp(self):
        self.__repo = Repository()
        self.__instructiune = Instructiune(1, 1, "I", 10, 15)


    def tearDown(self):
        del self.__instructiune
        del self.__repo


    def testName(self):
       assert(len(self.__repo.getAll())== 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()