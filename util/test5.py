#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/16 
"""
num=59
number_chance=3
print('you hava only 3 chance to guess ')
for i in range(1,number_chance+1):
    print('chance '+str(i))
    guess=int(input('enter an integer:'))
    if guess==num:
        print('Binggo,you are right')
        break
    elif guess<num:
        print('no no !!number is higher than you hava '+str(number_chance-1)+'chance left')
    else:
        print('no no !!number is lower than you hava '+str(number_chance-1)+'chance left')
print('Done')