# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:58:24 2020

@author: felix
"""
import tkinter as tk #in python 3.x: tkinter wird kleingeschrieben
import os
import keyboard
from time import sleep
################################
##
## All buttons implemented
##
##############################
button1 = tk.Button(rechner, text=' 1 ', fg='black', bg='red', 
                     command=lambda: press(1), height=1, width=7) 
button1.pack(expand=1)

##
buttoncontrol = tk.Button(rechner, text=' control ', fg='black', bg='red', 
                     command=lambda: control2(), height=1, width=7) 
buttoncontrol.pack(expand=1)  

##
clear_button = tk.Button(rechner, text='clr', fg='black', bg='red', 
                     command=lambda: clear(), height=1, width=7) 
clear_button.pack(side="bottom")

##
button = tk.Button(rechner,text="OK",command=rechner.destroy)
button.pack(side="bottom")


##
button = tk.Button(rechner,text="Abort",command=rechner.destroy)
button.pack(side="top")