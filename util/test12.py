#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/28 
"""
###圖形界面
from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

'''
root=Tk()
w=Label(root,text='Guess Number Game')
w.pack()
'''
mb.showinfo('welcome','welcome to guess number game')

number=59
while True:
    guess=dl.askinteger('Number','please input a number!')
    if guess==number:
        output='Bingo,you guess right!!'
        mb.showinfo('Hint:',output)
        break
    elif guess <number:
        output='lower!!!'
        mb.showinfo('low:',output)
    else:
        output='higher!!'
        mb.showinfo('higher:',output)
print('Done!!')
