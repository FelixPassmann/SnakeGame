# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:03:27 2020

@author: felix
"""
from time import sleep
from threading import Thread, enumerate

a = 1

def pulse():
    while(True):
        global a
        sleep(2)
        print('pulse ' + str(a))
        a=a+1
 

T1 = Thread(target=pulse)
T1.start()

T1.get_ident()
 a = 100
 
 for thread in enumerate(): 
    print(thread.name)
