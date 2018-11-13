#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/28 
"""

class Student:
    '''
    def __init__(self,name,grade):#實例化構造函數，self標示實例化的對象本身，相當於java的this
        self.name=name
        self.grade=grade
    def introduce(self):
        print("hi i'am " +self.name)
        print('my grade is '+str(self.grade))
    def improve(self,amount):
        self.grade=self.grade+amount
jim=Student('jim',8)
jim.introduce()
jim.improve(10)
jim.introduce()

def make_cake():
    return "cake"

def add_candle(cake_func): #可以用一個函數作為入參
    def insert_candle():
        return cake_func()+"\tcandle"
    return insert_candle

gifts_func=add_candle(make_cake)
print(make_cake())
print(gifts_func())
'''



def add_candle(cake_func): #可以用一個函數作為入參
    def insert_candle():
        return cake_func()+"\tcandle"
    return insert_candle
@add_candle #裝飾器 make作為該函數的入參
def make_cake():
    return "cake"

#make_cake=add_candle(make_cake)
print(make_cake()) #cake	candle
#print(gifts_func())
