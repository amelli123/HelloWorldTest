#This is a test file to print hello world only when run and not when imported
#Ameer Melli 4/3/24

import sys

#Function to see if something has been imported
def Has_Imported(moudle_name):
    return moudle_name in sys.modules

#Function to print hello world
def hello():
    return print('Hello World :)')

#Main that prints hello world if the file was not imported
if not Has_Imported("TestingFile"):
    hello()
