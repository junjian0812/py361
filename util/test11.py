#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/28 
"""
#GUI graphical user interface
# tkinter:GUI library  for Python

from tkinter import *

import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root =Tk()
w=Label(root,text='label title000000000000000000')
w.pack()

mb.showinfo('welcome','welcome message')
guess=dl.askinteger('number','enter a number')

output='this is a outputmessage'
mb.showinfo('output',output)
