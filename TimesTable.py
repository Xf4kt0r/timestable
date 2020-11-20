#!/usr/bin/python3

import sys
import os
import ctypes
os.system("")

class bcolors():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def nl():
    print('\r')

def section():
    print(bcolors.BLUE + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + bcolors.ENDC)
    
filename = os.environ['PWD']+str("/NewTimesTable.csv")
org_stdout = sys.stdout
st = input("Provde start of the times table: ")
en = int(input("Provide the end of the times table: "))
nl()
en += 1
z = range(int(st),int(en))

def toprow():
    print("X", end = ',')
    for a in (z):
        print(a, end = ',')
    nl()

def table():
    for x in (z):
        print(x, end = ',')
        for y in (z):
            print(x*y, end = ',')
        nl()

def TimesTable():
    toprow()
    table()

def createTable():
    sys.stdout = open(filename, "w")
    TimesTable()
    sys.stdout.close()
    sys.stdout = org_stdout

def screenout():
    TimesTable()
    createTable()

section()
print(bcolors.BLUE + "| " + bcolors.GREEN + "Your file is saved here:" + filename + bcolors.BLUE + " |" + bcolors.ENDC)
section()
screenout()







