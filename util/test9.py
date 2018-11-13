#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/28 
"""

#enample of syntax errors
# while True:
#     print('hello XX!!!')
#example of exception :ZeroDivisionError: division by zero
#print(8/0)

#ypeError: must be str, not int
# num=6
# print('nihao '+num)

# while True:
#     try:
#         x=int(input('please into a number:'))
#         break
#     except ValueError:
#         print('not valid input,try again...')
#         #不處理，異常直接拋出來
#         raise

try:
    f=open('myfile.txt')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print('OS error:{0}'.format(err))
except ValueError:
    print('could not convert data to an interger')

