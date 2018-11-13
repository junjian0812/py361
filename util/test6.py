#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/28 
"""
a_list=[0,1,2,4]
print('using continue:')
for i in a_list:
'''0是真，非0為假'''
    if not i:
        continue
    print(i)
print('using pass:')
for a in a_list:
    if not a:
        pass
    print(a)

