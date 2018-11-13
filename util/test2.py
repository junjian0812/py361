#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/16 
"""
num=50
guess=int(input('enter an integer:'))
if guess ==num:
    print('binggo!you guess it right.')
    print('but yoo!!!!')
elif guess< num:
    print('no ,the number is higher than that')
else:
    print('no ,the number is lower than that')
print('Done')

