'''
Created on Dec 19, 2016

@author: User
'''
from repository.Repository import Repository
from controller.Controller import Controller
from ui.Console import Console

instrRepo = Repository()
instrController = Controller(instrRepo)
ui = Console(instrController)
ui.runApp()