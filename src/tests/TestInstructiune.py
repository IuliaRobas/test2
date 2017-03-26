'''
Created on Dec 19, 2016

@author: User
'''
import unittest

from domain.Instructiune import Instructiune

class TestInstructiune(unittest.TestCase):


    def setUp(self):
        self.__instructiune = Instructiune(1, 1, "I", 10, 15)


    def tearDown(self):
        del self.__instructiune


    def testName(self):
        assert(self.__instructiune.instrID == 1)
        assert(self.__instructiune.instrType == "I")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()