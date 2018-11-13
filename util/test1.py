#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lijj 
@time: 2018/10/16 
"""

x=60
def foo():
    global x
    print("x is :"+str(x))
    x=3
    print("change local x to "+str(x))
foo()
def fun(a,b=4,c=8):
    print('a is ',a,'and b is ',b,'and c is ',c)
fun(b=5,a=3)
def print_params(fpara,*nums,**words):
    print('fpara:'+str(fpara))
    print('nums:'+str(nums))
    print('words:'+str(words))
print_params('hello',1,3,5,7,word='python',another_word='java')