#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/16 
"""
num=50
guess_flag=False
while guess_flag==False:
    guess=int(input('Enter an Integer:'))
    if guess==num:
        guess_flag=True
    elif guess<num:
        print('No,the number is higher than that,keep guessing')
    else:
        print('No,the numner is lower than that,keep guessing')
print('Binggo!you guessed it right.')
print('but you do not win only pricess!')
print('Done')