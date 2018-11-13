#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/28 
"""
some_sentences='''\
i love learning python
because python is fun
and also easy to use
'''
f=open('../fileIo/some_sentences.txt','w')
f.write(some_sentences)
f.close()

#默認模式r
f=open('../fileIo/some_sentences.txt')
while True:
    line =f.readline()
    if len(line)==0:
        break
    print(line)
f.close()
